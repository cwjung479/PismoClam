# Generated by Django 2.1.3 on 2019-03-13 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190312_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='beaches',
        ),
    ]