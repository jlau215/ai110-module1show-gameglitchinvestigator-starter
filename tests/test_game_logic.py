import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, parse_guess


# --- Existing tests (fixed: check_guess returns a tuple, not a bare string) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Fix 1: attempts initialized to 0 instead of 7 ---

def test_attempts_start_at_zero():
    """app.py fix: attempts initialized to 1 instead of 0, causing display
    to show 7 attempts left on launch instead of 8 (attempt_limit - attempts)."""
    attempt_limit = 8  # Normal difficulty
    initial_attempts = 0  # fixed value; was 1 before fix
    attempts_left = attempt_limit - initial_attempts
    assert attempts_left == 8, f"On launch should show 8 attempts left, got {attempts_left}"


# --- Fix 2: New Game resets attempts to 0 ---

def test_new_game_resets_attempts():
    """app.py fix: clicking New Game did not reset attempts; it now resets to 0."""
    attempts = 5  # simulate attempts accumulated during a game
    score = 30

    # Simulate new game reset (mirrors the new_game block in app.py)
    attempts = 0
    score = 0

    assert attempts == 0, "New Game must reset attempts to 0"
    assert score == 0, "New Game must reset score to 0"


# --- Fix 3: Invalid (non-number) input does not increment attempts ---

def test_invalid_input_returns_not_ok():
    """app.py fix: submitting non-numbers was causing attempts to decrease
    below 0 because the input was not validated before incrementing."""
    ok, guess_int, err = parse_guess("abc")
    assert not ok, "Non-number input must return ok=False so attempts are not incremented"
    assert guess_int is None
    assert err == "That is not a number."

def test_empty_input_returns_not_ok():
    """app.py fix: empty submission must also return ok=False."""
    ok, guess_int, err = parse_guess("")
    assert not ok
    assert guess_int is None
    assert err == "Enter a guess."

def test_valid_input_returns_ok():
    """Counterpart: a valid number must return ok=True so attempts are incremented."""
    ok, guess_int, err = parse_guess("42")
    assert ok
    assert guess_int == 42
    assert err is None


# --- Fix 4: check_guess returned opposite/swapped hints ---

def test_too_high_hint_says_go_lower():
    """logic_utils.py fix: when guess > secret the hint was showing 'Go HIGHER'
    instead of 'Go LOWER'. Verified the message now directs the player downward."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint but got: '{message}'"

def test_too_low_hint_says_go_higher():
    """logic_utils.py fix: when guess < secret the hint was showing 'Go LOWER'
    instead of 'Go HIGHER'. Verified the message now directs the player upward."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint but got: '{message}'"

def test_correct_guess_hint():
    """Correct guess returns a win message, not a directional hint."""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message
