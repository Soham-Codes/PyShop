from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all() # Gets all the products from the database
    # Product.objects.filter() # Filters the products based on the given parameters
    # Product.objects.get() # Gets a single product based on the given parameters
    # Product.objects.save() # Saves the product to the database
    return render(request, 'index.html', 
                  {'products': products})

def new(request):
    return HttpResponse('New Products')

