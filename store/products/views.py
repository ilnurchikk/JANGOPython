from django.shortcuts import render

def index(request):
    return render(request, 'products/index.html')
# Create your views here.
def products(request):
    return render(request, 'products/products.html')