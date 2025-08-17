from django.test import TestCase, Client
from django.conf import settings
import stripe
from django.contrib.auth.models import User
from item.models import Item, Category
from .models import Cart, CartItem, Order, OrderItem
from ninja.testing import TestClient
from .views import router as cart_router


class CartAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        # Use Django Ninja's TestClient and pass the router
        self.client = TestClient(cart_router)
        self.category = Category.objects.create(name='Test Category')
        self.item = Item.objects.create(
            category=self.category,
            name='Test Item',
            description='A test item',
            price=10.00,
            image=None,
            is_sold=False,
            created_by=self.user,
        )

    def test_add_item_to_cart(self):
        payload = {'item_id': self.item.id}

        # URL is now relative to the router's root: /add
        response = self.client.post("/add", json=payload, user=self.user)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Cart.objects.filter(user=self.user).exists())
        self.assertTrue(
            CartItem.objects.filter(cart__user=self.user, item=self.item).exists())

    def test_cannot_add_sold_item(self):
        self.item.is_sold = True
        self.item.save()

        user2 = User.objects.create_user(username='user2', password='password')

        payload = {'item_id': self.item.id}

        response = self.client.post("/add", json=payload, user=user2)

        self.assertEqual(response.status_code, 409)
        self.assertFalse(
            CartItem.objects.filter(cart__user=user2, item=self.item).exists())

    def test_remove_item_from_cart(self):
        cart, _ = Cart.objects.get_or_create(user=self.user)
        CartItem.objects.create(cart=cart, item=self.item)

        self.assertTrue(CartItem.objects.filter(cart=cart, item=self.item).exists())

        payload = {'item_id': self.item.id}

        # Use DELETE method and correct relative URL
        response = self.client.delete("/remove", json=payload, user=self.user)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(CartItem.objects.filter(cart=cart, item=self.item).exists())

    def test_get_cart_contents(self):
        cart, _ = Cart.objects.get_or_create(user=self.user)
        CartItem.objects.create(cart=cart, item=self.item)

        # Corrected URL path with the trailing slash
        response = self.client.get("/", user=self.user)

        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertIn('cart_items', response_data)
        self.assertEqual(len(response_data['cart_items']), 1)
        self.assertEqual(response_data['cart_items'][0]['item']['id'], self.item.id)

    def test_checkout_cart(self):
        """
        Test that a checkout request correctly creates an Order and OrderItem.
        """
        # First, add the item to the cart so we have something to checkout.
        cart, _ = Cart.objects.get_or_create(user=self.user)
        CartItem.objects.create(cart=cart, item=self.item)

        # Make a POST request to the checkout endpoint.
        response = self.client.post("/checkout/", user=self.user)

        # Assert that the response status code is 201 (Created).
        self.assertEqual(response.status_code, 201)

        # Assert that an Order and OrderItem were created.
        self.assertTrue(Order.objects.filter(user=self.user).exists())
        self.assertTrue(
            OrderItem.objects.filter(order__user=self.user, item=self.item).exists())

        # Assert that the cart is now empty.
        self.assertEqual(CartItem.objects.filter(cart=cart).count(), 0)

class StripeAuthenticationTest(TestCase):
    def test_stripe_secret_key(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        self.assertIsNotNone(settings.STRIPE_SECRET_KEY)

        try:
            stripe.Product.list(limit=1)
            success = True
        except stripe.error.AuthenticationError:
            success = False
        except Exception as e:
            print(f"An unexpected error occured: {e}")
            success = False

        self.assertTrue(success,
                        "Stripe authentication failed. "
                        "Please check the STRIPE_SECRET_KEY")