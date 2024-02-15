from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain


def choose_format(data, format_name):
    match format_name:
        case 'stylish':
            return make_stylish(data)
        case 'plain':
            return make_plain(data)
        case 'json':
            return make_json(data)
        case _:
            raise ValueError(f"Unknown format: {format_name}")
