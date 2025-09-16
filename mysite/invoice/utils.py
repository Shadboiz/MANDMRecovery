import datetime
import random

def generate_invoice_number():
    now = datetime.datetime.now()
    date_part = now.strftime('%Y%m%d%H%M%S')  # e.g., 20250427153045
    random_part = random.randint(1000, 99999)  # Random 4 digits
    return f"INV-{date_part}-{random_part}"

def get_date_string():
    now = datetime.datetime.now()
    invoice_date = now.strftime('%d / %m / %Y')  # e.g., 27 / 04 / 2025
    return invoice_date