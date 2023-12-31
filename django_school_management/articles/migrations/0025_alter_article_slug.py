# Generated by Django 4.2.3 on 2023-07-14 20:40

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0024_alter_article_id_alter_blogconfiguration_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Article URL Address'),
        ),
    ]
