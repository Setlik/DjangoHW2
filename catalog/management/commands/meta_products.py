from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Добавляет продукты в базу данных"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        electronics = Category.objects.create(name="Электроника")
        clothing = Category.objects.create(name="Одежда")
        books = Category.objects.create(name="Книги")

        products = [
            {"name": "Ноутбук", "price": 70000, "category": electronics},
            {"name": "Футболка", "price": 1500, "category": clothing},
            {"name": "Книга по Python", "price": 800, "category": books},
            {"name": "Смартфон", "price": 30000, "category": electronics},
            {"name": "Джинсы", "price": 2500, "category": clothing},
        ]

        for product in products:
            Product.objects.create(
                name=product["name"],
                price=product["price"],
                category=product["category"],
            )

        self.stdout.write(self.style.SUCCESS("Продукты успешно добавлены"))
