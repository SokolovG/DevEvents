# DevEvents

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Litestar](https://img.shields.io/badge/litestar-2.14.0-blue.svg)

DevEvents is a comprehensive platform that aggregates and manages tech conferences and developer meetups. Our mission is
to help developers stay updated about upcoming tech events and provide organizers with tools to promote their meetups
effectively.

## 📋 Features

- **Browse Events**: Discover upcoming tech events and conferences
- **Track Events**: Follow interesting events and set reminders
- **Organize Events**: Create and manage your own tech events
- **User Profiles**: Personalized profiles with event history
- **Event Registration**: Simple registration process for attendees
- **Comments & Discussions**: Engage with speakers and other attendees

## 🛠️ Technology Stack

### Backend

- **Framework**: [Litestar](https://litestar.dev/) - Modern, high-performance API framework
- **Database**: PostgreSQL with AsyncPG
- **ORM**: SQLAlchemy 2.0 (async)
- **Validation**: Pydantic v2
- **Migration**: Alembic
- **Admin Panel**: SQLAdmin
- **Packet manager**: Uv

### DevOps

- **Containerization**: Docker & Docker Compose
- **CI/CD**: To be implemented

## 🚀 Installation and Setup

### Prerequisites

- Docker and Docker Compose
- Python 3.12+ (for local development)
- PostgreSQL (for local development without Docker)

### Using Docker (Recommended)

1. Clone the repository:

```bash
git clone https://github.com/yourusername/DevEvents.git
cd DevEvents
```

2. Create a `.env` file with the following content:

```
# Database
POSTGRES_DB=dev_events
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/dev_events
```

3. Build and start the containers:

```bash
docker-compose up --build
```

4. Access the applications:
    - Backend API: http://localhost:8000
    - API Documentation: http://localhost:8000/schema/swagger
    - Admin Panel: http://localhost:8000/admin
    - Frontend (when implemented): http://localhost:5173

### Local Development Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/DevEvents.git
cd DevEvents
```

2. Create a virtual environment and install dependencies:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

3. Create a `.env` file with the following content:

```
# Database
POSTGRES_DB=dev_events
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/dev_events
```

4. Create the database in your local PostgreSQL instance.

5. Run migrations:

```bash
alembic upgrade head
```

6. Seed the database with test data:

```bash
python -m backend.src.main run-seeders
```

7. Start the development server:

```bash
uvicorn backend.src.main:app --reload
```

## 🧪 Database Seeding

To populate the database with test data:

```bash
# Using Docker
docker-compose exec backend python -m backend.src.infrastructure.database.seeders.run_seeder

# Local development
python -m backend.src.main run-seeders
```

## 📝 API Documentation

The API documentation is automatically generated and available at:

- Swagger UI: http://localhost:8000/schema/swagger
- ReDoc: http://localhost:8000/schema/redoc

Key endpoints:

- `GET /api/v1/events` - List all events
- `GET /api/v1/events/{event_id}` - Get event details
- More endpoints coming soon...

## 🛠️ Development

### Creating Migrations

When you make changes to database models, you need to create a migration:

```bash
# Using Docker
docker-compose exec backend alembic revision --autogenerate -m "description"

# Local development
alembic revision --autogenerate -m "description"
```

### Running Tests

Tests to be implemented. The command will be:

```bash
pytest
```

### Code Style

This project uses:

- Mypy for type checking
- Ruff for format and linter

To check your code:

```bash
# Format and linting code
ruff backend/

# Type checking
mypy backend/

```

## 🧠 Architecture Overview

DevEvents follows Clean Architecture principles:

1. **Domain Layer** - Contains business entities and rules
2. **Application Layer** - Contains use cases and interfaces for external services
3. **Infrastructure Layer** - Contains implementations of interfaces defined in the application layer
4. **Interface Layer** - Contains API controllers, CLI commands, and other user interfaces

This architecture ensures:

- Independence from frameworks
- Testability
- Independence from the UI
- Independence from the database
- Independence from external agencies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Acknowledgments

- Litestar team for the amazing framework
- All contributors to the project
