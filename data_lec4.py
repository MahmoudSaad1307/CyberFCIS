# -*- coding: utf-8 -*-

LEC4_DATA = {
    "id": "lec4",
    "number": 4,
    "title": "User Authentication",
    "instructor": "Dr. Alshaimaa Abo-alian",
    "faculty": "Faculty of Computer & Information Sciences, Ain Shams University",
    "badge": "L4: Passwords, Tokens & Biometrics",
    "summary_html": """
    <div class="space-y-6">
        <!-- Section: Foundations -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🔑</span> 1. Foundations of User Authentication
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div class="space-y-3">
                    <p>
                        <strong>User Authentication</strong> (also called <em>entity authentication</em> or <em>identification</em>) is the process of verifying that the entity requesting access to a system is genuinely who or what it claims to be.
                    </p>
                    <div class="p-3 bg-slate-800/60 rounded border border-cyan-500/40">
                        <strong class="text-cyan-300 block">Role in Security Architecture:</strong>
                        <ul class="list-disc list-inside mt-1 space-y-1">
                            <li>Acts as the <strong>first line of defense</strong> for all systems.</li>
                            <li>Forms the foundation for <strong>Access Control</strong> and <strong>Accountability</strong>.</li>
                            <li>All audit trails and attribution depend on successful authentication.</li>
                        </ul>
                    </div>
                    <div class="p-3 bg-slate-800/60 rounded border border-slate-700">
                        <strong class="text-white block mb-1">Mutual Authentication:</strong>
                        <p>Both the client and the server authenticate each other. Example: Online banking where the browser verifies the bank's TLS certificate (server authenticates to client) AND the customer logs in with credentials (client authenticates to server).</p>
                    </div>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-2">The Three Authentication Factors:</h4>
                    <div class="space-y-2">
                        <div class="p-3 bg-blue-950/30 rounded border border-blue-800/50">
                            <div class="flex items-center gap-2 mb-1">
                                <span class="text-blue-300 font-bold">Factor 1 — Knowledge</span>
                                <span class="text-xs font-mono text-blue-400 bg-blue-950/50 px-1.5 py-0.5 rounded">Something You Know</span>
                            </div>
                            <p>Passwords, passphrases, PINs, security questions.</p>
                            <p class="text-slate-400 text-[11px] mt-0.5">Most common. Weakest alone due to cognitive load and sharing risks.</p>
                        </div>
                        <div class="p-3 bg-emerald-950/30 rounded border border-emerald-800/50">
                            <div class="flex items-center gap-2 mb-1">
                                <span class="text-emerald-300 font-bold">Factor 2 — Possession</span>
                                <span class="text-xs font-mono text-emerald-400 bg-emerald-950/50 px-1.5 py-0.5 rounded">Something You Have</span>
                            </div>
                            <p>Smart cards, USB hardware tokens, mobile OTP apps, QR codes.</p>
                            <p class="text-slate-400 text-[11px] mt-0.5">Requires physical theft to compromise alone.</p>
                        </div>
                        <div class="p-3 bg-purple-950/30 rounded border border-purple-800/50">
                            <div class="flex items-center gap-2 mb-1">
                                <span class="text-purple-300 font-bold">Factor 3 — Inherence</span>
                                <span class="text-xs font-mono text-purple-400 bg-purple-950/50 px-1.5 py-0.5 rounded">Something You Are/Do</span>
                            </div>
                            <p><strong>Static Physiological:</strong> Fingerprint, iris, retina, face geometry.<br/><strong>Dynamic Behavioral:</strong> Voice pattern, keystroke dynamics, gait, handwriting signature.</p>
                        </div>
                    </div>
                    <div class="p-3 bg-amber-950/20 border border-amber-700/50 rounded mt-2">
                        <strong class="text-amber-300 block mb-1">MFA (Multi-Factor Authentication):</strong>
                        <p class="text-[11px] text-slate-300">Requires TWO or more independent factors (e.g., Password + OTP Token). Ensures a single stolen credential is insufficient for access.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section: Password Authentication -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🔒</span> 2. Password Authentication & Secure Storage
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <strong class="text-white block mb-2">Human Bottleneck Problem:</strong>
                    <p class="mb-2">Passwords impose heavy cognitive load across multiple accounts, leading to predictable insecure choices:</p>
                    <ul class="list-disc list-inside space-y-1 text-slate-300">
                        <li>Leetspeak substitutions (p4ssw0rd)</li>
                        <li>Keyboard walk patterns (qwerty, 123456)</li>
                        <li>Personal information (birthdays, pet names)</li>
                        <li>Mnemonic phrases or song lyrics</li>
                        <li>Simple dictionary words with suffix numbers</li>
                    </ul>
                    <div class="p-2 bg-rose-950/30 border border-rose-800/40 rounded mt-2">
                        <strong class="text-rose-300">Inverse Relationship:</strong><br/>
                        <span class="text-[11px]">Security and Convenience are <strong>inversely proportional</strong> for passwords. Stronger password policies → More user frustration → More workarounds.</span>
                    </div>
                </div>
                <div>
                    <strong class="text-white block mb-2">Secure Password Storage Evolution:</strong>
                    <div class="space-y-2">
                        <div class="p-2 bg-rose-950/20 border border-rose-700/40 rounded">
                            <strong class="text-rose-300">❌ Method 1: Encryption</strong>
                            <code class="block font-mono text-[11px] mt-1">Store: ID | E(K, P)</code>
                            <p class="text-[11px] mt-1 text-slate-400">Flawed: The secret decryption key K must also be stored on the same system. Compromise of K compromises all passwords.</p>
                        </div>
                        <div class="p-2 bg-amber-950/20 border border-amber-700/40 rounded">
                            <strong class="text-amber-300">⚠️ Method 2: Hashing</strong>
                            <code class="block font-mono text-[11px] mt-1">Store: ID | H(P)</code>
                            <p class="text-[11px] mt-1 text-slate-400">Better — no decryption possible. BUT: Same passwords → same hash → vulnerable to Rainbow Table precomputation attacks.</p>
                        </div>
                        <div class="p-2 bg-emerald-950/20 border border-emerald-700/40 rounded">
                            <strong class="text-emerald-300">✅ Method 3: Salted Hashing (Best Practice)</strong>
                            <code class="block font-mono text-[11px] mt-1">Store: ID | Salt | H(P ∥ Salt)</code>
                            <p class="text-[11px] mt-1 text-slate-400">Appends a unique random salt to each password before hashing. Defeats Rainbow Tables and forces unique hashes per user even for identical passwords.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section: Password Attacks -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>⚔️</span> 3. The 8 Types of Password Attacks & Defenses
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
                <div class="space-y-2">
                    <div class="p-3 bg-slate-800/50 rounded border border-rose-800/30">
                        <span class="text-rose-300 font-bold">1. Offline Dictionary Attack</span>
                        <p class="mt-1">Steal the entire password hash database. Test massive lists of dictionary words offline using high-performance GPU rigs. No lockout mechanism applies.</p>
                    </div>
                    <div class="p-3 bg-slate-800/50 rounded border border-rose-800/30">
                        <span class="text-rose-300 font-bold">2. Brute-Force Attack</span>
                        <p class="mt-1">Systematically generate and try ALL possible character combinations against an online account.</p>
                        <span class="text-emerald-300 block mt-1">Defense: Account lockout after ≤ 5 failed attempts.</span>
                    </div>
                    <div class="p-3 bg-slate-800/50 rounded border border-rose-800/30">
                        <span class="text-rose-300 font-bold">3. Password Spraying</span>
                        <p class="mt-1">Use a small set of the most common passwords (e.g., "Winter2024!") tried across MANY different accounts. Avoids per-account lockout triggers.</p>
                    </div>
                    <div class="p-3 bg-slate-800/50 rounded border border-rose-800/30">
                        <span class="text-rose-300 font-bold">4. Guessing</span>
                        <p class="mt-1">Uses specific personal information about the target (birthdate, spouse's name, pet, sports team) to intelligently guess passwords.</p>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="p-3 bg-slate-800/50 rounded border border-rose-800/30">
                        <span class="text-rose-300 font-bold">5. Computer Hijacking</span>
                        <p class="mt-1">Attacker physically accesses an already-authenticated, unattended user session (e.g., user left workstation unlocked and walked away).</p>
                    </div>
                    <div class="p-3 bg-slate-800/50 rounded border border-rose-800/30">
                        <span class="text-rose-300 font-bold">6. Exploiting User Mistakes</span>
                        <p class="mt-1">Leveraging written-down passwords on sticky notes, unchanged default credentials, or reused passwords across multiple systems.</p>
                    </div>
                    <div class="p-3 bg-slate-800/50 rounded border border-rose-800/30">
                        <span class="text-rose-300 font-bold">7. Credential Stuffing</span>
                        <p class="mt-1">Replaying previously leaked username/password pairs (from other breaches) across multiple websites, banking on password reuse behavior.</p>
                    </div>
                    <div class="p-3 bg-slate-800/50 rounded border border-rose-800/30">
                        <span class="text-rose-300 font-bold">8. Eavesdropping</span>
                        <p class="mt-1">Intercepting credentials transmitted in plaintext across a network (HTTP, unencrypted Wi-Fi, ARP poisoning for MITM).</p>
                    </div>
                </div>
            </div>
            <div class="mt-3 p-3 bg-emerald-950/20 border border-emerald-700/40 rounded text-xs text-slate-300">
                <strong class="text-emerald-300 block mb-1">Proactive Defenses (Beyond Lockout):</strong>
                <ul class="list-disc list-inside space-y-0.5">
                    <li>User education and password hygiene training.</li>
                    <li>Computer-generated random passwords and secure password managers.</li>
                    <li>Proactive password rule enforcement (minimum length, complexity requirements).</li>
                    <li>Compromised-password databases (HaveIBeenPwned integration).</li>
                    <li><strong>Bloom Filters:</strong> Probabilistic data structure for efficient password checks with zero false negatives (never approves a known-breached password).</li>
                </ul>
            </div>
        </div>

        <!-- Section: Token-Based Authentication -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>📱</span> 4. Token-Based Authentication (OTP Tokens)
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <p class="mb-3"><strong>Tokens</strong> are physical or digital objects in the user's possession that generate <strong>One-Time Passwords (OTPs)</strong>. OTPs are valid for a single session/transaction.</p>
                    <div class="p-3 bg-blue-950/20 border border-blue-800/50 rounded mb-2">
                        <strong class="text-blue-300">TOTP — Time-Based OTP (RFC 6238)</strong>
                        <p class="mt-1">OTP code changes automatically every <strong>30–60 seconds</strong> based on a time synchronization between client token and authentication server.</p>
                        <span class="font-mono text-xs text-blue-200 block mt-1">TOTP = HMAC(K, floor(time / interval))</span>
                        <p class="text-slate-400 text-[11px] mt-1">Examples: Google Authenticator, Microsoft Authenticator, Authy</p>
                    </div>
                    <div class="p-3 bg-purple-950/20 border border-purple-800/50 rounded">
                        <strong class="text-purple-300">HOTP — HMAC-Based OTP (RFC 4226)</strong>
                        <p class="mt-1">OTP code changes on a specific <strong>triggered event</strong> (e.g., pressing a physical token button). Uses an incrementing counter.</p>
                        <span class="font-mono text-xs text-purple-200 block mt-1">HOTP = Truncate(HMAC-SHA1(K, counter))</span>
                        <p class="text-slate-400 text-[11px] mt-1">Example: RSA SecurID hardware token</p>
                    </div>
                </div>
                <div>
                    <div class="overflow-x-auto">
                        <table class="w-full border border-slate-700 text-[11px]">
                            <thead class="bg-slate-800 text-slate-300">
                                <tr>
                                    <th class="p-2 border border-slate-700">Feature</th>
                                    <th class="p-2 border border-slate-700">TOTP</th>
                                    <th class="p-2 border border-slate-700">HOTP</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800 text-slate-300">
                                <tr><td class="p-2 font-semibold">Trigger</td><td class="p-2 text-cyan-300">Time (every 30-60s)</td><td class="p-2 text-purple-300">Event (button press)</td></tr>
                                <tr><td class="p-2 font-semibold">Variable</td><td class="p-2">Unix Timestamp</td><td class="p-2">Counter Value</td></tr>
                                <tr><td class="p-2 font-semibold">Sync Risk</td><td class="p-2">Clock drift</td><td class="p-2">Counter desync</td></tr>
                                <tr><td class="p-2 font-semibold">Codes expire</td><td class="p-2">Automatically</td><td class="p-2">Only when used</td></tr>
                                <tr><td class="p-2 font-semibold">RFC</td><td class="p-2">RFC 6238</td><td class="p-2">RFC 4226</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section: Biometric Authentication -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>👁️</span> 5. Biometric Authentication: Workflow & Accuracy Metrics
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <strong class="text-white block mb-2">Biometric System Workflow:</strong>
                    <div class="p-3 bg-slate-800/60 rounded border border-slate-700 mb-2 font-mono text-[11px] text-cyan-300">
                        Sensor → Feature Extraction → Template → Matcher → Decision
                    </div>
                    <div class="p-3 bg-slate-800/50 rounded border border-slate-700 mb-2">
                        <strong class="text-white">Enrollment:</strong> User registers their biometric (e.g., scans fingerprint multiple times). System creates a reference template.
                    </div>
                    <div class="p-3 bg-blue-950/20 rounded border border-blue-800/40 mb-2">
                        <strong class="text-blue-300">Verification (1:1 Matching):</strong> Claimed identity is compared against THEIR OWN stored template only. (e.g., "Is this the fingerprint for user John?")
                    </div>
                    <div class="p-3 bg-purple-950/20 rounded border border-purple-800/40">
                        <strong class="text-purple-300">Identification (1:N Matching):</strong> Biometric compared against the ENTIRE enrolled database to find who this person is. (e.g., "Who is this person in our DB?")
                    </div>
                </div>
                <div>
                    <strong class="text-white block mb-2">Accuracy Metrics — FAR, FRR, EER/CER:</strong>
                    <div class="space-y-2">
                        <div class="p-3 bg-rose-950/20 border border-rose-700/50 rounded">
                            <strong class="text-rose-300 block">FAR — False Acceptance Rate</strong>
                            <p>The percentage of <strong>imposters</strong> incorrectly accepted as genuine users.</p>
                            <p class="text-slate-400 text-[11px] mt-0.5">High FAR = Security risk. Low FAR = Stricter system.</p>
                        </div>
                        <div class="p-3 bg-amber-950/20 border border-amber-700/50 rounded">
                            <strong class="text-amber-300 block">FRR — False Rejection Rate</strong>
                            <p>The percentage of <strong>legitimate users</strong> incorrectly rejected by the system.</p>
                            <p class="text-slate-400 text-[11px] mt-0.5">High FRR = Usability problem (frustrating legitimate users).</p>
                        </div>
                        <div class="p-3 bg-cyan-950/20 border border-cyan-700/50 rounded">
                            <strong class="text-cyan-300 block">EER/CER — Equal Error Rate / Crossover Error Rate</strong>
                            <p>The threshold point at which <strong>FAR equals FRR</strong>. Represents the overall system accuracy:</p>
                            <p class="text-emerald-300 mt-0.5">Lower EER = More accurate biometric system.</p>
                            <div class="mt-1 p-1.5 bg-slate-800/60 rounded font-mono text-[11px] text-cyan-200">
                                At EER: FAR = FRR | Best accuracy tradeoff threshold
                            </div>
                        </div>
                    </div>
                    <div class="mt-2 p-2 bg-slate-800/40 rounded border border-slate-700 text-[11px]">
                        <strong class="text-white">Inverse FAR/FRR Relationship:</strong> Lowering the matching threshold → Easier to accept → Higher FAR (less secure), Lower FRR. Raising threshold → Harder to accept → Lower FAR (more secure), Higher FRR.
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,
    "memory_aids": [
        {"title": "3 Authentication Factors", "content": "Knowledge (Something You KNOW: password, PIN) | Possession (Something You HAVE: smart card, token) | Inherence (Something You ARE/DO: biometrics)."},
        {"title": "MFA Golden Rule", "content": "MFA requires 2+ DIFFERENT factor types. Password + Security Question = NOT MFA (both are knowledge). Password + OTP Token = MFA ✅"},
        {"title": "Password Storage Methods", "content": "Encryption (bad — key stored with data) → Hashing (better — but rainbow tables!) → Salted Hashing (BEST — unique per user, kills rainbow tables)."},
        {"title": "Rainbow Table Defense", "content": "SALTING defeats rainbow table attacks. A salt is a unique random string appended to each password before hashing, forcing unique hash outputs for identical passwords."},
        {"title": "TOTP vs HOTP", "content": "TOTP = Time-based OTP (changes every 30-60 seconds automatically). HOTP = Event-based/HMAC OTP (changes when you press a button/trigger an event)."},
        {"title": "FAR vs FRR vs EER", "content": "FAR = Imposters wrongly accepted (security risk). FRR = Real users wrongly rejected (usability issue). EER = Where FAR = FRR (lower EER = better system)."},
        {"title": "Biometric: Verification vs Identification", "content": "Verification = 1:1 match (Is THIS the right person?). Identification = 1:N search (WHO is this person in the entire DB?)."},
        {"title": "Password Spraying vs Brute Force", "content": "Brute Force = Many passwords against ONE account (triggers lockout). Spraying = FEW common passwords across MANY accounts (evades per-account lockout)."}
    ],
    "mcqs": [
        {
            "id": 1,
            "q": "User Authentication is described as the first line of defense and forms the basis for which two security functions?",
            "options": [
                "Encryption and Compression",
                "Access Control and Accountability",
                "Threat Detection and Incident Response",
                "Patch Management and Vulnerability Scanning"
            ],
            "ans": "B",
            "explanation": "Authentication is fundamental because all Access Control decisions (who gets what access) and Accountability (audit trail attribution) depend on correctly identifying the requesting entity."
        },
        {
            "id": 2,
            "q": "In which authentication scenario does a bank server present a TLS certificate to a customer's browser AND the customer logs in with a password?",
            "options": [
                "Single-Factor Authentication",
                "Role-Based Authentication",
                "Mutual Authentication",
                "Delegation-Based Authentication"
            ],
            "ans": "C",
            "explanation": "Mutual Authentication means BOTH parties verify each other's identity. The bank authenticates to the user (TLS cert) and the user authenticates to the bank (credentials)."
        },
        {
            "id": 3,
            "q": "A user's fingerprint scan is classified under which authentication factor category?",
            "options": ["Knowledge (Something you know)", "Possession (Something you have)", "Inherence (Something you are)", "Delegation (Something you grant)"],
            "ans": "C",
            "explanation": "Biometrics like fingerprints, iris scans, and facial recognition fall under Factor 3 — Inherence (Something You Are/Do)."
        },
        {
            "id": 4,
            "q": "Which combination correctly represents true Multi-Factor Authentication (MFA)?",
            "options": [
                "Password + Security Question",
                "PIN + Mother's maiden name",
                "Password (Knowledge) + Hardware OTP Token (Possession)",
                "Fingerprint + Iris scan"
            ],
            "ans": "C",
            "explanation": "MFA requires factors from DIFFERENT categories. Password (Knowledge) + Hardware Token (Possession) = 2 different factors = MFA. Password + security question = 2 Knowledge factors (NOT MFA)."
        },
        {
            "id": 5,
            "q": "Why is password storage using ENCRYPTION alone considered flawed?",
            "options": [
                "Encrypted passwords cannot be compared against user input.",
                "The secret decryption key must also be stored on the same system, so compromising the system compromises all passwords.",
                "Encryption algorithms are too slow for real-time login verification.",
                "Encrypted passwords are always longer than the original password, wasting storage."
            ],
            "ans": "B",
            "explanation": "Encryption requires storing the decryption key somewhere on the system. If the system is compromised, the attacker gets both the encrypted passwords and the key to decrypt them all."
        },
        {
            "id": 6,
            "q": "What problem with simple password hashing (without salting) makes it vulnerable to precomputed database attacks?",
            "options": [
                "Hash functions are reversible by design.",
                "The same password always produces the same hash, enabling rainbow table lookups.",
                "Hash functions are too slow for password verification.",
                "Hash outputs are too short and easily guessable."
            ],
            "ans": "B",
            "explanation": "Without salting, identical passwords produce identical hashes. Attackers precompute massive hash lookup tables (rainbow tables) for common passwords and instantly match stored hashes."
        },
        {
            "id": 7,
            "q": "What is the purpose of adding a 'Salt' to a password before hashing it?",
            "options": [
                "To increase the password length making brute force harder.",
                "To add a symmetric encryption layer on top of the hash.",
                "To append a unique random string per user, ensuring identical passwords produce different hashes and defeating precomputed tables.",
                "To reduce the hash output size for faster lookups."
            ],
            "ans": "C",
            "explanation": "Salting appends a unique per-user random value to the password before hashing. This ensures two identical passwords produce completely different hashes, destroying rainbow table effectiveness."
        },
        {
            "id": 8,
            "q": "An attacker steals an organization's password hash database and runs it against a dictionary of millions of words using GPU clusters. This is called:",
            "options": [
                "Password Spraying",
                "Credential Stuffing",
                "Offline Dictionary Attack",
                "Eavesdropping"
            ],
            "ans": "C",
            "explanation": "An Offline Dictionary Attack takes the stolen hash file and tests pre-computed hashes of dictionary words offline, away from any lockout mechanism."
        },
        {
            "id": 9,
            "q": "Why does 'Password Spraying' avoid triggering account lockout policies?",
            "options": [
                "It uses zero-day exploits to bypass the lockout mechanism directly.",
                "It uses only encrypted traffic so the server cannot see the password attempts.",
                "It tests only a few common passwords per account, spreading the attack across many accounts to stay under lockout thresholds.",
                "It disables the account lockout service remotely before the attack."
            ],
            "ans": "C",
            "explanation": "By only attempting a few common passwords per account (e.g., 1-2 attempts), spraying stays under typical 3-5 attempt lockout thresholds while targeting thousands of accounts."
        },
        {
            "id": 10,
            "q": "An attacker replays username/password pairs obtained from a previous data breach at a different website, exploiting password reuse. This attack is known as:",
            "options": [
                "Brute Force Attack",
                "Guessing Attack",
                "Credential Stuffing",
                "Offline Dictionary Attack"
            ],
            "ans": "C",
            "explanation": "Credential Stuffing specifically uses verified username/password pairs from one breach to attack other services, leveraging the widespread habit of password reuse."
        },
        {
            "id": 11,
            "q": "What is a Bloom Filter used for in the context of password security?",
            "options": [
                "Encrypting passwords using a bloom hashing scheme.",
                "An efficient probabilistic check for whether a new password matches known compromised passwords, with zero false negatives.",
                "A salt generation algorithm for password hashing.",
                "A visual CAPTCHA mechanism to prevent automated login attempts."
            ],
            "ans": "B",
            "explanation": "Bloom Filters provide space-efficient probabilistic membership testing. For passwords, they proactively check if a new password exists in a breached password list, with zero false negatives (a compromised password is never approved)."
        },
        {
            "id": 12,
            "q": "What distinguishes TOTP from HOTP?",
            "options": [
                "TOTP uses RSA key pairs; HOTP uses symmetric AES keys.",
                "TOTP codes change automatically every 30-60 seconds; HOTP codes change only when triggered by an event (counter increment).",
                "TOTP is used only for server authentication; HOTP is for client authentication.",
                "TOTP stores the OTP in the cloud; HOTP stores it on the device."
            ],
            "ans": "B",
            "explanation": "TOTP (RFC 6238) is time-synchronized; codes expire automatically. HOTP (RFC 4226) is event-driven; codes only change when a specific event (like button press) occurs."
        },
        {
            "id": 13,
            "q": "What formula does TOTP use to generate its one-time password?",
            "options": [
                "TOTP = SHA256(UserID + Timestamp)",
                "TOTP = HMAC(K, floor(UnixTime / TimeInterval))",
                "TOTP = AES(PrivateKey, CurrentSecond)",
                "TOTP = MD5(UserPassword + Salt + Counter)"
            ],
            "ans": "B",
            "explanation": "TOTP uses HMAC applied to the secret key K and the current Unix timestamp divided by the time interval (typically 30 seconds)."
        },
        {
            "id": 14,
            "q": "What does FAR (False Acceptance Rate) measure in a biometric system?",
            "options": [
                "The percentage of legitimate users incorrectly rejected by the system.",
                "The percentage of impostors who are incorrectly accepted as authentic users.",
                "The speed at which the biometric sensor captures fingerprints.",
                "The number of users that can be enrolled in the biometric database."
            ],
            "ans": "B",
            "explanation": "FAR measures the security risk of a biometric system — specifically the rate at which unauthorized imposters are incorrectly authenticated."
        },
        {
            "id": 15,
            "q": "What does FRR (False Rejection Rate) measure in a biometric system?",
            "options": [
                "The percentage of impostors incorrectly accepted as genuine.",
                "The percentage of genuine users incorrectly rejected and denied access.",
                "The rate at which biometric templates expire from the database.",
                "The accuracy of the sensor hardware in capturing biometric data."
            ],
            "ans": "B",
            "explanation": "FRR measures the usability problem — how often the system incorrectly denies access to legitimate users, creating operational frustrations."
        },
        {
            "id": 16,
            "q": "What does the EER (Equal Error Rate) or CER (Crossover Error Rate) represent?",
            "options": [
                "The highest possible FAR value achievable by the system.",
                "The threshold point at which the False Acceptance Rate equals the False Rejection Rate, representing overall accuracy.",
                "The error introduced by clock drift in TOTP systems.",
                "The minimum number of enrollment scans required for a biometric system."
            ],
            "ans": "B",
            "explanation": "EER/CER is the operating point where FAR = FRR. A lower EER indicates a more accurate biometric system overall."
        },
        {
            "id": 17,
            "q": "If a biometric system's threshold is increased (more strict matching required), how does this affect FAR and FRR?",
            "options": [
                "Both FAR and FRR increase.",
                "FAR decreases (more secure) but FRR increases (more legitimate rejections).",
                "FAR increases and FRR decreases.",
                "Both FAR and FRR decrease simultaneously."
            ],
            "ans": "B",
            "explanation": "Stricter matching threshold → Harder to pass → Fewer imposters accepted (lower FAR, more secure) but also more legitimate users rejected (higher FRR, less convenient)."
        },
        {
            "id": 18,
            "q": "Which biometric modality is classified as 'static physiological'?",
            "options": [
                "Keystroke dynamics",
                "Gait analysis",
                "Voice pattern recognition",
                "Iris pattern scan"
            ],
            "ans": "D",
            "explanation": "Static physiological biometrics are unchanging body characteristics: fingerprint, iris, retina, face geometry. Dynamic behavioral includes voice, keystroke dynamics, gait, and signature."
        },
        {
            "id": 19,
            "q": "What is the difference between biometric Verification (1:1) and biometric Identification (1:N)?",
            "options": [
                "Verification is used for criminals; Identification is for employees.",
                "Verification compares claimed identity against their own template (1:1). Identification compares against the entire database to find who it is (1:N).",
                "Verification uses fingerprints; Identification uses iris scans.",
                "They are the same process with different terminology."
            ],
            "ans": "B",
            "explanation": "Verification is 1:1 — confirming 'you are who you claim to be.' Identification is 1:N — finding 'who is this unknown person' by searching the entire database."
        },
        {
            "id": 20,
            "q": "Which of the following is a 'dynamic behavioral' biometric?",
            "options": [
                "Retina scan",
                "Fingerprint pattern",
                "Keystroke dynamics",
                "Facial geometry"
            ],
            "ans": "C",
            "explanation": "Dynamic behavioral biometrics measure patterns in actions and movements: keystroke dynamics (typing rhythm), gait analysis, voice pattern, and handwriting. Retina, fingerprint, and facial geometry are static physiological."
        }
    ]
}

