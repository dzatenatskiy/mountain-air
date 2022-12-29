from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FeedBackForm

# Create your views here.

def home(request):
    return render(request, 'blog/index.html', context={})

def contact(request):
    form = FeedBackForm()
    
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    return render(request, 'blog/contact.html', {'form': form})


def gallery(request):
    return render(request, 'blog/gallery.html', context={})

def rooms(request):
    return render(request, 'blog/rooms.html', context={})

def standart_rooms(request):
    return render(request, 'blog/standart-family-room.html', context={})

def lux_rooms(request):
    return render(request, 'blog/lux-family-room.html', context={})

def about_us(request):
    return render(request, 'blog/about_us.html', context={})

def pravila(request):
    return render(request, 'blog/pravila.html', context={})