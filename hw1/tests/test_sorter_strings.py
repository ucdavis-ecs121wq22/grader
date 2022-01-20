import src.sorter_api as sorter
import pytest

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