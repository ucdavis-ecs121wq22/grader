import json
import os
from datetime import datetime

def test_merge_order():
    cmd = os.popen('git log --min-parents=2 --pretty=format:\'{"commit": "%H", "author": "%aN <%aE>", "branch": "%D", "date": "%ai", "message": \"""%B\""", "notes": \"""%N\""" },\' \
        $@  | awk \'BEGIN { print("[") } { print($0) } END { print("]") }\' | python -u -c \
        \'import ast,json,sys; print(json.dumps(ast.literal_eval(sys.stdin.read())))\'')
    history = json.loads(cmd.read())
    merge_sort_strings_string_date = None
    merge_cli_string_date = None

    for obj in history:
        message = obj["message"].split(" ")
        if (message[0] == "Merge" and message[1] == "pull" and message[2] == "request"):
            if ("add/sort_strings" in message[5]):
                merge_sort_strings_string_date = obj["date"][0:19]
            elif ("add/cli" in message[5]):
                merge_cli_string_date = obj["date"][0:19]    

    assert merge_sort_strings_string_date != None
    assert merge_cli_string_date != None

    date_time_format = '%Y-%m-%d %H:%M:%S'
    sort_strings_merge_date = None
    cli_merge_date = None

    sort_strings_merge_date = datetime.strptime(merge_sort_strings_string_date, date_time_format)
    cli_merge_date = datetime.strptime(merge_cli_string_date, date_time_format)    
    assert (sort_strings_merge_date != None) and (cli_merge_date != None) and (sort_strings_merge_date < cli_merge_date)