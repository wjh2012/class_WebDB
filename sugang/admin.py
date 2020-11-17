from django.contrib import admin

from sugang.models import Subject, Sign

class SignInline(admin.StackedInline):
    model = Sign
    extra = 2

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = (SignInline,)
    list_display = ('id', 'subj')

@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'name')
