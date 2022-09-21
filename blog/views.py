from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedBackForm

# Create your views here.

def home(request):
    return render(request, 'blog/index.html', context={})

def contact(request):
    form = FeedBackForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'blog/contact.html', {'form': form})


def gallery(request):
    return render(request, 'blog/gallery.html', context={})
