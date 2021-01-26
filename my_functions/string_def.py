def substring_after(pattern, string):
    ret_string = string
    first = string.find(pattern)
    if first != -1:
        ret_string = string[first: len(string)]
    return ret_string


def substring_after_last(pattern, string):
    ret_string = string
    last = string.rfind(pattern)
    if last != -1:
        ret_string = string[last: len(string)]
    return ret_string


def substring_before(pattern, string):
    ret_string = string
    first = string.find(pattern)
    if first != -1:
        ret_string = string[: first]
    return ret_string


def substring_before_last(pattern, string):
    ret_string = string
    last = string.rfind(pattern)
    if last != -1:
        ret_string = string[: last]
    return ret_string


def header_replace(in_string, file_name):
    name = substring_before_last(".", file_name)
    phase_name = name.upper()
    class_name = name[0].capitalize() + name[1:]
    ret_string = in_string.replace("ClassName", class_name)
    ret_string = ret_string.replace("PHASE_NAME", phase_name)
    ret_string = ret_string.replace("phaseName", name.lower())
    return ret_string
