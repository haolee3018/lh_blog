from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    if request.method == 'GET':

        return render(request, 'web/index.html')

