from django.http import HttpResponse
from django.shortcuts import render
from .models import product, Contact
from math import ceil
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
def  index(request):
#    products =product.objects.all()
#    print(products)
#    n = len(products)
#    nSlides = n//4 + ceil((n/4)-(n//4))
#    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

    # return HttpResponse("Index Shop")

def  about(request):
    return render(request,"shop/about.html")
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contacts = Contact(name=name, email=email, phone=phone, desc=desc)
        contacts.save()
    return render(request, 'shop/contact.html')
def  tracker(request):
     return render(request,"shop/tracker.html")
def  search(request):
     return render(request,"shop/search.html")
def productView(request , myid):
    # Fetch the product using the id
    products = product.objects.filter(id=myid)
    


    return render(request, 'shop/prodView.html', {'product':products[0]})
def  checkout(request):
    return render(request,"shop/checkout.html")