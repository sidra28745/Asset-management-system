from .models import Item, IssueItem, ReturnItem
from django.contrib import admin

admin.site.register(Item)
admin.site.register(IssueItem)
admin.site.register(ReturnItem)