#!/usr/bin/env python3

from gedcom-parse import parse

if __name__ == '__main__':
    import sys
    args = sys.argv
    print(args)
    if len(args) == 1:
        # normal start
        pass
    else:
        if args[1] == "--just-parse":
            if args[2] == "--json":
                json_return = True
            elif args[2] == "--dict":
                json_return = False
            else:
                print("HI")
                raise AttributeError("Flag --just-parse has to be followed by either --json or --dict.")
            try:
                filepath = args[3]
            except IndexError:
                raise IndexError("When using --just-parse the filepath to a gedcom file has to be provided.")
            data = parse(filepath, json_return)
            return data