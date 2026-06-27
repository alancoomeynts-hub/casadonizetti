from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from .models import Menu, MenuItem, MenuSection


class MenuViewTests(TestCase):

    def test_render_menu(self):
        self.menu = Menu(name="Spring Menu", is_active=True,)
        self.menu.save()

        self.section=MenuSection(menu=self.menu,name="Early Bird", slug="early-bird", sort_order=1,is_active=True,)
        self.section.save()

        self.featured_item=MenuItem(name="Risotto",section=self.section,price=Decimal("20.00"),is_featured=True,)
        self.featured_item.save()

        self.non_featured_item=MenuItem(name="Water",section=self.section,price=Decimal("3.00"),is_featured=False,)
        self.non_featured_item.save()

        response = self.client.get(reverse("menu"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["menu"], self.menu)
        self.assertIn(self.featured_item, response.context["featured_items"])
        self.assertNotIn(self.non_featured_item, response.context["featured_items"])

    def test_menupage_returns_404_when_menu_item_is_missing(self):
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 404)
