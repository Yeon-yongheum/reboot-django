# Generated by Django 2.2.5 on 2019-09-11 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastlifes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pastlife',
            old_name='pastlife',
            new_name='job',
        ),
    ]