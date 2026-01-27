# 3-Tier Docker Application

A simple full-stack web application with a PostgreSQL database, Flask backend API, and Nginx frontend.

## Architecture

- **Frontend**: Nginx serving a static HTML interface
- **Backend**: Flask API for managing messages
- **Database**: PostgreSQL for persistent storage

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone/navigate to the project directory:
   ```bash
   cd 3-tier-docker-app
   ```

2. Start all services:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - Frontend: http://localhost
   - Backend API: http://localhost:5000

## Services

| Service | Port | Purpose |
|---------|------|---------|
| Frontend | 80 | Web UI for adding and viewing messages |
| Backend | 5000 | Flask API (`/add`, `/messages` endpoints) |
| Database | 5432 | PostgreSQL (internal) |

## Usage

- **Add a message**: Enter text in the frontend and click "Send"
- **View messages**: Messages are automatically displayed below in a list
- **API endpoints**:
  - `POST /add` - Add a message
  - `GET /messages` - Retrieve all messages

## Stopping the Application

```bash
docker-compose down
```

To also remove the database volume:
```bash
docker-compose down -v
```
