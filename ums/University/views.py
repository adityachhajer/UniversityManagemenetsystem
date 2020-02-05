from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'University/index.html')

def about(request):
    return render(request,'University/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'University/contact.html')

def search(request):
    return HttpResponse("we are at search")

def view(request):
    return HttpResponse("we are at view")

