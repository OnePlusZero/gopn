from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, verbose_name="Автор")
    title = models.CharField(max_length=200,verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст пiдзаголовка")
    textcontent = models.TextField(verbose_name="Текст новини", null=True)
    picture = models.ImageField(upload_to='images', blank=True, null=True)
    # slug - поле для формирования
    slug = models.SlugField(max_length=250,unique_for_date='created_date', null=True)

    created_date = models.DateTimeField(
            default=timezone.now,verbose_name="дата створення")
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name="дата публiкацii")

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.created_date.year, self.created_date.month,self.created_date.day, self.slug])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class NewsList(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, verbose_name="Автор")
    title = models.CharField(max_length=200,verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст пiдзаголовка")
    picture = models.ImageField(upload_to='images', blank=True, null=True)
    pdf = models.FileField(upload_to='pdf', null=True)
    slug = models.SlugField(max_length=250,unique_for_date='created_date', null=True)

    created_date = models.DateTimeField(
            default=timezone.now,verbose_name="дата створення")
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name="дата публiкацii")

    def get_absolute_urls(self):
        return reverse('post_details', args=[self.created_date.year, self.created_date.month, self.created_date.day, self.slug])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
