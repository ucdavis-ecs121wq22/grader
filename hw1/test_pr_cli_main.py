import json
import os

def test_pr_cli_main():
    cmd = os.popen('git log --min-parents=2 --pretty=format:\'{"commit": "%H", "author": "%aN <%aE>", "branch": "%D", "date": "%ai", "message": \"""%B\""", "notes": \"""%N\""" },\' \
        $@  | awk \'BEGIN { print("[") } { print($0) } END { print("]") }\' | python -u -c \
        \'import ast,json,sys; print(json.dumps(ast.literal_eval(sys.stdin.read())))\'')
    history = json.loads(cmd.read())
    branch_merge_found = False
    for obj in history:
        message = obj["message"].split(" ")
        if (message[0] == "Merge" and message[1] == "pull" and message[2] == "request" and "add/cli" in message[5]):
            branch_merge_found = True

    assert branch_merge_found == True