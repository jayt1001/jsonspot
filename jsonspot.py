from comDef import parse_response, _have_json,_have_key

@parse_response
def have_key(response, key, global_search=None):
    if response.get(key):  # 找到了key就直接返回
        return True
    elif global_search:  # 看是否全局
        return _have_key(response, key)
    else:
        return False


@parse_response
def is_expect(response, expect_dict):
    return response == expect_dict

@parse_response
def have_json(response, value, global_search=None):
    response_items = list(response.items())
    if isinstance(value, dict):
        if len(value) == 1:
            value_items = list(value.items())[0]
            if value_items in response_items:
                return True
            elif global_search:
                return _have_json(response_items, value_items)
            else:
                return False





