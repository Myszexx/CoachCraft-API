from datetime import date

def calculate_age(birthdate):
    return date.today().year - birthdate.year - (
                (date.today().month, date.today().day) < (birthdate.month, birthdate.day))

def is_youth_player(birthdate):
    return calculate_age(birthdate) <= 21

