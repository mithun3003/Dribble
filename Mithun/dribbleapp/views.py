from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def designers(request):
    return render(request, 'designers.html')

def teams(request):
    return render(request, 'teams.html')

def community(request):
    return render(request, 'community.html')

def jobs(request):
    return render(request, 'jobs.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def search(request):
    query = request.GET.get('q', '')
    return render(request, 'search.html', {'query': query})
