import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from faker import Faker
from second_app.models import User

fake = Faker()

# The below code should be in populate script
for i in range(10):
    fname, lname = fake.name().split()
    mail = fake.free_email()
    user = User(
        first_name=fname,
        last_name=lname,
        email=mail
    )
    user.save()
