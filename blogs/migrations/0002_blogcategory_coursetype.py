# Generated by Django 2.2.24 on 2021-08-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='coursetype',
            field=models.CharField(default='', max_length=200),
        ),
    ]
