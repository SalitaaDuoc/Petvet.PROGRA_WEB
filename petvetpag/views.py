from django.shortcuts import render
from .models import product
from .forms import productForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'petvetpag/index.html')

def porhacer(request):
    context = {}
    return render(request, 'petvetpag/porhacer.html')

#Crud productos (Tienda)
def tienda(request, context={}):
    productos = product.objects.all()
    context = {
        'productos': productos,
        'form': productForm()}
    return render(request, 'petvetpag/tienda.html', context)

def product_create(request):
    context = {}

    if request.method == 'POST':
        print('----------------------------Se llego a post')
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            print('---------------------------Formulario valido')
            form.save()
            form = productForm()
            context['message'] = "Guardado exitosamente"
            context['form'] = form
        else:
            print('---------------------------Formulario invalido'+str(form.errors))
            context['message'] = "Formulario invalido"
    else:
        print('---------------------------Se llego a get')
        context['message'] = "No se ha registrado ningun producto"

    return tienda(request, context)

def product_update(request, id):
    context = {}
    return tienda(request, context)

def product_delete(request, id):
    context = {}
    return tienda(request, context)
