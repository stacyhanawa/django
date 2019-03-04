import utils

import sys

if len(sys.argv) ==2:
    command = sys.argv[1]
    if command == "build":
        print("Build was specified")
        utils.main()
    elif command == "new":
        print("New page was specified")
        text = "<h1>New Content!<h1><p>New content<p>"
        open("content/new_content_page.html", "w+").write(text)
    else:
        print("Please specify 'build' or 'new'")
else:
    print('''Usage:
Rebuild site: python3 manage.py build
Create new page: python3 manage.py new''')
