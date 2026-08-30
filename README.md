# Setup

## 1. Create a virtual environment
python3 -m venv venv

### 2. Activate it
source venv/bin/activate

## 3. Install dependencies
pip install -r requirements.txt

# 4. Create your MySQL database (update settings.py with your own credentials)
CREATE DATABASE aula_db;

# 5. Run migrations
python manage.py migrate

# 6. Create your own superuser
python manage.py createsuperuser

# 7. Run the server
python manage.py runserver

## Testing the App

### Customer-facing reservation page
http://127.0.0.1:8000/make_reservation/
Make a booking as a customer — no login required.

### Staff dashboard (requires a staff account)
http://127.0.0.1:8000/staff/
Register a new account at /staff/register/, then log in at /staff/login/.
By default, new accounts have no special permissions. To test manager vs.
waiter behavior, log into /admin/ with your superuser account, create two
Groups named "managers" and "waiters," and assign your test account to one.

### Reservations management (staff only)
http://127.0.0.1:8000/make_reservation/staff/
View, edit, and delete reservations. Only accounts in the "managers" group
can delete; "waiters" can view/create/edit only.

### Raw API (for inspecting the underlying data)
http://127.0.0.1:8000/make_reservation/drf/
Shows the same reservation data as above, via Django REST Framework's
browsable API — useful for testing the API directly (e.g. with Postman).