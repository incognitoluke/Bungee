"""CommunitySupport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from contact.views import contact_create_view
from Pages.views import home_view, contact_view, submission_view, terms_view
from volunteer.views import volunteer_view
from need.views import order_view, order_list_view, dynamic_order_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_create_view, name='contact'),
    path('submission/', submission_view, name='submission'),
    path('volunteer/', volunteer_view, name='volunteer'),
    path('donate/', order_list_view, name='donate'),
    #path('donate/<str:town>/', order_list_view, name='donate_view'),
    path('donate/<int:id>/', dynamic_order_view, name='donate_view'),
    path('order/', order_view, name='order'),
    path('terms/', terms_view, name='terms'),
    path('admin/', admin.site.urls)
]
