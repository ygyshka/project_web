from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):

    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=255, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    date_create = models.DateTimeField(verbose_name='дата создания', auto_now=True)
    to_published = models.BooleanField(verbose_name='Опубликовать?')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} {self.content} {self.date_create} {self.to_published} {self.view_count}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
