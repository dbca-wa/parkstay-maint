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
       response['Cache-Control'] = 'public, max-age=300'
       return response

