from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name_category = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name_category


class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
