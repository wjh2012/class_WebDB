from django.db import models
from django.urls import reverse

class Subject(models.Model):
    subj = models.CharField('SUBJ', max_length=30)
    prof = models.CharField('PROF', max_length=30, blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True) 

    class Meta:
        ordering = ('subj',)
    
    def __str__(self):
        return self.subj
    
    def get_absolute_url(self):
        return reverse('sugang:subject_detail', args=(self.id,))

class Sign(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField('NAME', max_length=30)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('sugang:sign_detail', args=(self.id,))

