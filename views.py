import glob
import os

import requests
from django.http import HttpResponse
from django.shortcuts import render

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
    all_html_files = glob.glob("templates/*.html")
    all_html_files.remove("templates/base.html")
    
    pages = []

    for file_path in all_html_files:
        result = convert(file_path)
        pages.append(result)
    return pages

pages = navigation()

def index(request):
    index_html = open("templates/index.html").read()
    context = {
        "pages": pages,
        "selected": "/"
    }
    return render(request, "index.html", context)

def about(request):
    about_html = open("templates/about.html").read()
    response = requests.get('https://api.github.com/users/stacyhanawa/repos')
    repos = response.json()
    context = {
        "pages": pages,
        "selected": "about",
        "github_repos": repos,
    }
    return render(request, "about.html", context)
    
def contact(request):
    contact_html = open("templates/contact.html").read()
    context = {
        "pages": pages,
        "selected": "contact"
    }
    return render(request, "contact.html", context)

def post(request):
    post_html = open("templates/post.html").read()
    context = {
        "pages": pages,
        "selected": "post"
    }
    return render(request, "post.html", context)


