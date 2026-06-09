# University Course Directory API

## Running the Project

Build the containers:

```bash
docker compose build
```

Start the application:

```bash
docker compose up
```

The application will be available at:

```text
http://localhost:8000/
```

## Running Migrations

Create migrations:

```bash
docker compose exec web python manage.py makemigrations
```

Apply migrations:

```bash
docker compose exec web python manage.py migrate
```

## Creating a Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

Admin page:

```text
http://localhost:8000/admin/
```

## Part 1 Website URLs

```text
/
/departments/
/departments/<id>/
/courses/<id>/
```

## Part 2 API URLs

```text
/api/departments/
/api/courses/
/api/students/
/api/enrollments/
/api/audit-logs/
```

## How I Tested the API

I used the Django REST Framework browsable API to test the endpoints.

The following scenarios were tested:

* Listing departments
* Creating departments
* Listing courses
* Creating and updating courses
* Listing students
* Creating and updating students
* Creating enrollments
* Rejecting duplicate enrollments
* Rejecting enrollments for inactive courses
* Verifying audit logs were created automatically

## Example Valid Requests

### Create Department

```json
{
    "name": "Computer Science",
    "code": "CSC",
    "description": "Department for computer science and software engineering courses.",
    "building_name": "Engineering Building"
}
```

### Create Enrollment

```json
{
    "student": 1,
    "course": 1,
    "status": "active"
}
```

## Example Invalid Requests

### Duplicate Enrollment

```json
{
    "student": 1,
    "course": 1,
    "status": "active"
}
```

Expected result:

```text
Student is already enrolled in this course.
```

### Enrollment for an Inactive Course

```json
{
    "student": 1,
    "course": 2,
    "status": "active"
}
```

Expected result:

```text
Cannot enroll in an inactive course.
```

## Signals Used

Django signals were used to automatically create audit log entries when:

* A student is created
* A course is created
* An enrollment is created

The signals are located in `registrations/signals.py`.

## Transaction Used

Enrollment creation uses `transaction.atomic()` to make sure the operation is completed as a single transaction.

If any part of the enrollment process fails, all database changes are rolled back so that incomplete data is not saved.
