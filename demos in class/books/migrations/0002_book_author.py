# Generated by Django 3.1.4 on 2020-12-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
