from django.shortcuts import render, get_object_or_404

from .models import (User, Artist, Album, Song, Playlist, PlaylistSong)


def index(request):
    return render(request, "base.html", {'registered': registered})


registered = True


def album_list(request):
    albums = Album.objects.all()
    albums_with_genre = {}

    for album in albums:
        if album.genre not in albums_with_genre:
            albums_with_genre[album.genre] = []
        albums_with_genre[album.genre].append(album)

    return render(request, "album_list.html", {'albums_with_genre': albums_with_genre})


def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    # print(album.name)
    songs = Song.objects.filter(album__name=album.name)
    # print(songs)

    return render(request, "album_songs.html", {'songs': songs, 'album': album})


def song_detail(request, album_id, song_id):
    song = Song.objects.get(pk=song_id)
    album = Album.objects.get(pk=album_id)
    artist = Artist.objects.get(pk=song.artist_id)
    return render(request, "song_detail.html", {'song': song, 'album': album, 'artist': artist})
