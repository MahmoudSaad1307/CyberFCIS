# -*- coding: utf-8 -*-

LEC2_DATA = {
    "id": "lec2",
    "number": 2,
    "title": "Cybersecurity Threat Landscape",
    "instructor": "Dr. Alshaimaa Abo-alian",
    "faculty": "Faculty of Computer & Information Sciences, Ain Shams University",
    "badge": "L2: Actors, Surfaces & Frameworks",
    "summary_html": """
    <div class="space-y-6">
        <!-- Section: Hacker Types -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🎭</span> 1. Types of Hackers
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="p-4 bg-emerald-950/20 border border-emerald-800/40 rounded-lg">
                    <h4 class="text-emerald-400 font-bold mb-1">White-Hat Hackers</h4>
                    <span class="text-xs text-emerald-300 font-mono block mb-2">Authorized Attackers</span>
                    <p class="text-xs text-slate-300">Act with explicit organizational authorization to discover security vulnerabilities with the sole intent of fixing and correcting them.</p>
                </div>
                <div class="p-4 bg-rose-950/20 border border-rose-800/40 rounded-lg">
                    <h4 class="text-rose-400 font-bold mb-1">Black-Hat Hackers</h4>
                    <span class="text-xs text-rose-300 font-mono block mb-2">Unauthorized Attackers</span>
                    <p class="text-xs text-slate-300">Seek to defeat security controls and compromise the CIA triad with malicious intent (data theft, ransom, sabotage, extortion).</p>
                </div>
                <div class="p-4 bg-amber-950/20 border border-amber-800/40 rounded-lg">
                    <h4 class="text-amber-400 font-bold mb-1">Gray-Hat Hackers</h4>
                    <span class="text-xs text-amber-300 font-mono block mb-2">Semi-Authorized Attackers</span>
                    <p class="text-xs text-slate-300">Act without prior authorization, but lack malicious intent to destroy data. They locate flaws and inform targets, often demanding rewards or recognition.</p>
                </div>
            </div>
        </div>

        <!-- Section: Threat Actor Spectrum -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>👥</span> 2. Threat Actor Classifications & Motivations
            </h3>
            <p class="text-slate-300 text-sm mb-3">
                A <strong>threat actor</strong> (or <strong>cyber adversary</strong>) is any individual or entity responsible for attacks. They are characterized by their location (internal vs. external), skill level, resources/funding, and intent.
            </p>
            <div class="space-y-3 text-xs text-slate-300">
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700/60">
                    <div class="flex justify-between items-center mb-1">
                        <strong class="text-cyan-300 text-sm">Low Skill & Opportunistic: Script Kiddies</strong>
                        <span class="px-2 py-0.5 rounded bg-slate-700 text-slate-300 font-mono">Unskilled</span>
                    </div>
                    <p>Young, lone operators with low resources. Rely on pre-made, free, or low-cost attack tools. They are non-discriminating in target selection (scan IP ranges indiscriminately). Motivated by curiosity, data exfiltration, or service disruption (DoS).</p>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700/60">
                    <div class="flex justify-between items-center mb-1">
                        <strong class="text-cyan-300 text-sm">Ideological & Political: Hacktivists & Cyberterrorists</strong>
                        <span class="px-2 py-0.5 rounded bg-slate-700 text-slate-300 font-mono">Ideological</span>
                    </div>
                    <p><strong>Hacktivists</strong> (e.g. Anonymous, WikiLeaks) are motivated by political, social, or religious beliefs (not money!). Use website defacement, doxing, data leaks, and DoS for public protest. <strong>Cyberterrorists</strong> share similar ideologies but hold extreme aims, actively targeting critical infrastructure to spread fear and widespread disruption.</p>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700/60">
                    <div class="flex justify-between items-center mb-1">
                        <strong class="text-cyan-300 text-sm">Profit & Professional: Organized Cybercrime</strong>
                        <span class="px-2 py-0.5 rounded bg-slate-700 text-slate-300 font-mono">Financial</span>
                    </div>
                    <p>Highly organized groups operating like corporations. Motivated purely by illegal financial gain. Target banks, retailers, and healthcare holding rich data. Deploy large-scale ransomware campaigns, phishing, and monetize stolen records on the Dark Web.</p>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700/60">
                    <div class="flex justify-between items-center mb-1">
                        <strong class="text-cyan-300 text-sm">Strategic & National: Nation-State Attackers (APTs)</strong>
                        <span class="px-2 py-0.5 rounded bg-rose-900/60 text-rose-300 font-mono">Highest Sophistication</span>
                    </div>
                    <p>State-sponsored military or intelligence agencies with massive funding and zero time constraints. Execute <strong>Advanced Persistent Threats (APTs)</strong>:</p>
                    <ul class="list-disc list-inside ml-2 mt-1 space-y-0.5 text-slate-400">
                        <li><strong>Advanced:</strong> Use custom zero-days, innovative evasion tactics, and bespoke malware.</li>
                        <li><strong>Persistent:</strong> Maintain covert, long-term access inside target networks for months or years.</li>
                        <li><strong>Motive:</strong> Political/economic espionage (theft of defense secrets) or sabotage of critical utilities.</li>
                    </ul>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700/60">
                    <div class="flex justify-between items-center mb-1">
                        <strong class="text-cyan-300 text-sm">Internal & Unintentional: Shadow IT & Insider Threats</strong>
                        <span class="px-2 py-0.5 rounded bg-amber-900/60 text-amber-300 font-mono">Internal</span>
                    </div>
                    <p><strong>Shadow IT</strong> occurs when employees bypass corporate IT to use unapproved cloud storage or apps (e.g., unauthorized Google Drive or Dropbox). Their intent is benign/convenience, but it leaks corporate data. <strong>Insider Threats</strong> involve employees or contractors who abuse legitimate credentials maliciously or through negligence.</p>
                </div>
            </div>
        </div>

        <!-- Section: Attack Surface vs Threat Vector -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🌐</span> 3. Attack Surface vs. Threat Vector
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div class="p-4 bg-slate-800/50 rounded-lg border border-slate-700">
                    <h4 class="text-cyan-300 font-bold text-sm mb-1">Attack Surface (The "WHERE")</h4>
                    <p class="mb-2">The total sum of all entry points and vulnerabilities (digital, physical, human) that an attacker could exploit.</p>
                    <span class="text-slate-400 block font-mono">Examples: Open network ports, public APIs, web apps, IoT devices, employees vulnerable to social engineering.</span>
                </div>
                <div class="p-4 bg-slate-800/50 rounded-lg border border-slate-700">
                    <h4 class="text-cyan-300 font-bold text-sm mb-1">Threat Vector (The "HOW")</h4>
                    <p class="mb-2">The specific method or technical path utilized by a threat actor to deliver a payload or compromise a system.</p>
                    <span class="text-slate-400 block font-mono">Examples: Phishing email, SQL injection, malicious USB drive, brute force password attack.</span>
                </div>
            </div>
            <div class="mt-3 p-3 bg-slate-800/30 rounded border border-cyan-500/30 text-xs text-cyan-200">
                💡 <strong>Golden Rule:</strong> While the attack surface is the <em>where</em>, the threat vector is the <em>how</em>. (E.g., a phishing email is a <strong>vector</strong> targeting the human <strong>attack surface</strong>).
            </div>
        </div>

        <!-- Section: NIST CSF 2.0 -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🏛️</span> 4. NIST Cybersecurity Framework (CSF 2.0)
            </h3>
            <p class="text-xs text-slate-300 mb-3">
                Voluntary guidelines and best practices organized around <strong>6 Core Functions</strong>:
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 text-xs">
                <div class="p-3 bg-amber-950/20 border border-amber-700/50 rounded">
                    <strong class="text-amber-400 text-sm block">1. GOVERN (GV)</strong>
                    <span class="text-slate-400 text-[11px] block mb-1">Strategy & Roles</span>
                    <p class="text-slate-300">Establishes risk management strategy, organizational context, policies, and supply chain oversight. (GV.OC, GV.RM, GV.SC, GV.RR, GV.PO, GV.OV)</p>
                </div>
                <div class="p-3 bg-blue-950/20 border border-blue-700/50 rounded">
                    <strong class="text-blue-400 text-sm block">2. IDENTIFY (ID)</strong>
                    <span class="text-slate-400 text-[11px] block mb-1">Asset Management</span>
                    <p class="text-slate-300">Understands organizational context, inventory of systems, data assets, risk assessments, and improvement plans. (ID.AM, ID.RA, ID.IM)</p>
                </div>
                <div class="p-3 bg-purple-950/20 border border-purple-700/50 rounded">
                    <strong class="text-purple-400 text-sm block">3. PROTECT (PR)</strong>
                    <span class="text-slate-400 text-[11px] block mb-1">Safeguards & IAM</span>
                    <p class="text-slate-300">Implements safeguards to ensure critical services: Identity & Access Control, awareness training, data security, platform security. (PR.AA, PR.AT, PR.DS, PR.PS, PR.IR)</p>
                </div>
                <div class="p-3 bg-yellow-950/20 border border-yellow-700/50 rounded">
                    <strong class="text-yellow-400 text-sm block">4. DETECT (DE)</strong>
                    <span class="text-slate-400 text-[11px] block mb-1">Monitoring & Alerts</span>
                    <p class="text-slate-300">Identifies cybersecurity events in a timely manner through continuous telemetry monitoring, log analysis, and anomaly alerting. (DE.CM, DE.AE)</p>
                </div>
                <div class="p-3 bg-rose-950/20 border border-rose-700/50 rounded">
                    <strong class="text-rose-400 text-sm block">5. RESPOND (RS)</strong>
                    <span class="text-slate-400 text-[11px] block mb-1">Incident Management</span>
                    <p class="text-slate-300">Executes actions regarding detected incidents: containment, forensic analysis, communication, and mitigation strategies. (RS.MA, RS.AN, RS.CO, RS.MI)</p>
                </div>
                <div class="p-3 bg-emerald-950/20 border border-emerald-700/50 rounded">
                    <strong class="text-emerald-400 text-sm block">6. RECOVER (RC)</strong>
                    <span class="text-slate-400 text-[11px] block mb-1">Resilience & Continuity</span>
                    <p class="text-slate-300">Restores damaged systems and capabilities, executes disaster recovery plans, and communicates restoration milestones. (RC.RP, RC.CO)</p>
                </div>
            </div>
        </div>

        <!-- Section: Threat Modeling: STRIDE, DREAD, PASTA, ATT&CK -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>📐</span> 5. Threat Modeling: STRIDE, DREAD, PASTA & ATT&CK
            </h3>
            <p class="text-xs text-slate-300 mb-2">
                <strong>Threat Modeling</strong> is a structured, proactive process conducted early in the SDLC to answer 4 fundamental questions:
            </p>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-2 text-center text-xs mb-4">
                <div class="p-2 bg-slate-800/60 rounded border border-slate-700">1. What are we building? <span class="block text-cyan-300 font-mono">(Scope)</span></div>
                <div class="p-2 bg-slate-800/60 rounded border border-slate-700">2. What can go wrong? <span class="block text-cyan-300 font-mono">(Threat ID)</span></div>
                <div class="p-2 bg-slate-800/60 rounded border border-slate-700">3. What will we do? <span class="block text-cyan-300 font-mono">(Mitigation)</span></div>
                <div class="p-2 bg-slate-800/60 rounded border border-slate-700">4. How well did we do? <span class="block text-cyan-300 font-mono">(Validation)</span></div>
            </div>
            <blockquote class="text-center font-mono text-cyan-300 text-xs italic mb-4">
                "Think like an attacker to defend like an architect."
            </blockquote>

            <!-- STRIDE Table -->
            <h4 class="text-sm font-bold text-white mb-2">Microsoft STRIDE Framework</h4>
            <div class="overflow-x-auto text-xs mb-4">
                <table class="w-full text-left border border-slate-800">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-2 border border-slate-700">Letter</th>
                            <th class="p-2 border border-slate-700">Threat Category</th>
                            <th class="p-2 border border-slate-700">Security Violation</th>
                            <th class="p-2 border border-slate-700">Example</th>
                            <th class="p-2 border border-slate-700">Standard Mitigation</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800 text-slate-300">
                        <tr><td class="p-2 font-bold text-cyan-400">S</td><td class="p-2 font-semibold">Spoofing</td><td class="p-2">Authenticity</td><td class="p-2">Credential theft, IP spoofing</td><td class="p-2 text-emerald-300">Strong multi-factor authentication</td></tr>
                        <tr><td class="p-2 font-bold text-cyan-400">T</td><td class="p-2 font-semibold">Tampering</td><td class="p-2">Integrity</td><td class="p-2">Modifying data in transit or in DB</td><td class="p-2 text-emerald-300">Hashes, HMAC, access control, checksums</td></tr>
                        <tr><td class="p-2 font-bold text-cyan-400">R</td><td class="p-2 font-semibold">Repudiation</td><td class="p-2">Non-repudiation</td><td class="p-2">Attacker deletes audit logs after fraud</td><td class="p-2 text-emerald-300">Immutable audit logs, digital signatures</td></tr>
                        <tr><td class="p-2 font-bold text-cyan-400">I</td><td class="p-2 font-semibold">Information Disclosure</td><td class="p-2">Confidentiality</td><td class="p-2">Data leakage, eavesdropping</td><td class="p-2 text-emerald-300">Encryption (TLS/AES), strict ACLs</td></tr>
                        <tr><td class="p-2 font-bold text-cyan-400">D</td><td class="p-2 font-semibold">Denial of Service (DoS)</td><td class="p-2">Availability</td><td class="p-2">Flooding web server (SYN flood, DDoS)</td><td class="p-2 text-emerald-300">Load balancing, rate limiting, redundancy</td></tr>
                        <tr><td class="p-2 font-bold text-cyan-400">E</td><td class="p-2 font-semibold">Elevation of Privilege</td><td class="p-2">Authorization</td><td class="p-2">Standard user gains admin root shell</td><td class="p-2 text-emerald-300">Principle of least privilege, input validation</td></tr>
                    </tbody>
                </table>
            </div>

            <!-- DREAD & PASTA & MITRE -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs text-slate-300">
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700">
                    <strong class="text-white block mb-1">DREAD Model</strong>
                    <p class="mb-1">Quantifies threat severity (0–10 scale):</p>
                    <span class="font-mono text-cyan-300 block mb-1">Score = (D + R + E + A + D) / 5</span>
                    <p class="text-slate-400 text-[11px]">Damage, Reproducibility, Exploitability, Affected users, Discoverability. Discontinued by Microsoft due to subjective scoring inconsistencies.</p>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700">
                    <strong class="text-white block mb-1">PASTA Framework</strong>
                    <p class="mb-1"><strong>Process for Attack Simulation & Threat Analysis</strong> (2015, VerSprite).</p>
                    <p class="text-slate-400 text-[11px]">7-step risk-centric framework aligning security countermeasures with business impact and real-world attack simulations.</p>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700">
                    <strong class="text-white block mb-1">MITRE ATT&CK</strong>
                    <p class="mb-1">Knowledge base of real-world attacker TTPs:</p>
                    <ul class="text-[11px] text-slate-400 list-disc list-inside">
                        <li><strong>Tactics:</strong> Adversary's "why" (goals)</li>
                        <li><strong>Techniques:</strong> Specific "how" methods</li>
                        <li><strong>Procedures:</strong> Exact "what" scripts/commands</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """,
    "memory_aids": [
        {"title": "Hacker Hat Colors", "content": "White = Authorized & Benevolent. Black = Unauthorized & Malicious. Gray = Unauthorized but No Malicious Destruction."},
        {"title": "Threat Vector vs Attack Surface", "content": "Attack Surface is the WHERE (doorway, open port, human). Threat Vector is the HOW (phishing email, SQL injection)."},
        {"title": "NIST CSF 2.0 (G-I-P-D-R-R)", "content": "Govern (GV) ➔ Identify (ID) ➔ Protect (PR) ➔ Detect (DE) ➔ Respond (RS) ➔ Recover (RC)."},
        {"title": "STRIDE Mnemonic", "content": "Spoofing (Identity) | Tampering (Data alteration) | Repudiation (Denial) | Info Disclosure (Leak) | DoS (Downtime) | Elevation of Privilege (Admin gain)."},
        {"title": "DREAD Components", "content": "Damage, Reproducibility, Exploitability, Affected users, Discoverability. Score = Average of the 5 values."},
        {"title": "Why DREAD Was Discontinued", "content": "Microsoft dropped DREAD because different analysts produced wildly subjective and inconsistent scores for the same threat."},
        {"title": "PASTA (7 Steps)", "content": "Risk-centric framework: 1. Business Objectives ➔ 2. Scope ➔ 3. Decomposition ➔ 4. Threat ➔ 5. Vuln ➔ 6. Simulate Attack ➔ 7. Mitigate."},
        {"title": "MITRE ATT&CK TTPs", "content": "Tactics = The 'Why' (objective). Techniques = The 'How' (method). Procedures = The 'What' (commands & tools used)."}
    ],
    "mcqs": [
        {
            "id": 1,
            "q": "Which type of hacker breaks into systems without prior authorization, but discloses vulnerabilities directly to the vendor without causing malicious destruction?",
            "options": ["White-hat hacker", "Black-hat hacker", "Gray-hat hacker", "Script kiddie"],
            "ans": "C",
            "explanation": "Gray-hat hackers act without proper authorization, but they do so without malicious intent, aiming to inform targets of vulnerabilities."
        },
        {
            "id": 2,
            "q": "What primary characteristic defines 'Script Kiddies'?",
            "options": [
                "Extensive expertise in reverse-engineering binaries.",
                "High skill and deep financial backing from organized syndicates.",
                "Lack of advanced technical skill, relying on pre-made automated tools and exploits.",
                "Exclusively launching attacks inside physical server rooms."
            ],
            "ans": "C",
            "explanation": "Script kiddies are unskilled attackers who work mostly alone using pre-written tools and scripts developed by more skilled individuals."
        },
        {
            "id": 3,
            "q": "What is the primary motivation driving Hacktivist groups like Anonymous or WikiLeaks?",
            "options": [
                "Illegal financial gain through ransomware extortion.",
                "Advancing political, social, or ideological beliefs through disruption and data leaks.",
                "Conducting state-sponsored military espionage.",
                "Assisting enterprise organizations in hardening network security."
            ],
            "ans": "B",
            "explanation": "Hacktivists are explicitly not motivated by money; their motivation is political, social, or ideological disruption (e.g., website defacement, leaks)."
        },
        {
            "id": 4,
            "q": "How do Cyberterrorists primarily differ from general Hacktivists?",
            "options": [
                "They never use Distributed Denial of Service (DDoS) attacks.",
                "They hold more extreme aims, specifically attacking critical infrastructure to spread fear and cause widespread disruption.",
                "They are strictly authorized internal corporate personnel.",
                "They have no ideological or political agenda."
            ],
            "ans": "B",
            "explanation": "Cyberterrorists have more extreme aims than hacktivists, using attacks against critical infrastructure to spread fear and mass disruption."
        },
        {
            "id": 5,
            "q": "What distinguishes Advanced Persistent Threats (APTs) launched by Nation-State actors?",
            "options": [
                "They only execute quick, short-lived denial of service attacks.",
                "They are opportunistic, random, and rely solely on free public scripts.",
                "They utilize sophisticated, innovative evasion techniques (Advanced) and maintain long-term covert access (Persistent).",
                "They are carried out exclusively by young lone actors seeking social media clout."
            ],
            "ans": "C",
            "explanation": "APTs are sophisticated, state-sponsored attacks designed to infiltrate covertly (advanced) and maintain unauthorized access for extended periods (persistent)."
        },
        {
            "id": 6,
            "q": "When employees use unapproved cloud storage services to share corporate files because corporate tools are inconvenient, what security issue is occurring?",
            "options": ["Nation-State Espionage", "Shadow IT", "Zero-day exploitation", "Physical Security Breach"],
            "ans": "B",
            "explanation": "Shadow IT refers to employees adopting IT systems, software, or cloud services without the authorization or knowledge of corporate IT."
        },
        {
            "id": 7,
            "q": "Which statement correctly captures the relationship between Attack Surface and Threat Vector?",
            "options": [
                "Attack surface is the technique (how), while threat vector is the entry point (where).",
                "Attack surface is the entry points/vulnerabilities (where), while threat vector is the specific method/technique (how).",
                "They are interchangeable terms referring to firewall rules.",
                "Threat vectors only apply to physical facilities."
            ],
            "ans": "B",
            "explanation": "The attack surface is WHERE an attacker can enter (ports, APIs, humans), whereas the threat vector is HOW they attack (phishing, SQL injection, brute force)."
        },
        {
            "id": 8,
            "q": "Which function was added as a foundational core function in the NIST Cybersecurity Framework (CSF 2.0)?",
            "options": ["Govern (GV)", "Audit (AU)", "Compensate (CP)", "Isolate (IS)"],
            "ans": "A",
            "explanation": "NIST CSF 2.0 expanded the original 5 functions (Identify, Protect, Detect, Respond, Recover) by adding 'Govern (GV)' to address strategy, policies, and oversight."
        },
        {
            "id": 9,
            "q": "In NIST CSF, which function involves continuous monitoring, anomaly detection, and security logging?",
            "options": ["Identify", "Protect", "Detect", "Recover"],
            "ans": "C",
            "explanation": "The Detect (DE) function encompasses activities such as Continuous Monitoring (DE.CM) and Adverse Event Analysis (DE.AE)."
        },
        {
            "id": 10,
            "q": "Which core principle encapsulates the mindset of threat modeling?",
            "options": [
                "'Trust, but verify.'",
                "'Think like an attacker to defend like an architect.'",
                "'Security through obscurity is paramount.'",
                "'Detecting incidents is better than preventing them.'"
            ],
            "ans": "B",
            "explanation": "Lecture 2 explicitly presents the threat modeling core motto: 'Think like an attacker to defend like an architect.'"
        },
        {
            "id": 11,
            "q": "What are the four fundamental questions answered during threat modeling?",
            "options": [
                "Who attacked? How much money was lost? Who is to blame? Can we prosecute?",
                "What are we building? What can go wrong? What are we going to do about it? How well are we doing?",
                "Which hardware is oldest? When is the warranty expiring? Who is the vendor? What is the price?",
                "What is our budget? How many servers do we have? Is our firewall active? Who is on call?"
            ],
            "ans": "B",
            "explanation": "Threat modeling systematically evaluates: 1. What are we building? 2. What can go wrong? 3. What will we do? 4. How well are we doing?"
        },
        {
            "id": 12,
            "q": "In Microsoft's STRIDE framework, which threat category corresponds to an attacker impersonating another legitimate user or system?",
            "options": ["Spoofing", "Tampering", "Repudiation", "Elevation of Privilege"],
            "ans": "A",
            "explanation": "Spoofing is an attack where an adversary illicitly impersonates a legitimate user, device, or identity."
        },
        {
            "id": 13,
            "q": "What is the recommended technical mitigation against 'Tampering' in the STRIDE model?",
            "options": [
                "Load balancing and server redundancy",
                "Cryptographic checksums, hashes, and strict access controls",
                "User education against social engineering",
                "Auto-logout after session inactivity"
            ],
            "ans": "B",
            "explanation": "Tampering violates data integrity; the proper countermeasures are access controls, integrity checksums, and cryptographic hashes."
        },
        {
            "id": 14,
            "q": "An attacker fraudulently transfers company funds and subsequently deletes the audit logs to deny performing the action. Which STRIDE category does this represent?",
            "options": ["Tampering", "Repudiation", "Information Disclosure", "Elevation of Privilege"],
            "ans": "B",
            "explanation": "Repudiation occurs when an actor denies having performed an action, and the system lacks undeniable proof/audit records to hold them accountable."
        },
        {
            "id": 15,
            "q": "How does the DREAD risk assessment model calculate the overall threat risk score?",
            "options": [
                "Score = Damage × Exploitability",
                "Score = (Damage + Reproducibility + Exploitability + Affected Users + Discoverability) / 5",
                "Score = Base Metrics + Temporal Metrics + Environmental Metrics",
                "Score = (Threat × Vulnerability) / Impact"
            ],
            "ans": "B",
            "explanation": "DREAD evaluates five parameters on a 0–10 scale and averages them: Overall Risk Score = (D + R + E + A + D) / 5."
        },
        {
            "id": 16,
            "q": "Why was the DREAD threat scoring model largely discontinued by Microsoft?",
            "options": [
                "It was too computationally expensive to compute with algorithms.",
                "It suffered from high subjectivity and inconsistency between different security analysts.",
                "It failed to address cloud computing environments.",
                "It was replaced by the FBI's cybercrime statistics."
            ],
            "ans": "B",
            "explanation": "Slide 24 states that Microsoft discontinued DREAD due to its inherent subjectivity and inconsistency in numerical ratings."
        },
        {
            "id": 17,
            "q": "What is PASTA in the context of threat modeling?",
            "options": [
                "A password salting algorithm developed by Cisco.",
                "A 7-step risk-centric threat modeling framework focused on attack simulation.",
                "A hardware token protocol for generating one-time passwords.",
                "A database query tool for auditing SQL permissions."
            ],
            "ans": "B",
            "explanation": "PASTA (Process for Attack Simulation & Threat Analysis) is a 7-step risk-centric framework developed by Tony UcedaVélez and Marco M. Morana."
        },
        {
            "id": 18,
            "q": "In the MITRE ATT&CK framework, what represents the adversary's 'why' or short-term tactical goals (e.g., Initial Access, Exfiltration)?",
            "options": ["Procedures", "Techniques", "Tactics", "Exploits"],
            "ans": "C",
            "explanation": "Tactics describe the adversary's overarching tactical goals or the 'why' (e.g., Initial Access, Privilege Escalation, Exfiltration)."
        },
        {
            "id": 19,
            "q": "In MITRE ATT&CK, how is a 'Procedure' defined?",
            "options": [
                "The high-level policy approved by corporate management.",
                "The specific actions, tools, commands, and scripts used by an attacker to execute a technique.",
                "A legal document filed with law enforcement after an intrusion.",
                "The annual training plan for blue team analysts."
            ],
            "ans": "B",
            "explanation": "Procedures represent the specific implementations or the 'what'—the exact commands, tools, and scripts an attacker executes."
        },
        {
            "id": 20,
            "q": "An attacker uses a web proxy to exploit an unvalidated input field and elevate their account to root administrator. In STRIDE, this is an example of:",
            "options": ["Spoofing", "Elevation of Privilege", "Repudiation", "Denial of Service"],
            "ans": "B",
            "explanation": "Elevation of Privilege involves an attacker gaining higher privileges (e.g., administrator or root) than they are legitimately authorized to hold."
        }
    ]
}

