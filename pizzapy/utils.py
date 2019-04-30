import requests
import xmltodict

def request_json(url, **kwargs):
    """Send a GET request to one of the API endpoints that returns JSON.
    Send a GET request to an endpoint, ideally a URL from the urls module.
    The endpoint is formatted with the kwargs passed to it.
    This will error on an invalid request (requests.Request.raise_for_status()), but will otherwise return a dict.
    """
    r = requests.get(url.format(**kwargs))
    r.raise_for_status()
    return r.json()


def request_xml(url, **kwargs):
    """Send an XML request to one of the API endpoints that returns XML.
    
    This is in every respect identical to request_json. 
    """
    r = requests.get(url.format(**kwargs))
    r.raise_for_status()
    return xmltodict.parse(r.text)
