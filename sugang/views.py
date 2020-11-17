from django.views.generic import ListView,DetailView
from sugang.models import Subject, Sign

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from sugang.forms import SugangInlineFormSet


class SubjectLV(ListView):
    model = Subject

class SubjectDV(DetailView):
    model = Subject

class SignDV(DetailView):
    model = Sign


# 이하 추가
#--- Create/Change-list/Update/Delete for Photo
class SignCV(LoginRequiredMixin, CreateView):
    model = Sign
    fields = ('subject','name')
    success_url = reverse_lazy('sugang:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class SignChangeLV(LoginRequiredMixin, ListView):
    model = Sign
    template_name = 'sugang/sign_change_list.html'
    
    def get_queryset(self):
        return Sign.objects.filter(owner=self.request.user)

class SignUV(OwnerOnlyMixin, UpdateView):
    model = Sign
    fields = ('subject','name')
    success_url = reverse_lazy('sugang:index')

class SignDelV(OwnerOnlyMixin, DeleteView):
    model = Sign
    success_url = reverse_lazy('sugang:index')


#이하 추가
#--- Change-list/Delete for Album
class SubjectChangeLV(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'sugang/subject_change_list.html'

    def get_queryset(self):
        return Subject.objects.filter(owner=self.request.user)

class SubjectDelV(OwnerOnlyMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy('sugang:index')


#--- (InlineFormSet) Create/Update for Album
class SubjectSignCV(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ('subj', 'prof')
    success_url = reverse_lazy('sugang:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = SugangInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = SugangInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']

        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class SubjectSignUV(OwnerOnlyMixin, UpdateView):
    model = Subject
    fields = ('subj', 'prof')
    success_url = reverse_lazy('sugang:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = SugangInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = SugangInlineFormSet(instance=self.object)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))