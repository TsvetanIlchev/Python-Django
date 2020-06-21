from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My second project.</em>")

def help_page(request):
    my_dictionary = { 'help_page': "I am from help page view."}
    return render(request, 'AppTwo/help.html', context = my_dictionary)
