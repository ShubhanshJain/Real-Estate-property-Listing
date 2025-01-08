# 🏡 Real Estate Property Management Platform

A Django-based backend system for managing property listings, user portfolios, and efficient property search functionality. This platform provides endpoints for creating property listings, searching for properties with filters, and managing user-specific property data.




## Setup Instructions

1. Clone this repository

2. Install dependencies:

```bash
  pip install -r requirements.txt
```
3. Generate Django Secret Key:

```bash
  python3 manage.py shell

  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())
```

4. Run migrations:
```bash
  python manage.py makemigrations
  python manage.py migrate
```

5. Run the Server:
```bash
  python manage.py runserver
```



## API Reference

1. Property Management

#### Fetch

```http
  GET /api/properties/search/
```

#### Create

```http
  POST /api/properties/
```

Screeshots - 
#### GET
<img width="848" alt="Screenshot 2025-01-08 at 9 19 37 AM" src="https://github.com/user-attachments/assets/44bb07c7-fa9f-4d7a-8e6e-47b07904aa7e" />

#### POST
<img width="851" alt="Screenshot 2025-01-08 at 9 16 27 AM" src="https://github.com/user-attachments/assets/307db463-81de-4de1-a058-ea4e03f316d1" />


