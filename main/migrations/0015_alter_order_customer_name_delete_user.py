# Generated by Django 4.1 on 2023-02-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_productincart_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
