# Generated by Django 4.2 on 2023-05-03 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_eleve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='eleve',
        ),
    ]
