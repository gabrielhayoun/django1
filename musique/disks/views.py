from django.shortcuts import render, get_object_or_404

from .forms import SearchTitleForm
from .models import Album, Track


# Create your views here.

def albums(request):
    form = SearchTitleForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data['title']

        if title != "":
            album = Album.objects.filter(title__contains=title)
            return render(request, 'disks/albums.html', {'list_albums': album, 'form': form},)
        else:
            return render(request, 'disks/albums.html', {'list_albums': Album.objects.all(), 'form': form}, )
    return render(request, 'disks/albums.html', {'list_albums': Album.objects.all(), 'form': form},)


def track(request, id):
    album = get_object_or_404(Album, id=id)
    tracks = Track.objects.filter(album=album)
    time = []
    for obj in tracks:
        milli = obj.milliseconds % 1000
        sec = obj.milliseconds // 1000
        minute = sec // 60
        sec = sec % 60
        time.append([str(minute) + " min " + str(sec) + " sec " + str(milli) + " millisec", obj.id])
    return render(request, 'disks/tracks.html', locals())
