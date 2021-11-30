from django.contrib import admin
from django.utils.timezone import now
from evento.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at',
                    'subscribed_today')
    # as colunas de deseja
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'inscrito hoje ?.'
    subscribed_today.boolean = True

# registrar um modelo no admin
admin.site.register(Subscription, SubscriptionModelAdmin)
