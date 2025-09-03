from django.shortcuts import render


def home(request):
    template = 'home.html'
    return render(request, template)


def about(request):
    return render(request, 'toys/about.html')


def gallery(request):
    return render(request, 'toys/allery.html')


def contact(request):
    return render(request, 'toys/contact.html')
