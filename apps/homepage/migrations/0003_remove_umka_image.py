# Generated by Django 4.2.4 on 2023-08-14 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_social_network_facebook_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umka',
            name='image',
        ),
    ]