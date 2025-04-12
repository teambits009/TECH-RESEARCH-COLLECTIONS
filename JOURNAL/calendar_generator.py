import calendar

def boxify_month(month_str: str) -> str:
    """Wrap each month string in a neat ASCII box."""
    lines = month_str.splitlines()
    width = max(len(line) for line in lines)
    top = f"┌{'─' * (width + 2)}┐"
    bottom = f"└{'─' * (width + 2)}┘"
    boxed = [top]
    for line in lines:
        boxed.append(f"│ {line.ljust(width)} │")
    boxed.append(bottom)
    return "\n".join(boxed)

def generate_boxed_calendar(year: int) -> str:
    cal = calendar.TextCalendar(firstweekday=0)
    months = [cal.formatmonth(year, month).rstrip() for month in range(1, 13)]
    boxed_months = [boxify_month(month) for month in months]

    # Arrange months in 4 per row (3 rows of 4)
    output = f"{'='*30} Calendar for {year} {'='*30}\n\n"
    for i in range(0, 12, 4):
        row = boxed_months[i:i+4]
        row_lines = [r.splitlines() for r in row]
        for lines in zip(*row_lines):
            output += "   ".join(lines) + "\n"
        output += "\n"
    return output

def generate_full_calendar(start=2000, end=2080, filename="Boxed_Calendar_2000_to_2080.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for year in range(start, end + 1):  # ✅ include every year
            boxed = generate_boxed_calendar(year)
            f.write(boxed + "\n\n")
    print(f"✅ Full boxed calendar saved to '{filename}'")

if __name__ == "__main__":
    generate_full_calendar()
