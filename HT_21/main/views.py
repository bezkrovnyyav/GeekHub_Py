from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse

from rest_framework import viewsets

from .serializers import ProductSerializer, CategorySerializer
from .models import Products, Category
from .forms import ProductsForm


def main(request):
    value = request.POST.get('category')
    data = Products.objects.all()
    if value == 'phone':
        data = Products.objects.filter(category=1)
    elif value == 'tablet':
        data = Products.objects.filter(category=2)
    elif value == 'laptop':
        data = Products.objects.filter(category=3)
    return render(request, 'main/main.html', {'data': data})


def card_add(request):
    product_id = request.POST.get('product_id')
    cart = request.session.setdefault('cart', {})
    if product_id:
        products = cart.setdefault('product', [])
        products.append(product_id)
        request.session.modified = True
    return JsonResponse({'products': request.session['cart']})


def cart(request):
    id_products = request.session['cart']['product']
    list_all = []
    for id in id_products:
        product = Products.objects.filter(id=id)
        list_all.append(product)
    return render(request, 'main/basket.html', {'all': list_all})


def add_new_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'
    form = ProductsForm()
    data = {'form': form, 'error': error}
    return render(request, 'main/add.html', data)


def delete_products(request, pk):
    if request.user.is_superuser:
        try:
            product = Products.objects.get(id=pk)
            product.delete()
            return HttpResponseRedirect(reverse("home"))
        except Products.DoesNotExist:
            return HttpResponseNotFound("<p>Product not found</p>")


class ProductView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


