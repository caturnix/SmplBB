from django.db import models

# Create your models here.


class User(models.Model):
    username=models.CharField(max_length=200)

    def __unicode__(self):
        return self.username


class Topic(models.Model):
    def __unicode__(self):
        return self.title

    author=models.ForeignKey(User)
    title=models.TextField(max_length=2000)
    description=models.TextField(max_length=400)
    pub_date=models.DateTimeField('topic creation date')


class Post(models.Model):
    author=models.ForeignKey(User)
    topic=models.ForeignKey(Topic)
    content=models.TextField(max_length=65535)
    pub_date=models.DateTimeField('post date')

    def __unicode__(self):
        return self.content