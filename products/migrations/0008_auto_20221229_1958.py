# Generated by Django 3.1.1 on 2022-12-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20221229_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryproduct',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='products/images'),
        ),
    ]
