from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'petvetpag/index.html')

def porhacer(request):
    context = {}
    return render(request, 'petvetpag/porhacer.html')