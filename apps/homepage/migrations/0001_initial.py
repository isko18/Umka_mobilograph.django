# Generated by Django 4.2.4 on 2023-08-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social_network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.EmailField(max_length=254, verbose_name='Ссылка на instagram')),
                ('whatsapp', models.EmailField(max_length=254, verbose_name='Ссылка на WhatsApp')),
                ('facebook', models.EmailField(max_length=254, verbose_name='Ссылка на facebook')),
            ],
            options={
                'verbose_name': 'Социальные сети',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
        migrations.CreateModel(
            name='Umka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_site', models.CharField(max_length=50, verbose_name='Названия сайта')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок сайта')),
                ('image', models.ImageField(upload_to='image_hompage/', verbose_name='Фото своих работ')),
            ],
            options={
                'verbose_name': 'Настройка главной страницы',
                'verbose_name_plural': 'Настройки главной страницы',
            },
        ),
    ]
