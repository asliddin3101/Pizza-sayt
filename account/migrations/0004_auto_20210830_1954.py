# Generated by Django 3.2.5 on 2021-08-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210828_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password2',
            field=models.CharField(max_length=50),
        ),
    ]
