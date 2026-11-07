# -*- coding: utf-8 -*-

LEC1_DATA = {
    "id": "lec1",
    "number": 1,
    "title": "Introduction to Cybersecurity",
    "instructor": "Dr. Alshaimaa Abo-alian",
    "faculty": "Faculty of Computer & Information Sciences, Ain Shams University",
    "badge": "L1: Foundations & Core Concepts",
    "summary_html": """
    <div class="space-y-6">
        <!-- Section: Overview & Statistics -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>📊</span> 1. Cybersecurity Overview & 2024 Statistics
            </h3>
            <p class="text-slate-300 mb-3">
                Financial losses from reported cyberattacks have increased by <strong class="text-rose-400 font-semibold">33% since 2023</strong> according to FBI / USA Facts data.
            </p>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center my-4">
                <div class="p-3 bg-slate-800/60 rounded-lg border border-slate-700/60">
                    <span class="text-xs text-slate-400 uppercase font-mono">2018 Losses</span>
                    <div class="text-lg font-bold text-slate-200">$2.7B</div>
                </div>
                <div class="p-3 bg-slate-800/60 rounded-lg border border-slate-700/60">
                    <span class="text-xs text-slate-400 uppercase font-mono">2021 Losses</span>
                    <div class="text-lg font-bold text-slate-200">$6.9B</div>
                </div>
                <div class="p-3 bg-slate-800/60 rounded-lg border border-slate-700/60">
                    <span class="text-xs text-slate-400 uppercase font-mono">2023 Losses</span>
                    <div class="text-lg font-bold text-amber-400">$12.5B</div>
                </div>
                <div class="p-3 bg-slate-800/60 rounded-lg border border-cyan-500/40">
                    <span class="text-xs text-cyan-400 uppercase font-mono">2024 Losses (+33%)</span>
                    <div class="text-lg font-bold text-cyan-300">$16.6B</div>
                </div>
            </div>
            <ul class="list-disc list-inside space-y-2 text-slate-300 mt-3 text-sm">
                <li><strong class="text-cyan-300">Most Common Cybercrime:</strong> <strong>Phishing</strong> (highest victim count / complaint volume).</li>
                <li><strong class="text-cyan-300">Costliest Cybercrime:</strong> <strong>Investment scams</strong> causing over <strong>$6.6B</strong> in losses (47.9K complaints).</li>
                <li><strong class="text-cyan-300">Business Email Compromise (BEC):</strong> 21.4K complaints causing <strong>$2.8B</strong> in losses.</li>
                <li><strong class="text-cyan-300">Extortion:</strong> 86.4K complaints causing <strong>$143.2M</strong> in losses.</li>
            </ul>
        </div>

        <!-- Section: Importance of Cybersecurity -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🛡️</span> 2. The 8 Pillars of Cybersecurity Importance
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm text-slate-300">
                <div class="p-3 bg-slate-800/40 rounded border border-slate-800 flex gap-2 items-start">
                    <span class="text-cyan-400 font-bold">1.</span>
                    <div><strong class="text-white">Protects Sensitive Information:</strong> Keeps proprietary data, employee info, and operational secrets secure.</div>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-800 flex gap-2 items-start">
                    <span class="text-cyan-400 font-bold">2.</span>
                    <div><strong class="text-white">Ensures Business Continuity:</strong> Prevents downtime, ransom disruption, and loss of mission-critical services.</div>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-800 flex gap-2 items-start">
                    <span class="text-cyan-400 font-bold">3.</span>
                    <div><strong class="text-white">Maintains Customer Trust & Reputation:</strong> Avoids public brand damage and customer churn.</div>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-800 flex gap-2 items-start">
                    <span class="text-cyan-400 font-bold">4.</span>
                    <div><strong class="text-white">Prevents Financial Loss:</strong> Mitigates direct monetary theft, forensics costs, and lost revenue.</div>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-800 flex gap-2 items-start">
                    <span class="text-cyan-400 font-bold">5.</span>
                    <div><strong class="text-white">Protects Against Cyber Threats:</strong> Defends proactively against malware, APTs, and ransomware.</div>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-800 flex gap-2 items-start">
                    <span class="text-cyan-400 font-bold">6.</span>
                    <div><strong class="text-white">Safeguards Data Privacy:</strong> Regulates personal identifiable information (PII) usage and storage.</div>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-800 flex gap-2 items-start">
                    <span class="text-cyan-400 font-bold">7.</span>
                    <div><strong class="text-white">Protects Intellectual Property:</strong> Defends patents, algorithms, source code, and trade secrets.</div>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-800 flex gap-2 items-start">
                    <span class="text-cyan-400 font-bold">8.</span>
                    <div><strong class="text-white">Ensures Regulatory Compliance:</strong> Prevents legal penalties under laws like GDPR, HIPAA, and PCI-DSS.</div>
                </div>
            </div>
        </div>

        <!-- Section: Branches & Teams -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>⚔️</span> 3. Branches, Career Roles & Red vs. Blue Team
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="p-4 bg-rose-950/30 rounded-lg border border-rose-800/50">
                    <h4 class="text-rose-400 font-bold text-lg mb-2 flex items-center gap-2">
                        <span>⚔️</span> Red Team (Offensive Security)
                    </h4>
                    <p class="text-xs text-rose-200/80 mb-2">Simulates adversary attacks to identify and exploit vulnerabilities.</p>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                        <li>Ethical Hacking & Penetration Testing</li>
                        <li>Exploiting Vulnerabilities & Zero-Days</li>
                        <li>Black Box Testing</li>
                        <li>Social Engineering & Phishing Simulations</li>
                        <li>Web Application Security Scanning</li>
                    </ul>
                </div>
                <div class="p-4 bg-sky-950/30 rounded-lg border border-sky-800/50">
                    <h4 class="text-sky-400 font-bold text-lg mb-2 flex items-center gap-2">
                        <span>🛡️</span> Blue Team (Defensive Security)
                    </h4>
                    <p class="text-xs text-sky-200/80 mb-2">Defends systems, monitors activity, and mitigates security incidents.</p>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                        <li>Infrastructure Protection & Hardening</li>
                        <li>Incident Response (IR) & Damage Control</li>
                        <li>Operational Security & Log Monitoring</li>
                        <li>Proactive Threat Hunting</li>
                        <li>Digital Forensics (DFIR)</li>
                    </ul>
                </div>
            </div>
            <div class="overflow-x-auto text-xs">
                <table class="w-full text-left border border-slate-800">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-2 border border-slate-700">Cybersecurity Branch</th>
                            <th class="p-2 border border-slate-700">Associated Career Role</th>
                            <th class="p-2 border border-slate-700">Core Focus</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800 text-slate-300">
                        <tr><td class="p-2 font-mono text-cyan-300">Network Security</td><td class="p-2">Network Security Engineer</td><td class="p-2">Firewalls, routers, VPNs, perimeter security</td></tr>
                        <tr><td class="p-2 font-mono text-cyan-300">Application Security</td><td class="p-2">AppSec Engineer</td><td class="p-2">Secure coding, code reviews, DevSecOps</td></tr>
                        <tr><td class="p-2 font-mono text-cyan-300">Cloud Security</td><td class="p-2">Cloud Security Engineer</td><td class="p-2">AWS, Azure, GCP IAM, cloud architecture</td></tr>
                        <tr><td class="p-2 font-mono text-cyan-300">Endpoint Security</td><td class="p-2">Endpoint Security Engineer</td><td class="p-2">Workstations, laptops, mobile devices, EDR</td></tr>
                        <tr><td class="p-2 font-mono text-cyan-300">Penetration Testing</td><td class="p-2">Ethical Hacker</td><td class="p-2">Offensive testing, proof-of-concept exploits</td></tr>
                        <tr><td class="p-2 font-mono text-cyan-300">SOC Operations</td><td class="p-2">SOC Analyst</td><td class="p-2">24/7 monitoring, SIEM triage, alert correlation</td></tr>
                        <tr><td class="p-2 font-mono text-cyan-300">DFIR</td><td class="p-2">Incident Responder</td><td class="p-2">Digital forensics, breach containment, evidence</td></tr>
                        <tr><td class="p-2 font-mono text-cyan-300">Malware Analysis</td><td class="p-2">Malware Analyst</td><td class="p-2">Reverse engineering reverse malicious binaries</td></tr>
                        <tr><td class="p-2 font-mono text-cyan-300">GRC</td><td class="p-2">Risk & Compliance Analyst</td><td class="p-2">Governance, ISO 27001, compliance audits</td></tr>
                        <tr><td class="p-2 font-mono text-cyan-300">Threat Intelligence</td><td class="p-2">CTI Analyst</td><td class="p-2">Tracking adversary TTPs and campaigns</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Section: Definitions & InfoSec vs CyberSec -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>📖</span> 4. Core Definitions: InfoSec vs. Cybersecurity
            </h3>
            <div class="space-y-3 text-sm text-slate-300">
                <blockquote class="p-3 bg-slate-800/50 border-l-4 border-cyan-500 rounded text-slate-200 italic">
                    "Computer security, also known as cyber security or IT security, is the protection of computer systems from the theft or damage to their hardware, software or information, as well as from disruption or misdirection of the services they provide." 
                    <span class="block text-xs text-cyan-400 font-mono mt-1">— Morrie Gasser (1988)</span>
                </blockquote>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-2">
                    <div class="p-4 bg-slate-800/40 rounded border border-slate-700/60">
                        <h4 class="text-white font-bold mb-1">Information Security (InfoSec)</h4>
                        <p class="text-xs text-slate-300">Broader discipline. Protects sensitive information across <strong>both digital and non-digital formats</strong> (physical paperwork, file cabinets, locked rooms) as well as IT infrastructure.</p>
                    </div>
                    <div class="p-4 bg-slate-800/40 rounded border border-cyan-700/60">
                        <h4 class="text-cyan-300 font-bold mb-1">Cybersecurity</h4>
                        <p class="text-xs text-slate-300">A specialized subset of InfoSec focused <strong>exclusively on electronic data, technology, computer systems, networks, programs, and hardware</strong> connected to networks and the Internet.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section: CIA vs DAD -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🔺</span> 5. CIA Triad vs. DAD Triad (Defender vs. Attacker)
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-emerald-950/20 border border-emerald-800/50 rounded-lg">
                    <h4 class="text-emerald-400 font-bold mb-2">CIA Triad (Defender Objectives)</h4>
                    <ul class="text-xs space-y-2 text-slate-300">
                        <li><strong class="text-white">Confidentiality:</strong> Preventing unauthorized <em>disclosure</em> of sensitive information.</li>
                        <li><strong class="text-white">Integrity:</strong> Preventing unauthorized <em>modification or destruction</em> of data or systems.</li>
                        <li><strong class="text-white">Availability:</strong> Ensuring authorized users have <em>reliable and timely access</em> to systems and data whenever needed.</li>
                    </ul>
                </div>
                <div class="p-4 bg-rose-950/20 border border-rose-800/50 rounded-lg">
                    <h4 class="text-rose-400 font-bold mb-2">DAD Triad (Attacker Objectives)</h4>
                    <ul class="text-xs space-y-2 text-slate-300">
                        <li><strong class="text-white">Disclosure:</strong> Violation of confidentiality (unauthorized data access, theft, leaks).</li>
                        <li><strong class="text-white">Alteration:</strong> Violation of integrity (tampering with financial records, code tampering).</li>
                        <li><strong class="text-white">Denial / Destruction:</strong> Violation of availability (DDoS attacks, ransomware wipe, power sabotage).</li>
                    </ul>
                </div>
            </div>
            <div class="mt-4 p-3 bg-slate-800/40 rounded border border-slate-700/60 text-xs text-slate-300">
                <span class="text-amber-400 font-bold uppercase">Non-CIA Objectives:</span>
                <span class="ml-2"><strong>Authenticity</strong> (users/inputs are genuinely who they claim to be), <strong>Privacy</strong> (compliance with GDPR/HIPAA regarding PII), and <strong>Non-repudiation</strong> (inability to deny a performed transaction/action).</span>
            </div>
        </div>

        <!-- Section: Terminology: CVE, CWE, CVSS, Exploit -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🏷️</span> 6. Cybercrime Chain & CVE vs. CWE vs. CVSS
            </h3>
            <div class="p-3 bg-slate-800/60 rounded border border-slate-700 text-center mb-4">
                <span class="text-sm font-mono text-cyan-300 font-bold">Vulnerability (Weakness) ➔ Threat (Danger Cause) ➔ Risk (Likelihood × Impact)</span>
            </div>
            <div class="overflow-x-auto text-xs">
                <table class="w-full text-left border border-slate-800">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-2 border border-slate-700">Standard</th>
                            <th class="p-2 border border-slate-700">What It Is</th>
                            <th class="p-2 border border-slate-700">Managed By</th>
                            <th class="p-2 border border-slate-700">Focus / Role</th>
                            <th class="p-2 border border-slate-700">Format & Example</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800 text-slate-300">
                        <tr>
                            <td class="p-2 font-bold text-cyan-300">CVE</td>
                            <td class="p-2">Dictionary of individual, known vulnerabilities</td>
                            <td class="p-2">MITRE Corporation + CNAs</td>
                            <td class="p-2">Specific instances / tracking across vendors</td>
                            <td class="p-2 font-mono">CVE-YYYY-NNNNN (e.g. CVE-2024-12345)</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-cyan-300">CWE</td>
                            <td class="p-2">Taxonomy of software design & coding flaws</td>
                            <td class="p-2">MITRE Corporation</td>
                            <td class="p-2">Root causes / the "why" behind the vulnerability</td>
                            <td class="p-2 font-mono">CWE-NNNNN (e.g. CWE-79 XSS, CWE-78 Injection)</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-cyan-300">CVSS</td>
                            <td class="p-2">Numerical severity scoring system (0 to 10)</td>
                            <td class="p-2">FIRST (Forum of Incident Response)</td>
                            <td class="p-2">Measures "how bad" / prioritizes remediation</td>
                            <td class="p-2 font-mono">CVSS v4.0 (0.1–3.9 Low, 4.0–6.9 Med, 7.0–8.9 High, 9.0–10.0 Crit)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mt-4 text-xs text-slate-300">
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700">
                    <strong class="text-white block mb-1">Exploit & Zero-Day:</strong> An exploit is code/technique taking advantage of a flaw. A <strong>Zero-day</strong> is exploited before known to vendors or before a patch exists.
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700">
                    <strong class="text-white block mb-1">Dark Web & Deep Web:</strong> The Dark Web requires special routing software (Tor) and accounts for <strong>&lt;1%</strong> of the Deep Web. The Deep Web accounts for <strong>~96%</strong> of total web data.
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700">
                    <strong class="text-white block mb-1">Exploit-DB:</strong> Maintained by Offensive Security for sharing legitimate proof-of-concept (PoC) security research exploits.
                </div>
            </div>
        </div>

        <!-- Section: 5 Dimensions of Cyber Risk -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🎯</span> 7. The 5 Dimensions of Cyber Risk
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-5 gap-2 text-xs text-slate-300">
                <div class="p-3 bg-slate-800/50 rounded border border-slate-700">
                    <span class="text-amber-400 font-bold block mb-1">1. Financial</span>
                    Direct monetary loss, ransom payments, forensics, downtime revenue lost, stock drop.
                </div>
                <div class="p-3 bg-slate-800/50 rounded border border-slate-700">
                    <span class="text-amber-400 font-bold block mb-1">2. Operational</span>
                    Disruption to immediate business functions, assembly lines, supply chain, delivery.
                </div>
                <div class="p-3 bg-slate-800/50 rounded border border-slate-700">
                    <span class="text-amber-400 font-bold block mb-1">3. Compliance</span>
                    Legal penalties, GDPR / HIPAA fines, license revocation, contractual sanctions.
                </div>
                <div class="p-3 bg-slate-800/50 rounded border border-slate-700">
                    <span class="text-amber-400 font-bold block mb-1">4. Reputational</span>
                    Loss of customer confidence, negative PR, public devaluation of brand equity.
                </div>
                <div class="p-3 bg-slate-800/50 rounded border border-slate-700">
                    <span class="text-amber-400 font-bold block mb-1">5. Strategic</span>
                    Theft of IP / trade secrets, loss of competitive edge, long-term strategic road block.
                </div>
            </div>
        </div>

        <!-- Section: Security Controls -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>⚙️</span> 8. Security Controls: Categories & Functional Types
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700">
                    <h4 class="font-bold text-white text-sm mb-2">Controls by Category (How they are implemented)</h4>
                    <ul class="space-y-1.5 list-disc list-inside">
                        <li><strong class="text-cyan-300">Managerial / Administrative:</strong> Policies, guidelines, employee awareness workshops, IR plans.</li>
                        <li><strong class="text-cyan-300">Technical:</strong> Hardware/software automated mechanisms (firewalls, IDS, AV, encryption).</li>
                        <li><strong class="text-cyan-300">Operational:</strong> People-executed day-to-day routines (log reviews, manual vulnerability patching).</li>
                        <li><strong class="text-cyan-300">Physical:</strong> Facilities and perimeter protection (locks, fences, security guards, CCTV).</li>
                    </ul>
                </div>
                <div class="p-3 bg-slate-800/40 rounded border border-slate-700">
                    <h4 class="font-bold text-white text-sm mb-2">Controls by Functional Type (What they achieve)</h4>
                    <ul class="space-y-1.5 list-disc list-inside">
                        <li><strong class="text-cyan-300">Preventive:</strong> Stop incidents before they occur (firewalls, encryption, locks, training).</li>
                        <li><strong class="text-cyan-300">Detective:</strong> Identify and alert during/after an event (log monitoring, IDS, security cameras).</li>
                        <li><strong class="text-cyan-300">Corrective:</strong> Mitigate damage or restore systems (backups, disaster recovery, IR teams).</li>
                        <li><strong class="text-cyan-300">Deterrent:</strong> Psychologically discourage attackers (warning signs, guard presence).</li>
                        <li><strong class="text-cyan-300">Compensating:</strong> Alternative safeguards when primary control isn't feasible (e.g. strict passwords when MFA isn't supported).</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """,
    "memory_aids": [
        {"title": "CIA vs. DAD", "content": "Defenders protect Confidentiality, Integrity, Availability. Attackers seek Disclosure, Alteration, Denial/Destruction."},
        {"title": "InfoSec vs. CyberSec", "content": "InfoSec covers ALL data formats (digital + paper + physical rooms). Cybersecurity covers EXCLUSIVELY electronic/networked data."},
        {"title": "Vulnerability vs Threat vs Risk", "content": "Vulnerability is the flaw (the door is unlocked). Threat is the actor/event (a burglar). Risk is the likelihood & damage (burglary occurs)."},
        {"title": "CVE vs CWE vs CVSS", "content": "CVE = Unique dictionary ID (Which flaw). CWE = Category / root cause (Why it happened). CVSS = Numerical score 0-10 (How bad it is)."},
        {"title": "Red Team vs Blue Team", "content": "Red Team = Offensive (pentesting, exploiting, social engineering). Blue Team = Defensive (SOC, monitoring, forensics, damage control)."},
        {"title": "Zero-Day Exploit", "content": "An exploit released BEFORE the vendor knows of the vulnerability or has issued a protective patch."},
        {"title": "Web Breakdown", "content": "Surface Web = ~4% (indexed). Deep Web = ~96% (unindexed DBs/portals). Dark Web = <1% of Deep Web (Tor overlay)."},
        {"title": "Compensating Control", "content": "A substitute control implemented when the primary control cannot be deployed (e.g., complex passwords for legacy apps without MFA)."}
    ],
    "mcqs": [
        {
            "id": 1,
            "q": "According to the FBI / USA Facts data presented in Lecture 1, by what percentage did net financial losses from reported cyberattack complaints increase from 2023 to 2024?",
            "options": ["15%", "25%", "33%", "50%"],
            "ans": "C",
            "explanation": "Lecture 1 specifically highlights on slide 3 that net financial losses from cyberattacks reached $16.6B in 2024, representing a 33% increase compared to 2023 ($12.5B)."
        },
        {
            "id": 2,
            "q": "Which cybercrime category accounted for the HIGHEST total financial loss ($6.6 billion) in 2024 according to FBI statistics?",
            "options": ["Phishing", "Investment scams", "Extortion", "Business Email Compromise (BEC)"],
            "ans": "B",
            "explanation": "While phishing had the highest victim complaint count (most common), investment scams caused the largest monetary loss at $6.6B."
        },
        {
            "id": 3,
            "q": "How does Information Security (InfoSec) differ fundamentally from Cybersecurity?",
            "options": [
                "InfoSec protects only electronic systems, whereas Cybersecurity covers physical paper files.",
                "InfoSec covers sensitive data in both digital and non-digital formats, while Cybersecurity focuses exclusively on electronic data and networked technology.",
                "Cybersecurity is governed by laws, whereas InfoSec has no regulatory compliance.",
                "There is no difference; they are exact technical synonyms."
            ],
            "ans": "B",
            "explanation": "InfoSec encompasses all forms of sensitive information (including physical paperwork and locked rooms), whereas cybersecurity is a subset exclusively focused on electronic data and networked technologies."
        },
        {
            "id": 4,
            "q": "What were the primary cybercrime complaints and financial loss numbers for Business Email Compromise (BEC) in 2024?",
            "options": [
                "86.4K complaints and $143.2M losses",
                "21.4K complaints and $2.8B losses",
                "47.9K complaints and $6.6B losses",
                "3.2K complaints and $364.9M losses"
            ],
            "ans": "B",
            "explanation": "Slide 4 shows Business Email Compromise recorded 21.4K complaints with $2.8B in total financial losses."
        },
        {
            "id": 5,
            "q": "In the DAD triad (representing attacker objectives), which threat corresponds directly to violating Integrity?",
            "options": ["Disclosure", "Alteration", "Denial", "Destruction"],
            "ans": "B",
            "explanation": "In the DAD triad: Disclosure violates Confidentiality, Alteration violates Integrity (unauthorized modification), and Denial/Destruction violates Availability."
        },
        {
            "id": 6,
            "q": "Which cybersecurity objective guarantees that a sender or entity cannot deny having executed a digital transaction or action?",
            "options": ["Authenticity", "Non-repudiation", "Integrity", "Privacy"],
            "ans": "B",
            "explanation": "Non-repudiation ensures an entity cannot dispute or deny the validity of a transaction or digital communication they previously performed."
        },
        {
            "id": 7,
            "q": "Which of the following is classified as a 'Virtual Asset'?",
            "options": ["Data center generator", "IoT environmental sensor", "Proprietary database schema", "Network edge router"],
            "ans": "C",
            "explanation": "Databases, software, virtual machines, and trade secrets are virtual assets, whereas routers, servers, laptops, and sensors are physical/real assets."
        },
        {
            "id": 8,
            "q": "What is the correct logical progression of the Cybercrime Chain?",
            "options": [
                "Threat ➔ Vulnerability ➔ Risk",
                "Risk ➔ Threat ➔ Vulnerability",
                "Vulnerability ➔ Threat ➔ Risk",
                "Exploit ➔ Risk ➔ Vulnerability"
            ],
            "ans": "C",
            "explanation": "The cybercrime chain progresses as Vulnerability (the underlying flaw) ➔ Threat (the potential event/actor exploiting it) ➔ Risk (the realized likelihood and impact of harm)."
        },
        {
            "id": 9,
            "q": "Who manages the Common Vulnerabilities and Exposures (CVE) dictionary, and what is its standard identification format?",
            "options": [
                "FIRST; format is CVSS-NNNNN",
                "MITRE Corporation in collaboration with CNAs; format is CVE-YYYY-NNNNN",
                "Offensive Security; format is CWE-NNNNN",
                "NIST; format is CSF-YYYY-ID"
            ],
            "ans": "B",
            "explanation": "CVE is managed by MITRE Corporation along with CVE Numbering Authorities (CNAs), utilizing the format CVE-YYYY-NNNNN."
        },
        {
            "id": 10,
            "q": "What is the primary role of Common Weakness Enumeration (CWE)?",
            "options": [
                "Assigning a 0–10 numerical severity rating to an exploit.",
                "Listing specific commercial software patches released by Microsoft.",
                "Serving as a taxonomy of common software coding and design flaws to identify root causes (the 'why').",
                "Providing a catalog of proof-of-concept exploits for ethical hackers."
            ],
            "ans": "C",
            "explanation": "CWE categorizes architectural, design, and coding weaknesses (the 'why' or root cause behind vulnerabilities) like CWE-78 (OS Command Injection) or CWE-79 (XSS)."
        },
        {
            "id": 11,
            "q": "A CVSS v4.0 vulnerability score of 8.2 falls under which qualitative severity rating?",
            "options": ["Low", "Medium", "High", "Critical"],
            "ans": "C",
            "explanation": "CVSS severity scale: 0.1–3.9 is Low, 4.0–6.9 is Medium, 7.0–8.9 is High, and 9.0–10.0 is Critical. Hence, 8.2 is classified as High."
        },
        {
            "id": 12,
            "q": "What defines a 'Zero-day' exploit?",
            "options": [
                "An attack that takes zero seconds to complete over the network.",
                "An exploit taking advantage of a vulnerability before the vendor is aware of it or before a patch is available.",
                "A vulnerability that has been assigned a CVSS score of 0.0.",
                "An exploit published on Exploit-DB on the first day of every month."
            ],
            "ans": "B",
            "explanation": "A zero-day exploit targets a flaw that is unknown to the vendor/public, leaving zero days of defense since no official patch exists."
        },
        {
            "id": 13,
            "q": "What percentage of the Deep Web is estimated to be composed of the Dark Web?",
            "options": ["About 50%", "Over 90%", "Less than 1%", "Roughly 25%"],
            "ans": "C",
            "explanation": "The Deep Web (unindexed web resources) makes up ~96% of the web, and the Dark Web (requiring specialized overlay networks like Tor) represents less than 1% of the Deep Web."
        },
        {
            "id": 14,
            "q": "Which organization maintains 'The Exploit Database' (Exploit-DB) for public security research?",
            "options": ["MITRE Corporation", "FIRST", "Offensive Security", "Cisco Systems"],
            "ans": "C",
            "explanation": "The Exploit Database (exploit-db.com) is an open repository of proof-of-concept exploits maintained by Offensive Security."
        },
        {
            "id": 15,
            "q": "Under human threat categories, what is an accidental system misconfiguration made by an authorized IT employee classified as?",
            "options": ["Malicious - Directed", "Malicious - Random", "Benign - Human Error", "Natural Threat"],
            "ans": "C",
            "explanation": "Threat taxonomy distinguishes natural causes from human causes; human causes split into benign intent (human error) and malicious intent."
        },
        {
            "id": 16,
            "q": "A company suffers a major breach resulting in a $20M fine under GDPR regulations. Which dimension of cyber risk does this represent?",
            "options": ["Operational Risk", "Compliance Risk", "Strategic Risk", "Reputational Risk"],
            "ans": "B",
            "explanation": "Compliance risk deals specifically with legal sanctions, regulatory penalties (GDPR/HIPAA), and loss of operating certifications."
        },
        {
            "id": 17,
            "q": "Which cybersecurity role is specifically responsible for 24/7 security monitoring, alert triage, and SIEM correlation?",
            "options": ["Ethical Hacker", "SOC Analyst", "Cloud Security Engineer", "Risk & Compliance Analyst"],
            "ans": "B",
            "explanation": "SOC Analysts staff the Security Operations Center to perform continuous monitoring, triage security alerts, and analyze telemetry."
        },
        {
            "id": 18,
            "q": "A security awareness training workshop for new hires is an example of which security control CATEGORY?",
            "options": ["Technical control", "Physical control", "Operational control", "Managerial / Administrative control"],
            "ans": "D",
            "explanation": "Managerial (administrative) controls involve policies, guidelines, risk assessments, and security awareness training programs."
        },
        {
            "id": 19,
            "q": "Which specific functional type of security control is intended to mitigate damage and restore systems following a cyberattack?",
            "options": ["Preventive control", "Deterrent control", "Corrective control", "Compensating control"],
            "ans": "C",
            "explanation": "Corrective controls (such as data backups and incident response plans) aim to mitigate damage and restore operations after a breach occurs."
        },
        {
            "id": 20,
            "q": "An organization relies on an old legacy server that cannot support Multi-Factor Authentication (MFA). The security team enforces a stricter password policy and IP whitelisting instead. What type of control is this?",
            "options": ["Compensating control", "Detective control", "Deterrent control", "Directive control"],
            "ans": "A",
            "explanation": "Compensating controls are alternative safeguards deployed when the primary recommended security control is technically or economically infeasible."
        }
    ]
}

