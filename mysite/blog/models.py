from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0,"Проект"),
    (1,"Опубликовано")
)

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField('Время обновления',auto_now= True)
    content = models.TextField('Текст')
    created_on = models.DateTimeField('Время создания', auto_now_add=True)
    status = models.IntegerField('Статус', choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField('Имя',max_length=80)
    email = models.EmailField()
    body = models.TextField("Комментарий")
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Комментарий {} от {}'.format(self.post, self.name)