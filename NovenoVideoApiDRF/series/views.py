from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class HelloWorld(View):
    def get(self, request):
        context = {
            'items': list(range(10)),
        }
        return render(request, "index.html", context)