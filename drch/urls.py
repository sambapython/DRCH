"""drch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from sign.views import home_view, signout_view, patient_view,visit_create,\
visit_update, menu_view, role_view, user_view, user_create_view, submenu_view,\
user_update_view, liveclaimsfeed_view, claims_view
from sign.models import Menu, Role, UserProfile, Submenu
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path("claims/",claims_view),
	path("liveclaimsfeed/",liveclaimsfeed_view),
	path('admin/', admin.site.urls),
	path('', home_view),
	re_path('patient_details/(?P<pk>[0-9]+)/', patient_view),
	path('patient_details/', patient_view),
	path('signout/', signout_view),
	path("visit_create/",visit_create),
	re_path("visit_update/(?P<pk>[0-9]+)/",visit_update),
	path("submenus/",submenu_view),
	path("submenu_create/",login_required(CreateView.as_view(
		model = Submenu,
		fields= "__all__",
		success_url = "/submenus/",
		))),
	re_path("submenu_update/(?P<pk>[0-9]+)/",login_required(UpdateView.as_view(
		model = Submenu,
		fields= "__all__",
		success_url = "/submenus/",
		))),
	re_path("submenu_delete/(?P<pk>[0-9]+)/",login_required(DeleteView.as_view(
		model = Submenu,
		success_url = "/submenus/",
		))),
	
	path("menus/",menu_view),
	path("menu_create/",login_required(CreateView.as_view(
		model = Menu,
		fields= "__all__",
		success_url = "/menus/",
		))),
	re_path("menu_update/(?P<pk>[0-9]+)/",login_required(UpdateView.as_view(
		model = Menu,
		fields= "__all__",
		success_url = "/menus/",
		))),
	re_path("menu_delete/(?P<pk>[0-9]+)/",login_required(DeleteView.as_view(
		model = Menu,
		success_url = "/menus/",
		))),
	path("roles/",role_view),
	path("role_create/",login_required(CreateView.as_view(
		model = Role,
		fields= "__all__",
		success_url = "/roles/",
		))),
	re_path("role_update/(?P<pk>[0-9]+)/",login_required(UpdateView.as_view(
		model = Role,
		fields= "__all__",
		success_url = "/roles/",
		))),
	re_path("role_delete/(?P<pk>[0-9]+)/",login_required(DeleteView.as_view(
		model = Role,
		success_url = "/roles/",
		))),
	path("users/",user_view),
	path("user_create/",user_create_view),
	re_path("user_update/(?P<pk>[0-9]+)/",user_update_view),
	re_path("user_delete/(?P<pk>[0-9]+)/",login_required(DeleteView.as_view(
		model = UserProfile,
		success_url = "/users/",
		))),
]
