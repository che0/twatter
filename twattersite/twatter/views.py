# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from twatter.models import Twat, MOOD_CHOICES

try:
    from unidecode import unidecode
except ImportError:
    unidecode = lambda x: unicode(x).encode('ascii', 'replace')

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
        response.set_cookie('twatter_user', form.cleaned_data['author'], max_age=3600*24*90)
        return response
    
    def get_context_data(self, **kwargs):
        context = super(PostTwat, self).get_context_data(**kwargs)
        context['moods'] = MOOD_CHOICES
        return context

def last(request):
    twats = Twat.objects.all()[:1]
    if len(twats) < 1:
        return HttpResponse('no twats yet', 'text/plain')
    
    twat = twats[0]
    return HttpResponse(unidecode(unicode(twat)), 'text/plain')
