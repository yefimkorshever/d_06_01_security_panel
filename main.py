import os
from pprint import pprint

import django
from django.db import connection, reset_queries

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit  # noqa: E402


def main():
    reset_queries()
    remaining_visitors = Visit.objects.filter(leaved_at=None)
    print('\n')
    print(remaining_visitors)
    print('\n')
    pprint(connection.queries[0])


if __name__ == '__main__':
    main()
