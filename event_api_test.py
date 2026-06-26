from core.event_api import EventAPI
from core.xml_parser import parse_xml

api = EventAPI()

events = api.read_events(20)

print()

print("Security Events Found:", len(events))

print()

for event in events:

    parsed = parse_xml(event)

    print(parsed["event_id"])