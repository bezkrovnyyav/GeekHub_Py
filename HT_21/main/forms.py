from django import forms
from .models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'category']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name product',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'details for product',
            }),
        }



