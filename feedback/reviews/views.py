from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

# Create your views here.

def review(request):
    if request.method == "POST":
        existing_review = Review.objects.all()[0]
        form = ReviewForm(request.POST, instance=existing_review)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })
    

def thank_you(request):
    return render(request, "reviews/thank_you.html")
