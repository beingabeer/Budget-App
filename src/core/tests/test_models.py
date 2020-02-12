from django.test import TestCase
from core.models import Project, Category, Expense
from django.contrib.auth.models import User


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.project1 = Project.objects.create(
            owner=self.user, name="Project 1", budget=5000
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEqual(self.project1.slug, "project-1")

    def test_budget_left(self):
        category1 = Category.objects.create(project=self.project1, name="development")

        Expense.objects.create(
            project=self.project1, title="expense1", amount=1000, category=category1
        )

        Expense.objects.create(
            project=self.project1, title="expense2", amount=3000, category=category1
        )

        self.assertEqual(self.project1.budget_left(), 1000)

    def test_project_total_transaction(self):
        project2 = Project.objects.create(
            owner=self.user, name="Project2", budget=10000
        )

        category1 = Category.objects.create(project=self.project1, name="development")

        Expense.objects.create(
            project=self.project1, title="expense1", amount=1000, category=category1
        )

        Expense.objects.create(
            project=project2, title="expense2", amount=3000, category=category1
        )

        self.assertEqual(self.project1.total_transactions(), 1)
