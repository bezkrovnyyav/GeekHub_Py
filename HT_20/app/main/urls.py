from .views import main, card_add, add_new_product, basket, delete_products
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main, name='home'),
    path('add_to_cart/<int:pk>', card_add, name='basket'),
    path('addnewproduct/', add_new_product, name='add'),
    path('basket/', basket, name='basket'),
    path('delete/<int:pk>', delete_products, name='delete'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
