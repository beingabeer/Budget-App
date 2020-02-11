## Overview
A Budget Tracking application built in Django

Clone and Install dependencies:

```
python3 -m pip3 install -r requirements.txt
```

In settings/base.py -> set a secret key

then run following commands:

```
python3 manage.py createsuperuser
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## How does it work?
To get started, create an acount. Then click on the 'Add Project' button to create an expense project. All user projects are listed out on the home page.

![](https://github.com/beingabeer/Budget-App/blob/master/src/index.png)

## Add Expenses by clicking on the 'Add Expense' button
Users have the ability to add, update or delete their own expeses.

![](https://github.com/beingabeer/Budget-App/blob/master/src/budget-detail.png)


