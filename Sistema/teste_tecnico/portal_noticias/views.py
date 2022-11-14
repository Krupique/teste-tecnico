from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import Noticia, Comentario
from .forms import ComentarioForm
from django.db.models import Count


def homePage(request):

    list_news = Noticia.objects.values('id', 'title').order_by('-created_at').annotate(count=Count('comentario'))

    return render(request, 'home/index.html', {'list_news': list_news})

def detailedNews(request, id):
    news = get_object_or_404(Noticia, pk=id)


    list_comments = Comentario.objects.filter(noticia=id).order_by('-created_at')[:10]
    

    return render(request, 'home/news.html', {'news': news, 'list_comments': list_comments})

@csrf_exempt
def loadComments(request):
    if request.method == "POST":
        data = request.POST.dict()

        print(data)
        
        list_comments = Comentario.objects.filter(noticia=data['noticia']).order_by('-created_at')[:int(data['paginationNumber'])]
        

        ser_instance = serializers.serialize('json', list_comments)

        return JsonResponse({"instance": ser_instance}, status=200)


@csrf_exempt
def postComment(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)

        if form.is_valid():

            instance = form.save()

            ser_instance = serializers.serialize('json', [ instance, ])

            return JsonResponse({"instance": ser_instance}, status=200)



    return JsonResponse({"instance": "Erro"}, status=200)