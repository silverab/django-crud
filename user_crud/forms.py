from django import forms
from .models import Users

class UserForm(forms.ModelForm):

	class Meta:
		model = Users
		# fields = '__all__'
		fields = ('username', 'first_name', 'eductaion', 'current_status', 'mobile', 'city')
		labels = {
			'username': 'Username',
			'first_name': 'First Name',
			'eductaion': 'Education',
			'current_status': 'Status',
			'mobile': 'Mobile',
			'city': 'City'
		}

	def __init__(self, *args, **kwargs):
		super(UserForm,self).__init__(*args, **kwargs)
		self.fields['current_status'].empty_label = 'Choose'
		# self.fields['emp_code'].required = False