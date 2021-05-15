from django.shortcuts import render, get_object_or_404
from .models import Album, Track


# Create your views here.

def albums(request):
    return render(request, 'disks/albums.html', {'list_albums': Album.objects.all()})

def track(request, id):
    album = get_object_or_404(Album, id=id)
    tracks = []
    time = []
    for obj in Track.objects.all():
        if obj.album.title == album.title:
            tracks.append(obj)
            milli = obj.milliseconds % 1000
            sec = obj.milliseconds // 1000
            minute = sec // 60
            sec = sec % 60
            time.append([str(minute)+" min "+str(sec)+" sec "+str(milli) + " millisec", obj.id])
    return render(request, 'disks/tracks.html', locals())


