from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Mikaelle Rubia Pinheiro Sousa', cpf='05792803579',
                    email='mikaelle.rubia@outlook.com', phone='73981164664')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self. email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'mikaelle.rubia@outlook.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['mikaelle.rubia@outlook.com', 'mikaelle.rubia@outlook.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
                'Mikaelle Rubia Pinheiro Sousa',
                '05792803579',
                'mikaelle.rubia@outlook.com',
                '73981164664'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

        # self.assertIn('Mikaelle Rubia Pinheiro Sousa', self.email.body)
        # self.assertIn('05792803579', self.email.body)
        # self.assertIn('mikaelle.rubia@outlook.com', self.email.body)
        # self.assertIn('73981164664', self.email.body)
