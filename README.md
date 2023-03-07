# Impact Analyzer

Impact Analyzer is a sample web application for tagging data in tables uploaded to the system.
Adding tags to data is helpful for qualitative data analysis, for example.

## Concepts and tools

This application is written in python using the Django framework. Some of the concepts and tools exercised here are:

- Storing trees in relational databases using Materialized Path trees
- Basic Django usage
- Django custom commands
- Django rest framework
- Database migrations and seeders
- Dependency injection
- Swagger documentation
- Development containers using Docker and Visual Studio Code
- Python 3 Virtual Envs

The application allows adding tags and uploading CSV tables. Each table cell can have zero or more tags.

As this is just a sample application, there are limitations and known bugs:

- The supported CSV files should be comma-separated, and strings should be between double quotes.
  Any other settings will not work with this application.
- Changing the parent of a tag in the tags tree is currently not supported.
- Test cases are limited to a few samples.

## Instructions for running the application

Create a copy of the `.env.example` file to `.env`. Some environment variables are defined here.
Please note that many settings (e.g., the database ones) are still defined at `impact_analyzer/settings.py`.
Some of those settings should ideally be moved to the environment settings.

The application requires Python 3.8.x.

If you use Visual Studio Code, start the development container.
Instructions for setting them up are [in this link](https://code.visualstudio.com/docs/devcontainers/containers).

If you use another IDE, we recommend using python virtual environments.
You can find instructions about how to setup them [in this link](https://docs.python.org/3/library/venv.html).

The Visual Studio Code development container depends on the database container and will start the database container automatically.
If you are using another IDE, you need to start the database container manually:

```
docker-compose up -d impact-analyzer-db
```

Note that you might need to change the database settings in the application settings.

Proceed with installing the dependencies:

```
pip install -r requirements.txt
```

Migrate the database with the command below:

```
python manage.py migrate
```

Optionally, you can initialize the sample tags tree in the database with the command below:

```
python manage.py seed_tags_table
```

Finally, run the application with the command below:

```
python manage.py runserver 0.0.0.0:8000
```

You can run the tests using the following command:

```
python manage.py test --pattern=test_*.py
```
