import pytest
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# --- Bug 2: Higher/Lower hint messages were swapped ---
# The original code returned "Go HIGHER!" when guess > secret and "Go LOWER!" when guess < secret,
# which is the opposite of what the player needs to do.

def test_bug2_too_high_message_says_go_lower():
    # guess=81, secret=50 — guess is too high, player needs to go lower
    outcome, message = check_guess(81, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"expected 'Go LOWER' hint but got: {message}"

def test_bug2_too_low_message_says_go_higher():
    # guess=50, secret=81 — guess is too low, player needs to go higher
    outcome, message = check_guess(50, 81)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"expected 'Go HIGHER' hint but got: {message}"

# --- Bug 1: New Game did not reset session status ---
# This bug lives entirely in Streamlit session state (app.py), not in a pure function,
# so it cannot be unit tested with pytest. Manual test: win or lose a game, click
# "New Game", and verify the guess input is available and status is "playing".

@pytest.mark.skip(reason="Bug 1 involves Streamlit session_state — not unit testable")
def test_bug1_new_game_resets_status():
    pass

# --- Bug 5: Pressing Enter did not submit the guess ---
# This bug was a missing st.form() wrapper in app.py (UI-only).
# There is no pure function to test; verify manually by typing a guess and pressing Enter.

@pytest.mark.skip(reason="Bug 5 involves Streamlit form/UI behavior — not unit testable")
def test_bug5_enter_key_submits_guess():
    pass
