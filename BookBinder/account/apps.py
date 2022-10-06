from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'account'
    def ready(self):
        import account.signals
