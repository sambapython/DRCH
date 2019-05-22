from django.forms import ModelForm
from sign.models import Visit, UserProfile

class VisitForm(ModelForm):
	class Meta:
		model = Visit
		fields = ["payment", "cause","status"]

class UserForm(ModelForm):
	class Meta:
		model=UserProfile
		fields = ["username", 'password','role']