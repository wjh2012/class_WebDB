from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
# ListView를 상속받은 클래스는 object_list 멤버변수를 사용할 수 있다
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'bookmark/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Bookmark.objects.filter(Q(title__icontains=searchWord) | Q(url__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        
        return render(self.request, self.template_name, context)