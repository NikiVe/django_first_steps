# Generated by Django 3.1.4 on 2020-12-10 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201210_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
            preserve_default=False,
        ),
    ]
