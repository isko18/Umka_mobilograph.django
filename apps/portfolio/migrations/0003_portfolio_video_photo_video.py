# Generated by Django 4.2.3 on 2023-08-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_video_alter_portfolio_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_video',
            name='photo_video',
            field=models.ImageField(default=1, upload_to='video_image/', verbose_name='Фото для обложки видео'),
            preserve_default=False,
        ),
    ]
