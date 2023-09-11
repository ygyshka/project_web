from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': "Рыба", 'description': "Морская/речная продукция"},
            {'name': "Мясо", 'description': "Продукция белкового состава"},
            {'name': "Молоко", 'description': "Продукция молочного состава"},
        ]
        # для меньшей нагрузки подключения к бд лучше использовать такой метод передачи данных к модели
        # с дальнейшей записью в бд, в противном случае если идти через цикл по списку и кажэдый item
        # по одному записывать в бд, будет большое количество подключений и это нагрузит бд

        category_for_create = []
        for item in category_list:
            category_for_create.append(
                Category(**item)
            )

        Category.objects.bulk_create(category_for_create)
