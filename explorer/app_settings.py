from django.conf import settings

# Required
EXPLORER_CONNECTION_NAME = getattr(settings, 'EXPLORER_CONNECTION_NAME', None)
EXPLORER_CONNECTION_PII_NAME = getattr(
    settings, 'EXPLORER_CONNECTION_PII_NAME', None)

# Change the behavior of explorer
EXPLORER_SQL_BLACKLIST = getattr(settings, 'EXPLORER_SQL_BLACKLIST', ('ALTER', 'RENAME ', 'DROP', 'TRUNCATE',
                                 'INSERT INTO', 'UPDATE', 'REPLACE', 'DELETE', 'CREATE TABLE', 'SCHEMA', 'GRANT', 'OWNER TO'))
EXPLORER_SQL_WHITELIST = getattr(
    settings, 'EXPLORER_SQL_WHITELIST', ('CREATED', 'DELETED', 'REGEXP_REPLACE'))
EXPLORER_DEFAULT_ROWS = getattr(settings, 'EXPLORER_DEFAULT_ROWS', 1000)
EXPLORER_SCHEMA_EXCLUDE_APPS = getattr(settings, 'EXPLORER_SCHEMA_EXCLUDE_APPS', (
    'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.admin'))
EXPLORER_TRANSFORMS = getattr(settings, 'EXPLORER_TRANSFORMS', [])
EXPLORER_PERMISSION_VIEW = getattr(
    settings, 'EXPLORER_PERMISSION_VIEW', lambda u: u.is_staff)
EXPLORER_PERMISSION_CHANGE = getattr(
    settings, 'EXPLORER_PERMISSION_CHANGE', lambda u: u.is_staff)
EXPLORER_RECENT_QUERY_COUNT = getattr(
    settings, 'EXPLORER_RECENT_QUERY_COUNT', 10)
CSV_DELIMETER = getattr(settings, "EXPLORER_CSV_DELIMETER", ",")

# API access
EXPLORER_TOKEN = getattr(settings, 'EXPLORER_TOKEN', 'CHANGEME')
# These are callable to aid testability by dodging the settings cache.
# There is surely a better pattern for this, but this'll hold for now.


def EXPLORER_GET_USER_QUERY_VIEWS(): return getattr(
    settings, 'EXPLORER_USER_QUERY_VIEWS', {})


def EXPLORER_TOKEN_AUTH_ENABLED(): return getattr(
    settings, 'EXPLORER_TOKEN_AUTH_ENABLED', False)


# Async task related. Note that the EMAIL_HOST settings must be set up for email to work.
ENABLE_TASKS = getattr(settings, "EXPLORER_TASKS_ENABLED", False)
S3_ACCESS_KEY = getattr(settings, "EXPLORER_S3_ACCESS_KEY", None)
S3_SECRET_KEY = getattr(settings, "EXPLORER_S3_SECRET_KEY", None)
S3_BUCKET = getattr(settings, "EXPLORER_S3_BUCKET", None)
FROM_EMAIL = getattr(settings, 'EXPLORER_FROM_EMAIL',
                     'django-sql-explorer@example.com')
