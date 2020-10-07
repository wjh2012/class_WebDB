from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('NAME', max_length=100, blank=False)
    stdnum = models.CharField('STDNUM', max_length=50, blank=False)
    grade = models.CharField('GRADE', max_length=50, blank=False)
    major = models.CharField('MAJOR', max_length=50, blank=False)
    add_dt = models.DateField('ADD', auto_now=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('stdnum','name')