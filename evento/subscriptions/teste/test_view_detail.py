from django.test import TestCase
from evento.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscritonDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Mikaelle Rubia Pinheiro Sousa',
            cpf='05792803579',
            email='mikaelle.rubia@outlook.com',
            phone='73981164664'
        )
        self.resp = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf,
                    self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)

        # self.assertContains(self.resp, 'Mikaelle Rubia Pinheiro Sousa')
        # self.assertContains(self.resp, '05792803579')
        # self.assertContains(self.resp, 'mikaelle.rubia@outlook.com')
        # self.assertContains(self.resp, '73981164664')


class SubscritonNotFoundTest(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, resp.status_code)
