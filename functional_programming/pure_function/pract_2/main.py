from datetime import datetime


def sort_dates(dates: list):
    new_dates = dates.copy()
    sorted_dates = sorted(new_dates, key=parse_date)
    return sorted_dates


def parse_date(date_str):
    return datetime.strptime(date_str, "%m-%d-%Y")
