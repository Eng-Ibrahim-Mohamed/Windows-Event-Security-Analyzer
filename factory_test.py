from core.event_api import EventAPI
from core.xml_parser import parse_xml
from core.security_event_factory import create_security_event

api = EventAPI()

events = api.read_events(1)

parsed = parse_xml(events[0])

security_event = create_security_event(parsed)

print(security_event)