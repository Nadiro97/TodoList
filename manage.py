#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')
=======
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project3.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'commerce.settings')
>>>>>>> 70db9d68f73573ece0e788de4b8a3904fd58a66b
>>>>>>> f3631a0ed60b9932d75f71ff6f787c58c93ac0bb
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
    main()
