# Generated by Django 4.2 on 2023-04-19 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_auther'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2023, 4, 19)),
            preserve_default=False,
        ),
    ]
