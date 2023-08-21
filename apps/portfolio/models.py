from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title_portfolo = models.CharField(
        max_length=100,
        verbose_name="Названия фото"
    )
    image_portfolio = models.ImageField(
        upload_to="portfolio_image/",
        verbose_name="Фото портфолио"
    )
    descriptions_image = models.CharField(
        max_length=255,
        verbose_name="Описание фото"
    )

    def __str__(self):
        return self.title_portfolo
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Добавление портфолио фото"

class Project_video(models.Model):
    title_video = models.CharField(
        max_length=100,
        verbose_name="Название видео"
    )
    video_profile = models.FileField(
        upload_to="vipdeo_portfolio/",
        verbose_name="Видео портфолио"
    )
    photo_video = models.ImageField(
        upload_to="video_image/",
        verbose_name="Фото для обложки видео"
    )
    descriptions_video = models.CharField(
        max_length=255,
        verbose_name="Описание видео"
    )

    def __str__(self):
        return self.title_video
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Добавление портфолио видео"
