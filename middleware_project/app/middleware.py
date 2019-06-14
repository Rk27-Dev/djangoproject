class  existig_middleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request,*args, **kwargs):
        print('pre-processing of request')
        response=self.get_response(request)
        print('post-processing of request')
        return  response
from django.http import HttpResponse
class ApplicationMaintanecemiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request, *args, **kwargs):
        return  HttpResponse('<currently application under the maintanence plzz wait 2 days...>')