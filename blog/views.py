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
