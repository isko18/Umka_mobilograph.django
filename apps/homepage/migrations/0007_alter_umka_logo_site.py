# Generated by Django 4.2.4 on 2023-08-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_umka_logo_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umka',
            name='logo_site',
            field=models.ImageField(upload_to='logo/', verbose_name='Логотип сайта'),
        ),
    ]
