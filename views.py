import glob
import os

import requests
from django.http import HttpResponse
from django.shortcuts import render

templates_base = "base.html"

def convert(file_path):
    file_name = os.path.basename(file_path)
    page_title, extension = os.path.splitext(file_name)
    if page_title == "index":
        output_filename = "/"
    else:
        output_filename = page_title
    return {
                "filename": file_path,
                "title": page_title,
                "output_filename": output_filename
           }

def navigation():
    all_html_files = glob.glob("content/*.html")
    
    pages = []

    for file_path in all_html_files:
        result = convert(file_path)
        pages.append(result)
    return pages

pages = navigation()

def index(request):
    index_html = open("content/index.html").read()
    context = {
        "content": index_html,
        "pages": pages,
        "selected": "/"
    }
    return render(request, templates_base, context)

def about(request):
    about_html = open("content/about.html").read()
    context = {
        "content": about_html,
        "pages": pages,
        "selected": "about"
    }
    return render(request, templates_base, context)
    
def contact(request):
    contact_html = open("content/contact.html").read()
    context = {
        "content": contact_html,
        "pages": pages,
        "selected": "contact"
    }
    return render(request, templates_base, context)

def post(request):
    post_html = open("content/post.html").read()
    context = {
        "content": post_html,
        "pages": pages,
        "selected": "post"
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

