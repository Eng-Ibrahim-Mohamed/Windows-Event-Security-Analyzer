from event_reader import read_security_events
from detections import analyze_events
from report_generator import generate_report

events = read_security_events(limit=3000)

results = analyze_events(
    events
)

report = generate_report(
    results
)

print(report)

with open(
    "report.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(report)

print("Report Saved Successfully")