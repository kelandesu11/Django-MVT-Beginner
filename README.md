# Django MVT University Course Directory

This project is a beginner Django MVT web application for a basic University Course Directory.

The website allows users to view university departments, department details, courses inside each department, and course details.

## Technologies Used

- Python
- Django
- PostgreSQL
- Docker
- Docker Compose

## How to Run the Project

Build the Docker containers:

    docker compose build

Start the project:

    docker compose up

Open the website in your browser:

    http://localhost:8000/

## How to Create Migrations

Run this command after creating or changing models:

    docker compose run web python manage.py makemigrations

## How to Run Migrations

Run this command to apply migrations to the PostgreSQL database:

    docker compose run web python manage.py migrate

## How to Create a Superuser

Run this command:

    docker compose run web python manage.py createsuperuser

Then open the admin panel:

    http://localhost:8000/admin/

Use the admin panel to create sample data.

## ADMIN-USER:
###  Username: admin123
###   Email: admin@test.com
###   Password: admin123
###   Password Again: admin123

## Available Pages

Home page:

    /

Department list page:

    /departments/

Department detail page:

    /departments/<department_id>/

Course detail page:

    /courses/<course_id>/

Admin panel:

    /admin/

## Sample Data

Sample data can be created through the Django admin panel.

Example departments:

- Computer Science
- Mathematics
- Business Administration

Example courses:

- CSC101 - Intro to Programming
- CSC201 - Data Structures
- MTH101 - College Algebra
- MTH220 - Statistics
- BUS101 - Intro to Business
- BUS250 - Marketing Principles

Example students:

- Alex Carter
- Jamie Lee
- Morgan Smith
- Taylor Brown
- Jordan Miller

## Project Structure

    django-mvt-assignment/
      Dockerfile
      docker-compose.yml
      requirements.txt
      manage.py
      university_portal/
      departments/
      courses/
      students/
      templates/
      README.md

## Home page: http://localhost:8000/
## Departments page: http://localhost:8000/departments/
## Admin-URL: http://localhost:8000/admin/