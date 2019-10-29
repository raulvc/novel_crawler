# novel_crawler
Simple text crawler for fetching novel chapters.

## Arguments
| arg | expanded       | required | explanation                                       | example                                                               |
|-----|----------------|----------|---------------------------------------------------|-----------------------------------------------------------------------|
| -i  | --initial-page | true     | an http link as a starting point                  | http://novelfull.com/everyone-else-is-a-returnee/prologue-part-1.html |
| -o  | --out          | false    | output file (default: book.txt in cwd)            | ~/ebooks/everyone_else_is_a_returnee.txt                              |
| -a  | --append       | false    | whether to truncate (fully overwrite) output file | y                                                                     |

## Deps
- python3
- venv
- Selenium
- BeautifulSoup

### Installing deps using pip
```
# install venv
pip install venv

# Set your cwd to project's folder
$ cd novel_crawler

# use virtual env
$ virtualenv -p $(which python3) .
$ source venv/bin/activate 

# install deps
pip install -r requirements.txt
```

## Running
```
# Set your cwd to project's folder
$ cd novel_crawler

$ source venv/bin/activate

$ (venv) python3 main.py -i "http://novelfull.com/everyone-else-is-a-returnee/prologue-part-1.html" -o ~/ebooks/everyone_else_is_a_returnee.txt -a y
```
