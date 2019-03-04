import glob

import requests
from django.http import HttpResponse
from django.shortcuts import render

templates_base = "base.html"


def index(request):
    index_html = open("content/index.html").read()
    context = {
        "content": index_html,
    }
    return render(request, templates_base, context)

def about(request):
    about_html = open("content/about.html").read()
    context = {
        "content": about_html,
    }
    return render(request, templates_base, context)
    
def contact(request):
    contact_html = open("content/contact.html").read()
    context = {
        "content": contact_html,
    }
    return render(request, templates_base, context)

def post(request):
    post_html = open("content/post.html").read()
    context = {
        "content": post_html,
    }
    return render(request, templates_base, context)


#def about(request):
#    # Django comes with a "shortcut" function called "render", that
#    # lets us read in HTML template files in separate directories to
#    # keep our code better organized.
#    context = {
#        'name': 'Ash Ketchum',
#        'pokemon': 'Pikachu',
#    }
#    return render(request, 'about.html', context)


#def post(request):
#    # We can also combine Django with APIs
#    response = requests.get('https://api.github.com/users/michaelpb/repos')
#    repos = response.json()
#    context = {
#        'github_repos': repos,
#    }
#    return render(request, 'post.html', context)

