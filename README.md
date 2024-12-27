
# FastAPI PostgreSQL Project

This project is a simple FastAPI-based application that interacts with a PostgreSQL database. It allows users to create, update, delete, and retrieve items from a database using HTTP requests.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [License](#license)

## Overview
This FastAPI app provides a RESTful API for managing items in a PostgreSQL database. The app allows users to:
- Add new items
- Update existing items
- Delete items
- Retrieve one or all items

The project is designed to provide basic CRUD operations for a simple item management system.

## Installation

### Prerequisites
- Python 3.7 or higher
- PostgreSQL installed and running
- `psycopg2` and `FastAPI` libraries

### Steps

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/fastapi-postgresql-project.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the PostgreSQL database:
    - Ensure your PostgreSQL server is running.
    - Create a new database called `postgres` (or use an existing one).
    - Create the required table using the SQL schema below.

4. Run the FastAPI app:
    ```bash
    uvicorn main:app --reload
    ```

Your app will now be running at `http://127.0.0.1:8000`.

## Usage

The API provides the following endpoints for interacting with the items.

### API Endpoints

#### `POST /items/`
Create a new item in the database.

**Request body:**
```json
{
    "name": "item_name",
    "item_id": 123
}

Response:

{
    "message": "inserted"
}

GET /items/

Retrieve all items from the database.

Response:

{
    "all data": [
        {
            "name": "item_name",
            "item_id": 123
        },
        ...
    ]
}

GET /items/{litem_id}

Retrieve a specific item by item_id.

Response:

{
    "response": {
        "name": "item_name",
        "item_id": 123
    }
}

PUT /items/{item_id}/{name}

Update an existing item by item_id.

Request body:

{
    "name": "new_name",
    "last_id": 123
}

Response:

{
    "item_id": 123,
    "name": "new_name"
}

DELETE /items/{last_id1}

Delete an item by item_id.

Response:

"massage : deleted :("

Database Schema

The app interacts with a PostgreSQL database. Below is the SQL schema for the data_item table:

CREATE TABLE data_item (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    item_id INT UNIQUE NOT NULL
);

Database Functions

The database operations are defined in the post.py file with the following functions:

add(name, item_id): Inserts a new item into the data_item table.

update(name, item_id, last_id): Updates an existing item by item_id.

deleted(last_id1): Deletes an item by item_id.

showed_all(): Retrieves all items from the data_item table.

showed(id): Retrieves a specific item by item_id.


