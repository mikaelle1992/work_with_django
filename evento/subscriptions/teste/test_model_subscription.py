from django.test import TestCase
from evento.subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Mikaelle Rubia Pinheiro Sousa',
            cpf='05792803579',
            email='mikaelle.rubia@outlook.com',
            phone='73981164664'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Mikaelle Rubia Pinheiro Sousa', str(self.obj))