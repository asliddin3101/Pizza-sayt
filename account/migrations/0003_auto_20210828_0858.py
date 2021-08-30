# Generated by Django 3.2.5 on 2021-08-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password1',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]