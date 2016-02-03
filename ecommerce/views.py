from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import  ContactForm
# Create your views here.
def about(request):
	title = 'About Us'
	context = { "title" : title }
	return render(request, "about.html", context)


def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_fullname = form.cleaned_data.get("full_name")
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'samirkumar1813@hotmail.com']
		contact_message = "%s: %s via %s"%(
			form_fullname,
			form_message,
			form_email)

		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject,
			contact_message,
			from_email,
			to_email,
			#html_message=some_html_message,
			fail_silently=True)

	context = { "title" : title, "form"  : form,}
	return render(request, "contact.html", context)