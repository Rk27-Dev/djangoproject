from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from .serializers import restserializer
from .models import restmodel
# Create your views here.
class restcurd(View):
    def get(self,request,*args,**kwargs):
        jason_data=request.body
        stream=io.BytesIO(jason_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            emp=restmodel.objects.get(id=id)
            serializer=restserializer(emp)
            jason_data=JSONRenderer().render(serializer.data)
            return HttpResponse(jason_data,content_type='application/json')
        qs=restmodel.objects.all()
        jason_data = JSONRenderer().render(qs.data)
        return HttpResponse(jason_data, content_type='application/json')

