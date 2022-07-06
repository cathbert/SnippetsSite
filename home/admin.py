from django.contrib import admin
from .models import Snippet, Quotes, Theme


admin.site.register(Snippet)
admin.site.register(Quotes)
admin.site.register(Theme)