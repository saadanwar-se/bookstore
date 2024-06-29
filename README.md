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
Use seperate .env files for running app with docker and without docker

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

6. **Command to start your Docker service:
sudo docker-compose up -d
 
7. **Start Interactive Shell:**
sudo docker exec -it {name of container} sh

8. **Apply migrations:**
python manage.py migrate


8. **Command to down your Docker service:
sudo docker-compose down


Running Tests

9. **To run tests for the project:
python manage.py test