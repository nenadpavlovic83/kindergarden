from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

def home(request):
    return render(request, 'home.html')




#
# def word_count(request):
#     return render(request, 'count.html')

#
class ThanksPage(TemplateView):
    template_name = 'thanks.html'
