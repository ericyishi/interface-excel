
class global_var(object):
    """将列名与列号匹配"""
    # case_id
    Id = '0'
    url = '1'
    run = '2'
    request_way = '3'
    header = '4'
    case_depend = '5'
    data_depend = '6'
    field_depend = '7'
    data = '8'
    expect = '9'
    result = '10'

# ��ȡcaseid


def get_id():
    return global_var.Id

# ��ȡurl


def get_url():
    return global_var.url

# ��ȡrun


def get_run():
    return global_var.run

# ��ȡrequest_way


def get_request_way():
    return global_var.request_way

# ��ȡheader


def get_header():
    return global_var.header

# ��ȡcase_depend


def get_case_depend():
    return global_var.case_depend

# ��ȡdata_depend


def get_data_depend():
    return global_var.data_depend

# ��ȡfield_depend


def get_field_depend():
    return global_var.field_depend

# ��ȡdata


def get_data():
    return global_var.data

# ��ȡexpect


def get_expect():
    return global_var.expect

# ��ȡresult


def get_result():
    return global_var.result


def get_header_value():
    header = {
        "header": "1234",
        "cookie": "cody"
    }