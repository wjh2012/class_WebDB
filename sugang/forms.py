from django.forms import inlineformset_factory
from sugang.models import Subject, Sign

SugangInlineFormSet = inlineformset_factory(Subject, Sign, fields = ['name'], extra = 2)