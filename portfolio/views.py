from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


def project(request):
    return render(request, 'project-page.html')


def skills(request):
    return render(request, 'skills.html')
