from datetime import datetime, timedelta

def generate_2025_journal(filename="Journal_2025.txt"):
    year = 2025
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    hours = [f"{hour:02}:00 {'AM' if hour < 12 else 'PM'}" for hour in range(2, 24)]

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{'='*25} DIARY FOR 2025 {'='*25}\n\n")

        # Start from January 1st
        date = datetime(year, 1, 1)

        # Move to the Monday of the first week
        while date.weekday() != 0:
            date -= timedelta(days=1)

        while date.year <= year:
            week_start = date
            f.write(f"📅 Week of {week_start.strftime('%B %d, %Y')}\n")
            f.write("-" * 80 + "\n")

            for i in range(7):  # Monday to Sunday
                current_day = date + timedelta(days=i)

                # Only include days within 2025
                if current_day.year != year:
                    continue

                f.write(f"🗓️  {current_day.strftime('%A, %B %d, %Y')}\n")
                for hour in range(2, 24):
                    hour_fmt = f"{hour:02}:00 {'AM' if hour < 12 else 'PM'}"
                    f.write(f"    [{hour_fmt}] ______________________________\n")
                f.write("\n")

            f.write("=" * 80 + "\n\n")
            date += timedelta(weeks=1)

    print(f"✅ 2025 Diary saved to '{filename}'")

if __name__ == "__main__":
    generate_2025_journal()
