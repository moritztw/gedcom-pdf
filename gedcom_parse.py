#!/usr/bin/env python3

import json


def debug_help(section, subsection, subsubsection, line, data):
    # debug_help(section, subsection, subsubsection, line, data)
    print("-")
    print("section:", section)
    print("subsection:", subsection)
    print("subsubsection:", subsubsection)
    print(line)
    print(json.dumps(data, indent=2))


# open a parser to read through gedcom file, also get length of file to determine its end while reading
def get_parser(filepath):
    file_len = len([line.strip() for line in open(filepath, "r")])
    parser = open(filepath, "r")
    return parser, file_len


def parse(filepath, json_return=False):
    parser, file_len = get_parser(filepath)
    data = {}
    # Starting on line 1
    line_count = 1
    #
    section = None
    subsection = None
    subsubsection = None
    while True:
        # End while Loop, when all lines are read
        if line_count >= file_len:
            break
        # Read File Line by Line
        line = parser.readline()
        # Split Line, so the space separated values of each line can be accessed as a list.
        line = line.split()
        # Get the values out of line
        line_number = int(line[0])
        line_name = line[1]
        if len(line) > 2:
            line_data = " ".join(line[2:])
        else:
            line_data = None
        # Begin of new dataset
        if line_number == 0:
            section = line_name
            subsection = None
            subsubsection = None
            data[section] = {}
            data[section][line_name] = line_data
        # Depth 1 of dataset
        elif line_number == 1:
            subsection = line_name
            if subsection not in data[section]:
                data[section][subsection] = {}
            data[section][subsection][line_name] = line_data
        # Depth 2 of dataset
        elif line_number == 2:
            subsubsection = line_name
            if subsubsection not in data[section][subsection]:
                data[section][subsection][subsubsection] = {}
            data[section][subsection][subsubsection][subsubsection] = line_data
        # Depth 3 or more of dataset
        else:
            data[section][subsection][subsubsection][subsubsection] += " " + line_data
        # count line_count up
        line_count += 1
    if json_return:
        return json.dumps(data, indent=2)
    else:
        return data


# For module testing purpose
if __name__ == '__main__':
    js_data = parse("./shakespeare.ged", True)
    print(js_data)
