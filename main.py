import os
from pprint import pprint

import django
from django.db import connection, reset_queries


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit, Passcard  # noqa: E402


def main():
    print('\n')
    reset_queries()
    visits = Visit.objects.all()
    long_visits = [visit for visit in visits if visit.is_long(1000)]
    print(f'Visits more than 1000 minutes ({len(long_visits)})')
    print(long_visits)

    # print(visits)
    # passcard = Passcard.objects.all()[25]
    # visits = Visit.objects.filter(passcard=passcard)
    # # for visit in remaining_visits:
    #     print(visit.passcard.owner_name)
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

    # for query in connection.queries:
    #     print('\n')
    #     pprint(query)
    # pprint(connection.queries[0])

    print('\n')


if __name__ == '__main__':
    main()
