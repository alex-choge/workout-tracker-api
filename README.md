# workout-tracker-api
## Project Description
Welcome to my summative lab project! This is a backend REST API built with **Flask**, **SQLAlchemy**, and **Marshmallow** for a workout tracking application designed for personal trainers. It allows trainers to manage exercises, create workouts, and link exercises with specific sets, reps, and durations while maintaining robust data validation and relational constraints.

## Features
- **Exercises & Workouts:** Create, view, and delete exercises and workouts.
- **Join Table Relationships:** Add exercises to workouts with custom sets, reps, and durations.
- **Data Validation:** Built-in model validations, table constraints, and schema validations to keep data clean.
- **Database Seeding:** Easy setup script to populate sample data.

## Tech Stack
- Python 3.8+
- Flask (v2.2.2)
- Flask-SQLAlchemy (v3.0.3)
- Flask-Migrate (v3.1.0)
- Marshmallow (v3.20.1)

---

## Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the repository** and open your terminal inside the project folder.
2. **Install dependencies** using Pipenv:
   ```bash
   pipenv install
   pipenv shell
Run Instructions
To start the local development server, run:

Bash
python server/app.py
The application will run locally at http://localhost:5555. 

API Endpoints Reference Method Endpoint Description
GET/workoutsList all workouts
GET/workouts/<id>Show a single workout with its exercises and associated data
POST/workoutsCreate a new workout
DELETE/workouts/<id>Delete a workout and its associated join table records
GET/exercisesList all exercises
GET/exercises/<id>Show a single exercise with its associated workouts
POST/exercisesCreate a new exercise
DELETE/exercises/<id>Delete an exercise and its associated join table records
POST/workouts/<workout_id>/exercises/<exercise_id>/workout_exercisesAdd an exercise to a workout, including reps, sets, and duration

