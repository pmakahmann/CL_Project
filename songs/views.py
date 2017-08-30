from django.shortcuts import render


from . import models


def song_list(request):
    songs = models.Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})
