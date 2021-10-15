import json


def parse_response(func):
    """
    Convert response to dict
    """

    def parse(*args):
        _params = list(args)
        if not isinstance(_params[0], dict):
            _params[0] = json.loads(_params[0])
        return func(*args)

    return parse


def _have_json(response_items, value_items):
    for item in response_items:
        if isinstance(item[1], dict):
            _items = list(item[1].items())
            if value_items in _items:
                return True
            else:
                return _have_json(_items, value_items)
        else:
            return False


def _have_key(response, key):
    for value in response.values():
        if isinstance(value, dict):
            if value.get(key):
                return True
            else:
                return _have_key(value, key)
        else:
            return False
