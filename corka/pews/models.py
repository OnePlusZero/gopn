from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, verbose_name="Автор")
    title = models.CharField(max_length=200,verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")

    created_date = models.DateTimeField(
            default=timezone.now,verbose_name="дата створення")
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name="дата публiкацii")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
