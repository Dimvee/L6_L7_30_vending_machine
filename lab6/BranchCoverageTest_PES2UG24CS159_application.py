
import pytest
from vending_machine import select_item, make_change, purchase


# SELECT ITEM - BRANCH TESTS

def test_invalid_item():
    assert select_item("water", {}, 200) == "invalid"

def test_valid_item():
    assert select_item("cola", {"cola": 5}, 150) == "ok"

def test_sold_out():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"

def test_available_stock():
    assert select_item("cola", {"cola": 5}, 200) == "ok"

def test_insufficient_credit():
    assert select_item("cola", {"cola": 5}, 100) == "insufficient"

def test_sufficient_credit():
    assert select_item("cola", {"cola": 5}, 150) == "ok"


# MAKE CHANGE - BRANCH TESTS

def test_negative_amount():
    with pytest.raises(ValueError):
        make_change(-10)

def test_non_negative_amount():
    assert make_change(0) == []

def test_while_condition_true_and_false():
    assert make_change(150) == [100, 50]

def test_remaining_amount():
    assert make_change(3) is None

def test_no_remaining_amount():
    assert make_change(0) == []


# PURCHASE - BRANCH TESTS

def test_purchase_status_not_ok():
    assert purchase("water", {}, 200) == ("invalid", [])

def test_purchase_status_ok():
    stock = {"cola": 5}
    assert purchase("cola", stock, 150) == ("dispensed", [])

def test_change_is_none():
    stock = {"candy": 5}
    assert purchase("candy", stock, 78) == ("no_exact_change", [])

def test_change_is_available():
    stock = {"chips": 5}
    assert purchase("chips", stock, 175) == ("dispensed", [50, 25])
