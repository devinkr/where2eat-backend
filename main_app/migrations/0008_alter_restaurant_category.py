# Generated by Django 4.0.6 on 2022-07-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_restaurant_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.ManyToManyField(to='main_app.category'),
        ),
    ]
