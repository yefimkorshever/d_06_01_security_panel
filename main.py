import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


def main():
    passcards = Passcard.objects.all()
    active_passcards = [
        passcard for passcard in passcards
        if passcard.is_active
    ]
    print(
        f'Всего пропусков: {Passcard.objects.count()}',
        f'Активных пропусков: {len(active_passcards)}',
        sep='\n'
    )


if __name__ == '__main__':
    main()
