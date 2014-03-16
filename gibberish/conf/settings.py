
from django.conf import settings


FREQUENCY = getattr(settings, 'GIBBERISH_FREQUENCY', 3)
CHUNK_LENGTH = getattr(settings, 'GIBBERISH_CHUNK_LENGTH', 3)
URL_FLAG = getattr(settings, 'GIBBERISH_URL_FLAG', 'g')
