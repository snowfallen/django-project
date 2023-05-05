# Django-project
## Django simple project for learning main aspect this framework 
### Create and run all container you need to work:
```sh exec.sh build```
### Create django project running:
```docker-compose -f docker-compose.yml run --rm django django-admin startproject <name of project> .```
* Run: ``sh exec.sh runserver`` fot running django localserver.
### The secret key must be a large random value and it must be kept secret, copy your SECRET_KEY to secret_key.txt file in your root dir (don't forget add secret_key to your .gitignore file)
```sh exec.sh build createSuperUser```  for creating an admin account