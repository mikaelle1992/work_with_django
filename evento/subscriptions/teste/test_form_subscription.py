from django.test import TestCase
from evento.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        """Context must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accpet digits."""
        form = self.make_validet_form(cpf='ABC92803579')
        # self.assertFormErroMessage(
        #     form, 'cpf', "CPF deve conter apenas numeros")
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def assertFormErroMessage(self, form, fields, msg):
        erros = form.errors
        erros_list = erros[fields]
        self.assertListEqual([msg], erros_list)
        

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validet_form(cpf='12345')
        # self.assertEqual(['cpf'], list(form.errors))
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        erros = form.errors.as_data()
        erros_list = erros[field]
        exception = erros_list[0]
        self.assertEqual(code, exception.code)

    def make_validet_form(self, **kwargs):
        valid = dict(name='Mikaelle Rubia Pinheiro Sousa',
                     cpf='05792803579',
                     email='mikaelle.rubia@outlook.com',
                     phone='73981164664')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form
