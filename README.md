# 🚀 Flask + PostgreSQL + Docker + CI/CD Demo App

This project demonstrates a production-style backend setup using Flask, PostgreSQL, Docker, Nginx, and CI pipelines.

It is designed to showcase real-world backend engineering practices, including containerization, reverse proxy configuration, health checks, and environment-based configuration.

---

## 🧱 Tech Stack

* Python (Flask)
* PostgreSQL
* Docker & Docker Compose
* Nginx (reverse proxy)
* Gunicorn (WSGI server)
* GitHub Actions (CI)

---

## 📦 Architecture Overview

Client → Nginx → Gunicorn → Flask App → PostgreSQL

* **Nginx** handles incoming HTTP requests
* **Gunicorn** runs the Flask application
* **Flask** processes business logic
* **PostgreSQL** stores data
* **Docker Compose** orchestrates services

---

## ⚙️ Features

* Multi-container Docker setup
* Reverse proxy with Nginx
* Health check endpoint (`/health`)
* PostgreSQL database integration
* Environment-based configuration via `.env`
* CI pipeline with build validation

---

## 📁 Project Structure

```
.
├── app/                # Flask application
├── nginx/              # Nginx configuration
├── .github/workflows/  # CI pipeline
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env
```

---

## 🔧 Local Development

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-flask-postgresql-docker-ci-app.git
cd python-flask-postgresql-docker-ci-app
```

### 2. Set environment variables

Create a `.env` file:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=app_db
```

---

### 3. Run the application

```bash
docker compose up --build
```

---

### 4. Test endpoints

Health check:

```
http://localhost:5000/health
```

Example response:

```json
{
  "app": "running",
  "database": "connected",
  "status": "ok"
}
```

---

## 🔍 CI Pipeline

The project includes a GitHub Actions workflow that:

* Builds Docker images
* Validates container startup
* Ensures health endpoint is reachable

---

## 🌐 Production Considerations

This project follows production-oriented practices:

* Uses Gunicorn instead of Flask dev server
* Nginx as reverse proxy
* Environment variable configuration
* Container isolation
* Health checks for service monitoring

---

## 🚧 Future Improvements

* CI/CD with Docker image push
* Deployment to AWS EC2 / VPS
* HTTPS with Let's Encrypt
* Database migrations (Alembic)
* Logging & monitoring

---

## 🧠 Author

Zoltán Zsinka
Full Stack Developer / DevOps-oriented Engineer

---

## 📌 Notes

This project is part of a learning path focused on backend engineering and production-ready system design.
