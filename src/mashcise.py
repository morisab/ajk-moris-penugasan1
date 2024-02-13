#mashcise

def record_exercise(exercise_type, sets, reps):
    print(f"Recording exercise: {exercise_type}, {sets} sets, {reps} reps")
    return {"type": exercise_type, "sets": sets, "reps": reps}

def track_progress(exercise_records):
    progress = {}
    total_sets = 0
    total_reps = 0
    for record in exercise_records:
        if record["type"] not in progress:
            progress[record["type"]] = {"sets": record["sets"], "reps": record["reps"]}
        else:
            progress[record["type"]]["sets"] += record["sets"]
            progress[record["type"]]["reps"] += record["reps"]
        total_sets += record["sets"]
        total_reps += record["reps"]

    print("\nYour Progress:")
    for exercise, data in progress.items():
        print(f"- {exercise}: {data['sets']} sets, {data['reps']} reps")
    print(f"\nTotal: {total_sets} sets, {total_reps} reps")
    return progress

print("Welcome to Mashcise!")
print("Let's record your exercises.\n")

exercise_records = []
while True:
    exercise_type = input("Enter exercise type (or 'done' to finish): ")
    if exercise_type.lower() == 'done':
        break
    sets = int(input("Enter number of sets: "))
    reps = int(input("Enter number of reps per set: "))
    exercise_records.append(record_exercise(exercise_type, sets, reps))

print("\nRecording completed.\n")
track_progress(exercise_records)