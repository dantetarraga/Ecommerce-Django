# Generated by Django 4.1.7 on 2023-04-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_size_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
