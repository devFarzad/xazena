from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^submit/expense/$', views.submit_expense, name= 'submit expense'),
        url(r'^submit/income/$', views.submit_income, name= 'income expense'),
]
