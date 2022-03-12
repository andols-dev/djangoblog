from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    def comments(self):
        return self.comment_set.all()
    
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(verbose_name="comment", max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    

    def __str__(self):
        return self.content    
