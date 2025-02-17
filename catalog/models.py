from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    objects = None
    name = models.CharField(
        max_length=255,
        verbose_name="Наименование",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    category = models.CharField(
        max_length=255,
        verbose_name="Категория",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
    )
    stock = models.PositiveIntegerField(verbose_name="Количество на складе")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        null=True, auto_now=True, verbose_name="Дата последнего изменения"
    )
    is_published = models.BooleanField(
        default=False,  # Значение по умолчанию - не опубликовано
        verbose_name="Статус публикации",
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]
        permissions = [("can_unpublish_product", "can unpublish product")]


class Contact(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
