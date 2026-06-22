# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game had a Settings side bar on the left side of the screen. Below it had a Difficulty section with a clickable dropdown menu box. Below the box shows the range the secret number will be in and the number of attempts allowed. On the other side shows the game part of the page. It has a section called "Make a guess" and below has a blue information box saying "Guess a number between 1 and 100. Attempts left: 7" Below the blue section has a debug info dropdown which shows game informaation such as the secret number, score, guess and guess history. Below of the dropdown there is a section for entering your guess. There are 3 buttons for submitting guesses, starting a new game, and toggling show hint.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hints were telling the opposite way secret number was. The hint was telling me to go lower even though the secret was high and vice versa.
  2. New Game button does not work after using all of the attempts.
  3. Attempts do not match up between the left sidebar and the blue box telling how many attempts are left. In the left sidebar it says, "Attempts allowed: 8", but in the blue box it says "Attempts left: 7". Upon refreshing the game seems to start at 1 attempt being already used which is why it says 7 attempts left. Clicking New Game corrects the attempts.
  4. Attempts to not reset aftering clicking "New Game", making the user unable to submit their new guess.
  5. Submitting guesses that are non-numbers repeatedly will cause attempts left to go lower than 0.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                     | Expected Behavior                       | Actual Behavior                    | Console Output / Error |
|-------------------------------------------|-----------------------------------------|------------------------------------|------------------------|
| 91                                        | 91 should ouput "Go Lower"              | Outputs "Go Higher"                | None                   |
| ""                                        | Guess should not be accepted            | Guess is accepted and attempt used | None                   |
| abc                                       | Guess should not be accepted            | Guess is accepted and attempt used | None                   |
| Clicking New Game after all attempts used | Attempts reset to 8 and can submit guess| Attempts reset but cannot guess    | None                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI suggested that in order to fix the bug with hitting the New Game button it requireed 3 line changes. They suggested that in order to reset the number of attempts after clicking New Game, we need to have st.session_state.secret, st.session_state.status, and st.session_state.history set. These changes makes sure the state of the game is accurate and functions how the game is expected to work.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One example of an incorrect AI suggestion was in test_game_logic.py. For Fix 1 they said that the bug that was fixed was "attempts initialized to 0 instead of 7. This is incorrect. The issue with the game before the fix was that there would be 7 attempts left when the game first initializes when it should be 8.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I tested by running the app again and redoing my documented actions.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I did a manual test by running the app with the new code changes. It showed that my code was successful in fixing direct bugs I found earlier.
  
- Did AI help you design or understand any tests? How?
  The AI helped me understand the code more because at first the code looks confusing. After pinpointing certain lines, I asked the AI to explain what is going on. With that it helped me understand what is going on in the background.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit "reruns" are basically refreshes similar to how a browser will reload. In this case, streamlit will reload but will lose all memory of what happened. The state will reset to when the app was first initialized. A session state is a way to make an app remember what has happened and will store it in memory even after reruns. If the browser is refreshed, the apps memory will reset.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One strategy I want to reuse is a prompting one. I find that using "Act as a ..." helps generate more accurate results based on what I want. I feel that it is more consistent and gets technical to how real developers would analyze and fix code. Without this strategy, I think that I would run into more incorrect suggestions.

- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently next time while working with AI is providing full context to the AI especially about bugs I find. Context is important in order to get the most accurate and relevant response possible. Explaining the whole process of my thinking will help a lot with getting the correct solutions.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project made me think that AI generated code is not reliable. It needs to checked thoroughly before being pushed out.