from django.shortcuts import render

def home(request):
    return render(request, 'salon/home.html')

def services(request):
    return render(request, 'salon/services.html')

def gallery(request):
    return render(request, 'salon/gallery.html')

def about(request):
    return render(request, 'salon/about.html')

def contact(request):
    return render(request, 'salon/contact.html')

def booking(request):
    return render(request, 'salon/booking.html')