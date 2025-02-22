from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Создает группы пользователей"

    def handle(self, *args, **kwargs):
        group_names = [
            "product_moderator",
        ]

        for name in group_names:
            group, created = Group.objects.get_or_create(name=name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Группа "{name}" успешно создана.')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Группа "{name}" уже существует.')
                )
