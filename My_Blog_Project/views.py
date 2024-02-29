from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


def Index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))
