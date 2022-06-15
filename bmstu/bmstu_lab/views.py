from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Game


def index(request):
    a_list = Game.objects.all()
    return render(request, 'master/list.html', dict([('a_list', a_list)]))


def detail(request, game_id):
    try:
        a = Game.objects.get(id=game_id)
    except:
        raise Http404('Игра не найдена!')
    return render(request, 'master/detail.html', dict([('game', a)]))
