# Generated by Django 5.1.1 on 2024-09-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
    ]
