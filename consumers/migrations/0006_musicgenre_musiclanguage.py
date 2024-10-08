# Generated by Django 5.1.1 on 2024-10-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0005_music_mood'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MusicLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]