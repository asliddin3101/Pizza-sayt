# Generated by Django 3.2.5 on 2021-08-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20210820_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
    ]