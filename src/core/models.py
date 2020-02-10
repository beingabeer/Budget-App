from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def budget_left(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount

        return self.budget - total_expense_amount

    def total_transactions(self):
        expense_list = Expense.objects.filter(project=self)
        return expense_list.count()

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Project, self).save(*args, **kwargs)


class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Expense(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="expenses"
    )
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.title


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    queryset = Project.objects.filter(slug=slug).order_by("-id")
    exists = queryset.exists()
    if exists:
        new_slug = f"{slug}-{queryset.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Project)
