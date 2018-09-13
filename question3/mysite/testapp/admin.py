

from django.contrib import admin

from testapp.models import feedback
from testapp.models import Post

admin.site.register(feedback)

admin.site.register(Post)

