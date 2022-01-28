from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.utils import http
from django.views.generic import FormView


class FontPage(FormView):
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('hello world')
    def get(self,request, *args, **kwargs):
        return render(request,'polls/index.html')

class About(FormView):
    def get(self, request, *args, **kwargs):
        return render(request,'polls/about.html')

