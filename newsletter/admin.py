from django.contrib import admin
from .forms import NewsletterSignUpForm
from .models import NewsletterSignUp
# Register your models here.


class NewsletterSignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = NewsletterSignUpForm
	# class Meta:
	# 	model = NewsletterSignUp

admin.site.register(NewsletterSignUp, NewsletterSignUpAdmin)