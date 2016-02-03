from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render
from .forms import NewsletterSignUpForm
# Create your views here.
def home(request):

    title = "Welcome"
    form = NewsletterSignUpForm(request.POST or None)
    context = {
    	"title" : title,
    	"form"  : form
    }

    if form.is_valid():
    	instance = form.save(commit=True)

    ### some custom form validation can be performed
    # instance.full_name = full_name
    # instance.save()
    return render(request, "home.html", context)




