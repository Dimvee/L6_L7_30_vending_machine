
import pytest
from vending_machine import select_item, make_change, purchase


# SELECT ITEM TESTS

def test_invalid_item():
    assert select_item("water", {}, 200) == "invalid"

def test_sold_out():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"

def test_insufficient_credit():
    assert select_item("cola", {"cola": 5}, 100) == "insufficient"

def test_valid_selection():
    assert select_item("cola", {"cola": 5}, 150) == "ok"

def test_missing_stock():
    assert select_item("chips", {}, 200) == "sold_out"


# MAKE CHANGE TESTS

def test_negative_amount():
    with pytest.raises(ValueError):
        make_change(-10)

def test_zero_change():
    assert make_change(0) == []

def test_exact_change():
    assert make_change(150) == [100, 50]

def test_small_change():
    assert make_change(15) == [10, 5]

def test_unavailable_change():
    assert make_change(3) is None

def test_multiple_coins():
    assert make_change(190) == [100, 50, 25, 10, 5]


# PURCHASE TESTS

def test_successful_purchase():
    stock = {"cola": 5}
    assert purchase("cola", stock, 150) == ("dispensed", [])
    assert stock["cola"] == 4

def test_purchase_invalid_item():
    assert purchase("water", {}, 200) == ("invalid", [])

def test_purchase_sold_out():
    assert purchase("cola", {"cola": 0}, 200) == ("sold_out", [])

def test_purchase_insufficient_credit():
    assert purchase("cola", {"cola": 5}, 100) == ("insufficient", [])

def test_purchase_no_exact_change():
    stock = {"candy": 5}
    assert purchase("candy", stock, 78) == ("no_exact_change", [])
    assert stock["candy"] == 5

def test_purchase_with_change():
    stock = {"chips": 5}
    assert purchase("chips", stock, 175) == ("dispensed", [50, 25])
    assert stock["chips"] == 4
