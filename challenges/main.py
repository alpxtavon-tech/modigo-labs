def longest_streaks(daily_records):
    results = {}
    current_streak = {}

    for record in daily_records:
        for student, status in record.items():
            if status == "present":
                current_streak[student] = current_streak.get(student, 0) + 1
            else:
                current_streak[student] = 0

            results[student] = max(
                results.get(student, 0),
                current_streak[student]
            )

    return results
print