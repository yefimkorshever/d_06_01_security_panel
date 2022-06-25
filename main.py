import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


def main():
    active_passcards = Passcard.objects.filter(is_active=True)

    print(
        f'Всего пропусков: {Passcard.objects.count()}',
        f'Активных пропусков: {len(active_passcards)}',
        sep='\n'
    )


if __name__ == '__main__':
    main()
