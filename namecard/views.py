from django.shortcuts import render
from django.views.generic import ListView, DetailView
from namecard.models import Namecard_TBL

# Create your views here.
class NamecardLV(ListView):
    model = Namecard_TBL

class NamecardDV(DetailView):
    model = Namecard_TBL