# Generated by Django 5.1.1 on 2024-10-03 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='food_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='movie_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
