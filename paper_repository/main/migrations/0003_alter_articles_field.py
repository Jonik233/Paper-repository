# Generated by Django 4.1.3 on 2023-11-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_articles_options_remove_articles_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='field',
            field=models.CharField(choices=[('physics', 'Physics'), ('chemistry', 'Chemistry'), ('economics', 'Economics'), ('math', 'Math'), ('biology', 'Biology'), ('machine learning', 'Machine Learning')], max_length=100, verbose_name='Field'),
        ),
    ]
