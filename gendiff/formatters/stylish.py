from itertools import chain
from gendiff.utils import resolve_none_and_boolean

INDENT = '  '
STEP_INDENT = '    '
START_DEPTH = 0
STEP_INSIDE = 1


def make_stylish(diff):
    return format_diff(diff, START_DEPTH)


def format_diff(diff, depth):
    lines = [make_line(elem, depth) if isinstance(elem, dict) else
             make_line({"key": elem,
                        "status": "equal",
                        "old_value": diff.get(elem)}, depth)
             for elem in diff]

    final_result = chain("{", lines, [f"{STEP_INDENT * depth}" + "}"])
    return "\n".join(final_result)


def make_line(diff, depth):
    key = diff["key"]
    status = diff["status"]
    indent = f"{INDENT}{STEP_INDENT * depth}"

    if status == "equal":
        old_value = diff.get("old_value")
        value = resolve_value(old_value, depth)
        return f"{indent}  {key}: {value}"

    elif status == "added":
        new_value = diff.get("new_value")
        value = resolve_value(new_value, depth)
        return f"{indent}+ {key}: {value}"

    elif status == "removed":
        old_value = diff.get("old_value")
        value = resolve_value(old_value, depth)
        return f"{indent}- {key}: {value}"

    elif status == "updated":
        old_value = diff.get("old_value")
        value1 = resolve_value(old_value, depth)

        new_value = diff.get("new_value")
        value2 = resolve_value(new_value, depth)
        return f"{indent}- {key}: {value1}\n{indent}+ {key}: {value2}"

    elif is_nested(diff):
        nested = diff.get("nested")
        value = resolve_value(nested, depth)
        return f"{indent}  {key}: {value}"


def is_nested(elem):
    return elem.get("nested")


def resolve_value(diff, depth):
    if isinstance(diff, (dict, list)):
        return format_diff(diff, depth + STEP_INSIDE)
    return resolve_none_and_boolean(diff)
