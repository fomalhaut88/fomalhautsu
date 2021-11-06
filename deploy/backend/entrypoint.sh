#!/bin/bash

python manage.py migrate
echo "yes" | python manage.py collectstatic
python manage.py create_superuser -u $SUPERUSER_USERNAME -p $SUPERUSER_PASSWORD -q

exec "$@"
