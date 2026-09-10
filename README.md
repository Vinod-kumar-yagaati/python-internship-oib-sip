# Python Programming Track – Internship Submission

**Submitted by:** [YAGAATI VINOD KUMAR]
**Date:** [10-09-2026]
**Tasks Completed:** 3 of 5 (minimum requirement met) — Tier: Beginner

---

## Task 2 — BMI Calculator
**Folder:** `task2_bmi_calculator/`
**File:** `bmi_calculator.py`
**How to run:** `python3 bmi_calculator.py`
**Features implemented:**
- Command-line weight/height input
- BMI = weight / height²
- Category classification (Underweight / Normal / Overweight / Obese)
- Result rounded to 2 decimals
- Input validation (non-numeric & negative values rejected)

---

## Task 3 — Random Password Generator
**Folder:** `task3_password_generator/`
**File:** `password_generator.py`
**How to run:** `python3 password_generator.py`
**Features implemented:**
- Length input (min 8 enforced)
- Character type selection (uppercase/lowercase/numbers/symbols), min 2 required
- Password generation matching selected criteria
- Input validation
- Loop to generate multiple passwords in one session

---

## Task 5 — Chat Application
**Folder:** `task5_chat_application/`
**Files:** `server.py`, `client.py`
**How to run:**
1. Terminal 1: `python3 server.py`
2. Terminal 2: `python3 client.py` (enter a name, e.g. Alice)
3. Terminal 3: `python3 client.py` (enter a name, e.g. Bob)
4. Type messages in either client terminal — they appear in real time in the other, with a timestamp prefix.

**Features implemented:**
- Socket server accepting multiple client connections (threaded)
- Real-time bidirectional messaging
- Timestamp prefix on every message: `[HH:MM] Name: message`
- Join/disconnect notifications broadcast to other users
- Runs entirely on localhost (127.0.0.1:5050)

---

## Notes
- All scripts use only Python standard library (`socket`, `threading`, `random`, `string`, `datetime`) — no external dependencies needed, so no `pip install` required.
- Tested locally: BMI calculator and password generator tested with valid/invalid inputs; chat app tested with two simulated clients exchanging messages successfully.
