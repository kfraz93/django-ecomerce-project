from ninja import Router
from .schemas import AddToCartSchema, CartItemSchema, RemoveFromCartSchema
from .models import Cart, CartItem, Order, OrderItem
from item.models import Item
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from ninja import Schema

router = Router()

@router.post("/add", response={201: dict, 409: dict})
def add_to_cart(request, payload: AddToCartSchema):
    """
    Adds an item to the user's cart.
    """
    user = request.user
    item = get_object_or_404(Item, pk=payload.item_id)

    # Check if the item is already sold.
    if item.is_sold:
        # Return a 409 Conflict status code.
        return 409, {"message": "Item is already sold."}

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=user)

    # Add the item to the cart
    CartItem.objects.create(cart=cart, item=item)

    # Now, set the item to sold.
    item.is_sold = True
    item.save()

    return 201, {"message": "Item added to cart"}

@router.delete("/remove", response={204: None, 404: dict})
def remove_from_cart(request, payload: RemoveFromCartSchema):
    """
    Removes an item from user's cart
    :param request:
    :param payload:
    :return:
    """
    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, item__pk=payload.item_id)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        return 404, {"message": "Item not found in the cart"}

    #  Setting item to available
    item = cart_item.item
    item.is_sold = False
    item.save()

    #  Delete item in cart
    cart_item.delete()
    return 204, None

@router.get("/", response={200: dict})
def get_cart(request):
    """
    Retrieves the content of the cart
    :param request:
    :return:
    """
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart).order_by('-created')
    except Cart.DoesNotExist:
        return 200, {"cart_items": []}

    serialized_items = [CartItemSchema.from_orm(item).dict() for item in cart_items]
    return 200, {"cart_items": serialized_items}

@router.post("/checkout/", response={201: dict, 404: dict})
def checkout(request):
    """
    Processes the cart contents and creates an order
    :param request:
    :return:
    """
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except Cart.DoesNotExist:
        return 404, {"message": "Cart not found"}

    if not cart_items.exists():
        return 404, {"message": "Cart is empty"}

    #  create a new order for user
    order = Order.objects.create(user=request.user)

    #  Move items from cart to new Order
    for cart_item in cart_items:
        OrderItem.objects.create(
            order=order,
            item=cart_item.item,
            price=cart_item.item.price
        )

    #  Clear the cart
    cart_items.delete()
    return 201, {"message": "Order created successfully"}
