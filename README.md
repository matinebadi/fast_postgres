

This project demonstrates how to create a simple CRUD (Create, Read, Update, Delete) application using **FastAPI** and **PostgreSQL**.

## Requirements

- Python 3.7+
- FastAPI
- Psycopg2
- PostgreSQL database

## Installation

1. Clone the repository or download the project files.
2. Install the required dependencies:
   ```bash
   pip install fastapi psycopg2

3. Ensure you have PostgreSQL installed and a database set up (e.g., a database named postgres).


4. Create the data_item table in PostgreSQL:

CREATE TABLE data_item (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    item_id INT
);


5. Run the FastAPI app:

uvicorn app:app --reload

This will start the FastAPI server on http://localhost:8000.



API Endpoints

1. Create Item

URL: /items/

Method: POST

Request Parameters:

name (string) - The name of the item.

item_id (int) - The unique ID of the item.


Response:

{"message": "inserted"}



2. Read All Items

URL: /items/

Method: GET

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


3. Read Single Item

URL: /items/{litem_id}

Method: GET

Parameters:

litem_id (int) - The ID of the item.


Response:

{
  "response": {
    "name": "item_name",
    "item_id": 123
  }
}


4. Update Item

URL: /items/{item_id}/{name}

Method: PUT

Parameters:

item_id (int) - The ID of the item.

name (string) - The new name of the item.

last_id (int) - The current item ID to update.


Response:

{
  "item_id": 123,
  "name": "new_name"
}


5. Delete Item

URL: /items/{last_id1}/

Method: DELETE

Parameters:

last_id1 (int) - The ID of the item to delete.


Response:

"message: deleted :("


Code Explanation

FastAPI Endpoints

The FastAPI app consists of five endpoints:

1. POST /items/: Inserts a new item into the PostgreSQL database using the add function.


2. GET /items/: Retrieves all items from the database using the showed_all function.


3. GET /items/{litem_id}: Fetches a specific item based on its ID using the showed function.


4. PUT /items/{item_id}/{name}: Updates an item's name in the database using the update function.


5. DELETE /items/{last_id1}/: Deletes an item based on its ID using the deleted function.



PostgreSQL Functions

The database connection and the following functions handle the database operations:

add(name, ii): Adds a new item to the data_item table.

update(name, ii, last_id): Updates the name of an existing item with the provided last_id.

deleted(last_id1): Deletes an item with the specified last_id.

showed_all(): Retrieves all items from the data_item table.

showed(id): Retrieves a specific item by its item_id.


