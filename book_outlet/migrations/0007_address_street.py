# Generated by Django 3.0.14 on 2023-06-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_auto_20230607_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
