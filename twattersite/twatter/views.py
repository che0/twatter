# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from twatter.models import Twat

class ListTwats(ListView):
    model = Twat
    
    def get_queryset(self):
        return super(ListTwats, self).get_queryset()[:30]

class PostTwat(CreateView):
    model = Twat
    
    def get_initial(self):
        return {
            'author': self.request.COOKIES.get('twatter_user', ''),
            'mood': 'plain',
        }
    
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('list_twats')
    
    def form_valid(self, form):
        response = super(PostTwat, self).form_valid(form)
        response.set_cookie('twatter_user', form.cleaned_data['author'])
        return response