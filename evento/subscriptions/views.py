from django.contrib import messages
from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from evento.subscriptions.forms import SubscriptionForm
from django.core import mail


def subscribe(request):
    if request.method == 'POST':
        return create(request)

    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})
    # send email
    _send_email('subscriptions/subscription_email.txt', form.cleaned_data,
                'Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, form.cleaned_data['email'])

    # sucess feedback
    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')


def new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


def _send_email(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])

# MESSAGE = """
# Olá! tudo bem?

# Muito Obrigada por se inscrever no Eventex.

# Esses foram os dados que você nos forneceu
# em sua inscrição

# Nome: Mikaelle Rubia Pinheiro Sousa
# CPF: 05792803579
# Email: mikaelle.rubia@outlook.com
# Telefone: 73981164664

# Em até 48 horas úteis, a nossa equipe entrará em
# contato com você para concluirmos a sua matrícula.

# Atenciosamente,
# --
# Morena Santana

# """
