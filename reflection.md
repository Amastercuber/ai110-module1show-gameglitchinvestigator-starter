# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
normal ig

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. didnt let me guess after i pressed new game, it did reroll the mystery number though
  2. when target was 81 and i guessed 50 it said lower, i think it messed up higher vs lower
  3. sometimes get negative target
  4. says 8 attempts allowed but only actually gave me 7
  5. pressing enter on the keyboard to submit a guess did nothing

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|------------|-------------------|-----------------|------------------------|
| Won a game, clicked "New Game" | should start fresh and let me guess again | still showed "you already won", couldn't do anything | none |
| secret was 81, guessed 50 | "Go HIGHER!" since my guess was too low | said "Go LOWER!" which is the opposite | none |
| 2nd guess of 9, secret was 50 | "Too Low", go higher | said "Too High" even though 9 is way below 50 | none |
| Normal difficulty, played a full game | should get 8 attempts as advertised | ran out after only 7 guesses | none — attempts counter started at 1 instead of 0, so one was already used before the first guess |
| typed a guess and pressed Enter | guess should submit | nothing happened, had to click the button manually | none — no st.form() wrapper so Enter key isn't connected to the submit button |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used Claude Code (Claude Sonnet 4.6) throughout the whole project for finding bugs, writing fixes, refactoring, and generating tests.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  For bug 1, I described the symptom (can't guess after clicking New Game) and Claude pointed straight to the missing `st.session_state.status = "playing"` line in the New Game handler. I verified it by running the app, winning a game, clicking New Game, and confirming I could guess again without the "you already won" message blocking me.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  When Claude generated the first three pytest cases, they compared `check_guess(...)` directly to a string like `"Win"`, but `check_guess` actually returns a tuple `(outcome, message)`. All three tests failed when I ran `pytest`. I caught it from the error output and had Claude fix the assertions to unpack the tuple with `outcome, _ = check_guess(...)`.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  For UI bugs I manually tested the exact steps that originally triggered the bug like winning a game and clicking New Game to confirm the input unlocked, or guessing 50 with a secret of 81 to confirm the hint now said "Go HIGHER". For logic bugs I ran pytest and checked that the new tests passed and none of the old ones broke.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I ran `python -m pytest tests/test_game_logic.py -v` after writing the bug 2 tests. `test_bug2_too_high_message_says_go_lower` and `test_bug2_too_low_message_says_go_higher` both passed, which confirmed the hint messages were now returning in the right direction. 

- Did AI help you design or understand any tests? How?

  Yeah, I asked Claude to generate pytest cases targeting the specific bugs. It wrote the two bug 2 tests checking the message part of the tuple, which was the exact thing the original tests were missing. It also added skipped tests for bugs 1 and 5 with comments explaining why those can't be unit tested that actually helped me understand which bugs live in UI state vs pure logic.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Every time you click a button or change anything, Streamlit reruns the whole script from top to bottom, so anything you want to remember between those reruns (like the secret number or game status) has to be stored in `st.session_state`, otherwise it resets.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  Working iteratively with the AI describing one symptom at a time, verifying the fix, then moving to the next bug kept things from getting messy and made it easy to know what actually solved what.

- What is one thing you would do differently next time you work with AI on a coding task?

  I'd check AI outputs more carefully before accepting them, like I would have caught the broken tuple assertions in the tests right away instead of needing to run pytest to find out.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  AI is powerful but not perfect it can zero in on a bug really fast but also confidently write code that's subtly wrong, so you still have to actually understand what it's doing and not just copy-paste and trust it.
