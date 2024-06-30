from django.shortcuts import render
from .models import product

# Create your views here.
def index(request):
    context = {}
    return render(request, 'petvetpag/index.html')

def porhacer(request):
    context = {}
    return render(request, 'petvetpag/porhacer.html')

def tienda(request):
    productos = product.objects.all()
    context = {'productos': productos}
    return render(request, 'petvetpag/tienda.html', context)