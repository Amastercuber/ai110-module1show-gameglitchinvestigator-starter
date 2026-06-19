# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py` and open the app. Select a difficulty from the sidebar — the range and attempt count update accordingly.
2. Type a guess in the input box and either click "Submit Guess" or press Enter.
3. The hint  tells you to go higher or lower based on your guess relative to the secret.
4. Keep guessing .
5. Win or lose, click "New Game" and the game immediately resets and lets you guess again .



## 🧪 Test Results

```
$ python -m pytest tests/test_game_logic.py -v
============================= test session starts =============================
platform win32 -- Python 3.13.1, pytest-9.1.1, pluggy-1.6.0
collecting ... collected 7 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 42%]
tests/test_game_logic.py::test_bug2_too_high_message_says_go_lower PASSED [ 57%]
tests/test_game_logic.py::test_bug2_too_low_message_says_go_higher PASSED [ 71%]
tests/test_game_logic.py::test_bug1_new_game_resets_status SKIPPED       [ 85%]
tests/test_game_logic.py::test_bug5_enter_key_submits_guess SKIPPED      [100%]

======================== 5 passed, 2 skipped in 0.03s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
