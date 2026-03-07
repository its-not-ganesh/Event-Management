# Event Management Service

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.1-green.svg)](https://flask.palletsprojects.com/)

Build Event booking and seat inventory with agile practices.

This is a RESTful microservice for managing events, built with **Flask**, **SQLAlchemy**, and **PostgreSQL**, developed using **Test-Driven Development (TDD)** and **Agile** practices.

---

## Project Structure

```
Event-Management/
├── docker/
│   └── base/
│       └── Dockerfile          # Custom base image (replaces external pulls)
├── .devcontainer/
│   ├── Dockerfile              # Dev container image (extends base)
│   ├── devcontainer.json       # VS Code dev container config
│   ├── docker-compose.yml      # App + PostgreSQL compose stack
│   └── scripts/
│       ├── install-tools.sh    # Installs K3D, K9s
│       └── post-install.sh     # Post-create setup
├── service/
│   ├── __init__.py             # Flask app factory
│   ├── config.py               # App configuration
│   ├── routes.py               # REST API routes
│   ├── common/
│   │   ├── cli_commands.py     # Flask CLI extensions
│   │   ├── error_handlers.py   # HTTP error handlers
│   │   ├── log_handlers.py     # Logging setup
│   │   └── status.py           # HTTP status constants
│   └── models/
│       ├── __init__.py         # Model exports
│       └── persistent_base.py  # Base class with CRUD operations
├── tests/                      # Unit and integration tests
├── Makefile                    # Build, test, lint, deploy commands
├── Pipfile                     # Python dependencies
├── Procfile                    # Gunicorn process definition
├── setup.cfg                   # Tool configs (pytest, flake8, pylint, black)
└── wsgi.py                     # WSGI entry point
```

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine + Compose)
- [Visual Studio Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

---

## Getting Started

### 1. Build the Custom Base Image

This project uses a **self-built base image** instead of pulling a pre-built one. Build it once before opening the dev container:

```bash
make base-build
```

This creates `event-mgmt-base:latest` locally from `docker/base/Dockerfile`, which includes:

| Component | Version |
|-----------|---------|
| Python | 3.12 |
| Docker CLI | Latest stable |
| kubectl | Latest stable |
| Helm | Latest v3 |
| pipenv | Latest |
| OS | Debian Bookworm (slim) |

### 2. Open in Dev Container

Open the project in VS Code and when prompted, click **"Reopen in Container"**. Alternatively, use the Command Palette (`Ctrl+Shift+P`) and select **Dev Containers: Reopen in Container**.

This will:
- Build the dev container from `.devcontainer/Dockerfile` (using your base image)
- Start a PostgreSQL 15 database
- Install all Python dependencies from the Pipfile
- Install K3D and K9s for Kubernetes development
- Forward port **8080** to your host

### 3. Run the Service

```bash
make run
```

Or directly:

```bash
honcho start
```

The service will be available at **http://localhost:8080**.

---

## Development Workflow

### Install Dependencies

```bash
make install
```

### Run Tests

```bash
make test
```

Runs pytest with:
- Spec-style output (`--pspec`)
- Coverage reporting (`--cov=service`)
- Minimum 95% coverage enforcement (`--cov-fail-under=95`)

### Run Linter

```bash
make lint
```

Runs flake8 and pylint against `service/` and `tests/`.

### Code Formatting

Black is configured as the auto-formatter (line length: 127). VS Code will format on save.

### Generate a Secret Key

```bash
make secret
```

---

## Makefile Targets

| Target | Description |
|--------|-------------|
| `make help` | Display all available targets |
| `make base-build` | Build the custom base Docker image |
| `make base-build-multi` | Build multi-arch base image (amd64 + arm64) |
| `make install` | Install Python dependencies |
| `make lint` | Run flake8 and pylint |
| `make test` | Run unit tests with coverage |
| `make run` | Start the Flask service via Gunicorn |
| `make secret` | Generate a secret hex key |
| `make cluster` | Create a K3D Kubernetes cluster |
| `make cluster-rm` | Delete the K3D cluster |
| `make deploy` | Deploy to local Kubernetes |
| `make build` | Build the production container image |
| `make push` | Push image to container registry |
| `make buildx` | Build multi-platform production image |

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8080` | Port the service listens on |
| `FLASK_APP` | `wsgi:app` | Flask application entry point |
| `FLASK_DEBUG` | `True` | Enable debug mode (dev only) |
| `DATABASE_URI` | `postgresql+psycopg://postgres:postgres@localhost:5432/postgres` | PostgreSQL connection string |
| `SECRET_KEY` | `sup3r-s3cr3t` | Session secret (change in production) |
| `GUNICORN_BIND` | `0.0.0.0:8080` | Gunicorn bind address |

Copy `dot-env-example` to `.env` for local overrides:

```bash
cp dot-env-example .env
```

---

## Docker Architecture

This project eliminates external image dependencies by building everything from official upstream sources:

```
python:3.12-slim-bookworm          (Official Python base)
  └── event-mgmt-base:latest       (docker/base/Dockerfile — your custom base)
        └── dev container           (.devcontainer/Dockerfile — project-specific)
              + PostgreSQL 15       (docker-compose.yml — database sidecar)
```

To customize the base image name or tag:

```bash
make base-build BASE_IMAGE=my-custom-name BASE_TAG=v2
```

Then update `BASE_IMAGE` in `.devcontainer/docker-compose.yml` to match.

---

## Kubernetes Deployment

### Create a Local Cluster

```bash
make cluster
```

Creates a K3D cluster with:
- 2 worker nodes
- A local container registry at `cluster-registry:5000`
- Port 8080 mapped via load balancer

### Deploy the Service

```bash
make build    # Build the production image
make push     # Push to the local registry
make deploy   # Apply Kubernetes manifests from k8s/
```

### Tear Down

```bash
make cluster-rm
```

---

## Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.12 |
| Framework | Flask 3.1 |
| ORM | Flask-SQLAlchemy |
| Database | PostgreSQL 15 |
| DB Driver | psycopg 3 |
| Testing | pytest, factory-boy, coverage |
| Linting | flake8, pylint, black |
| Server | Gunicorn |
| Container | Docker, Docker Compose |
| Orchestration | Kubernetes (K3D) |
| Process Manager | honcho |

---

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
See the [LICENSE](LICENSE) file for details.
