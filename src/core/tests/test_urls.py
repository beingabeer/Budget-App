from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import ProjectListView, project_detail, ProjectCreateView


class TestUrls(SimpleTestCase):
    def test_list_url_resolves(self):
        url = reverse("list")
        self.assertEqual(resolve(url).func.view_class, ProjectListView)

    def test_create_project_url_resolves(self):
        url = reverse("add")
        self.assertEqual(resolve(url).func.view_class, ProjectCreateView)

    def test_project_detail_url_resolves(self):
        url = reverse("detail", args=["some-slug-here"])
        print(resolve(url))
        self.assertEquals(resolve(url).func, project_detail)

