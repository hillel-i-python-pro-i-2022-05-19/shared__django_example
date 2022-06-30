import logging
import random

from django.core.management.base import BaseCommand, CommandParser

from apps.humans.models import Human


class Command(BaseCommand):
    help = 'Create humans'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('amount', type=int, )

    def handle(self, *args, **options):
        amount_of_human = options['amount']

        logger = logging.getLogger('create_humans')
        logger.setLevel(logging.INFO)

        logger.info(f'Amount of users before: {Human.objects.count()}')

        for _ in range(amount_of_human):
            human = Human(
                name='',
                age=random.randint(0, 150)
            )
            human.save()

        logger.info(f'Amount of users after: {Human.objects.count()}')
