# Generated by Django 2.2.4 on 2019-09-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0022_product_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review_date',
            field=models.DateField(help_text='Review date of this product'),
        ),
    ]
