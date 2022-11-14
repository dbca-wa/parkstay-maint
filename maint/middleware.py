import re
import datetime

#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone

class CacheControl(object):

    def __init__(self, get_response):
            self.get_response = get_response

    def __call__(self, request):
       response= self.get_response(request)
       #response['Cache-Control'] = 'public, max-age=300'
       return response


class RedirectUrls(object):

    def __init__(self, get_response):
            self.get_response = get_response

    def __call__(self, request):
       print (request.path)
       if request.path == '/' or request.path.startswith('/static/') or request.path.startswith('/media/'): 
          response= self.get_response(request)
          response['Cache-Control'] = 'public, max-age=300'
          return response
       else:
          response =HttpResponse("<script>window.location.replace('/');</script>Redirecting")
          response['Cache-Control'] = 'public, max-age=10'
          return response
