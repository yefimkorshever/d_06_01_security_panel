import os
from pprint import pprint

import django
from django.db import connection, reset_queries
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit, Passcard  # noqa: E402


def main():
    reset_queries()
    remaining_visits = Visit.objects.filter(leaved_at=None)

    print('\n')
    for visit in remaining_visits:
        print(visit.passcard)
    #     now = localtime()
    #     entry = localtime(visit.entered_at)
    #     period = now - entry
    #     print(
    #         'Entered storage, Moscow time:',
    #         entry,
    #         'Remains in storage:',
    #         period,
    #         sep='\n'
    #     )

    print('\n')
    pprint(connection.queries[0])


if __name__ == '__main__':
    main()
