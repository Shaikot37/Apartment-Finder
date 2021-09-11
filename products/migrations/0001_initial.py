# Generated by Django 3.0.7 on 2020-11-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adverts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ad_Title', models.TextField()),
                ('price_Title', models.TextField(blank=True, default=None)),
                ('price', models.IntegerField()),
                ('property_location', models.TextField()),
                ('Address', models.TextField()),
                ('listing_category', models.CharField(choices=[('RENT', 'Rent'), ('SALE', 'Sale')], default='RENT', max_length=40)),
                ('sq_ft', models.TextField()),
                ('bed_rooms', models.TextField()),
                ('bath_rooms', models.TextField()),
                ('image', models.TextField(blank=True, default=None, max_length=2083)),
                ('property_url', models.TextField(blank=True, default=None)),
                ('picture', models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%y/%m/%d/')),
                ('lat', models.DecimalField(decimal_places=13, max_digits=21)),
                ('longi', models.DecimalField(decimal_places=13, max_digits=21)),
            ],
        )
        
    ]