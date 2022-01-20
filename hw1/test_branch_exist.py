import subprocess

def test_does_branches_exist_as_specified():
    branch_cmd = """
    git branch -r
    """
    add_sort_strings_branch_exists = False
    add_cli_branch_exists = False
    main_branch_exists = False

    log_branch = subprocess.check_output(branch_cmd, shell=True, text=True, stderr=subprocess.STDOUT)
    
    if log_branch != None:
        for branch in log_branch.split("\n"):
            branch = branch.replace('origin/', '').strip()
            if (branch == "add/sort_strings"):
                add_sort_strings_branch_exists = True
            elif (branch == "add/cli"):
                add_cli_branch_exists = True
            elif (branch == "main"):
                main_branch_exists = True

    assert add_sort_strings_branch_exists == True
    assert add_cli_branch_exists == True
    assert main_branch_exists == True