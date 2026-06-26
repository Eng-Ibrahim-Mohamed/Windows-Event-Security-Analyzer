from core.event_api import EventAPI
from core.xml_parser import parse_xml
from core.security_event_factory import create_security_event
from core.detection_engine import DetectionEngine


api = EventAPI()

handles = api.read_events(100)

events = []

for handle in handles:

    parsed = parse_xml(handle)

    event = create_security_event(parsed)

    events.append(event)


engine = DetectionEngine(events)

results = engine.analyze()

print(results)