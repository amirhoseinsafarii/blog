# Generated by Django 3.2.4 on 2021-07-08 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'permissions': [], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
    ]
