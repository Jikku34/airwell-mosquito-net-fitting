# Generated by Django 5.0.2 on 2024-02-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirWellApp', '0004_alter_userenquirymodel_enquiry_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_price',
            field=models.CharField(max_length=100),
        ),
    ]
