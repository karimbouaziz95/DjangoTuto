from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_birthdays = {
    "january": "Jenya Korkeshko",
    "february": "Sbou3i",
    "march": "Tarak Bouaziz",
    "april": "Chayma Bouaziz",
    "may": "Looouzen",
    "june": "Mee & Hamdi",
    "july": "Kush",
    "august": None,
    "september": "Nejah ben Rhaiem",
    "october": None,
    "november": None,
    "december": "Mom & Dad <3"
}

months_by_number = {
    1: "january",
    2: "february",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10: "october",
    11:"november",
    12: "december"
}

# Create your views here.

def index(request):
    months = list(monthly_birthdays.keys())
    return render(
        request, "challenges/index.html", {
            "months": months,
        }
    )


def monthly_challenge(request, month):
    try:
        persons = monthly_birthdays[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "persons": persons
        })
    except:
        #response_data = render_to_string("404.html")
        #return HttpResponseNotFound(response_data)
        # OR
        raise Http404() # For this 404.html in templates SHOULD be there

def monthly_challenge_by_number(request, month):
    try:
        redirect_path = reverse("month-challenge-url", args=[months_by_number[month]]) # dynamically changed to:  /challenges/
        return HttpResponseRedirect(redirect_path)   # Redirect to another url
    except:
        return HttpResponse(f"<h1>Your lucky number is: {month}</h1>")
