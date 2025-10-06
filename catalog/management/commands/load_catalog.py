import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Загружает категории и продукты из catalog_data.json'

    def handle(self, *args, **options):
        try:
            with open('catalog_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Файл catalog_data.json не найден!'))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Ошибка в формате JSON!'))
            return

        # Если data это словарь с категориями и продуктами
        if isinstance(data, dict):
            categories = data.get('categories', [])
            products = data.get('products', [])
        # Если data это просто список категорий
        elif isinstance(data, list):
            categories = data
            products = []
        else:
            self.stdout.write(self.style.ERROR('Неизвестный формат данных в JSON!'))
            return

        # Сначала создаём категории
        for cat in categories:
            obj, created = Category.objects.get_or_create(
                name=cat['name'],
                defaults={'description': cat.get('description', '')}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Категория "{obj.name}" создана'))

        # Затем создаём продукты
        for prod in products:
            try:
                category = Category.objects.get(name=prod['category'])
            except Category.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Категория "{prod["category"]}" не найдена для продукта "{prod["name"]}"'))
                continue

            obj, created = Product.objects.get_or_create(
                name=prod['name'],
                defaults={
                    'price': prod.get('price', 0),
                    'category': category
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт "{obj.name}" создан'))

        self.stdout.write(self.style.SUCCESS('Загрузка
        self.stdout.write(self.style.SUCCESS('Загрузка завершена!'))

