from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from evento.subscriptions.forms import SubscriptionForm
from django.core import mail


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            body = render_to_string('subscriptions/subscription_email.txt',
                                    form.cleaned_data)

            mail.send_mail('Confirmação de inscrição',
                            body,
                            'contato@eventex.com.br',
                            ['contato@eventex.com.br', form.cleaned_data['email']])
                            #  corpo do email
            messages.success(request, 'Inscrição realizada com sucesso!')

            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html', 
            {'form': form})

    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)

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