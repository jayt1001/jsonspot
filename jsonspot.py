from .comDef import parse_response, _have_json, _have_key


@parse_response
def have_key(response, key, global_search=FutureWarning):
    if response.get(key):  # 找到了key就直接返回
        return True
    elif global_search:  # 看是否全局
        return _have_key(response, key)
    return False


@parse_response
def is_expect(response, expect_dict):
    return response == expect_dict


@parse_response
def have_json(response, value, global_search=False):
    response_items = list(response.items())
    if isinstance(value, dict):
        if len(value) == 1:
            value_items = list(value.items())[0]
            if value_items in response_items:
                return True
            elif global_search:
                return _have_json(response_items, value_items)
            return False


@parse_response
def more_comparison(response, expect_list):
    """
    多条件比较
    """
    result_list = []
    for expect in expect_list:
        expect_data = expect['data']
        expect_len = len(expect_data)
        if isinstance(expect_data, (list, tuple, dict)) and expect_len > 0:  # 代表只验证key是否存在
            result_list.append(_more_equal_have_key(response, expect_data, 0, expect_len, expect['equal']))
        else:
            result_list.append(False)
    return result_list


def _more_equal_have_key(res_data, expect_data, index, expect_len, equal):
    _data = expect_data[index]
    if isinstance(_data, dict):
        return have_json(res_data, _data)
    else:
        res_data = res_data.get(expect_data[index])
        if res_data:
            if index + 1 == expect_len:  # 代表遍历到最后一个元素且正确了
                return equal
            elif isinstance(res_data, dict):
                return _more_equal_have_key(res_data, expect_data, index + 1, expect_len, equal)
            return False
        return not equal






