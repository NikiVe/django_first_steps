# Generated by Django 3.1.4 on 2020-12-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20201214_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='image_url',
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default='', upload_to='pets'),
            preserve_default=False,
        ),
    ]
