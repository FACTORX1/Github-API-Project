from django.db import models
from datetime import datetime
# Create your models here.

class GithubUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, null=True)
    blog = models.CharField(max_length=200, null=True)
    public_posts = models.IntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    followers = models.IntegerField(null=True)
    following = models.IntegerField(null=True)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        if(self.username):
            return str(self.username)
        else:
            return str(self.user_id)