# Install requirements
pip install requerimets.txt 

# configurate settings_local with example_settings_local on coosalud app

# Create DB instance
python manage.py migrate

# create SuperUser
python manage.py createsuperuser

# Run project
python manage.py runserver

# urls front
http://localhost:8000/admin

# Url token jwt
http://localhost:8000/api/token

# Url Refresh Token jwt
http://localhost:8000/api/token/refresh/

# Url Upload CSV Verification ## TO DO
http://localhost:8000/service/api/check-upload

# Url Upload CSV -> Model Service ## TO DO
http://localhost:8000/service/api/service-upload
