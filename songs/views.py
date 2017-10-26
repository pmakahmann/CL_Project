from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)


from . import models


def song_list(request):
    songs = models.Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

class SongListView(ListView):
    context_object_name = 'songs'
    model = models.Song

# Create Views for full CRUD capabilities

class SongDetailView(DetailView):
    model = models.Song

class SongCreateView(CreateView):
    fields = ('title', 'artist', 'composition_date')
    model = models.Song

class SongUpdateView(UpdateView):
    fields = ('title', 'artist', 'composition_date')
    model = models.Song

class SongDeleteView(DeleteView):
    model = models.Song
    success_url = reverse_lazy("songs:list")
