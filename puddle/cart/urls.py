from django.urls import path
from ninja import NinjaAPI
from .views import router as cart_router

api = NinjaAPI(urls_namespace='cart-api')
api.add_router("/cart", cart_router)

urlpatterns = [
    path("", api.urls),
]