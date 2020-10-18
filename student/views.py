from django.shortcuts import render
from django.views.generic import ListView, DetailView
from student.models import Student

from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
class StudentLV(ListView):
    model = Student

class StudentDV(DetailView):
    model = Student

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'student/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Student.objects.filter(Q(name__icontains=searchWord) | Q(stdnum__icontains=searchWord) | Q(major__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        
        return render(self.request, self.template_name, context) # No Redirection