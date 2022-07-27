def arithmetic_arranger(data: list, show_result=False):
    # Maps the length of the largest element, and returns the width for later formatting
    width = tuple(map(lambda x: len(max(x.split(), key=len)) + 2, data))
    total = []
    top = []
    bottom = []
    # Checks if there are not too many problems to solve
    if len(data) > 5:
        return "Error: Too many problems."
    for x in data:
        a, b, op = x.split()[0], x.split()[2], x.split()[1]
        top.append(a)
        bottom.append((op, b))
        # Checks the length of the numbers provided, they must be mot more than 4 digits
        if len(a) > 4 or len(b) > 4:
            return "Error: Numbers cannot be more than four digits."
        try:
            total.append(__apply_operator(a, op, b))
        except ValueError:
            return "Error: Numbers must only contain digits."
        except KeyError:
            return "Error: Operator must be '+' or '-'."
    return __get_formated(top, bottom, width, total, show_result)


def __apply_operator(a, op, b):
    """Extracts provided operator and conducts calculation"""
    __operator = {"-": "sub", "+": "add"}
    method = '__%s__' % __operator[op]  # creates a double score operator __operator__
    return getattr(int(a), method)(int(b))  # uses (a).__operator__(b) for calculation


def __get_formated(top, bottom, width, total, show_result):
    string = ""
    count = 0
    for a in top:
        string += f"{a:>{width[count]}}    "
        count += 1
    string = string.rstrip() + "\n"
    count = 0
    for op, b in bottom:
        string += f"{op}{b:>{width[count] - 1}}    "
        count += 1
    string = string.rstrip() + "\n"
    count = 0
    for x in range(len(width)):
        for y in range(width[count]):
            string += "-"
        string += "    "
        count += 1
    string = string.rstrip() + "\n"
    if show_result:
        count = 0
        for a in total:
            string += f"{a:>{width[count]}}    "
            count += 1
    return string.rstrip()
