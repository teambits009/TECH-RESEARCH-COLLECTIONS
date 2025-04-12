from datetime import datetime, timedelta

def generate_journal(filename="Journal_2000_to_2080.txt"):
    start_year = 2000
    end_year = 2080
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    hours = [f"{h:02}:00 {'AM' if h < 12 else 'PM'}" for h in range(2, 24)]

    with open(filename, "w", encoding="utf-8") as f:
        for year in range(start_year, end_year + 1):
            f.write(f"{'='*20} JOURNAL FOR {year} {'='*20}\n\n")

            # Start from Jan 1st of the year
            date = datetime(year, 1, 1)

            # Round down to the first Monday
            while date.weekday() != 0:
                date -= timedelta(days=1)

            # Go until end of the year
            while date.year <= year:
                f.write(f"Week of {date.strftime('%B %d, %Y')}\n")
                f.write("-" * 80 + "\n")

                for i in range(7):  # Monday to Sunday
                    current_day = date + timedelta(days=i)
                    f.write(f"  {current_day.strftime('%A, %B %d, %Y')}\n")
                    for hour in range(2, 24):
                        hour_fmt = f"{hour:02}:00 {'AM' if hour < 12 else 'PM'}"
                        f.write(f"    [{hour_fmt}] ______________________________\n")
                    f.write("\n")

                f.write("=" * 80 + "\n\n")
                date += timedelta(weeks=1)

    print(f"✅ Journal saved to '{filename}'")

if __name__ == "__main__":
    generate_journal()
