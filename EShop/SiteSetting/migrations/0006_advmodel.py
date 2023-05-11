# Generated by Django 4.2 on 2023-05-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSetting', '0005_alter_slidersetting_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='images/advertise')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
                ('position', models.CharField(choices=[('product_list', 'لیست محصولات'), ('product_detail', 'جزئیات محصولات'), ('about_us', 'درباره ما')], max_length=200)),
            ],
        ),
    ]
