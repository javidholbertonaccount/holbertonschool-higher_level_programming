import os

def generate_invitations(template, attendees):
    if type(template) is not str:
        print("Error: Template should be a string.")
        return
    if type(attendees) is not list or not all(type(a) is dict for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        output = template
        for placeholder in ['name', 'event_title', 'event_date', 'event_location']:
            val = attendee.get(placeholder)
            if val is None:
                val = "N/A"
            output = output.replace(f"{{{placeholder}}}", str(val))
        
        with open(f"output_{idx}.txt", 'w', encoding='utf-8') as f:
            f.write(output)
