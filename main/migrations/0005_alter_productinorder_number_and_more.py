# Generated by Django 4.1 on 2022-10-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_productimage_image_alter_productinorder_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='number',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_per_item',
            field=models.FloatField(),
        ),
    ]
