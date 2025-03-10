from datetime import date

def get_current_season():
    current_year = date.today().year
    next_year = current_year + 1
    return f"{current_year}/{next_year}"