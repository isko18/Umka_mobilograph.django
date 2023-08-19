from django.db import models

# Create your models here.
class About(models.Model):
    title_about = models.CharField(
        max_length=100,
        verbose_name="Заголовок текста"
    )
    text_about = models.CharField(
        max_length=255,
        verbose_name="Описание текста"
    )
    image_about = models.ImageField(
        upload_to="image_about/",
        verbose_name="Мое фото"
    )

    def __str__(self):
        return self.title_about
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Oбо мне"
