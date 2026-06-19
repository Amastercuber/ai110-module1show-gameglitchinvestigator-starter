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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
