#mashcise

def record_exercise(exercise_type, reps):
    print(f"Recording exercise: {exercise_type}, {reps} reps")
    return {"type": exercise_type, "reps": reps}

def track_progress(exercise_records):
    return progress