# SHOP-DJANGO PROJECT


#### Stack:

- [Python](https://www.python.org/downloads/)
- [Django](https://docs.djangoproject.com/en/4.1/)
- [Redis](https://redis.io/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [PostgreSQL](https://www.postgresql.org/)

```
In this project, an online store was developed, 
as well as an api that allows you to interact with various clients.
```
## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.10 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Create superuser:
   ```bash
   ./manage.py createsuperuser
   ```

4. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver 
   ```

   

