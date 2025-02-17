from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название",
    )
    content = models.TextField(verbose_name="Содержимое")
    preview_image = models.ImageField(
        upload_to="blog/images/", verbose_name="Изображение", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать")
    views_count = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
