from django.shortcuts import render
from .models import Album

# Create your views here.

def albums(request):
    return render(request, 'disks/albums.html', {'list_albums': Album.objects.all()})
