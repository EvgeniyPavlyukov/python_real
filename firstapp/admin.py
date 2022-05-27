from django.contrib import admin
from firstapp.models import Order, StatusCRM, CommentCrm

# Register your models here.
admin.site.register(Order)
admin.site.register(StatusCRM)
admin.site.register(CommentCrm)