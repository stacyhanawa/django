import glob

import os
from jinja2 import Template

def convert(file_path):
    file_name = os.path.basename(file_path)
    page_title, extension = os.path.splitext(file_name)
    output = "docs/" + file_name
    return {
                "filename": file_path,
                "title": page_title,
                "output": output,
                "output_filename": file_name
            }


def main():
    all_html_files = glob.glob("content/*.html")

    pages = []

    for files in all_html_files:
        result = convert(files)
        pages.append(result)

    template_html = open("templates/base.html").read()
    template = Template(template_html)

    for page in pages:
        file_path = page['filename']
        index_html = open(file_path).read()
        page_html = template.render(
            title = page['title'],
            content = index_html,
            pages = pages,
            selected = page["output_filename"]
        )
        open(page['output'], "w+").write(page_html)
    
if __name__ == "__main__":
    main()
