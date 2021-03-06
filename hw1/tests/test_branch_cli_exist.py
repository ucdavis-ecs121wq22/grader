import subprocess

def test_branch_does_cli_branch_exist():
    branch_cmd = """
    git branch -r
    """
    add_cli_branch_exists = False
    
    log_branch = subprocess.check_output(branch_cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    
    if log_branch != None:
        for branch in log_branch.split("\n"):
            branch = branch.replace('origin/', '').strip()
            if (branch == "add/cli"):
                add_cli_branch_exists = True

    assert add_cli_branch_exists == True