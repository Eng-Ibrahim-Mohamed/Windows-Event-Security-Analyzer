from core.event_api import EventAPI
from core.xml_parser import parse_xml
from core.security_event_factory import create_security_event

from core.detection_engine import DetectionEngine
from core.correlation_engine import CorrelationEngine


api = EventAPI()

handles = api.read_events(100)

events = []

for handle in handles:

    parsed = parse_xml(handle)

    events.append(
        create_security_event(parsed)
    )

result = DetectionEngine(events).analyze()

alerts = CorrelationEngine(result).analyze()

print()

print("=" * 60)

print("CORRELATION ALERTS")

print("=" * 60)

if not alerts:

    print("\nNo Correlation Alerts")

for alert in alerts:

    print(alert)