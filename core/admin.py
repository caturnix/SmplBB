__author__ = 'Swan'
from django.contrib import admin
from core.models import Topic
from core.models import User
from core.models import Post

admin.site.register(Topic)
admin.site.register(User)
admin.site.register(Post)
