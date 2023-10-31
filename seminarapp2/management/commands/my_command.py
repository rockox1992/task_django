from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'Hello world!' to output."

    def handle(self, *args, **kwargs):
        self.stdout.write('Вместо привычного print необходимо использовать self.stdout.write '
                          'для печати информации в стандартный поток вывода - консоль.')
