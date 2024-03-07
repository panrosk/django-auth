
# Custom Authentication Django Project


## Django Rest Framework and JWT Authentication: T

This project integrates Django Rest Framework for building APIs and uses JWT for secure token-based authentication.

## Getting Started
Prerequisites
Before integrating the Custom Authentication Django Project into your project, ensure that you have the following prerequisites:

Python (3.11 or higher)
Poetry (for package management)
Django (5.0 or higher)
Django Rest Framework
PyJWT (JWT library for Python)


## Installation
Clone the repository:

bash
Copy code
git clone https://github.com/panrosk/django-auth.git
Navigate to the project directory:

bash
Copy code
cd djang-auth
Install dependencies:

bash
Copy code
poetry install
Apply migrations:

bash
Copy code
poetry run python manage.py migrate
Start the development server:

bash
Copy code
poetry run python manage.py runserver
Now, the Custom Authentication Django Project is ready to be integrated into your Django project.

Usage
Integration: Import the custom authentication app into your Django project's INSTALLED_APPS:

python
Copy code
# settings.py

INSTALLED_APPS = [
    # ...
    'custom_auth',
    # ...
]
Configuration: Configure the authentication settings in your project's settings.py file:

python
Copy code
# settings.py

AUTH_USER_MODEL = 'custom_auth.CustomUser'
URL Configuration: Include the authentication URLs in your project's urls.py:

python
Copy code
# urls.py

from django.urls import path, include

urlpatterns = [
    # ...
    path('auth/', include('custom_auth.urls')),
    # ...
]
Templates: Customize authentication templates as needed, located in the templates directory of the custom_auth app.

Contributing
If you encounter issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the GitHub repository.

License
This project is licensed under the MIT License.

Acknowledgments
Special thanks to the Django community and contributors for providing a robust framework that enables the creation of powerful and customizable authentication systems.

Thank you for choosing the Custom Authentication Django Project! If you have any questions or need assistance, please don't hesitate to contact us.

Happy coding!
