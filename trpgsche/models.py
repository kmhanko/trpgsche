from django.conf import settings
from django.db import models
#from django.utils import timezone

# Create your models here.
class Post(models.Model): #モデルであり、DjangoのModelをおそらく継承している
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self): #公開のためのメソッド
        self.save()

    def __str__(self): #ポストのタイトルを返すメソッド
        return self.title