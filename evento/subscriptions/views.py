from django.conf import settings
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from evento.subscriptions.forms import SubscriptionForm
from django.core import mail
from evento.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    # passando os dados de form.cleaned_data para o create do banco
    subscription = Subscription.objects.create(**form.cleaned_data)

    # send email
    _send_email('subscriptions/subscription_email.txt', {'subscription': subscription},
                'Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, subscription.email)

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
        # subscription = Subscription(
        #     name='Mikaelle Rubia Pinheiro Sousa',
        #     cpf='05792803579',
        #     email='mikaelle.rubia@outlook.com',
        #     phone='73981164664'
        # )
    except Subscription.DoesNotExist:
        raise Http404
    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})


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
