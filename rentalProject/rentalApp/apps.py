from django.apps import AppConfig


class RentalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rentalApp'

    def ready(self):
        import rentalApp.signals