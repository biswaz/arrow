from django.apps import AppConfig


class ForwarderConfig(AppConfig):
    name = 'forwarder'
    verbose_name = "Forwarder"
    icon = '<i class="material-icons">business_center</i>'

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
