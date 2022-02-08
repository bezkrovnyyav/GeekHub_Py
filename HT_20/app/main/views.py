from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse

from .models import Products, Card
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


@login_required
def card_add(request, pk):
    post = get_object_or_404(Products, id=pk)
    Card.objects.create(user=request.user, product=post)
    return HttpResponseRedirect(reverse('home'))


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


@login_required
def basket(request):
    data = {'product': Card.objects.filter(user=request.user)}
    return render(request, 'main/basket.html', data)


def delete_products(request, pk):
    if request.user.is_superuser:
        try:
            product = Products.objects.get(id=pk)
            product.delete()
            return HttpResponseRedirect(reverse("home"))
        except Products.DoesNotExist:
            return HttpResponseNotFound("<p>Product not found</p>")
