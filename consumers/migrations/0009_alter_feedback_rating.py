# Generated by Django 5.1.1 on 2024-10-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0008_alter_feedback_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]