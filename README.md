# DjangoTuto

**A collection of small Django example projects and apps for learning and demos.**

**Project Overview**

This repository contains multiple small Django projects and example apps used for tutorials and practice. Each top-level folder is a separate Django project or app, intended to be run independently for learning purposes.

**Included Projects / Apps**

- [book_store](book_store/): A bookstore example with `book_outlet` app (models, views, templates).
- [feedback](feedback/): A project demonstrating review/feedback functionality with a `reviews` app.
- [monthly_challenges](monthly_challenges/): A simple app showing monthly challenge pages and routing.
- [my_site](my_site/): A basic blog-style project with a `blog` app.
- [mypage](mypage/): Small demo project for practicing app layout and views.

**Repository Structure (highlight)**

- book_store/: Django project with `book_outlet` app and templates.
- feedback/: Django project and `reviews` app (forms, models, static files).
- monthly_challenges/: Django project demonstrating URL routing and templates.
- my_site/: Simple blog project with `blog` app.
- mypage/: Small demo project.
- static/, templates/: shared example static files and templates used by demos.

**Requirements**

- Python 3.8+ (adjust to your environment)
- Django (the projects were created with Django; typical versions 3.x or 4.x)

It's recommended to create a virtual environment per project before installing dependencies.

**Quick Setup (per project)**

1. Open a terminal and change into the project folder you want to run, for example:

```bash
cd book_store
```

2. Create and activate a virtual environment (macOS / Linux example):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Django if you don't have it already:

```bash
pip install django
```

4. Apply migrations and run the development server:

```bash
python manage.py migrate
python manage.py runserver
```

5. Open your browser at `http://127.0.0.1:8000/` for the running project.

**Running Tests**

Each app may include tests. Run them with the project's `manage.py`:

```bash
python manage.py test
```

**Notes & Tips**

- Database files (SQLite) are included for some demo projects for convenience. If you want a clean start, remove the `db.sqlite3` file in the project folder and re-run `migrate`.
- Templates live under each app's `templates/` directory; static files are under `static/`.
- Migrations for apps are in the respective `migrations/` folders.

**Contributing**

Contributions are welcome. For small tutorial projects, please:

- Fork the repo
- Make changes in a branch
- Open a pull request with a short description of what you changed and why

**License**

This repository does not include a license file. Add one if you plan to reuse or distribute the code.

**Contact / Author**

This repo is maintained by the owner of the repository. For questions or clarifications, open an issue in the repository.

