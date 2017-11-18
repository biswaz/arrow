from django.apps import AppConfig

#using ManagerConfig invokeded a strange error, may be random. Not used as of now
class ManagerConfig(AppConfig):
    name = 'arrow.manager'
    verbose_name = "Manager"
