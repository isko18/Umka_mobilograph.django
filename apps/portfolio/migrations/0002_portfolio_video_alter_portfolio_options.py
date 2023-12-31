# Generated by Django 4.2.3 on 2023-08-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_video', models.CharField(max_length=100, verbose_name='Название видео')),
                ('video_profile', models.FileField(upload_to='video/', verbose_name='Видео портфолио')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Добавление портфолио видео',
            },
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': '', 'verbose_name_plural': 'Добавление портфолио фото'},
        ),
    ]
