import os
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Exercise, Workout, WorkoutExercises
from schemas import exercises_schema, exercise_schema, workouts_schema, workout_schema, workout_exercise_schema

app = Flask(__name__)

# Absolute path configuration for SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize app components only once
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Welcome to the Workout Tracker API!"

@app.route('/workouts', methods=['GET', 'POST'])
def handle_workouts():
    if request.method == 'GET':
        return jsonify(workouts_schema.dump(Workout.query.all()))
    
    data = request.json
    new_workout = Workout(date=data['date'], duration_minutes=data['duration_minutes'], notes=data.get('notes'))
    db.session.add(new_workout)
    db.session.commit()
    return jsonify(workout_schema.dump(new_workout)), 201

@app.route('/workouts/<int:id>', methods=['GET', 'DELETE'])
def handle_workout(id):
    workout = Workout.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(workout_schema.dump(workout))
    db.session.delete(workout)
    db.session.commit()
    return '', 204

@app.route('/exercises', methods=['GET', 'POST'])
def handle_exercises():
    if request.method == 'GET':
        return jsonify(exercises_schema.dump(Exercise.query.all()))
    
    data = request.json
    new_ex = Exercise(name=data['name'], category=data['category'], equipment_needed=data.get('equipment_needed', False))
    db.session.add(new_ex)
    db.session.commit()
    return jsonify(exercise_schema.dump(new_ex)), 201

@app.route('/exercises/<int:id>', methods=['GET', 'DELETE'])
def handle_exercise(id):
    ex = Exercise.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(exercise_schema.dump(ex))
    db.session.delete(ex)
    db.session.commit()
    return '', 204

@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_workout_exercise(workout_id, exercise_id):
    data = request.json
    new_we = WorkoutExercises(
        workout_id=workout_id,
        exercise_id=exercise_id,
        reps=data['reps'],
        sets=data['sets'],
        duration_seconds=data['duration_seconds']
    )
    db.session.add(new_we)
    db.session.commit()
    return jsonify(workout_exercise_schema.dump(new_we)), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)