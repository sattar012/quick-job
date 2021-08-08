# Generated by Django 2.2.24 on 2021-08-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_delete_companies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('Companies', models.CharField(max_length=200)),
                ('url', models.TextField()),
            ],
        ),
    ]
