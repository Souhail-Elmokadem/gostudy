# Generated by Django 4.2 on 2023-05-03 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='categorie',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.categorie'),
        ),
    ]
