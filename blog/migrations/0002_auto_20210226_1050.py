# Generated by Django 3.1.3 on 2021-02-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=350),
        ),
    ]