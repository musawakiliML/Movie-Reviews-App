# Generated by Django 4.1.6 on 2023-02-15 16:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tagline',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
