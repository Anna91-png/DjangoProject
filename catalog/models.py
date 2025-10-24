from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(blank=True, unique=True, verbose_name="URL-имя")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (₼)")
    price_rub = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена (₽)")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Изображение товара")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL-имя")
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='products',
        null=True,  # ← добавляем, чтобы старые записи не ломались
        blank=True  # ← можно добавить, если используешь формы
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]
        permissions = [
        ('can_unpublish_product', 'Может отменять публикацию продукта')
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
