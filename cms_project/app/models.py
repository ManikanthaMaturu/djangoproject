from django.db import models
from django.contrib.auth.models import User


# class UserPost(models.Model):
#     username = models.CharField(max_length=100)
#     MobileNumber = models.IntegerField()
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#     objects = models.manager
#
#     class Meta:
#         db_table = "user_table"


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.manager

    class Meta:
        db_table = "post_table"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.manager

    class Meta:
        db_table = "like_table"
