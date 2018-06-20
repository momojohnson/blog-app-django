# A BASIC DJANGO BLOG
[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0.1-brightgreen.svg)](https://djangoproject.com)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/momojohnson/blog-app-django
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Setup the local configurations:

```
 create .env and setup your configurations
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.