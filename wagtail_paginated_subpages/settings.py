

from django.conf import settings

def get(key, default):
  return getattr(settings, key, default)


PAGINATION_REDIRECT_INDEX_TO_ROOT = get(
    'PAGINATION_REDIRECT_INDEX_TO_ROOT',
    True
)

PAGINATION_PAGE_SIZE_DEFAULT = get(
    'PAGINATION_PAGE_SIZE_DEFAULT',
    12
)

PAGINATION_DEFAULT_PAGE_SIZES = get(
    'PAGINATION_DEFAULT_PAGE_SIZES',
    [12, 24, 48, 96]
)
