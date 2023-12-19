# FizzBuzz REST API

## Overview

This Django REST Framework project provides a REST API for a modified version of the classic FizzBuzz game. It includes two main endpoints: one for generating FizzBuzz sequences based on user-provided parameters, and another for retrieving statistics about the most frequent requests made to the API.

## Features

- **FizzBuzz Endpoint:** Returns a list of strings from 1 to a specified limit, where multiples of two specified integers are replaced with user-defined strings.
- **Statistics Endpoint:** Provides data on the most frequently used parameters for the FizzBuzz endpoint.

## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework

### Installation

1. **Clone the Repository:**

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. **Set Up a Virtual Environment:**

python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate

3. **Install Dependencies:**

pip install -r requirements.txt

4. **Run Migrations:**

python manage.py makemigrations
python manage.py migrate

5. **Start the Development Server:**

python manage.py runserver

6. **Access the API:**

The API will be available at `http://localhost:8000/`.

### Usage

#### FizzBuzz Endpoint

- **URL:** `/api/fizzbuzz/`
- **Method:** `GET`
- **URL Params:**
- `int1=[integer]`
- `int2=[integer]`
- `limit=[integer]`
- `str1=[string]`
- `str2=[string]`

- **Success Response:**
- **Code:** 200 OK
- **Content:** `[1, 2, "fizz", 4, "buzz", ...]`

- **Error Response:**
- **Code:** 400 BAD REQUEST
- **Content:** `{"error": "Invalid input..."}`

#### Statistics Endpoint

- **URL:** `/api/fizzbuzz/stats/`
- **Method:** `GET`

- **Success Response:**
- **Code:** 200 OK
- **Content:** `{"int1": 3, "int2": 5, "limit": 15, "str1": "fizz", "str2": "buzz", "hits": 10}`

- **Error Response:**
- **Code:** 404 NOT FOUND
- **Content:** `{"error": "No requests made yet."}`

### Testing

Run the test suite with:

python manage.py test
