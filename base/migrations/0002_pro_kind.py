# Generated by Django 4.0.4 on 2022-05-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro',
            name='kind',
            field=models.CharField(default='ice', max_length=100),
        ),
    ]