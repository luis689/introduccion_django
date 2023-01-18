from multiprocessing import context
from django.views.generic import View
from django.shortcuts import render


class HomeView(View):
    "Get request: Lo que pide la informacion para que se pueda ver"
    "Post request: Es lo que el usuario envia al servidor"
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'index.html', context)