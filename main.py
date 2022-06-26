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
    passcard = Passcard.objects.all()[25]
    visits = Visit.objects.filter(passcard=passcard)

    print('\n')
    print(visits)
    # for visit in remaining_visits:
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

    for query in connection.queries:
        print('\n')
        pprint(query)
    # pprint(connection.queries[0])

    print('\n')


if __name__ == '__main__':
    main()
