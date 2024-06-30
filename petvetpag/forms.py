from django import forms
from .models import category, product

class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name']
        labels = {
            'name': 'Nombre de categoria'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de la categoria'
                }
            )
        }

class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'description', 'image', 'price', 'stock', 'category']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'image': 'Imagen',
            'price': 'Precio',
            'stock': 'Cantidad',
            'category': 'Categoría'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripción del producto'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cantidad del producto'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }

