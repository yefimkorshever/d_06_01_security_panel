import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


def main():
    passcards = Passcard.objects.all()
    print(
        f'owner_name: {passcards[0].owner_name}',
        f'passcode: {passcards[0].passcode}',
        f'created_at: {passcards[0].created_at}',
        f'is_active: {passcards[0].is_active}',
        sep='\n'
    )


if __name__ == '__main__':
    main()
