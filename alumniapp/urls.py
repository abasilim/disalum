from django.urls import path
from django.views.generic import TemplateView

app_name = 'alumniapp'

urlpatterns = [
    path('', TemplateView.as_view(template_name ='alumniapp/index.html')),
]