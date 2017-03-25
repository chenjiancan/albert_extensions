#!/usr/bin/env python

"""
albert extension: ls DIR as input
usage:
    ls /some/where
    hit tab, and you will see commands list below the input box
    select one of those, hit enter, it will take you to the directory you choosed in nautilus
"""

import os
import sys
import json

albert_op = os.environ.get("ALBERT_OP")

f = open("/tmp/testlog", "a+")
f.writelines(str(albert_op))
f.close()

if albert_op == "METADATA":
    metadata="""{
      "iid":"org.albert.extension.external/v2.0",
      "name":"ls",
      "version":"1.0",
      "author":"raiz",
      "dependencies":[],
      "trigger":"ls"
    }"""
    print(metadata)
    sys.exit(0)

elif albert_op == "NAME":
    print(IBAN)
    f.close()
    sys.exit(0)

elif albert_op == "INITIALIZE":
    sys.exit(0)

elif albert_op == "FINALIZE":
    sys.exit(0)

elif albert_op == "SETUPSESSION":
    sys.exit(0)

elif albert_op == "SETUPSESSION":
    sys.exit(0)

elif albert_op == "TEARDOWNSESSION":
    sys.exit(0)

elif albert_op == "QUERY":

    albert_query = os.environ.get("ALBERT_QUERY")

    query_words = str(albert_query).split()
    query_arg = query_words[1:][0]

    # discript = "ls %s" % (query_args[0], )
    discript = os.popen("ls %s" % (query_arg, )).read()
    discript_array = discript.split('\n')
    discript = ' '.join(discript_array)

    result = {}
    items = []

    actions = []
    for file_or_dir in discript_array:
        is_file = os.path.isfile(os.path.join(query_arg,file_or_dir))
        if is_file:
            action = {
                "name": "goto {} 's directory".format(os.path.join(query_arg,file_or_dir)),
                "command":  "nautilus",
                "arguments": [query_arg, ]
            }
        else:
            action = {
                "name": "goto {}".format(os.path.join(query_arg,file_or_dir)),
                "command":  "nautilus",
                "arguments": [os.path.join(query_arg,file_or_dir), ]
            }
        actions.append(action)

    item = {
        "id":"extension.wide.unique.id.ls",
        "name":"ls",
        # "description":"ls description.",
        "description": str(discript),
        "icon":"accessories-calculator",
        "actions":actions
    }

    items.append(item)
    result['items'] = items
    print(json.dumps(result))
    sys.exit(0)

elif albert_op == "COPYTOCLIPBOARD":
    clipboard.copy(sys.argv[1])
    sys.exit(0)
