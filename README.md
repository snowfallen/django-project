# Django-project
Django simple project for learning main aspect this framework
1. Create .env using .env.example.
2. Create and run all container you need to work:
2. ``docker-compose -f docker-compose.yml up --build -d``
3. Create django project running:
4. ``docker-compose -f docker-compose.yml run --rm django django-admin startproject <name of project> .``