# 🛡️ CyberFCIS — Cybersecurity Study Portal & Exam Coach

A comprehensive study portal, memory coach, interactive exam simulator, and solved previous exams archive for university cybersecurity courses.

**Course Instructors & Examiners:**  
- **Dr. Alshaimaa Abo-alian** (Faculty of Computers and Information Sciences, Ain Shams University)  
- **Prof. Walaa Khaled** (Faculty of Computers and Information Sciences, Ain Shams University)  

**Institution:** Faculty of Computers and Information Sciences (FCIS), Ain Shams University  
**Subject:** INF423 Cyber Security  
**Textbooks:**
- *Information Security* (8th Edition) by Mark Ciampa
- *Cisco CyberOps Associate CBROPS 200-201 Official Cert Guide* by Omar Santos

---

## 🚀 Features

### 1. 📝 Official Previous Exams Solved (Dedicated Tab)
* **Problem 1: Password Cracking & Precomputed Storage (Final Exam 11/01/2025 - 11 Marks):**
  * **Keyspace & Storage Space Derivation:** Step-by-step mathematical proof calculating total combinations ($N = 62$, $L = 8 \implies 62^8 = 218,340,105,584,896 \approx 2.1834 \times 10^{14}$ passwords), entry size (8 bytes password + 32 bytes binary SHA-256 = 40 bytes/entry), and total storage space required (**8.73 Petabytes** decimal / **7.76 Petabytes / 7,943 TB** binary; or ~15.72 PB for hex).
  * **Rainbow Tables & Time-Memory Trade-Off (TMTO):** Explains reduction functions, hash chains, storing only endpoints ($P_0$ and $P_m$), factor-of-$m$ disk space compression, and multi-reduction mitigation of chain collisions.
  * **5 Effective Mitigation Strategies:** Cryptographic Salting (unique random salt kills rainbow tables), Slow Key-Stretching Hashes (Argon2id, bcrypt, PBKDF2), Secret Pepper in HSM, Password Length & Entropy enforcement, and Multi-Factor Authentication (MFA).
* **Problem 2: Relational Database Access Control Matrix & SQL DCL (Final Exam 11/01/2025 - Question 4 - 15 Marks):**
  * Discretionary Access Control (DAC) model identification and drawbacks (Trojan horse vulnerabilities, lack of information flow control, matrix scalability).
  * Listing other existing models (MAC, RBAC, ABAC).
  * Generating Access Control Lists (ACLs) for Table1, Table2, Table3.
  * Production-ready SQL DCL statements (`GRANT SELECT`, `GRANT INSERT, UPDATE, DELETE`, column-level security).
  * Thorough explanation of `CASCADE` (recursive revocation down the grant tree) vs. `RESTRICT` (safe default abort on existing dependencies) in `REVOKE` statements.
* **Problem 3: University File System Access Control & Bell-LaPadula (BLP) Model (Question 4 - 12 Marks):**
  * Modeling ownership scenarios via Access Control Matrix (ACM), Access Control Lists (ACLs), and Capability Lists (C-Lists).
  * Discretionary Access Control (DAC) pros & cons.
  * Complete 8-row Bell-LaPadula (BLP) Mandatory Access Control table for all user-file combinations (Prof. Smith TS, TA1 S, Student1 C, Student2 U $\times$ FileA S, FileB C) with clear `Allowed` / `Denied` statuses and exact justifications based on the Simple Security Property (*No Read Up*) and the $\ast$-Property (*No Write Down*).
  * Core differences between MAC and DAC.
* **Problem 4: 10 High-Yield Official Exam MCQs:**
  * Complete interactive question cards with instant evaluation, verified official answer keys, tested concept badges, and in-depth distractor breakdowns explaining why wrong choices are incorrect.

---

### 2. ⚡ Instant Question Feedback Engine
* As soon as an option is selected across any lecture quiz, exam simulator, or past paper MCQ, the application immediately reveals correctness:
  * **Correct:** Emerald green glow with `✓ Correct` badge.
  * **Incorrect:** Rose red styling with `✗ Your Choice` badge.
  * **Immediate Right Answer Reveal:** The correct option is automatically highlighted in emerald green with `Correct Answer` badge so you learn immediately without waiting.
* Pedagogical justification card expands beneath the question with an option to *"Try Again"*.

---

### 3. 🎲 All-Lectures 100Q Shuffled Exam Simulator
* Aggregates all 100 questions from Lectures 1 through 5 into a single randomized exam mode.
* **🔀 Reshuffle Order:** Uses the Fisher-Yates algorithm to randomize question order on demand.
* **Filter Chips:** Filter by *All Questions*, *Unanswered*, *Missed / Review Needed*, or *Correct*.
* **Lecture Source Citations:** Shows which lecture each question originated from.
* **100-Question Jump Matrix:** A 100-pill interactive matrix with smooth one-click scrolling to any question.

---

### 4. 📚 5 Complete Lecture Modules
* **Lecture 1:** Introduction to Cybersecurity, FBI Statistics, CIA vs. DAD, Assets, CVE/CWE/CVSS, Controls & Risk Dimensions.
* **Lecture 2:** Cybersecurity Threat Landscape, Threat Actors, Attack Surfaces vs. Threat Vectors, NIST CSF 2.0, STRIDE, DREAD, PASTA, and MITRE ATT&CK.
* **Lecture 3:** Fundamentals of Cryptography, Symmetric vs. Asymmetric, Hashes, CSPRNGs, One-Time Pad, HMAC, and Key Management.
* **Lecture 4:** User Authentication, Factors, Password Storage & Salting, 8 Password Attacks, Bloom Filters, TOTP vs. HOTP, Biometrics (FAR/FRR/EER).
* **Lecture 5:** Access Control Models (DAC, MAC, RBAC, ABAC), Bell-LaPadula Model (WURD rules), SQL DCL (GRANT/REVOKE), and RBAC Constraints.

---

### 5. 🧠 Memory Aids & 3D Interactive Flashcards
* 3D perspective flip-cards for rapid recall of golden rules, definitions, and distinctions.
* Star (`★`) button to mark concepts as **Mastered** with real-time progress counters (`X/42 Mastered`).

---

### 6. 📊 Live Floating HUD & Keyboard Shortcuts
* Sticky bottom HUD tracks solved count, live score, accuracy percentage, and flame streaks (`🔥 Streak`).
* Progress automatically persists in `localStorage`.
* Press `Ctrl + K` or `/` anywhere to focus the global search bar.

---

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MahmoudSaad1307/CyberFCIS.git
   ```
2. Open `index.html` in any modern web browser (Chrome, Edge, Firefox, Safari).
   * **Zero dependencies or build tools required!** Fully standalone and operates 100% offline.

---

## 🛠️ Project Structure

```text
├── index.html              # Main interactive single-page study portal (Tailwind CSS + Vanilla JS)
├── build_portal.py         # Python builder script to re-generate index.html from data modules
├── data_previous_exams.py  # Solved past papers, math derivations, BLP matrices & 10 exam MCQs
├── data_lec1.py            # Lecture 1 summary, memory cards & 20 MCQs
├── data_lec2.py            # Lecture 2 summary, memory cards & 20 MCQs
├── data_lec3.py            # Lecture 3 summary, memory cards & 20 MCQs
├── data_lec4.py            # Lecture 4 summary, memory cards & 20 MCQs
├── data_lec5.py            # Lecture 5 summary, memory cards & 20 MCQs
├── .gitignore              # Git ignore file
└── README.md               # Complete documentation
```
