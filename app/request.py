
import urllib.request
import json
from .models import Popular
import app
base_url = None


def configure_request(app):

    global base_url
    base_url = app.config['BASE_URL']


def get_quote(name):

    get_quote_url = base_url.format(name)
    with urllib.request.urlopen(get_quote_url) as url:

        get_quote_url_data = url.read()

        get_quote_response = json.loads(get_quote_url_data)

        quote_results = None

        quote_results = process_quote_results(get_quote_response)

    return quote_results


def process_quote_results(quote_list):

    quote_results = []

    for key, value in quote_list.items():
        if key == 'author':
            author = value

            quote_results.append(author)

        if key == 'quote':
            quote = value
            quote_results.append(quote)

    return quote_results
