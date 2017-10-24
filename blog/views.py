# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Blog
# Create your views here.
def all_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs' : blogs})

def post_detail(request, id):
    blogs = Blog.objects.filter(id__icontains = id)
    context = { 'blogs' : blogs }
    return render(request, 'details.html', context)