from django.shortcuts import render
from django.views.generic import ListView, DetailView
from namecard.models import Namecard_TBL

from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
class NamecardLV(ListView):
    model = Namecard_TBL

class NamecardDV(DetailView):
    model = Namecard_TBL

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'namecard/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Namecard_TBL.objects.filter(Q(name__icontains=searchWord) | Q(tel__icontains=searchWord) | Q(group__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        
        return render(self.request, self.template_name, context)