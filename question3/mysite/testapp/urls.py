from django.conf.urls import url
from . import views

from .views import Homeview




urlpatterns=[

    # url('email/', views.emailView, name='email'),
    # url('success/', views.successView, name='success'),
    url(r'^$', Homeview.as_view(), name='home'),

]