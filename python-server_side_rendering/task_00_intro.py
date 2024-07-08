#!/usr/bin/env python3
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("template is {}: expected str".format(type(template).__name__))
    if len(template) == 0:
        raise ValueError("Template is empty, no output files generated.")
    if not isinstance(attendees, list):
        raise TypeError("attendees is {}: expected list".format(type(attendees).__name__))
    if not isinstance(attendees[0], dict):
        raise TypeError("attendees is list of {}: expected list of dict".format(type(attendees).__name__))
    if len(attendees) == 0:
        raise ValueError("No data provided, no output files generated.")

    ninvite = 1
    for attendee in attendees:
        output = template
        for k, v in attendee.items():
            if (v == None) or (v == ""):
                v = "N/A"
            output = output.replace("{%s}" % k, v)
        f = open("output_{}.txt".format(ninvite), "w")
        f.write(output)
        f.close()
        ninvite += 1
