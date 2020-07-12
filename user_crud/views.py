from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Users
# Create your views here.

def user_list(request):
	context = {'user_list' : Users.objects.all()} 
	return render(request, "user_crud/users/user_list.html", context)

def user_form(request, id=0):
	if request.method == 'GET':
		if id == 0:
			form = UserForm()
		else:	
			user = Users.objects.get(pk=id)
			form = UserForm(instance=user)
		return render(request, "user_crud/users/user_form.html", {'form': form})
	else:
		if id == 0:
			form = UserForm(request.POST)
		else:
			user = Users.objects.get(pk=id)
			form = UserForm(request.POST,instance=user)
		if form.is_valid():
			form.save()
		return redirect('/crud/list')

def user_delete(request, id):
	user = Users.objects.get(pk=id)
	user.delete()
	return redirect('/crud/list')