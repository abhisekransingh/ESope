# Generated by Django 4.1.7 on 2023-05-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customes_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customes',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
