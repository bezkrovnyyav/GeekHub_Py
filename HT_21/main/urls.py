from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from .views import main, card_add, add_new_product, delete_products, ProductView, CategoryView, cart

router = routers.DefaultRouter()
router.register(r'product', ProductView)
router.register(r'category', CategoryView)
urlpatterns = [
    path('', main, name='home'),
    path('add_to_cart/', card_add, name='basket'),
    path('addnewproduct/', add_new_product, name='add'),
    path('basket/', cart, name='cart'),
    path('delete/<int:pk>', delete_products, name='delete'),
    path('api/', include(router.urls)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
