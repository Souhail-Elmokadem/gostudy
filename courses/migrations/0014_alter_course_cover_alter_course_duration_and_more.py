# Generated by Django 4.2 on 2023-05-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_course_cover_alter_course_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cover',
            field=models.ImageField(blank=True, default='', null=True, upload_to='CourseCovers/img/%y/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, default='', null=True, upload_to='CourseVideos/lecons/%y'),
        ),
    ]