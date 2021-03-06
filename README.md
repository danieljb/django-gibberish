# Gibberish #

Turn perfectly proofread sites into a dyslectic paradise.

Gibberish is a django template tag to insert typos to your texts.

## Installation #

Install using `pip`:

    pip install -e git+http://github.com/danieljb/django-gibberish.git#egg=gibberish

Add `'gibberish'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        …
        'gibberish',
    )

## Usage #

Use gibberish in templates like this:

	# index.html
	{% load gibberish %}
	{% gibberish %}
	<h2>Hello World</h2>
	{% endgibberish %}

This might result someting like the following markup:

	# index.html
	<h2>Hlelo World</h2>

## Configuration #

The following options are available in your project’s `settings.py` file:

#### `GIBBERISH_FREQUENCY` #

Determines the gibberish modification rate, e.g. 4 samples `TOTAL_WORDS /4`.

Defaults to `3`.

#### `GIBBERISH_CHUNK_LENGTH` #

Set `GIBBERISH_CHUNK_LENGTH` to a lower value to improve readability. Accepted values are >= 2.

Defaults to `3`.

#### `GIBBERISH_URL_FLAG` #

The flag used as a GET parameter to switch gibberish on and off. Gibberish is enabled as long as any string is passed as the flag’s value, e.g. gibberish would be activated like this:

	http://127.0.0.1:8000/?g=ibberish

The following values disable gibberish:

* `0`
* `False`

Defaults to `g`.

## Todos #

* Tests
* Documentation
* Caching

## Disclaimer #

Note that this app currently is in alpha status. Since there was no excessive testing neither are test cases implemented, it might not work as expected in some situations. It seems to be working fine for me though.

## Copyright #

Django Gibberish is distributed under GNU General Public License. 
You should have received a copy of the GNU General Public License along with django-gibberish.  
If not, see <http://www.gnu.org/licenses/>.

Copyright (c) 2014, Daniel J. Becker
