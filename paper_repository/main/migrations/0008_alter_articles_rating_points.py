# Generated by Django 4.1.3 on 2023-12-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_articles_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='rating_points',
            field=models.IntegerField(default=0),
        ),
    ]
