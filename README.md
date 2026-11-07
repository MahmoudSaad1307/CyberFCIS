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

* **Interactive Single-Page Application (`index.html`):**
  * **Simplified Summaries:** Clean cards, visual tags, bold technical terms, and comparison tables.
  * **3D Flashcards:** Interactive flip-cards for rapid memory recall of golden rules and definitions.
  * **100 Exam MCQs (20 per lecture):** Interactive quiz engine with real-time scoring, percentage calculation, and detailed explanations for every option.
  * **Global Concept Search:** Filter by keyword (e.g. `BLP`, `FAR`, `STRIDE`, `HMAC`, `CVSS`).
  * **Dark OSINT/Terminal UI:** Styled with pure Tailwind CSS.

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
