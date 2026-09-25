#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zariya_jewellry.settings')
    try:
        from django.core.management import execute_from_command_line
        # Bypassing the database version check for older MariaDB/MySQL
        import django
        from django.db.backends.base.base import BaseDatabaseWrapper
        BaseDatabaseWrapper.check_database_version_supported = lambda self: None
        
        # MariaDB 10.4 fix for Django 5+
        from django.db.backends.mysql.features import DatabaseFeatures
        DatabaseFeatures.can_return_rows_from_bulk_insert = property(lambda self: False)
        DatabaseFeatures.can_return_columns_from_insert = property(lambda self: False)
        DatabaseFeatures.has_select_for_update_skip_locked = property(lambda self: False)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
