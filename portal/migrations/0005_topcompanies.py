# Generated by Django 2.2.24 on 2021-08-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_delete_topcompanies'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopCompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/')),
                ('companyName', models.CharField(max_length=100)),
                ('headquarters', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('founddate', models.CharField(max_length=100)),
                ('founder', models.CharField(max_length=100)),
                ('revenue', models.CharField(max_length=50)),
                ('employees', models.CharField(max_length=50)),
                ('url', models.TextField()),
            ],
        ),
    ]