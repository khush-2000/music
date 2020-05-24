#from django.http import HttpResponse
from .models import Album, Song
#from django.template import loader
from django.shortcuts import render, get_object_or_404
#from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    # html = ''
    # for album in all_albums:
    #     url = '/music/' + str(album.id) + '/'
    #     html += '<a href="url">' + album.album_title + '</a><br>'

    # return HttpResponse(html)
    #template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def details(request, album_id):
    # try:
    #    album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #    raise Http404("Album do not exist")
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {'album':Album, 'error_message':"Please enter a valid song!"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})
