#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Add the project directory to sys.path
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_booking_system.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_booking_system.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    main()
