from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Добавляет тестовые категории и продукты"

    def handle(self, *args, **options):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаём категории
        electronics = Category.objects.create(name="Electronics", description="Electronic devices")
        books = Category.objects.create(name="Books", description="Various books")

        # Создаём продукты
        Product.objects.create(name="iPhone 15", description="Latest iPhone", price=1200, category=electronics)
        Product.objects.create(name="Harry Potter Book", description="Fantasy book", price=20, category=books)

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно добавлены!"))
