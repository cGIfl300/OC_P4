def convert_to_integer(value):
    try:
        value = int(value)
    except ValueError:
        return None
    return value
