# Generated by Django 3.2 on 2021-07-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_paymentmethod_order_paymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='shippingPrice',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
