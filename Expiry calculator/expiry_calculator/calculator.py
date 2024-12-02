from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_expiry_date(start_date: str, duration: int, unit: str = 'years') -> str:
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    
  
    if unit == 'months':
        expiry_date_obj = start_date_obj + relativedelta(months=+duration)
    elif unit == 'years':
        expiry_date_obj = start_date_obj + relativedelta(years=+duration)
    else:
        raise ValueError("Unit must be 'months' or 'years'.")
    
    # Format the expiry date back into 'YYYY-MM-DD' format
    return expiry_date_obj.strftime('%Y-%m-%d')