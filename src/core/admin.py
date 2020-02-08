from django.contrib import admin
from .models import Project, Expense, Category


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields if field.name != "id"]

    class Meta:
        model = Project


class ExpenseModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Expense._meta.fields if field.name != "id"]

    class Meta:
        model = Expense


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = Category


admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Expense, ExpenseModelAdmin)
admin.site.register(Category, CategoryModelAdmin)

