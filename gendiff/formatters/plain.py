from gendiff.utils import resolve_none_and_boolean
import os


def resolve_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, dict):
        return '[complex value]'
    return resolve_none_and_boolean(value)


def make_plain(diff):
    lines = []

    def walk(items, path):
        for item in items:
            item_path = os.path.join(path, item["key"])
            item_path = os.path.normpath(item_path).replace("/", ".")
            if item.get("nested"):
                walk(item["nested"], item_path)
            else:
                lines.append(make_line(item, item_path))

    walk(diff, '')
    lines = filter(None, lines)
    return "\n".join(lines)


def make_line(item, path):
    status = item["status"]
    if status == 'added':
        new_value = resolve_value(item["new_value"])
        return f"Property '{path}' was added with value: {new_value}"
    elif status == 'removed':
        return f"Property '{path}' was removed"
    elif status == 'updated':
        old_value = resolve_value(item["old_value"])
        new_value = resolve_value(item["new_value"])
        return f"Property '{path}' was updated. From {old_value} to {new_value}"
