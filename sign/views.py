import csv

from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from sign.models import UserProfile, Visit, Menu, Role, Submenu, Claim
from django.contrib.auth.decorators import login_required
from sign.forms import VisitForm, UserForm

# Create your views here.
def claims_view(request):
	data = Claim.objects.all()
	return render(request, "sign/claim.html",{"data":data})
@login_required
def liveclaimsfeed_view(request):
	if request.method == "POST":
		columns = ['user','amount','description']
		inp = request.POST.get("submit")
		if inp == "import":
			f=request.FILES['file']
			c=0
			for row in f:
				row = row.decode("utf-8").strip()
				if c==0:
					c=c+1
					continue
				else:
					data = dict(zip(columns,row.split(",")))
					data['user'] = UserProfile.objects.get(id=data['user'])
					cl = Claim(**data)
					cl.save()
			return redirect("/claims")
		else:
			response = HttpResponse(content_type='text/csv')
			user = request.user 
			response['Content-Disposition'] = 'attachment; filename="claims-%s.csv"'%user.username
			writer = csv.writer(response)
			writer.writerow(columns)
			for row in Claim.objects.filter(user=request.user):
				row = [row.user.username, row.amount, row.description]
				writer.writerow(row)
			return response
	return render(request, "sign/liveclaimsfeed.html")
@login_required
def user_view(request):
	return render(request, "sign/user_list.html",
		{"data":UserProfile.objects.all()})
@login_required
def role_view(request):
	return render(request, "sign/role_list.html",
		{"data":Role.objects.all()})
@login_required
def menu_view(request):
	return render(request, "sign/menu_list.html",
		{"data":Menu.objects.all()})
@login_required
def submenu_view(request):
	return render(request, "sign/submenu_list.html",
		{"data":Submenu.objects.all()})
@login_required
def visit_create(request):
	msg=""
	if request.method=="POST":
		form = VisitForm(data=request.POST)
		if form.is_valid():
			inst = form.instance
			inst.user=request.user
			inst.save()
			return redirect("/patient_details")
		else:
			msg=form._errors
	else:
		form = VisitForm()
	return render(request,"sign/visit_form.html",
		{"form":form,"message":msg})
@login_required
def visit_update(request, pk):
	msg=""
	inst = Visit.objects.get(id=pk)
	if request.method=="POST":
		form = VisitForm(data=request.POST, instance=inst)
		if form.is_valid():
			form.save()
			return redirect("/patient_details")
		else:
			msg=form._errors
	else:
		form = VisitForm(instance=inst)
	return render(request,"sign/visit_form.html",
		{"form":form,"message":msg})

@login_required
def patient_view(request, pk=None):
	showing = ""
	if pk:
		showing = UserProfile.objects.get(id=pk).username
		data = Visit.objects.filter(user=pk,status=True)
	else:
		showing = request.user.username
		data = Visit.objects.filter(user=request.user,status=True,)
	return render(request, "sign/index.html",{"data":data,"showing":showing})

def signout_view(request):
	logout(request)
	return redirect("/")
def home_view(request):
	if request.user.is_authenticated:
		return redirect("/patient_details")
	msg = ""
	if request.method=="POST":
		data = request.POST
		username=data['username']
		pwd = data["password"]
		if "login" in data:
			user = authenticate(username=username, password=pwd)
			if user:
				login(request, user)
				return redirect("/patient_details")
			else:
				msg="wrong credentials"
		elif "reg" in data:
			UserProfile.objects.create_user(username=username, password=pwd)
			msg="user registered successfully"

	return render(request, "sign/home.html", {"message": msg})
def user_create_view(request):
	msg=""
	if request.method=="POST":
		form  = UserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.instance
			user.set_password(request.POST["password"])
			user.save()
			return redirect("/users/")
		else:
			msg=form._errors
	else:
		form = UserForm()
	return render(request, "sign/user_form.html",{"msg":msg,"form":form})
def user_update_view(request, pk):
	user = UserProfile.objects.get(pk=pk)
	msg=""
	if request.method=="POST":
		form  = UserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			user = form.instance
			user.set_password(request.POST["password"])
			user.save()
			return redirect("/users/")
		else:
			msg=form._errors
	else:
		form = UserForm(instance=user)
	return render(request, "sign/user_form.html",{"msg":msg,"form":form})