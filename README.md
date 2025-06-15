# 🍕 Pizza Restaurant API

A RESTful API for managing a pizza restaurant's menu and locations, built with Flask and SQLAlchemy following the MVC architecture pattern.

## 📋 Table of Contents

- [Setup Instructions](#setup-instructions)
- [Database Setup](#database-setup)
- [API Routes](#api-routes)
- [Example Requests & Responses](#example-requests--responses)
- [Validation Rules](#validation-rules)
- [Testing with Postman](#testing-with-postman)
- [Project Structure](#project-structure)

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Pipenv

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd pizza-api-challenge
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Set environment variable:**
   ```bash
   export FLASK_APP=server/app.py
   ```

## 🗄️ Database Setup

### Initialize Database

1. **Initialize migration repository:**
   ```bash
   flask db init
   ```

2. **Create initial migration:**
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply migrations:**
   ```bash
   flask db upgrade
   ```

### Seed Database

Populate the database with sample data:

```bash
PYTHONPATH=. pipenv run python server/seed.py
```

This will create:
- 3 restaurants (Dominic's Pizza, Kiki's Pizza, Tony's Italian)
- 5 pizzas (Margherita, Pepperoni, Supreme, Hawaiian, Vegetarian)
- 9 restaurant-pizza associations with various prices

## 🛠️ API Routes

### Restaurants

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/restaurants` | Get all restaurants |
| GET | `/restaurants/<id>` | Get specific restaurant with pizzas |
| DELETE | `/restaurants/<id>` | Delete restaurant |

### Pizzas

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/pizzas` | Get all pizzas |

### Restaurant Pizzas

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/restaurant_pizzas` | Create new restaurant-pizza association |

## 📝 Example Requests & Responses

### GET /restaurants

**Request:**
```http
GET /restaurants HTTP/1.1
Host: localhost:5000
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Dominic's Pizza",
    "address": "123 Main St, New York, NY"
  },
  {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "456 Oak Ave, Brooklyn, NY"
  }
]
```

### GET /restaurants/1

**Request:**
```http
GET /restaurants/1 HTTP/1.1
Host: localhost:5000
```

**Success Response:**
```json
{
  "id": 1,
  "name": "Dominic's Pizza",
  "address": "123 Main St, New York, NY",
  "restaurant_pizzas": [
    {
      "id": 1,
      "price": 12,
      "pizza_id": 1,
      "restaurant_id": 1,
      "pizza": {
        "id": 1,
        "name": "Margherita",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      "restaurant": {
        "id": 1,
        "name": "Dominic's Pizza",
        "address": "123 Main St, New York, NY"
      }
    }
  ]
}
```

**Error Response (404):**
```json
{
  "error": "Restaurant not found"
}
```

### DELETE /restaurants/1

**Request:**
```http
DELETE /restaurants/1 HTTP/1.1
Host: localhost:5000
```

**Success Response:**
```
HTTP/1.1 204 No Content
```

**Error Response (404):**
```json
{
  "error": "Restaurant not found"
}
```

### GET /pizzas

**Request:**
```http
GET /pizzas HTTP/1.1
Host: localhost:5000
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```

### POST /restaurant_pizzas

**Request:**
```http
POST /restaurant_pizzas HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Success Response (201):**
```json
{
  "id": 4,
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "456 Oak Ave, Brooklyn, NY"
  }
}
```

**Error Response (400):**
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

## ✅ Validation Rules

### RestaurantPizza Model
- **Price**: Must be an integer between 1 and 30 (inclusive)
- **Restaurant ID**: Must reference an existing restaurant
- **Pizza ID**: Must reference an existing pizza

### Required Fields
- All model fields are required unless specified otherwise
- POST requests must include all required fields in JSON format

## 🧪 Testing with Postman

### Import Collection

1. Open Postman
2. Click **Import**
3. Select **Upload Files**
4. Choose `challenge-1-pizzas.postman_collection.json`
5. Click **Import**

### Test Collection Includes

- ✅ Get all restaurants
- ✅ Get restaurant by ID (valid and invalid)
- ✅ Delete restaurant (valid and invalid)
- ✅ Get all pizzas
- ✅ Create restaurant pizza (valid)
- ✅ Create restaurant pizza (invalid price - too low/high)
- ✅ Create restaurant pizza (missing required fields)

### Running Tests

1. Ensure your Flask server is running:
   ```bash
   flask run
   ```

2. The server will be available at `http://localhost:5000`
3. Run individual requests or the entire collection
4. Check response status codes and JSON structure

## 📁 Project Structure

```
pizza-api-challenge/
├── server/
│   ├── __init__.py
│   ├── app.py                    # Flask app setup and configuration
│   ├── config.py                 # Database configuration
│   ├── models/                   # Data models (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── restaurant.py         # Restaurant model
│   │   ├── pizza.py              # Pizza model
│   │   └── restaurant_pizza.py   # RestaurantPizza join model
│   ├── controllers/              # Route handlers (Controllers)
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   └── seed.py                   # Database seeding script
├── migrations/                   # Database migration files
├── challenge-1-pizzas.postman_collection.json
├── Pipfile                       # Python dependencies
├── Pipfile.lock
└── README.md
```

## 🏃‍♂️ Running the Application

1. **Run the application:**
   ```bash
   FLASK_APP=server/app.py pipenv run flask run
   ```

   Or alternatively:
   ```bash
   export FLASK_APP=server/app.py
   pipenv run flask run
   ```

4. **Access the API:**
   - Base URL: `http://localhost:5000`
   - Test with Postman or curl commands

## 🔧 Development Notes

- The API follows RESTful conventions
- SQLAlchemy models include proper relationships and cascade deletes
- Input validation is handled at the model level
- Error responses follow consistent JSON format
- All routes return appropriate HTTP status codes

## 🎯 Features Implemented

- ✅ MVC architecture pattern
- ✅ SQLAlchemy models with relationships
- ✅ Data validation (price range 1-30)
- ✅ Cascading deletes (Restaurant → RestaurantPizza)
- ✅ Comprehensive error handling
- ✅ RESTful API endpoints
- ✅ Database migrations
- ✅ Seed data functionality
- ✅ Postman test collection