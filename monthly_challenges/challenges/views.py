from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Jenya Korkeshko",
    "february": "Sbou3i",
    "march": "Tarak Bouaziz",
    "april": "Chayma Bouaziz",
    "may": "Looouzen",
    "june": "Mee & Hamdi",
    "july": "Kush",
    "august": "Don't know aout",
    "september": "Nejah ben Rhaiem",
    "october": "October too",
    "november": "Also novemeber",
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
    months = list(monthly_challenges.keys())
    list_elements_months = ""
    for month in months:
        month_path = reverse("month-challenge-url", args=[month])
        list_elements_months += f"<li><a href='{month_path}' title='{month}'>{month.capitalize()}</a></li>"
    
    response_data = f"<ul>{list_elements_months}</ul>"
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        response_text = monthly_challenges[month]
        response_data = f"<h1>{response_text}</h1>"
    except:
        return HttpResponseNotFound("Not supported")
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    try:
        redirect_path = reverse("month-challenge-url", args=[months_by_number[month]]) # dynamically changed to:  /challenges/
        return HttpResponseRedirect(redirect_path)   # Redirect to another url
    except:
        return HttpResponse(f"<h1>Your lucky number is: {month}</h1>")
