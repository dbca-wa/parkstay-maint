import logging
from django.db.models import Q
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.base import View, TemplateView
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from django import forms
from django.views.generic.base import View, TemplateView
from django.template.loader import get_template
from django.template.loader import render_to_string
from confy import env

class WaitingPage(TemplateView):
    # preperation to replace old homepage with screen designs..

    template_name = 'maint/home.html'
    def render_to_response(self, context):

        template = get_template(self.template_name)
        #context['csrf_token_value'] = get_token(self.request)
        response = HttpResponse(template.render(context))
        response["Access-Control-Allow-Headers"] = "*"
        #response["X-Frame-Options"] = "ALLOW-FROM https://mooring-uat.dbca.wa.gov.au"
        return response

    def get_context_data(self, **kwargs):
        context = super(WaitingPage, self).get_context_data(**kwargs)
        context['QUEUE_URL'] = env('QUEUE_URL','')
        context['settings'] = settings
        return context

