
import re, random

from django import template
from django.template.base import Node
from django.utils.html import strip_tags

from ..conf import settings as gibberish_settings


FREQUENCY = getattr(gibberish_settings, 'FREQUENCY')
CHUNK_LENGTH = getattr(gibberish_settings, 'CHUNK_LENGTH')

register = template.Library()


def gibberishify(text, chunk_length=CHUNK_LENGTH):
    def chunk(text, size):
        return map(None, *([iter(text)] * size))

    return (
        text[0] +
        u''.join([
            u''.join(random.sample(
                [i for i in n if i is not None], 
                len([i for i in n if i is not None]))
            )
            for n in chunk(text[1:-1], chunk_length)
        ]) +
        text[-1]
    )


class GibberishNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        random_words = re.compile('\w{4,}').findall(strip_tags(output))
        gibberished_wordmap = map(
            lambda x: [x, gibberishify(x, chunk_length=CHUNK_LENGTH)], 
            random.sample(random_words, int(len(random_words) /FREQUENCY))
        )
        for word, gibberish in gibberished_wordmap:
            output = output.replace(word, gibberish, 1)
        return output


@register.tag
def gibberish(parser, token):
    nodelist = parser.parse(('endgibberish',))
    parser.delete_first_token()
    return GibberishNode(nodelist)
