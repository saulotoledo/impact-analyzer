# Impact Analyzer

Impact Analyzer is a sample web application for tagging data in tables uploaded to the system.
Adding tags to data is helpful for qualitative data analysis, for example.
As a sample scenario, we propose an application for analyzing the impact of projects from data.

## Concepts and tools

This application is written in python using Django framework. Some of the concepts and tools exercised here are:

- Storing trees in relational databases using Materialized Path trees
- Basic Django usage
- Django custom commands
- Django rest framework
- Database migrations and seeders
- Dependency injection
- Swagger documentation
- Development containers using Docker and Visual Studio Code
- Python 3 Virtual Envs

The application allows adding tags and upload CSV tables. Each table cell can have zero or more tags.

As this is just a sample application, there are limitations ans known bugs:

- The supported CSV files should be comma-separated, and strings should be between double quotes.
  Any other settings will not work with this application.
- Changing the parent of a tag in the tags tree is currently not supported.
- Test cases are limited to a few samples.

## Instrutions for running the application

The application requires Python 3.8.x.

If you use Visual Studio Code, start the development container. You can find more instructions [in this link](https://code.visualstudio.com/docs/devcontainers/containers).

If you use another IDE, I recommend you to use python virtual environments. You can find instructions about how to setup them [in this link](https://docs.python.org/3/library/venv.html).

the Visual Studio Code development container has a dependency to the database container. If you are using another IDE, you need to start the database container manually:

```
docker-compose up -d impact-analyzer-db
```

Note that you might need to change the database settings in your environment configuration.

You can run the application with the command below:

```
python manage.py runserver 0.0.0.0:8000
```

You can run the tests

"name": "Run Django app",
            "type": ""
            ],
            "django": true
        },
        {
            "name": "Run tests",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "test",
                "--pattern=test_*.py"
            ],
            "django": true
