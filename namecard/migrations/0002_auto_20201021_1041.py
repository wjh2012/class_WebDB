# Generated by Django 3.1.1 on 2020-10-21 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('namecard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='namecard_tbl',
            options={'ordering': ('group', 'name')},
        ),
    ]