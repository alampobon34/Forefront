from django.core.management import call_command
from django.core.management.base import BaseCommand
from tqdm import tqdm


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Creating tables"))
        call_command('makemigrations')
        call_command('migrate')

        self.stdout.write(self.style.SUCCESS('Table created successfully'))
        self.stdout.write(self.style.SUCCESS('Running basic setup'))
        progess_bar = tqdm(desc="Processing", total=1)

        self.stdout.write(self.style.SUCCESS('Data added successfully'))

        progess_bar.close()


