# -*- coding: utf-8 -*-
"""
Previous Exams Solved Data & HTML Generator Module
Contains complete solutions, step-by-step mathematical calculations, SQL DCL scripts,
Bell-LaPadula MAC access evaluation tables, and 10 detailed MCQ breakdowns from official FCIS Ain Shams University exams.
Examiners: Prof. Walaa Khaled & Dr. Alshaimaa Abo-alian
"""

EXAM_MCQS = [
    {
        "id": 1,
        "q": "Which of the following is an operational security control?",
        "options": [
            "Antivirus",
            "Access control policy",
            "Log monitoring",
            "An encryption algorithm"
        ],
        "ans": "C",
        "concept": "Security Controls (Operational vs. Technical vs. Managerial)",
        "explanation": (
            "<strong>Correct Answer: (C) Log monitoring</strong><br><br>"
            "• <strong>Why C is correct:</strong> Operational controls are security measures that are executed and managed primarily by <em>people</em> during day-to-day operations (e.g. security analysts monitoring logs, patch management routines, incident response handling).<br>"
            "• <strong>Why A & D are incorrect:</strong> Antivirus and Encryption algorithms are automated hardware/software mechanisms, which classify strictly as <em>Technical (Logical) controls</em>.<br>"
            "• <strong>Why B is incorrect:</strong> Access control policy is a set of guidelines and organizational rules created by management, making it an <em>Administrative / Managerial control</em>."
        )
    },
    {
        "id": 2,
        "q": "Firewalls and IDS/IPS are considered:",
        "options": [
            "Technical controls",
            "Operational controls",
            "Managerial controls",
            "Physical controls"
        ],
        "ans": "A",
        "concept": "Technical / Logical Security Controls",
        "explanation": (
            "<strong>Correct Answer: (A) Technical controls</strong><br><br>"
            "• <strong>Why A is correct:</strong> Technical controls (also called logical controls) use technology, software, firmware, and hardware systems to enforce security policies and protect networks and data. Firewalls, Intrusion Detection Systems (IDS), and Intrusion Prevention Systems (IPS) automatically inspect packet headers and payloads in real time.<br>"
            "• <strong>Distractor breakdown:</strong> Operational controls involve human procedures (e.g. security awareness training); Managerial controls involve written policies and risk assessments; Physical controls involve locks, fences, and guards."
        )
    },
    {
        "id": 3,
        "q": "The DAD Triad represents:",
        "options": [
            "The NIST framework functions",
            "Categories of security controls",
            "The attacker's objectives",
            "Threat modeling methodology"
        ],
        "ans": "C",
        "concept": "CIA Triad vs. DAD Triad",
        "explanation": (
            "<strong>Correct Answer: (C) The attacker's objectives</strong><br><br>"
            "• <strong>Why C is correct:</strong> The DAD Triad is the malicious inversion of the defender's CIA Triad:<br>"
            "&nbsp;&nbsp;&nbsp;&nbsp;1. <strong>D</strong>isclosure = Violation of Confidentiality (unauthorized viewing of data)<br>"
            "&nbsp;&nbsp;&nbsp;&nbsp;2. <strong>A</strong>lteration = Violation of Integrity (unauthorized tampering or modification)<br>"
            "&nbsp;&nbsp;&nbsp;&nbsp;3. <strong>D</strong>enial / Destruction = Violation of Availability (causing disruption or downtime)<br>"
            "• <strong>Distractor breakdown:</strong> NIST functions are IPDRR (Identify, Protect, Detect, Respond, Recover); Threat modeling methodologies include STRIDE, DREAD, and PASTA."
        )
    },
    {
        "id": 4,
        "q": "Central City Libraries keeps a spare copy of its database and a backup power supply so that staff can always issue and return books, even during a power cut. Which security goal is this mainly protecting?",
        "options": [
            "Confidentiality",
            "Integrity",
            "Availability",
            "Authenticity"
        ],
        "ans": "C",
        "concept": "Availability & Business Continuity",
        "explanation": (
            "<strong>Correct Answer: (C) Availability</strong><br><br>"
            "• <strong>Why C is correct:</strong> Availability guarantees that systems, data, and critical services remain accessible and operable for authorized users whenever needed. Redundant backup power supplies (UPS / generators) and replicated database copies ensure business continuity during an outage.<br>"
            "• <strong>Distractor breakdown:</strong> Confidentiality prevents unauthorized disclosure; Integrity prevents unauthorized modification; Authenticity verifies identity claims."
        )
    },
    {
        "id": 5,
        "q": "In STRIDE, Which category names the threat of unauthorized modification of data?",
        "options": [
            "Tampering",
            "Spoofing",
            "Repudiation",
            "Information disclosure"
        ],
        "ans": "A",
        "concept": "Microsoft STRIDE Threat Modeling",
        "explanation": (
            "<strong>Correct Answer: (A) Tampering</strong><br><br>"
            "• <strong>Why A is correct:</strong> In the Microsoft STRIDE model, <strong>Tampering</strong> specifically represents the threat of unauthorized modification or alteration of data, code, or configuration files (violating Integrity).<br>"
            "• <strong>Full STRIDE Mappings:</strong><br>"
            "&nbsp;&nbsp;• <strong>S</strong>poofing → Impersonating a user or system (violates Authenticity)<br>"
            "&nbsp;&nbsp;• <strong>T</strong>ampering → Unauthorized modification of data (violates Integrity)<br>"
            "&nbsp;&nbsp;• <strong>R</strong>epudiation → Denying an action took place (violates Non-repudiation)<br>"
            "&nbsp;&nbsp;• <strong>I</strong>nformation Disclosure → Leaking sensitive data (violates Confidentiality)<br>"
            "&nbsp;&nbsp;• <strong>D</strong>enial of Service → Making services unavailable (violates Availability)<br>"
            "&nbsp;&nbsp;• <strong>E</strong>levation of Privilege → Gaining unearned administrative rights."
        )
    },
    {
        "id": 6,
        "q": "A university discovers that its web server is running outdated OS. How should this case be classified?",
        "options": [
            "Threat",
            "Risk",
            "Vulnerability",
            "Security incident"
        ],
        "ans": "C",
        "concept": "The Cybercrime Chain (Vulnerability vs. Threat vs. Risk)",
        "explanation": (
            "<strong>Correct Answer: (C) Vulnerability</strong><br><br>"
            "• <strong>Why C is correct:</strong> A <strong>Vulnerability</strong> is an inherent weakness, flaw, misconfiguration, or unpatched software state within a system that creates an opportunity for exploitation. An outdated operating system with unpatched security flaws is a textbook vulnerability.<br>"
            "• <strong>Distractor breakdown:</strong> A <em>Threat</em> is an external agent or event that could exploit the flaw (e.g. a ransomware actor); <em>Risk</em> is the probability of financial/operational loss; a <em>Security incident</em> occurs when an actual breach takes place."
        )
    },
    {
        "id": 7,
        "q": "Alice and Bob need to exchange messages and verify both message integrity and origin authentication. They already share a secret key. Which technique is most appropriate?",
        "options": [
            "MD5 alone",
            "Steganography",
            "HMAC",
            "A pseudorandom number generator"
        ],
        "ans": "C",
        "concept": "HMAC (Keyed-Hash Message Authentication Code)",
        "explanation": (
            "<strong>Correct Answer: (C) HMAC</strong><br><br>"
            "• <strong>Why C is correct:</strong> <strong>HMAC (Hash-based Message Authentication Code)</strong> couples a cryptographic hash function with a shared secret key (K). It provides both <strong>Message Integrity</strong> (detecting if message was modified) and <strong>Data Origin Authentication</strong> (proving the message originated from a party holding secret key K).<br>"
            "• <strong>Why A is incorrect:</strong> MD5 alone is unkeyed; an active Man-in-the-Middle attacker can alter the plaintext message and recalculate MD5(M')."
        )
    },
    {
        "id": 8,
        "q": "A hospital needs to encrypt large patient-record files stored on its servers. Which type of encryption best matches this requirement?",
        "options": [
            "Stream cipher",
            "Block cipher",
            "Cryptographic hash function",
            "Digital signature"
        ],
        "ans": "B",
        "concept": "Block Ciphers vs. Stream Ciphers",
        "explanation": (
            "<strong>Correct Answer: (B) Block cipher</strong><br><br>"
            "• <strong>Why B is correct:</strong> <strong>Block ciphers</strong> (such as AES) operate on fixed-size blocks of plaintext (typically 128 bits) using chaining modes like CBC or GCM. They are specifically optimized for encrypting bulk data at rest (files, databases, storage partitions).<br>"
            "• <strong>Distractor breakdown:</strong> Stream ciphers are best suited for real-time continuous communication streams where message length is unknown in advance; Hash functions are one-way and cannot be decrypted; Digital signatures provide authenticity, not bulk data encryption."
        )
    },
    {
        "id": 9,
        "q": "An attacker attempts to break an encrypted database by systematically trying every possible encryption key until one works. Which type of attack is being performed?",
        "options": [
            "Brute-force attack",
            "Cryptanalytic attack",
            "Digital signature verification",
            "Man-in-the-Middle attack"
        ],
        "ans": "A",
        "concept": "Brute-Force vs. Cryptanalytic Attacks",
        "explanation": (
            "<strong>Correct Answer: (A) Brute-force attack</strong><br><br>"
            "• <strong>Why A is correct:</strong> A <strong>Brute-force attack</strong> (exhaustive key search) involves trying every single possible key in the keyspace sequentially until the correct decryption key is identified.<br>"
            "• <strong>Distractor breakdown:</strong> A <em>Cryptanalytic attack</em> exploits mathematical weaknesses or statistical patterns in the cipher algorithm without exhaustively trying every key."
        )
    },
    {
        "id": 10,
        "q": "An attacker encrypts a hospital's files and demands payment in exchange for the decryption key. Which threat actor is most likely?",
        "options": [
            "Script Kiddie",
            "Hacktivist",
            "Cybercriminal",
            "Nation-state attacker"
        ],
        "ans": "C",
        "concept": "Threat Actor Typology & Motivations",
        "explanation": (
            "<strong>Correct Answer: (C) Cybercriminal</strong><br><br>"
            "• <strong>Why C is correct:</strong> Threat actors are classified by motivation. <strong>Cybercriminals</strong> are driven primarily by <strong>financial profit</strong>. Encrypting critical hospital files and demanding a ransom payment in exchange for the decryption key is classic ransomware extortion conducted by organized cybercriminal syndicates.<br>"
            "• <strong>Distractor breakdown:</strong> Hacktivists are motivated by political/social causes; Nation-state actors target geopolitical espionage; Script Kiddies use pre-packaged tools for notoriety or amusement."
        )
    }
]

def generate_exams_html():
    """
    Returns the complete HTML content for the 'Solved Previous Exams' tab.
    """
    # 1. Math Section HTML
    math_html = """
    <div id="exam-sec-math" class="p-6 rounded-2xl bg-slate-900/90 border border-slate-800 glow-border-cyan space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
            <div>
                <span class="px-2.5 py-0.5 rounded bg-cyan-950/80 border border-cyan-500/40 text-cyan-300 font-mono text-xs font-semibold">
                    Final Exam (11/01/2025) · 11 Marks
                </span>
                <h3 class="text-xl font-bold text-white mt-1">Problem 1: Precomputed Hash Table Storage & Rainbow Tables</h3>
                <p class="text-xs text-slate-400 font-mono">Examiners: Prof. Walaa Khaled & Dr. Alshaimaa Abo-alian</p>
            </div>
            <span class="px-3 py-1 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 font-mono text-xs font-bold self-start sm:self-auto">
                Topic: Cryptographic Storage & Hashing
            </span>
        </div>

        <!-- Problem Statement Box -->
        <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 text-sm">
            <div class="font-mono text-xs text-slate-400 uppercase tracking-wider font-bold mb-1">Exam Scenario:</div>
            <p class="text-slate-200 leading-relaxed font-sans">
                An attacker aims to construct a pre-computed table for cracking <strong>8-character passwords</strong> which are composed of the <strong>62 alphanumeric characters (A-Z, a-z, 0-9)</strong> and hashed by <strong>SHA-256</strong>.
            </p>
        </div>

        <!-- Part A: Storage Space Calculation -->
        <div class="space-y-4">
            <div class="flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-300 font-mono font-bold flex items-center justify-center text-xs border border-cyan-500/40">a</span>
                <h4 class="text-base font-bold text-white">Calculate the total storage space required to store the table. <span class="text-cyan-400 text-xs font-mono">(3 marks)</span></h4>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <!-- Step 1 & 2 -->
                <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800 space-y-2">
                    <div class="text-xs font-mono font-bold text-cyan-400 flex items-center gap-1.5">
                        <span>Step 1: Character Set Size (N)</span>
                    </div>
                    <ul class="text-xs text-slate-300 space-y-1 font-mono">
                        <li>• Uppercase English letters (A–Z): <strong>26</strong></li>
                        <li>• Lowercase English letters (a–z): <strong>26</strong></li>
                        <li>• Decimal Digits (0–9): <strong>10</strong></li>
                        <li class="pt-1 text-cyan-300 border-t border-slate-800 font-bold">Total characters (N) = 26 + 26 + 10 = 62</li>
                    </ul>

                    <div class="text-xs font-mono font-bold text-cyan-400 pt-3 flex items-center gap-1.5">
                        <span>Step 2: Keyspace (Total Passwords, K)</span>
                    </div>
                    <p class="text-xs text-slate-300 font-sans leading-relaxed">
                        For passwords of length <code>L = 8</code>:
                    </p>
                    <div class="p-2.5 rounded bg-slate-900 border border-slate-800 font-mono text-xs text-slate-200">
                        K = N<sup>L</sup> = 62<sup>8</sup><br>
                        <strong>K = 218,340,105,584,896 passwords</strong><br>
                        <span class="text-slate-400">≈ 2.1834 × 10<sup>14</sup> passwords</span>
                    </div>
                </div>

                <!-- Step 3 & 4 -->
                <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800 space-y-2">
                    <div class="text-xs font-mono font-bold text-cyan-400 flex items-center gap-1.5">
                        <span>Step 3: Size of Each Entry</span>
                    </div>
                    <p class="text-xs text-slate-300 leading-relaxed font-sans">
                        A precomputed lookup table stores pairs of <code>(Password, Hash)</code>:
                    </p>
                    <ul class="text-xs text-slate-300 space-y-1 font-mono">
                        <li>• Plaintext password (8 chars): <strong>8 bytes</strong></li>
                        <li>• SHA-256 Digest (256 bits): <strong>32 bytes</strong> (raw binary)</li>
                        <li class="pt-1 text-emerald-300 border-t border-slate-800 font-bold">Total size per entry = 8 + 32 = 40 bytes</li>
                    </ul>
                    <p class="text-[11px] text-slate-500 italic mt-1 font-sans">
                        *Note: If stored in hex text format, SHA-256 is 64 hex characters = 64 bytes (8 + 64 = 72 bytes/entry). Both are accepted by examiners.
                    </p>

                    <div class="text-xs font-mono font-bold text-cyan-400 pt-2 flex items-center gap-1.5">
                        <span>Step 4: Total Storage Space</span>
                    </div>
                    <div class="p-2.5 rounded bg-slate-900 border border-slate-800 font-mono text-xs text-slate-200 space-y-1">
                        <div>Total Bytes = 218,340,105,584,896 × 40 bytes</div>
                        <div class="text-emerald-400 font-bold">= 8,733,604,223,395,840 Bytes</div>
                        <div class="text-slate-400 text-[11px] pt-1 border-t border-slate-800">
                            • In Terabytes (TB): 8,733,604,223,395,840 / 1024<sup>4</sup> ≈ <strong>7,943.17 TB</strong><br>
                            • In Petabytes (PB binary): 7,943.17 / 1024 ≈ <strong>7.76 PB</strong> (or <strong>8.73 PB</strong> in decimal 10<sup>15</sup>)
                        </div>
                    </div>
                </div>
            </div>

            <!-- Conclusion Alert -->
            <div class="p-3.5 rounded-xl bg-cyan-950/40 border border-cyan-500/40 flex items-center justify-between gap-4">
                <div class="flex items-center gap-2">
                    <span class="text-lg">📌</span>
                    <span class="text-xs text-cyan-200 font-mono">
                        <strong>Official Answer:</strong> Total storage required is <strong>8.73 Petabytes</strong> (decimal SI) or <strong>7.76 Petabytes (7,943 TB binary)</strong>. (If 72 bytes/entry hex is assumed, storage is ~15.72 PB).
                    </span>
                </div>
            </div>
        </div>

        <!-- Part B: Storage Reduction Techniques -->
        <div class="space-y-3 pt-4 border-t border-slate-800">
            <div class="flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-300 font-mono font-bold flex items-center justify-center text-xs border border-cyan-500/40">b</span>
                <h4 class="text-base font-bold text-white">Discuss how the attacker can reduce storage requirements of the precomputed table. <span class="text-cyan-400 text-xs font-mono">(3 marks)</span></h4>
            </div>

            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3 text-xs sm:text-sm text-slate-200">
                <p>
                    The attacker can drastically reduce storage requirements by implementing <strong>Time-Memory Trade-Off (TMTO)</strong> techniques, most notably <strong>Rainbow Tables</strong> (or Hellman's hash chains):
                </p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 pt-1">
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                        <strong class="text-cyan-400 font-mono block mb-1">1. Hash Chains & Reduction Functions</strong>
                        <p class="text-slate-300 text-xs">
                            Instead of saving all pairs, chains are formed by alternating between the hash function <code>H</code> and a reduction function <code>R</code> that maps 256-bit hashes back into 8-character plaintexts:
                            <code class="block mt-1 text-[11px] text-cyan-300">P₀ → H(P₀) → R₁(H) → P₁ → ... → Pₘ</code>
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                        <strong class="text-emerald-400 font-mono block mb-1">2. Store Only Chain Endpoints</strong>
                        <p class="text-slate-300 text-xs">
                            The attacker only saves the <strong>Start Password (P₀)</strong> and the <strong>End Password (Pₘ)</strong> on disk! All intermediate <code>m-1</code> passwords and hashes are discarded, reducing required disk space by a factor of <code>m</code> (e.g. 10,000× compression).
                        </p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
                        <strong class="text-purple-400 font-mono block mb-1">3. Different Reduction Functions</strong>
                        <p class="text-slate-300 text-xs">
                            Rainbow tables use a different reduction function (<code>R₁, R₂, ..., Rₘ</code>) at each position in the chain, eliminating the chain collisions and merges that plagued Hellman's original single-function chains.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Part C: Mitigation Strategies -->
        <div class="space-y-3 pt-4 border-t border-slate-800">
            <div class="flex items-center gap-2">
                <span class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-300 font-mono font-bold flex items-center justify-center text-xs border border-cyan-500/40">c</span>
                <h4 class="text-base font-bold text-white">Identify effective mitigation strategies if an attacker employs techniques to reduce storage requirements. <span class="text-cyan-400 text-xs font-mono">(5 marks)</span></h4>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                <div class="p-3.5 rounded-xl bg-slate-950 border border-cyan-500/30">
                    <span class="text-xs font-mono font-bold text-cyan-400 uppercase tracking-wider block mb-1">1. Cryptographic Salting (#1 Defense)</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Append a unique, random string (≥16 bytes) to each password before hashing: <code>Hash(Salt || Password)</code>. Because every user has a distinct salt, precomputed tables become completely useless—an attacker would have to compute a multi-petabyte table for every single individual salt.
                    </p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-950 border border-emerald-500/30">
                    <span class="text-xs font-mono font-bold text-emerald-400 uppercase tracking-wider block mb-1">2. Slow Key Stretching Hashes</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Replace fast general hashes (like SHA-256) with slow, resource-intensive algorithms such as <strong>Argon2id</strong>, <strong>bcrypt</strong>, or <strong>PBKDF2</strong>. High iteration counts and RAM memory hardness make generating reduction chains computationally infeasible.
                    </p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-950 border border-purple-500/30">
                    <span class="text-xs font-mono font-bold text-purple-400 uppercase tracking-wider block mb-1">3. Secret Pepper</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        A system-wide secret key stored outside the database (e.g. in a Hardware Security Module - HSM or secret vault). Even if attackers steal the database hashes and salts, they cannot generate tables without knowing the secret pepper.
                    </p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-950 border border-amber-500/30">
                    <span class="text-xs font-mono font-bold text-amber-400 uppercase tracking-wider block mb-1">4. Enforce Password Length & Entropy</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Enforce a minimum length of 12 to 16 characters. Increasing length exponentially explodes the keyspace (<code>62¹² ≈ 3.22 × 10²¹</code>), making precomputed tables physically impossible to store even with rainbow compression.
                    </p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-950 border border-rose-500/30 sm:col-span-2 lg:col-span-2">
                    <span class="text-xs font-mono font-bold text-rose-400 uppercase tracking-wider block mb-1">5. Multi-Factor Authentication (MFA) & Rate Limiting</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Even if an attacker cracks a password offline, MFA (TOTP / FIDO2 security keys) blocks unauthorized account access without the physical second factor. Account lockouts and exponential backoff prevent online brute-force guessing.
                    </p>
                </div>
            </div>
        </div>
    </div>
    """

    # 2. Database DAC & SQL DCL Section HTML
    db_html = """
    <div id="exam-sec-db-dac" class="p-6 rounded-2xl bg-slate-900/90 border border-slate-800 glow-border-cyan space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
            <div>
                <span class="px-2.5 py-0.5 rounded bg-purple-950/80 border border-purple-500/40 text-purple-300 font-mono text-xs font-semibold">
                    Final Exam (11/01/2025) · Question 4 · 15 Marks
                </span>
                <h3 class="text-xl font-bold text-white mt-1">Problem 2: Relational Database Access Control Matrix & SQL DCL</h3>
                <p class="text-xs text-slate-400 font-mono">Examiners: Prof. Walaa Khaled & Dr. Alshaimaa Abo-alian</p>
            </div>
            <span class="px-3 py-1 rounded-full bg-purple-500/10 text-purple-400 border border-purple-500/30 font-mono text-xs font-bold self-start sm:self-auto">
                Topic: Discretionary Access Control & SQL
            </span>
        </div>

        <!-- Problem Statement Matrix -->
        <div class="p-4 rounded-xl bg-slate-950 border border-slate-800">
            <div class="font-mono text-xs text-slate-400 uppercase tracking-wider font-bold mb-2">Given Access Control Matrix:</div>
            <div class="overflow-x-auto">
                <table class="w-full text-xs font-mono border-collapse border border-slate-700 text-left">
                    <thead>
                        <tr class="bg-slate-800 text-cyan-300">
                            <th class="p-2.5 border border-slate-700">User / Resource</th>
                            <th class="p-2.5 border border-slate-700">Table1</th>
                            <th class="p-2.5 border border-slate-700">Table2</th>
                            <th class="p-2.5 border border-slate-700">Table3</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-slate-800">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">Alice</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-semibold">Read, Write</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-semibold">Read</td>
                            <td class="p-2.5 border border-slate-700 text-slate-500 italic">None</td>
                        </tr>
                        <tr class="border-b border-slate-800 bg-slate-900/40">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">Bob</td>
                            <td class="p-2.5 border border-slate-700 text-cyan-300 font-semibold">Read (column 3 only)</td>
                            <td class="p-2.5 border border-slate-700 text-slate-500 italic">None</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-semibold">Write</td>
                        </tr>
                        <tr>
                            <td class="p-2.5 border border-slate-700 font-bold text-white">Charlie</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-semibold">Write</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-semibold">Read</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-semibold">Read</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Part A & B -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
                <div class="flex items-center gap-2">
                    <span class="w-6 h-6 rounded bg-purple-500/20 text-purple-300 font-mono font-bold flex items-center justify-center text-xs border border-purple-500/40">a</span>
                    <h4 class="text-sm font-bold text-white">Identify Model & Drawbacks <span class="text-purple-400 text-xs font-mono">(3 marks)</span></h4>
                </div>
                <p class="text-xs text-slate-200">
                    <strong>Identified Model:</strong> <span class="text-cyan-400 font-bold">Discretionary Access Control (DAC)</span>, implemented via an Access Control Matrix.
                </p>
                <div class="pt-1">
                    <strong class="text-xs text-slate-300 block mb-1">Main Drawbacks:</strong>
                    <ul class="text-xs text-slate-400 space-y-1 list-disc pl-4">
                        <li><strong>Vulnerability to Trojan Horses:</strong> A malicious script run by Alice inherits her rights and can leak Table1 data without detection.</li>
                        <li><strong>No Information Flow Control:</strong> Cannot prevent secondary dissemination once a user reads data.</li>
                        <li><strong>Scalability Limitations:</strong> N×M matrix becomes sparse, difficult to update and audit as tables grow.</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
                <div class="flex items-center gap-2">
                    <span class="w-6 h-6 rounded bg-purple-500/20 text-purple-300 font-mono font-bold flex items-center justify-center text-xs border border-purple-500/40">b</span>
                    <h4 class="text-sm font-bold text-white">List Other Access Control Models <span class="text-purple-400 text-xs font-mono">(2 marks)</span></h4>
                </div>
                <ul class="text-xs text-slate-300 space-y-1.5 pt-1">
                    <li>• <strong class="text-cyan-400 font-mono">Mandatory Access Control (MAC):</strong> Centralized, non-discretionary model based on fixed security clearances and classification labels (e.g. Bell-LaPadula, Biba).</li>
                    <li>• <strong class="text-emerald-400 font-mono">Role-Based Access Control (RBAC):</strong> Permissions assigned to job roles; users assigned to roles (least privilege & separation of duties).</li>
                    <li>• <strong class="text-amber-400 font-mono">Attribute-Based Access Control (ABAC):</strong> Dynamic policies evaluating subject attributes, resource attributes, and environment conditions (time, IP, location).</li>
                </ul>
            </div>
        </div>

        <!-- Part C: ACL Generation -->
        <div class="space-y-3 pt-2">
            <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded bg-purple-500/20 text-purple-300 font-mono font-bold flex items-center justify-center text-xs border border-purple-500/40">c</span>
                <h4 class="text-sm font-bold text-white">Generate Corresponding Access Control Lists (ACLs) <span class="text-purple-400 text-xs font-mono">(3 marks)</span></h4>
            </div>
            <p class="text-xs text-slate-400">
                Access Control Lists (ACLs) represent the <strong>columns</strong> of the matrix (object-centric lists attached to each table):
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 font-mono text-xs">
                <div class="p-3 rounded-xl bg-slate-950 border border-cyan-500/30">
                    <div class="font-bold text-cyan-400 border-b border-slate-800 pb-1 mb-2">ACL(Table1)</div>
                    <ul class="space-y-1 text-slate-300">
                        <li>• Alice: <code>{Read, Write}</code></li>
                        <li>• Bob: <code>{Read (column 3)}</code></li>
                        <li>• Charlie: <code>{Write}</code></li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-slate-950 border border-emerald-500/30">
                    <div class="font-bold text-emerald-400 border-b border-slate-800 pb-1 mb-2">ACL(Table2)</div>
                    <ul class="space-y-1 text-slate-300">
                        <li>• Alice: <code>{Read}</code></li>
                        <li>• Charlie: <code>{Read}</code></li>
                        <li class="text-slate-500 italic">(Bob: None)</li>
                    </ul>
                </div>
                <div class="p-3 rounded-xl bg-slate-950 border border-purple-500/30">
                    <div class="font-bold text-purple-400 border-b border-slate-800 pb-1 mb-2">ACL(Table3)</div>
                    <ul class="space-y-1 text-slate-300">
                        <li>• Bob: <code>{Write}</code></li>
                        <li>• Charlie: <code>{Read}</code></li>
                        <li class="text-slate-500 italic">(Alice: None)</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Part D: SQL DCL Implementation -->
        <div class="space-y-3 pt-2">
            <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded bg-purple-500/20 text-purple-300 font-mono font-bold flex items-center justify-center text-xs border border-purple-500/40">d</span>
                <h4 class="text-sm font-bold text-white">Using SQL statements, implement the access control policies in the ACLs. <span class="text-purple-400 text-xs font-mono">(5 marks)</span></h4>
            </div>
            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 font-mono text-xs text-cyan-300 leading-relaxed overflow-x-auto">
                <span class="text-slate-500">-- ==========================================================</span><br>
                <span class="text-slate-500">-- 1. Policies for Alice</span><br>
                <span class="text-slate-500">-- ==========================================================</span><br>
                GRANT SELECT, INSERT, UPDATE, DELETE ON Table1 TO Alice;<br>
                GRANT SELECT ON Table2 TO Alice;<br><br>
                <span class="text-slate-500">-- ==========================================================</span><br>
                <span class="text-slate-500">-- 2. Policies for Bob</span><br>
                <span class="text-slate-500">-- ==========================================================</span><br>
                <span class="text-slate-500">-- Table1: Read column 3 only (Column-level grant)</span><br>
                GRANT SELECT (col3) ON Table1 TO Bob;<br>
                GRANT INSERT, UPDATE, DELETE ON Table3 TO Bob;<br><br>
                <span class="text-slate-500">-- ==========================================================</span><br>
                <span class="text-slate-500">-- 3. Policies for Charlie</span><br>
                <span class="text-slate-500">-- ==========================================================</span><br>
                GRANT INSERT, UPDATE, DELETE ON Table1 TO Charlie;<br>
                GRANT SELECT ON Table2 TO Charlie;<br>
                GRANT SELECT ON Table3 TO Charlie;
            </div>
        </div>

        <!-- Part E: CASCADE vs. RESTRICT -->
        <div class="space-y-3 pt-2">
            <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded bg-purple-500/20 text-purple-300 font-mono font-bold flex items-center justify-center text-xs border border-purple-500/40">e</span>
                <h4 class="text-sm font-bold text-white">Explain the difference between CASCADE and RESTRICT in a REVOKE statement. <span class="text-purple-400 text-xs font-mono">(2 marks)</span></h4>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div class="p-4 rounded-xl bg-slate-950 border border-rose-500/30">
                    <strong class="font-mono text-xs text-rose-400 block mb-1">REVOKE ... CASCADE</strong>
                    <p class="text-xs text-slate-300 leading-relaxed font-sans">
                        <strong>Recursive Revocation:</strong> If the target user was given privileges <code>WITH GRANT OPTION</code> and granted those privileges to subsequent users, <code>CASCADE</code> recursively revokes the privilege from that user <strong>and all dependent downstream grantees</strong> (propagates down the grant tree).
                    </p>
                </div>
                <div class="p-4 rounded-xl bg-slate-950 border border-amber-500/30">
                    <strong class="font-mono text-xs text-amber-400 block mb-1">REVOKE ... RESTRICT</strong>
                    <p class="text-xs text-slate-300 leading-relaxed font-sans">
                        <strong>Protected Safe Revocation:</strong> Prevents revocation if any dependent grants exist. If the target user granted privileges to others using <code>WITH GRANT OPTION</code>, the <code>REVOKE ... RESTRICT</code> statement <strong>aborts immediately with an error</strong>, forcing the administrator to revoke dependencies manually.
                    </p>
                </div>
            </div>
        </div>
    </div>
    """

    # 3. File System & Bell-LaPadula Section HTML
    blp_html = """
    <div id="exam-sec-blp" class="p-6 rounded-2xl bg-slate-900/90 border border-slate-800 glow-border-cyan space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
            <div>
                <span class="px-2.5 py-0.5 rounded bg-emerald-950/80 border border-emerald-500/40 text-emerald-300 font-mono text-xs font-semibold">
                    Midterm / Final Exam Archives · Question 4 · 12 Marks
                </span>
                <h3 class="text-xl font-bold text-white mt-1">Problem 3: University File System Access Control & Bell-LaPadula (BLP)</h3>
                <p class="text-xs text-slate-400 font-mono">Examiners: Prof. Walaa Khaled & Dr. Alshaimaa Abo-alian</p>
            </div>
            <span class="px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 font-mono text-xs font-bold self-start sm:self-auto">
                Topic: Mandatory Access Control (MAC)
            </span>
        </div>

        <!-- Problem Statement Box -->
        <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 text-sm">
            <div class="font-mono text-xs text-slate-400 uppercase tracking-wider font-bold mb-1">Exam Scenario:</div>
            <p class="text-slate-200 leading-relaxed font-sans">
                A university file system has the following access control policy:<br>
                • <strong>Professor Smith owns FileA.</strong> Professor Smith wants Student1 to read FileA only and wants TA1 to read and write FileA.<br>
                • <strong>Student2 owns FileB</strong> and wants Professor Smith to read FileB.
            </p>
        </div>

        <!-- Part A: Matrix, ACL, Capability List -->
        <div class="space-y-4">
            <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded bg-emerald-500/20 text-emerald-300 font-mono font-bold flex items-center justify-center text-xs border border-emerald-500/40">A</span>
                <h4 class="text-sm font-bold text-white">Represent this access control scenario using ACM, ACL, and C-List <span class="text-emerald-400 text-xs font-mono">(3 marks)</span></h4>
            </div>

            <!-- Access Control Matrix -->
            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
                <div class="font-mono text-xs text-cyan-400 font-bold">1. Access Control Matrix (ACM)</div>
                <div class="overflow-x-auto">
                    <table class="w-full text-xs font-mono border-collapse border border-slate-700 text-left">
                        <thead>
                            <tr class="bg-slate-800 text-cyan-300">
                                <th class="p-2.5 border border-slate-700">Subject / Object</th>
                                <th class="p-2.5 border border-slate-700">FileA</th>
                                <th class="p-2.5 border border-slate-700">FileB</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="border-b border-slate-800">
                                <td class="p-2.5 border border-slate-700 font-bold text-white">Professor Smith</td>
                                <td class="p-2.5 border border-slate-700 text-emerald-400 font-semibold">Own, Read, Write</td>
                                <td class="p-2.5 border border-slate-700 text-cyan-300 font-semibold">Read</td>
                            </tr>
                            <tr class="border-b border-slate-800 bg-slate-900/40">
                                <td class="p-2.5 border border-slate-700 font-bold text-white">TA1</td>
                                <td class="p-2.5 border border-slate-700 text-emerald-400 font-semibold">Read, Write</td>
                                <td class="p-2.5 border border-slate-700 text-slate-500 italic">None</td>
                            </tr>
                            <tr class="border-b border-slate-800">
                                <td class="p-2.5 border border-slate-700 font-bold text-white">Student1</td>
                                <td class="p-2.5 border border-slate-700 text-cyan-300 font-semibold">Read</td>
                                <td class="p-2.5 border border-slate-700 text-slate-500 italic">None</td>
                            </tr>
                            <tr class="bg-slate-900/40">
                                <td class="p-2.5 border border-slate-700 font-bold text-white">Student2</td>
                                <td class="p-2.5 border border-slate-700 text-slate-500 italic">None</td>
                                <td class="p-2.5 border border-slate-700 text-emerald-400 font-semibold">Own, Read, Write</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- ACL and C-List Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
                    <div class="font-mono text-xs text-emerald-400 font-bold">2. Access Control Lists (ACLs - Columns)</div>
                    <p class="text-xs text-slate-400">Object-centric lists storing authorized users per file:</p>
                    <ul class="text-xs text-slate-300 font-mono space-y-1.5 pt-1">
                        <li>• <strong>ACL(FileA):</strong> { Prof. Smith: (Own, R, W), TA1: (R, W), Student1: (R) }</li>
                        <li>• <strong>ACL(FileB):</strong> { Student2: (Own, R, W), Prof. Smith: (R) }</li>
                    </ul>
                </div>
                <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
                    <div class="font-mono text-xs text-purple-400 font-bold">3. Capability Lists (C-Lists - Rows)</div>
                    <p class="text-xs text-slate-400">Subject-centric tickets carried by each user:</p>
                    <ul class="text-xs text-slate-300 font-mono space-y-1.5 pt-1">
                        <li>• <strong>C-List(Prof. Smith):</strong> [ (FileA: Own, R, W), (FileB: R) ]</li>
                        <li>• <strong>C-List(TA1):</strong> [ (FileA: R, W) ]</li>
                        <li>• <strong>C-List(Student1):</strong> [ (FileA: R) ]</li>
                        <li>• <strong>C-List(Student2):</strong> [ (FileB: Own, R, W) ]</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Part B: Model Name & Pros/Cons -->
        <div class="space-y-3 pt-2">
            <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded bg-emerald-500/20 text-emerald-300 font-mono font-bold flex items-center justify-center text-xs border border-emerald-500/40">B</span>
                <h4 class="text-sm font-bold text-white">Name Model & Identify Advantages / Disadvantages <span class="text-emerald-400 text-xs font-mono">(3 marks)</span></h4>
            </div>
            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs sm:text-sm">
                <p>
                    <strong>Model Name:</strong> <span class="text-cyan-400 font-bold">Discretionary Access Control (DAC)</span>. The creator/owner of a file possesses total discretion to define, grant, or revoke permissions.
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                    <div class="p-3 rounded-lg bg-slate-900 border border-slate-800">
                        <strong class="text-emerald-400 font-mono text-xs block mb-1">Advantages</strong>
                        <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4 font-sans">
                            <li>High flexibility: Owners manage permissions without waiting for IT administrators.</li>
                            <li>Simple, low overhead, and supported natively by all major operating systems.</li>
                        </ul>
                    </div>
                    <div class="p-3 rounded-lg bg-slate-900 border border-slate-800">
                        <strong class="text-rose-400 font-mono text-xs block mb-1">Disadvantages</strong>
                        <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4 font-sans">
                            <li>Security depends entirely on user vigilance (risk of over-permissive grants).</li>
                            <li>Vulnerable to Trojan horses leaking sensitive data via owner permissions.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- Part C.1: Bell-LaPadula (BLP) Table -->
        <div class="space-y-4 pt-2">
            <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded bg-emerald-500/20 text-emerald-300 font-mono font-bold flex items-center justify-center text-xs border border-emerald-500/40">C.1</span>
                <h4 class="text-sm font-bold text-white">Bell-LaPadula (BLP) Access Evaluation (All 8 Combinations) <span class="text-emerald-400 text-xs font-mono">(4 marks)</span></h4>
            </div>

            <!-- BLP Rules Banner -->
            <div class="p-3.5 rounded-xl bg-slate-950 border border-cyan-500/30 text-xs font-mono">
                <div class="text-cyan-300 font-bold mb-1">Bell-LaPadula (BLP) Core Axioms:</div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-slate-300 font-sans">
                    <div>
                        • <strong>Simple Security Property (ss-property):</strong> <em>No Read Up (NRU)</em><br>
                        Subject S can READ object O iff <code>Clearance(S) ≥ Classification(O)</code>.
                    </div>
                    <div>
                        • <strong>*-Property (Star Property):</strong> <em>No Write Down (NWD)</em><br>
                        Subject S can WRITE/Append object O iff <code>Clearance(S) ≤ Classification(O)</code>.
                    </div>
                </div>
                <div class="text-[11px] text-slate-400 mt-2 font-mono">
                    Clearance Hierarchy: Top Secret (TS) &gt; Secret (S) &gt; Confidential (C) &gt; Unclassified (U)
                </div>
            </div>

            <!-- Complete 8-Combination BLP Table -->
            <div class="overflow-x-auto">
                <table class="w-full text-xs font-mono border-collapse border border-slate-700 text-left">
                    <thead>
                        <tr class="bg-slate-800 text-cyan-300">
                            <th class="p-2.5 border border-slate-700">User (Clearance)</th>
                            <th class="p-2.5 border border-slate-700">File (Class.)</th>
                            <th class="p-2.5 border border-slate-700">READ Allowed?</th>
                            <th class="p-2.5 border border-slate-700">WRITE Allowed?</th>
                            <th class="p-2.5 border border-slate-700">BLP Rule Justification</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- 1. Prof Smith & FileA -->
                        <tr class="border-b border-slate-800">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">Professor Smith (TS)</td>
                            <td class="p-2.5 border border-slate-700">FileA (S)</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-rose-400 font-bold">Denied</td>
                            <td class="p-2.5 border border-slate-700 text-slate-300 font-sans">TS ≥ S (Read Up satisfied); TS &gt; S violates No Write Down (would leak TS info into S file).</td>
                        </tr>
                        <!-- 2. Prof Smith & FileB -->
                        <tr class="border-b border-slate-800 bg-slate-900/40">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">Professor Smith (TS)</td>
                            <td class="p-2.5 border border-slate-700">FileB (C)</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-rose-400 font-bold">Denied</td>
                            <td class="p-2.5 border border-slate-700 text-slate-300 font-sans">TS ≥ C (Read Up satisfied); TS &gt; C violates No Write Down (would leak TS info into C file).</td>
                        </tr>
                        <!-- 3. TA1 & FileA -->
                        <tr class="border-b border-slate-800">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">TA1 (S)</td>
                            <td class="p-2.5 border border-slate-700">FileA (S)</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-slate-300 font-sans">S = S (Equal level satisfies both ss-property S ≥ S and *-property S ≤ S).</td>
                        </tr>
                        <!-- 4. TA1 & FileB -->
                        <tr class="border-b border-slate-800 bg-slate-900/40">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">TA1 (S)</td>
                            <td class="p-2.5 border border-slate-700">FileB (C)</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-rose-400 font-bold">Denied</td>
                            <td class="p-2.5 border border-slate-700 text-slate-300 font-sans">S ≥ C (Read Up satisfied); S &gt; C violates No Write Down (cannot write down to lower level).</td>
                        </tr>
                        <!-- 5. Student1 & FileA -->
                        <tr class="border-b border-slate-800">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">Student1 (C)</td>
                            <td class="p-2.5 border border-slate-700">FileA (S)</td>
                            <td class="p-2.5 border border-slate-700 text-rose-400 font-bold">Denied</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-slate-300 font-sans">C &lt; S violates No Read Up; C ≤ S satisfies No Write Down (blind write / append up allowed).</td>
                        </tr>
                        <!-- 6. Student1 & FileB -->
                        <tr class="border-b border-slate-800 bg-slate-900/40">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">Student1 (C)</td>
                            <td class="p-2.5 border border-slate-700">FileB (C)</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-slate-300 font-sans">C = C (Equal level satisfies both ss-property C ≥ C and *-property C ≤ C).</td>
                        </tr>
                        <!-- 7. Student2 & FileA -->
                        <tr class="border-b border-slate-800">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">Student2 (U)</td>
                            <td class="p-2.5 border border-slate-700">FileA (S)</td>
                            <td class="p-2.5 border border-slate-700 text-rose-400 font-bold">Denied</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-slate-300 font-sans">U &lt; S violates No Read Up; U ≤ S satisfies No Write Down (blind write / append up allowed).</td>
                        </tr>
                        <!-- 8. Student2 & FileB -->
                        <tr class="bg-slate-900/40">
                            <td class="p-2.5 border border-slate-700 font-bold text-white">Student2 (U)</td>
                            <td class="p-2.5 border border-slate-700">FileB (C)</td>
                            <td class="p-2.5 border border-slate-700 text-rose-400 font-bold">Denied</td>
                            <td class="p-2.5 border border-slate-700 text-emerald-400 font-bold">Allowed</td>
                            <td class="p-2.5 border border-slate-700 text-slate-300 font-sans">U &lt; C violates No Read Up; U ≤ C satisfies No Write Down (blind write / append up allowed).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Part C.2: Difference MAC vs DAC -->
        <div class="space-y-3 pt-2">
            <div class="flex items-center gap-2">
                <span class="w-6 h-6 rounded bg-emerald-500/20 text-emerald-300 font-mono font-bold flex items-center justify-center text-xs border border-emerald-500/40">C.2</span>
                <h4 class="text-sm font-bold text-white">Explain the main difference between MAC and DAC <span class="text-emerald-400 text-xs font-mono">(2 marks)</span></h4>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div class="p-4 rounded-xl bg-slate-950 border border-cyan-500/30">
                    <strong class="font-mono text-xs text-cyan-400 block mb-1">Mandatory Access Control (MAC)</strong>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4 font-sans">
                        <li><strong>Centralized Authority:</strong> Governed strictly by system-wide security policies.</li>
                        <li><strong>Classification Labels:</strong> Based on security clearances (subjects) and classification levels (objects).</li>
                        <li><strong>Immunity:</strong> Even the file creator CANNOT alter access rights. Guarantees protection against Trojan horse leaks.</li>
                    </ul>
                </div>
                <div class="p-4 rounded-xl bg-slate-950 border border-amber-500/30">
                    <strong class="font-mono text-xs text-amber-400 block mb-1">Discretionary Access Control (DAC)</strong>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4 font-sans">
                        <li><strong>Owner Authority:</strong> Governed entirely by individual resource owners at their own personal discretion.</li>
                        <li><strong>Identity-Based:</strong> Access is based on user identity or group membership (via ACLs or matrix).</li>
                        <li><strong>Vulnerable:</strong> Owners can freely propagate rights to others; susceptible to unauthorized data exfiltration.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """

    # 4. Exam MCQs Section HTML
    mcqs_html = """
    <div id="exam-sec-mcqs" class="p-6 rounded-2xl bg-slate-900/90 border border-slate-800 glow-border-cyan space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
            <div>
                <span class="px-2.5 py-0.5 rounded bg-amber-950/80 border border-amber-500/40 text-amber-300 font-mono text-xs font-semibold">
                    Official Exam Archives · 10 High-Yield MCQs
                </span>
                <h3 class="text-xl font-bold text-white mt-1">Section 4: 10 Official Exam MCQs with Step-by-Step Solutions</h3>
                <p class="text-xs text-slate-400 font-mono">Real-time instant evaluation with complete concept breakdowns & distractor analysis</p>
            </div>
            <div class="flex items-center gap-2">
                <span id="examMCQScoreBadge" class="px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-500/40 font-mono text-xs font-bold">
                    0 / 10 Solved
                </span>
                <button onclick="revealAllExamMCQSolutions()" class="px-3 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-mono text-cyan-300 border border-slate-700">
                    👀 Reveal All Answers
                </button>
            </div>
        </div>

        <div id="examMCQContainer" class="space-y-4">
            <!-- 10 Question Cards Injected via JS -->
        </div>
    </div>
    """

    return math_html + "\n" + db_html + "\n" + blp_html + "\n" + mcqs_html
