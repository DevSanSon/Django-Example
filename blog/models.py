# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Гарчиг")
    body = models.TextField()
    author = models.CharField(max_length = 50, verbose_name = "Нийтлэгч")
    
    
    def get_absoulte_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])
    
    def __unicode__(self):
        return self.title