def hex_to_rgb(hex_color):
    hex_str = str(hex_color)
    if len(hex_str) == 6 and (is_hexadecimal(hex_str)):
        r = int(hex_str[:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:], 16)
        return r, g, b

    raise Exception("not a hex color string")

# Don't edit below this line


def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False
