
from .conf import settings as gibberish_settings


URL_FLAG = getattr(gibberish_settings, 'URL_FLAG')


class GibberishMiddleware(object):
    def process_request(self, request):
        request_g = request.GET.get(URL_FLAG, None)
        if request_g in [0, "0", False, "False"]:
            request.session.pop('gibberish', None)
        elif request_g:
            request.session['gibberish'] = True
        return None
