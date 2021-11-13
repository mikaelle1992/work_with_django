from django.shortcuts import render

from evento.subscriptions.forms import subscriptionForm


def subscribe(request):
    context = {'form': subscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)