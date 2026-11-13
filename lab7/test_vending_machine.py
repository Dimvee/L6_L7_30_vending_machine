
from hypothesis import given, settings, strategies as st
from vending_machine import parse_coins, slot_position, change_due

# Anything a user (or attacker) might feed in
junk = st.one_of(st.none(), st.text(), st.integers(), st.floats(), st.binary())


# ---------- parse_coins ----------
@settings(max_examples=500)
@given(junk)
def test_parse_coins_no_crash(s):
    try:
        result = parse_coins(s)
    except Exception as e:
        assert False, f"parse_coins crashed on {s!r}: {type(e).__name__}: {e}"
    assert isinstance(result, list)
    assert all(isinstance(c, int) and c > 0 for c in result)


@given(st.lists(st.integers(min_value=1, max_value=1000), min_size=1))
def test_parse_coins_valid_roundtrip(coins):
    assert parse_coins(",".join(map(str, coins))) == coins


# ---------- slot_position ----------
@settings(max_examples=500)
@given(junk)
def test_slot_position_no_crash(s):
    try:
        result = slot_position(s)
    except Exception as e:
        assert False, f"slot_position crashed on {s!r}: {type(e).__name__}: {e}"
    assert result is None or (
        isinstance(result, tuple) and len(result) == 2
        and result[0] >= 0 and result[1] >= 0
    )


@given(st.sampled_from("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), st.integers(min_value=1, max_value=999))
def test_slot_position_valid(letter, num):
    assert slot_position(f"{letter}{num}") == (ord(letter) - ord("A"), num - 1)


# ---------- change_due ----------
@settings(max_examples=500)
@given(junk)
def test_change_due_no_crash(s):
    try:
        result = change_due(s)
    except Exception as e:
        assert False, f"change_due crashed on {s!r}: {type(e).__name__}: {e}"
    assert isinstance(result, str)


@given(st.integers(min_value=0, max_value=10**6), st.integers(min_value=0, max_value=10**6))
def test_change_due_valid(paid, price):
    result = change_due(f"{paid}/{price}")
    if paid >= price:
        assert result == f"{(paid - price) // 5} five-coins"
    else:
        assert result == "insufficient payment"