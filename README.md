# bookstore
# Bookstore Django Project

This project is a Django-based web application for managing a bookstore. It includes functionality for managing books, authors, and categories, and is set up to run using Docker and Docker Compose with a PostgreSQL database.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Local Development](#local-development)
  - [Using Docker](#using-docker)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)

## Project Structure


## Requirements

- Docker
- Docker Compose

## Setup Instructions

### Local Development

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/bookstore.git
   cd bookstore

2. **Create and activate a virtual environment:**
python -m venv venv
source venv/bin/activate

3. **Install dependencies:**
pip install -r requirements.txt

4. **Apply migrations and run the server:**
python manage.py migrate
python manage.py runserver

Using Docker

5. **Build the image:**
sudo docker-compose build

6. **Apply migrations:**
sudo docker-compose exec app python manage.py migrate

7. **Command to start your Docker service:
sudo docker-compose up -d

8. **Command to down your Docker service:
sudo docker-compose down


Running Tests

9. **To run tests for the project:
python manage.py test