# Generated by Django 3.2.4 on 2021-06-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210606_0524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'permissions': [],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
