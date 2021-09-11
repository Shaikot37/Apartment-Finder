# Generated by Django 3.0.8 on 2021-01-25 19:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adverts',
            name='bookmarked',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='adverts',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=13, default=None, max_digits=21),
        ),
        migrations.AlterField(
            model_name='adverts',
            name='longi',
            field=models.DecimalField(blank=True, decimal_places=13, default=None, max_digits=21),
        ),
    ]
