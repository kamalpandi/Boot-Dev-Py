def format_line(line):
    striped_line = line.strip()
    capitalize = striped_line.upper()
    return capitalize.replace(".","") + "..."
