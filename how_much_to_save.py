"""How much money do you need to save/month to get X in Y year?"""
from datetime import datetime

def how_much_money(year, month, money):
    now = datetime.now()
    final_year = (year - int(now.year)) * 12
    final_month = month - int(now.month)
    if final_month < 0:
        pos_month = 12 - final_month
        return "You will have to save", round(money / (final_year + pos_month)), "each month."
    else:
        return "You will have to save", round(money / (final_year + final_month)), "each month."


print(how_much_money(2020,3,1000))
