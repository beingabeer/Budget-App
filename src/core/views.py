from django.shortcuts import render, get_object_or_404
from .models import Project, Expense, Category
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .forms import ExpenseForm
import json


def project_list(request):
    project_list = Project.objects.all()
    return render(request, "project-list.html", {"project_list": project_list})


def project_detail(request, slug):

    project = get_object_or_404(Project, slug=slug)

    if request.method == "GET":
        category_list = Category.objects.filter(project=project)
        return render(
            request,
            "project-detail.html",
            {
                "project": project,
                "expense_list": project.expenses.all(),
                "category_list": category_list,
            },
        )

    elif request.method == "POST":
        # Create and process the form
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            amount = form.cleaned_data["amount"]
            category_name = form.cleaned_data["category"]

            category = get_object_or_404(Category, project=project, name=category_name)

            Expense.objects.create(
                project=project, title=title, amount=amount, category=category
            ).save()

    elif request.method == "DELETE":
        id = json.loads(request.body)["id"]
        expense = Expense.objects.get(id=id)
        expense.delete()

        return HttpResponse("")

    return HttpResponseRedirect(slug)


class ProjectCreateView(CreateView):
    model = Project
    template_name = "add-project.html"
    fields = ("name", "budget")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST["categoriesString"].split(",")
        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id), name=category
            ).save()

        return HttpResponseRedirect(self.get_success_url())

