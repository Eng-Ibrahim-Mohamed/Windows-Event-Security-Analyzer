from core.event_api import EventAPI
from core.xml_parser import parse_xml
from core.security_event_factory import create_security_event

from core.detection_engine import DetectionEngine
from core.alert_engine import AlertEngine


api = EventAPI()

handles = api.read_events(100)

events = []

for handle in handles:

    parsed = parse_xml(handle)

    events.append(
        create_security_event(parsed)
    )

engine = DetectionEngine(events)

result = engine.analyze()

alert_engine = AlertEngine(result)

alerts = alert_engine.generate()

print()

print("=" * 60)

print("SECURITY ALERTS")

print("=" * 60)

if not alerts:

    print("\nNo Alerts Found")

for alert in alerts:

    print(alert)