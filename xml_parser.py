import xml.etree.ElementTree as ET
import win32evtlog


def render_xml(event_handle):

    return win32evtlog.EvtRender(
        event_handle,
        win32evtlog.EvtRenderEventXml
    )


def parse_xml(event_handle):

    xml = render_xml(event_handle)

    root = ET.fromstring(xml)

    namespace = {
        "e": "http://schemas.microsoft.com/win/2004/08/events/event"
    }

    system = root.find("e:System", namespace)

    event_data = root.find("e:EventData", namespace)

    fields = {}

    if event_data is not None:

        for item in event_data.findall("e:Data", namespace):

            fields[item.attrib.get("Name")] = item.text or ""

    event_id = int(
        system.find(
            "e:EventID",
            namespace
        ).text
    )

    timestamp = system.find(
        "e:TimeCreated",
        namespace
    ).attrib.get("SystemTime", "")

    computer = system.find(
        "e:Computer",
        namespace
    ).text

    provider = system.find(
        "e:Provider",
        namespace
    ).attrib.get("Name", "")

    return {

        "event_id": event_id,

        "timestamp": timestamp,

        "computer": computer,

        "provider": provider,

        "fields": fields

    }