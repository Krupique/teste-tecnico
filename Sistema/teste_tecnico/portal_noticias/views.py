from django.shortcuts import render, get_object_or_404

from .models import Noticia, Comentario
from django.db.models import Count


def homePage(request):

    list_news = Noticia.objects.values('id', 'title').order_by('-created_at').annotate(count=Count('comentario'))

    return render(request, 'home/index.html', {'list_news': list_news})

def detailedNews(request, id):
    news = get_object_or_404(Noticia, pk=id)

    list_comments = Comentario.objects.filter(noticia=id)

    return render(request, 'home/news.html', {'news': news, 'list_comments': list_comments})