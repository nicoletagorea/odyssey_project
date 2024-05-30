# Odyssey Project: Movie API Project

This project provides a FastAPI-based API for managing movie data stored in a JSON file. It supports operations to fetch, add, update, and delete movie records.

## Installation

To get started with this project, follow these steps:

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/movie-api.git
cd movie-api
```
### Create a Virtual Environment
It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Dependencies
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```
### Running the Project
To run the FastAPI application, follow these steps:

Ensure you are in the project directory and your virtual environment is activated.
Start the FastAPI application using uvicorn:
```bash
uvicorn app.main:app --reload
```
The API will be available at http://127.0.0.1:8000. You can access the API documentation at http://127.0.0.1:8000/docs.

### Project Structure
odyssey_project
    /app
        __init__.py
        api.py
    /data_processing
        __init__.py
        data_processing.py
    /scraper
        __init__.py
        scraper.py
    /testing
    test_data_processing.py
    movies.json
    README.md
    requirements.txt

### Testing the Project
To test the project, you can use tools like curl, Postman, or directly interact with the API documentation provided by FastAPI at http://127.0.0.1:8000/docs.

Example Requests:

Get All Movies
```bash
curl -X GET "http://127.0.0.1:8000/movies" -H "accept: application/json"
```
Get Movies by Year
```bash
curl -X GET "http://127.0.0.1:8000/movies/2020" -H "accept: application/json"
```
Add Movies for a Specific Year
```bash
curl -X POST "http://127.0.0.1:8000/movies/2020" -H "accept: application/json"
```
Update Movies for a Specific Year
```bash
curl -X PUT "http://127.0.0.1:8000/movies/2020" -H "accept: application/json"
```
Delete a Movie by Year and Name
```bash
curl -X DELETE "http://127.0.0.1:8000/movies/2020/Inception" -H "accept: application/json"
```