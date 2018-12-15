from django.shortcuts import render
from django.views.generic import View
from .script import main, data_keys

from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(View):
    def __init__(self, **kwargs):
        self.context = {}
        super(HomeView, self).__init__(**kwargs)

    def get(self, request, *_, **__):
        return render(request, 'index.html', self.context)

    def post(self, request, *_, **__):
        self.context['word'] = request.POST.get('word')
        (state, word) = main(request.POST.get('word'))
        if state == 1:
            self.context['meanings'] = word
        elif state == 0:
            self.context['related_word'] = word
        else:
            self.context['words'] = 'No Words'
        return render(request, 'index.html', self.context)


class ListDataKeys(APIView):
    def get(self, _, format=None):
        data = data_keys()
        return Response(data)
