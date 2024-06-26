# member/management/commands/import_membership_levels.py

from django.core.management.base import BaseCommand
from member.models import MembershipLevel


class Command(BaseCommand):
    help = 'Import initial membership levels'

    def handle(self, *args, **kwargs):
        levels = [
            ('Junior Basic', 1, 1, 1, 0, 21000),
            ('Junior Plus', 2, 1, 2, 1, 32000),
            ('Junior Ultra', 3, 2, 4, 2, 50000),
            ('Intermediate Basic', 1, 1, 1, 0, 32000),
            ('Intermediate Plus', 2, 1, 2, 1, 40000),
            ('Intermediate Ultra', 2, 2, 4, 2, 60000),
            ('Senior Basic', 1, 1, 1, 0, 35000),
            ('Senior Plus', 2, 1, 2, 1, 48000),
            ('Senior Ultra', 2, 2, 4, 2, 80000),
        ]
        for name, skill_training, problem_solving, competition_guidance, camp, price in levels:
            MembershipLevel.objects.get_or_create(
                name=name,
                defaults={
                    'skill_training': skill_training,
                    'problem_solving': problem_solving,
                    'competition_guidance': competition_guidance,
                    'camp': camp,
                    'price': price
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported membership levels'))
