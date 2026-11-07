# 🛡️ CyberFCIS — Cybersecurity Study Portal & Exam Coach

A comprehensive study portal, memory coach, and interactive exam simulator for university cybersecurity courses.

**Course Instructor:** Dr. Alshaimaa Abo-alian  
**Institution:** Faculty of Computers and Information Sciences (FCIS), Ain Shams University  
**Textbooks:**
- *Information Security* (8th Edition) by Mark Ciampa
- *Cisco CyberOps Associate CBROPS 200-201 Official Cert Guide* by Omar Santos

---

## 🚀 Features

* **5 Complete Lectures Covered:**
  * **Lecture 1:** Introduction to Cybersecurity, FBI Statistics, CIA vs. DAD, Assets, CVE/CWE/CVSS, Controls & Risk Dimensions.
  * **Lecture 2:** Cybersecurity Threat Landscape, Threat Actors, Attack Surfaces vs. Threat Vectors, NIST CSF 2.0, STRIDE, DREAD, PASTA, and MITRE ATT&CK.
  * **Lecture 3:** Fundamentals of Cryptography, Symmetric vs. Asymmetric, Hashes, CSPRNGs, One-Time Pad, HMAC, and Key Management.
  * **Lecture 4:** User Authentication, Factors, Password Storage & Salting, 8 Password Attacks, Bloom Filters, TOTP vs. HOTP, Biometrics (FAR/FRR/EER).
  * **Lecture 5:** Access Control Models (DAC, MAC, RBAC, ABAC), Bell-LaPadula Model (WURD rules), SQL DCL (GRANT/REVOKE), and RBAC Constraints.

* **⚡ Instant Question Feedback Engine:**
  * As soon as an option is selected, the application immediately indicates if it is **Correct** (emerald green glow) or **Incorrect** (rose red).
  * If answered incorrectly, the correct answer is automatically highlighted with a `Correct Answer` badge so you learn immediately without waiting.
  * The full pedagogical justification expands beneath the question.
  * Includes a "Try Again" option if you want to re-attempt questions after reviewing.

* **🎲 All-Lectures 100Q Shuffled Exam Simulator:**
  * Aggregates all 100 questions from Lectures 1 through 5 into a single randomized exam mode.
  * **🔀 Reshuffle Order:** Uses the Fisher-Yates algorithm to randomize question order on demand.
  * **Filter Chips:** Filter by *All Questions*, *Unanswered*, *Missed / Review Needed*, or *Correct*.
  * **Source Tags:** Shows which lecture each question originated from.
  * **100-Question Jump Matrix:** A 100-pill visual overview grid indicating answered status and jumping directly to any question.

* **📊 Live Floating HUD & Streak Tracker:**
  * Real-time tracking of questions solved, live score, accuracy percentage, and correct streaks (`🔥 Streak`).
  * Persists answers and progress in `localStorage` across reloads.

* **🧠 3D Interactive Flashcards & Mastery Tracking:**
  * Interactive 3D flip-cards for rapid memorization of golden rules, definitions, and distinctions.
  * Star (`★`) button to mark concepts as mastered with a real-time mastery counter.

* **🔍 Global Concept Search:**
  * Press `Ctrl + K` or `/` to search across all summaries, flashcards, and questions (e.g. `BLP`, `FAR`, `STRIDE`, `HMAC`, `CVSS`).

* **🎨 Dark OSINT/Cyber Terminal Theme:**
  * Built with Tailwind CSS, custom animations, clean typography (Inter & JetBrains Mono), and print-ready stylesheets.

---

## 💻 How to Run

1. Simply clone the repository:
   ```bash
   git clone https://github.com/MahmoudSaad1307/CyberFCIS.git
   ```
2. Open `index.html` in any web browser (Chrome, Edge, Firefox, Safari).
   * No dependencies, build tools, or web servers required! Works 100% offline.

---

## 🛠️ Project Structure

```text
├── index.html          # Main interactive single-page study portal (Tailwind CSS + Vanilla JS)
├── build_portal.py     # Python builder script to re-generate index.html from data modules
├── data_lec1.py        # Lecture 1 summary, memory cards & 20 MCQs
├── data_lec2.py        # Lecture 2 summary, memory cards & 20 MCQs
├── data_lec3.py        # Lecture 3 summary, memory cards & 20 MCQs
├── data_lec4.py        # Lecture 4 summary, memory cards & 20 MCQs
├── data_lec5.py        # Lecture 5 summary, memory cards & 20 MCQs
├── .gitignore          # Git ignore file
└── README.md           # Documentation
```
