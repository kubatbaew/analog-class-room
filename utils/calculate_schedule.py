def calculate_percentage(value, max_value):
    if value:
        return (value / max_value) * 100
    else:
        return 0

def categorize_percentage(percentage):
    if 90 <= percentage <= 100:
        return "Отлично"
    elif 70 <= percentage < 90:
        return "Хорошо"
    elif 50 <= percentage < 70:
        return "Удовлетворительно"
    else:
        return "Не удовлетворительно"
