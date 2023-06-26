from django.urls import path
from portfolio.views import index, contacts, project, skills

urlpatterns = [
    path('', index, name='main'),
    path('contacts', contacts, name='contacts'),
    path('projects', project, name='project'),
    path('skills', skills, name='skills'),
]
