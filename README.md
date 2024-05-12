# TSD-django

## Description

Provide a brief description of your project here.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Setup

#### 1. Clone the repository:

```bash
git clone <repository-url>
```

#### 2. Navigate to the project directory:

```bash
cd <project-directory>
```

### Usage

#### 1. Build Docker Images

Build the Docker images for the project:

```bash
docker-compose build
```


#### 2. Run Docker Containers

Run the Docker containers either in detached mode (-d) or in the foreground:

```bash
docker-compose up
```

Or, to run in detached mode:

```bash
docker-compose up -d
```


#### 3. Make Migrations

Source the shell script to create Django migrations:

```bash
source ./bin/makemigrations.sh
```

#### 4. Apply migrations

Source the shell script to apply Django migrations:

```bash
source ./bin/migrate.sh
```