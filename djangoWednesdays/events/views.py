from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Tony"
    month = month.capitalize()
    month_number = int(list(calendar.month_name).index(month))

    cal = HTMLCalendar().formatmonth(year, month_number)
    now_year = datetime.now().year
    time = datetime.now().strftime('%I:%M:%S %p')

    return render(request, 'home.html', {
        "first_name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "now_year": now_year,
        "time": time,
    })

