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


#### 5. Tasks

##### Task 1 (5 points)

Your task is to create an endpoint to display all tasks that have estimation value greater than 5. The code for the endpoint should be written in the `views.py` file. To filter the tasks we recommend using filtering query:
```py
models.ModelName.objects.filter(fieldName_gt=value)
```

After you manage to create the endpoint you should include it in the `urls.py` file so that it can be accessed.


##### Task 2 (10 points)

In this task your  job is to create a new viewset with cars. The `Car` model should have these fields:

- model (a char type field),
- year (an int type filed),
- price (a float type field),
- mileage (a float type field).

After you manage to write a new model for cars you should go ahead and create a new serializer in the `serializers.py` file as well as a new viewset in the `views.py` file. We suggest you look at the examples created for the `Task` model as this should be done in the similar way. After you manage to do all of this you should create migrations of the `Car` model and apply them. You can achieve this by executing the commands described in points 3 and 4. Lastly, same as in the first task you should add the url to it in the `urls.py` file.

##### Task 3 (15 points)

Your last task is fairly easy as it will require you to override the `create` method for the endpoint that you have written in the previous task. What you need to do is to make the mileage field optional in your `Car` model with default value (for example 0.0) and apply migrations. Then override the `create` method in the `views.py` file. It should take in a parameter with the value of the mileage you want your car to have. For this exercise you should use and evaluate this code snippet:

```py
mileage_param = openapi.Parameter('mileage', openapi.IN_QUERY, description="mileage manual param", type=openapi.TYPE_NUMBER)

#inside your car viewset
@swagger_auto_schema(request_body=serializers.CarSerializer, manual_parameters=[mileage_param])
    def create(self, request, *args, **kwargs):
        # your implementation of create method
```
