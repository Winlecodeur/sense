# Generated by Django 5.0.2 on 2024-06-29 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_examen_like_examen_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examen',
            name='like',
        ),
    ]
