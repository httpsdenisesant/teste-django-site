from django.test import TestCase
from django.urls import reverse

class TesteMinhaPagina(TestCase):
    def test_RenderHtml(self):
        res = self.client.get(reverse('myview'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res,'Seja Bem-Vindo')