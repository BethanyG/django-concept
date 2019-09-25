# Generated by Django 2.2.4 on 2019-09-25 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20190924_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='media_type',
            field=models.CharField(choices=[('VID', 'Video'), ('POD', 'Podcast'), ('PODEP', 'Podcast Episode'), ('TALK', 'Talk'), ('TUTOR', 'Tutorial'), ('COURSE', 'Course'), ('BOOK', 'Book'), ('BLOG', 'Blog'), ('GAME', 'Game'), ('EVENT', 'Event'), ('TOOL', 'Tool'), ('LIB', 'Library'), ('WEB', 'Website')], max_length=7),
        ),
    ]