from django import forms
from .models import NewsletterSignUp


class NewsletterSignUpForm(forms.ModelForm):
	class Meta:
		model = NewsletterSignUp
		fields = ['full_name','email']
		
	def clean_email(self):
		email = self.cleaned_data.get('email')

		email_base, provider = email.split("@")
		domain, extension = provider.split('.')

		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .EDU email address")

		return  email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		if not full_name :
			full_name = "Anonymous"
		return full_name