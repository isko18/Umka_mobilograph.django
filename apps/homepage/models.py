from django.db import models

# Create your models here.

class Umka(models.Model):
    logo_site = models.ImageField(
        verbose_name="Логотип сайта",
        upload_to="logo/"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок сайта"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Настройка главной страницы"
        verbose_name_plural="Настройки главной страницы"

class Social_network(models.Model):
    instagram = models.URLField(
        verbose_name="Ссылка на instagram"
    )
    whatsapp = models.URLField(
        verbose_name="Ссылка на WhatsApp"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на facebook"
    )

    def __str__(self):
        return self.instagram
    
    class Meta:
        verbose_name="Социальные сети"
        verbose_name_plural="Социальные сети"

