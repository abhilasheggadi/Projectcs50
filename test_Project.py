import pytest
from Project import summarize,keywordize,size

def test_size():
    assert size(1)==10
    with pytest.raises(ValueError,match="Enter 1 or 2 or 3 only"):
        size(4)

def test_summarize():
    t ="hey welcome to cs50, we'll be exploring the various programming languages with great quality of conteent and structured curriculum"
    assert len(summarize(t,p=15))!=0
    with pytest.raises(ValueError,match="Empty text"):
        summarize("   ",10)

def test_keywordize():
    t ="hey welcome to cs50, we'll be exploring the various programming languages with great quality of conteent and structured curriculum"
    r=keywordize(t)
    assert len(r) !=0 
    assert "\n" in r 
    with pytest.raises(ValueError,match="Empty text"):
        keywordize("")