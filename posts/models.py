from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'
    name = models.CharField(
        'Name', blank= False, null= False , max_length= 20, db_index= True, default= 'Anonymous'
    )
    body = models.CharField(
        'Body', blank= False, null= False , max_length= 200, db_index= True,
    )
    created_at = models.DateTimeField(
        'Created_at' , blank= True, auto_now_add=True
    )
    files = models.FileField(
        'Files', blank=True, null=True, # db_index= True
    )
    likes = models.PositiveIntegerField(
        'Likes'
    )