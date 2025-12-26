def get_median_font_size(font_sizes):
    if not font_sizes:
        return None
    sorted_font_sizes = sorted(font_sizes)
    n = len(sorted_font_sizes)
    if n % 2 == 0:
        return sorted_font_sizes[n // 2 - 1]

    else:
        return sorted_font_sizes[n // 2]
