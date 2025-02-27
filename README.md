# Recipe-Management-System
A full-stack Django web app with 5+ core features, including user authentication, encrypted passwords, CRUD operations, search, and image uploads. Built with Bootstrap for a responsive UI.


#Recipe Management System

#Description

A full-stack Django web application that allows users to add, edit, delete, and search recipes. Features user authentication, password encryption, and image uploads for enhanced functionality. Designed with Bootstrap for a seamless UI.

#Tech Stack

-Backend: Django, Python

-Frontend: HTML, CSS, Bootstrap

-Database: MySQL

#Features

✅ Secure login & registration with encrypted passwords
✅ CRUD operations for managing recipes
✅ Image uploads for recipes
✅ Search functionality for quick access
✅ Responsive UI with Bootstrap

#Installation Guide

#Clone the repository:

git clone <repo-link>
cd recipe-management

#Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

#Install dependencies:

pip install -r requirements.txt

#Run migrations:

python manage.py migrate

#Start the development server:

python manage.py runserver

Open in browser: http://127.0.0.1:8000/
