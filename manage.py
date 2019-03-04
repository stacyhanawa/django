# This is all boilerplate, don't touch this file for now!
import sys
import os
from django.conf import settings
from django.core.management import execute_from_command_line

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF='urls',
        STATIC_URL='static/',
        STATIC_ROOT=os.path.join(BASE_DIR, 'static'),
        INSTALLED_APPS=[
            'django.contrib.staticfiles',
        ],
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
        }],
    )

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
