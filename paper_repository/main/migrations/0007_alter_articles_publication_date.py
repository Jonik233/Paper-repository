# Generated by Django 4.1.3 on 2023-12-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_articles_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='publication_date',
            field=models.DateField(),
        ),
    ]