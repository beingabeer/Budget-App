## Overview
A Budget Tracking application built in Django

Clone and add the following to a '.env.dev' file in the root directory:

```
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

Build the docker image and run the container:

```
docker-compose build
docker-compose up -d
```

then run the following commands:

```
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

## How does it work?
To get started, create an acount. Then click on the 'Add Project' button to create an expense project. All user projects are listed out on the home page.

![](https://github.com/beingabeer/Budget-App/blob/master/src/index.png)

## Add Expenses by clicking on the 'Add Expense' button
Users have the ability to add, update or delete their own expeses.

![](https://github.com/beingabeer/Budget-App/blob/master/src/budget-detail.png)


