from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    print('this line prented by view')
    return HttpResponse('<h1> custom middleware</h1>')