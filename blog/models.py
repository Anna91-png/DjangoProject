from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog_previews/', blank=True, null=True, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
