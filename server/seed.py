#!/usr/bin/env python3
from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercises


with app.app_context():
    WorkoutExercises.query.delete()
    Workout.query.delete()
    Exercise.query.delete()


ex=Exercise(name="Push-up", category="Strength", equipment_needed=False)
w =Workout(date=date(2026, 6, 10), duration_minutes=30, notes="Quick session")
db.session.add(ex, w)
db.session.commit()

we =WorkoutExercises(workout_id=w.id, exercise_id=ex.id, reps=10, sets=3, duration_seconds=30)
db.session.add(we)
db.session.commit()

print("Database seeded successfully")

