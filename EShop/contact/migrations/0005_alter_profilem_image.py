# Generated by Django 4.2 on 2023-04-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_profilem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilem',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
