# Django-project
Django simple project for learning main aspect this framework
1. Create and run all container you need to work:
2.  ``sh exec.sh build``
3. Create django project running:
4. ``docker-compose -f docker-compose.yml run --rm django django-admin startproject <name of project> .``
5. Run: ``sh exec.sh runserver`` fot running django localserver.
6. The secret key must be a large random value and it must be kept secret, copy your SECRET_KEY to .env