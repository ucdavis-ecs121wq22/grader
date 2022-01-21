import subprocess

def test_main_does_cli_branch_exist():
    branch_cmd = """
    git branch -r
    """
    main_branch_exists = False
    
    log_branch = subprocess.check_output(branch_cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    
    if log_branch != None:
        for branch in log_branch.split("\n"):
            branch = branch.replace('origin/', '').strip()
            if (branch == "main"):
                main_branch_exists = True

    assert main_branch_exists == True