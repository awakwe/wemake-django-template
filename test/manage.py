#!/usr/bin/env python
import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')


def main() -> None:
    """
    Main function.

    It does several things:
    1. Sets default settings module, if it is not set
    2. Warns if Django is not installed
    3. Executes any given command
    """
    if 'DJANGO_SETTINGS_MODULE' not in os.environ:
        raise ValueError(
            "DJANGO_SETTINGS_MODULE environment variable is not set")

    try:
        from django.core import management
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and " +
            'available on your PYTHONPATH environment variable? Did you ' +
            'forget to activate a virtual environment?',
        )

    management.execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
