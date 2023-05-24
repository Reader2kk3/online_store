from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField("Категория", max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField("Описание", max_length=255, blank=True)
    cat_image = models.ImageField("Фотографии", upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def get_url(self):
        return reverse("products_by_category", args=[self.slug])

    def __str__(self):
        return self.category_name