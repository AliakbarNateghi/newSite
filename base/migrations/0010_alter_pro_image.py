# Generated by Django 4.0.4 on 2022-06-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_pro_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pro',
            name='image',
            field=models.ImageField(default='base/images/smoothie.jpg', upload_to='images'),
        ),
    ]
