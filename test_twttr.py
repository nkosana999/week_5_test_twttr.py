from twttr import shorten
import pytest

# Testing if the shorten() function catches and remove vowels?
def test_twttr_upper():
    assert shorten("PrIncE") == "Prnc"
    assert shorten("Prince") == "Prnc"

# Testing if shorten accepts numbers without raising errors?
def test_twttr_numbers():
    assert shorten("You12") == "Y12"

# Testing if shorten accepts punctuations without raising errors?
def test_twttr_punctuation():
    assert shorten("YOu!") == "Y!"