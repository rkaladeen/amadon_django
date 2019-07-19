from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
  context = { "all_products" : Product.objects.all() }
  return render(request, "amadon_app/index.html", context)

def checkout(request):
  # Function to adjust inventory Here

  # Function to render items bought here
  
  return render(request, "amadon_app/checkout.html")