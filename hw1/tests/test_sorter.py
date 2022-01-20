import src.sorter_api as sorter
import subprocess
import pytest
import os
import sys

ABS_PATH = os.path.dirname(__file__)
TESTS_FILES = os.path.join(ABS_PATH, "cases")
cli_path = os.path.join(ABS_PATH, "..", "src", "sorter_cli.py")
output_path = os.path.join(TESTS_FILES, "output.txt")

def capture(command):
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out,err = proc.communicate()
    return out, err, proc.returncode

def printfile(path) -> str:
    print(f"path: {path}")
    if not os.path.exists(path):
        print(f"file {path} not found.", file = sys.stdout)
        raise FileNotFoundError
    out, err, exitcode = capture(["cat", path])
    return str(out)

def test_verify_message():
    SRT = sorter.Sorter()
    assert SRT.sort_nums([3,1,7,0,9,10]) == [0,1,3,7,9,10]
    
def test_verify_sort_numbers_desc():
    SRT = sorter.Sorter("numbers", "desc")
    assert SRT.sort_nums([3,1,7,0,9,10]) == [10,9,7,3,1,0]
    
def test_verify_sort_numbers_desc():
    SRT_DESC = sorter.Sorter("NUMBERS", "DESC")
    assert SRT_DESC.sort_nums([3,1,7,0,9,10]) == [10,9,7,3,1,0]
    
def test_verify_sort_numbers_asc():
    SRT = sorter.Sorter("numbers", "asc")
    assert SRT.sort_nums([3,-1,7,0,9,10]) == [-1,0,3,7,9,10]
    
def test_verify_sort_strings_desc():
    SRT_DESC = sorter.Sorter("LEXICOGRAPHICALLY", "DESC")
    assert SRT_DESC.sort_strings(["karan", "prem", "mohammed"]) == ["prem", "mohammed", "karan"]
    
def test_verify_sort_strings_asc():
    SRT = sorter.Sorter("lexicographically", "asc")
    assert SRT.sort_strings(["karan", "prem", "mohammed"]) == ["karan", "mohammed", "prem"]

def test_verify_sort_strings_desc():
    SRT = sorter.Sorter("lexicographically", "desc")
    assert SRT.sort_strings(["karan", "prem", "mohammed"]) == ["prem", "mohammed", "karan"]
    
def test_verify_cli_sorter_numbers_asc():
    test_file = os.path.join(TESTS_FILES, "input_numbers.txt")
    command = ["python3", cli_path, "numbers", "asc", test_file, output_path]
    out, err, exitcode = capture(command)
    val = printfile(output_path).replace("\\n", "")
    assert "b'-11357'" == val
    assert exitcode == 0

def test_verify_cli_sorter_numbers_desc():
    test_file = os.path.join(TESTS_FILES, "input_numbers.txt")
    command = ["python3", cli_path, "numbers", "desc", test_file, output_path]
    out, err, exitcode = capture(command)
    val = printfile(output_path).replace("\\n", "")
    assert "b'7531-1'" == val
    assert exitcode == 0

def test_verify_cli_sorter_strings_asc():
    test_file = os.path.join(TESTS_FILES, "input_strings.txt")
    command = ["python3", cli_path, "lexicographically", "asc", test_file, output_path]
    out, err, exitcode = capture(command)
    val = printfile(output_path).replace("\\n", "")
    assert "b'applebananacactus'" == val
    assert exitcode == 0
    
def test_verify_cli_sorter_strings_desc():
    test_file = os.path.join(TESTS_FILES, "input_strings.txt")
    command = ["python3", cli_path, "lexicographically", "desc", test_file, output_path]
    out, err, exitcode = capture(command)
    val = printfile(output_path).replace("\\n", "")
    assert "b'cactusbananaapple'" == val
    assert exitcode == 0