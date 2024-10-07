from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name:", max_length=50, error_messages={
        "required": "Your name should not be empty!",
        "max_length": "Please enter a shorter name!"
    })