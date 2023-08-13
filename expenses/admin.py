from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'day', 'object_name', 'object_price')
    list_filter = ('date', 'day')

admin.site.register(Expense, ExpenseAdmin)
