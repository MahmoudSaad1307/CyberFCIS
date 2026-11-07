# -*- coding: utf-8 -*-

LEC5_DATA = {
    "id": "lec5",
    "number": 5,
    "title": "Access Control",
    "instructor": "Dr. Alshaimaa Abo-alian",
    "faculty": "Faculty of Computer & Information Sciences, Ain Shams University",
    "badge": "L5: DAC, MAC, RBAC & ABAC",
    "summary_html": """
    <div class="space-y-6">
        <!-- Section: Foundations & AAA -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🏛️</span> 1. Access Control Foundations, Objectives & AAA
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <div class="p-3 bg-slate-800/60 rounded border border-cyan-500/40 mb-3">
                        <strong class="text-cyan-300 block mb-1">Definition:</strong>
                        <p>Access Control is a security function that protects shared system resources against unauthorized access by enforcing a defined <strong>access control policy</strong> (describing which accesses are allowed and which are denied).</p>
                    </div>
                    <strong class="text-white block mb-2">3 Principal Objectives:</strong>
                    <div class="space-y-2">
                        <div class="p-2 bg-rose-950/20 border border-rose-800/40 rounded">
                            <strong class="text-rose-300">1. Keep Outsiders OUT:</strong> Prevent unauthorized users from gaining any access.
                        </div>
                        <div class="p-2 bg-amber-950/20 border border-amber-800/40 rounded">
                            <strong class="text-amber-300">2. Keep Insiders IN-BOUNDS:</strong> Prevent authorized users from accessing resources in an unauthorized manner or scope.
                        </div>
                        <div class="p-2 bg-emerald-950/20 border border-emerald-800/40 rounded">
                            <strong class="text-emerald-300">3. Enable Legitimate Work:</strong> Ensure authorized users can properly access resources needed for their legitimate tasks.
                        </div>
                    </div>
                    <div class="mt-3 p-2 bg-slate-800/40 rounded border border-slate-700 text-[11px]">
                        <strong class="text-white">Ubiquity Examples:</strong> Social networks (view permissions), OS file/process isolation, firewalls (drop unauthorized packets), physical badge readers.
                    </div>
                </div>
                <div>
                    <strong class="text-white block mb-2">AAA Framework:</strong>
                    <div class="space-y-2 mb-4">
                        <div class="p-3 bg-blue-950/20 border border-blue-800/40 rounded">
                            <strong class="text-blue-300 block">Authentication</strong>
                            <p>Verifying that presented credentials are valid and the entity is who they claim to be.</p>
                        </div>
                        <div class="p-3 bg-purple-950/20 border border-purple-800/40 rounded">
                            <strong class="text-purple-300 block">Authorization</strong>
                            <p>Granting or denying specific permissions to access a specific resource based on the authenticated identity.</p>
                        </div>
                        <div class="p-3 bg-teal-950/20 border border-teal-800/40 rounded">
                            <strong class="text-teal-300 block">Auditing</strong>
                            <p>Independent review of system records and event logs (using SIEM platforms like Splunk) to verify policy compliance and detect breaches after the fact.</p>
                        </div>
                    </div>
                    <strong class="text-white block mb-2">Core Terminology:</strong>
                    <div class="overflow-x-auto">
                        <table class="w-full border border-slate-700 text-[11px]">
                            <thead class="bg-slate-800"><tr><th class="p-1.5 border border-slate-700">Term</th><th class="p-1.5 border border-slate-700">Definition</th><th class="p-1.5 border border-slate-700">Examples</th></tr></thead>
                            <tbody class="divide-y divide-slate-800 text-slate-300">
                                <tr><td class="p-1.5 font-bold text-cyan-300">Subject</td><td class="p-1.5">Active entity requesting access</td><td class="p-1.5">User account, process, application</td></tr>
                                <tr><td class="p-1.5 font-bold text-cyan-300">Object</td><td class="p-1.5">Passive protected resource</td><td class="p-1.5">Files, databases, memory, printers, ports</td></tr>
                                <tr><td class="p-1.5 font-bold text-cyan-300">Access Right</td><td class="p-1.5">The manner/operation of access</td><td class="p-1.5">Read, Write, Execute, Delete, Create, Search</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div class="mt-3 p-3 bg-slate-800/40 rounded border border-slate-700 text-xs text-slate-300">
                <strong class="text-white">System Components:</strong>
                <span class="ml-2 text-cyan-300">Enforcement Mechanism</span> (intercepts EVERY access request and queries the decision function) ➔
                <span class="ml-2 text-purple-300">Decision Function</span> (evaluates the request against the security policy → Yes/No decision).
            </div>
        </div>

        <!-- Section: 4 Access Control Models Overview -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🔀</span> 2. The Four Access Control Models — Comparison
            </h3>
            <div class="overflow-x-auto text-xs">
                <table class="w-full text-left border border-slate-800">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-2 border border-slate-700">Model</th>
                            <th class="p-2 border border-slate-700">Full Name</th>
                            <th class="p-2 border border-slate-700">Who Controls Access?</th>
                            <th class="p-2 border border-slate-700">Basis for Decision</th>
                            <th class="p-2 border border-slate-700">Typical Use</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800 text-slate-300">
                        <tr>
                            <td class="p-2 font-bold text-cyan-300">DAC</td>
                            <td class="p-2">Discretionary Access Control</td>
                            <td class="p-2">Data Owner (self-managed)</td>
                            <td class="p-2">User identity</td>
                            <td class="p-2">Default model in Windows, Linux, macOS</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-purple-300">MAC</td>
                            <td class="p-2">Mandatory Access Control</td>
                            <td class="p-2">Central authority / OS enforces</td>
                            <td class="p-2">Security labels & clearance levels</td>
                            <td class="p-2">Military, government, top-secret classification</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-blue-300">RBAC</td>
                            <td class="p-2">Role-Based Access Control</td>
                            <td class="p-2">Administrator defines roles</td>
                            <td class="p-2">User's assigned role(s)</td>
                            <td class="p-2">Enterprise environments, HR systems, ERP</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-emerald-300">ABAC</td>
                            <td class="p-2">Attribute-Based Access Control</td>
                            <td class="p-2">Policy engine evaluates dynamically</td>
                            <td class="p-2">Subject + Object + Action + Environment attributes</td>
                            <td class="p-2">Cloud platforms, AWS IAM, fine-grained APIs</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Section: DAC -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>📋</span> 3. DAC — Discretionary Access Control & SQL Implementation
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <strong class="text-white block mb-2">4 Structures Implementing DAC:</strong>
                    <div class="space-y-2">
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">1. Access Matrix:</strong> 2D table of Subjects (rows) × Objects (columns). Cells contain access rights.
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">2. Access Control List (ACL):</strong> Column of the matrix stored with EACH object. Answers: <em>"Who can access this file?"</em>
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">3. Capability List:</strong> Row of the matrix stored with EACH subject. Answers: <em>"What can this user access?"</em> Must be unforgeable.
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">4. Authorization Table:</strong> Each row is a (Subject, Access Right, Object) triple. Sparse, normalized storage.
                        </div>
                    </div>
                </div>
                <div>
                    <strong class="text-white block mb-2">DAC in SQL (Data Control Language — DCL):</strong>
                    <div class="space-y-2">
                        <div class="p-2 bg-slate-800/60 rounded font-mono text-[11px] text-cyan-300">
                            GRANT SELECT, INSERT ON Employees TO Alice;<br/>
                            GRANT SELECT ON Employees TO Bob WITH GRANT OPTION;
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-white">WITH GRANT OPTION:</strong> Allows the recipient (Bob) to further propagate privileges to other users.
                        </div>
                        <div class="p-2 bg-slate-800/60 rounded font-mono text-[11px] text-rose-300">
                            REVOKE SELECT ON Employees FROM Alice CASCADE;<br/>
                            REVOKE SELECT ON Employees FROM Alice RESTRICT;
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-white">CASCADE:</strong> Recursively revokes privileges Bob granted to others.<br/>
                            <strong class="text-white">RESTRICT:</strong> Revoke fails if dependent grants exist (safe failure).
                        </div>
                        <div class="p-2 bg-slate-800/60 rounded font-mono text-[11px] text-emerald-300 mt-1">
                            CREATE VIEW Dept_Finance AS<br/>
                            SELECT * FROM Employees<br/>
                            WHERE Department = 'Finance';<br/>
                            GRANT SELECT ON Dept_Finance TO FinanceTeam;
                        </div>
                        <p class="text-[11px] text-slate-400">Row-Level Security via filtered views.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section: MAC & Bell-LaPadula -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🏛️</span> 4. MAC — Mandatory Access Control & Bell-LaPadula Model
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <div class="p-3 bg-slate-800/60 rounded border border-slate-700 mb-3">
                        <strong class="text-white block mb-1">MAC Mechanics:</strong>
                        <p>Developed by the U.S. Department of Defense. Access is enforced by the central OS based on mandatory labels — users CANNOT change these.</p>
                        <ul class="list-disc list-inside mt-1 space-y-0.5">
                            <li><strong>Security Classification:</strong> Label assigned to OBJECTS (data files, documents).</li>
                            <li><strong>Security Clearance:</strong> Label assigned to SUBJECTS (people, processes).</li>
                        </ul>
                    </div>
                    <strong class="text-white block mb-2">Classification Hierarchy (highest → lowest):</strong>
                    <div class="flex flex-col gap-1">
                        <div class="p-1.5 bg-rose-950/40 border border-rose-700/60 rounded text-center font-bold text-rose-300">TOP SECRET</div>
                        <div class="p-1.5 bg-orange-950/40 border border-orange-700/60 rounded text-center font-bold text-orange-300">SECRET</div>
                        <div class="p-1.5 bg-amber-950/40 border border-amber-700/60 rounded text-center font-bold text-amber-300">CONFIDENTIAL</div>
                        <div class="p-1.5 bg-yellow-950/40 border border-yellow-700/60 rounded text-center font-bold text-yellow-300">RESTRICTED</div>
                        <div class="p-1.5 bg-slate-800/60 border border-slate-600/60 rounded text-center font-bold text-slate-300">UNCLASSIFIED</div>
                    </div>
                </div>
                <div>
                    <strong class="text-white block mb-2">Bell-LaPadula (BLP) Model Rules:</strong>
                    <div class="space-y-3">
                        <div class="p-3 bg-blue-950/20 border border-blue-700/50 rounded">
                            <strong class="text-blue-300 block">Simple Security Property — "No Read Up"</strong>
                            <code class="font-mono text-[11px] block mt-1 text-blue-200">class(Subject) ≥ class(Object)</code>
                            <p class="mt-1">A subject can ONLY read an object at their OWN security level or BELOW (they can't read up to higher classified data).</p>
                            <p class="text-slate-400 text-[11px] mt-0.5">✅ SECRET user can read SECRET and CONFIDENTIAL data.<br/>❌ CONFIDENTIAL user CANNOT read SECRET data.</p>
                        </div>
                        <div class="p-3 bg-purple-950/20 border border-purple-700/50 rounded">
                            <strong class="text-purple-300 block">★-Property (Star Property) — "No Write Down"</strong>
                            <code class="font-mono text-[11px] block mt-1 text-purple-200">class(Subject) ≤ class(Object)</code>
                            <p class="mt-1">A subject can ONLY write to an object at their OWN level or ABOVE (they can't write down to lower classification). Prevents leaking classified data to lower-level storage.</p>
                            <p class="text-slate-400 text-[11px] mt-0.5">✅ SECRET user can write to SECRET and TOP SECRET objects.<br/>❌ SECRET user CANNOT write to CONFIDENTIAL objects (would leak down).</p>
                        </div>
                    </div>
                    <div class="mt-2 p-2 bg-amber-950/20 border border-amber-700/40 rounded text-[11px]">
                        <strong class="text-amber-300">BLP Focus:</strong> Bell-LaPadula is designed purely for <strong>Confidentiality</strong> (not integrity or availability). It enforces the information flow policy of the U.S. DoD.
                    </div>
                </div>
            </div>
        </div>

        <!-- Section: RBAC -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>👔</span> 5. RBAC — Role-Based Access Control
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <div class="p-3 bg-slate-800/60 rounded border border-slate-700 mb-3">
                        <strong class="text-white block mb-1">Core RBAC Concept:</strong>
                        <p>Assign permissions to <strong>roles</strong> (not individual users). Assign users to roles. This abstracts volatile user changes from the stable role structure.</p>
                        <code class="font-mono text-[11px] block mt-1 text-cyan-300">Users → Roles → Permissions → Objects</code>
                    </div>
                    <strong class="text-white block mb-2">Hierarchical RBAC:</strong>
                    <p class="mb-2">Senior roles <strong>inherit all access rights</strong> of their subordinate roles.</p>
                    <div class="p-2 bg-slate-800/60 rounded font-mono text-[11px] text-blue-300">
                        Director inherits Manager's rights<br/>
                        Manager inherits Employee's rights
                    </div>
                </div>
                <div>
                    <strong class="text-white block mb-2">RBAC Constraints:</strong>
                    <div class="space-y-2">
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">Mutually Exclusive (Separation of Duties):</strong> A single user cannot simultaneously hold conflicting roles (e.g., cannot be both "Purchase Order Creator" and "Purchase Order Approver").
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">Prerequisite:</strong> User can only acquire Role B if they already hold Role A. (e.g., Senior Analyst requires Analyst role first).
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">Cardinality:</strong> Limits the max number of users per role (e.g., max 2 "CISO" role holders) or the max roles per user.
                        </div>
                    </div>
                    <strong class="text-white block mt-3 mb-2">SQL RBAC Implementation:</strong>
                    <div class="p-2 bg-slate-800/60 rounded font-mono text-[11px] text-cyan-300">
                        CREATE ROLE Finance_Analyst;<br/>
                        GRANT SELECT ON Sales_Data TO Finance_Analyst;<br/>
                        GRANT Finance_Analyst TO Alice;<br/>
                        DROP ROLE Finance_Analyst;
                    </div>
                </div>
            </div>
        </div>

        <!-- Section: ABAC -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>⚡</span> 6. ABAC — Attribute-Based Access Control
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <div class="p-3 bg-slate-800/60 rounded border border-slate-700 mb-3">
                        <strong class="text-white block mb-1">ABAC Core Concept:</strong>
                        <p>Access decisions are made <strong>dynamically at runtime</strong> by evaluating a combination of attributes across four categories, connected by logic gates.</p>
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        <div class="p-2 bg-blue-950/20 border border-blue-800/40 rounded">
                            <strong class="text-blue-300 block">Subject Attributes:</strong>
                            Department, Job title, Security clearance, Hire date, Location
                        </div>
                        <div class="p-2 bg-purple-950/20 border border-purple-800/40 rounded">
                            <strong class="text-purple-300 block">Object Attributes:</strong>
                            Classification level, Owner, Data sensitivity, File type
                        </div>
                        <div class="p-2 bg-amber-950/20 border border-amber-800/40 rounded">
                            <strong class="text-amber-300 block">Action Attributes:</strong>
                            Read, Write, Delete, Execute, Approve, Transfer
                        </div>
                        <div class="p-2 bg-teal-950/20 border border-teal-800/40 rounded">
                            <strong class="text-teal-300 block">Environment Attributes:</strong>
                            Time of day, Date, IP address, Device type, Network zone
                        </div>
                    </div>
                    <div class="mt-2 p-2 bg-slate-800/50 rounded border border-slate-700 text-[11px]">
                        <strong class="text-white">Example Policy:</strong>
                        <code class="block font-mono text-cyan-300 mt-1">"GRANT IF Subject.Dept = 'HR' AND Subject.Clearance = 'Secret' AND Action = 'READ' AND Environment.Time BETWEEN 08:00 AND 18:00"</code>
                    </div>
                </div>
                <div>
                    <strong class="text-white block mb-2">Policy Languages:</strong>
                    <div class="space-y-1 mb-3">
                        <div class="p-1.5 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">XACML</strong> (eXtensible Access Control Markup Language) — XML-based OASIS standard, most widely adopted.
                        </div>
                        <div class="p-1.5 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">AWS IAM Policy Language</strong> — JSON-based, used for AWS resource access control.
                        </div>
                        <div class="p-1.5 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-cyan-300">Google Cloud IAM</strong>, <strong>ALFA</strong> (Abbreviated Language for Authorization), <strong>APL</strong> (Attribute Policy Language).
                        </div>
                    </div>
                    <strong class="text-white block mb-2">ABAC Advantages vs. Disadvantages:</strong>
                    <div class="grid grid-cols-1 gap-2">
                        <div class="p-2 bg-emerald-950/20 border border-emerald-700/40 rounded">
                            <strong class="text-emerald-300 block mb-0.5">✅ Advantages:</strong>
                            Fine-grained context-aware control, scales without role explosion, supports least privilege dynamically, flexible policy logic.
                        </div>
                        <div class="p-2 bg-rose-950/20 border border-rose-700/40 rounded">
                            <strong class="text-rose-300 block mb-0.5">❌ Disadvantages:</strong>
                            Complex policy management and debugging, performance overhead at high decision volume, requires accurate and standardized attribute data.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,
    "memory_aids": [
        {"title": "DAC vs MAC vs RBAC vs ABAC", "content": "DAC = Owner decides (discretionary). MAC = OS/Authority forces (mandatory labels). RBAC = Role determines (least privilege). ABAC = Attributes decide dynamically (context-aware)."},
        {"title": "BLP Simple Security — No Read Up", "content": "Class(Subject) ≥ Class(Object). A SECRET-cleared user can read SECRET and CONFIDENTIAL but CANNOT read TOP SECRET."},
        {"title": "BLP Star Property — No Write Down", "content": "Class(Subject) ≤ Class(Object). A SECRET-cleared user can write to SECRET and TOP SECRET but CANNOT write to CONFIDENTIAL (prevents data leakage downward)."},
        {"title": "ACL vs Capability List", "content": "ACL = attached to the OBJECT (Who can access this?). Capability List = held by the SUBJECT (What can I access?). Both are columns/rows of the Access Matrix."},
        {"title": "SQL GRANT CASCADE vs RESTRICT", "content": "CASCADE = recursively removes all dependent grants (chain revocation). RESTRICT = revoke fails if dependents exist (safe, prevents accidental broad revocation)."},
        {"title": "RBAC Constraints", "content": "Separation of Duties (mutually exclusive roles), Prerequisite (must hold Role A before B), Cardinality (max number of users per role)."},
        {"title": "ABAC 4 Attribute Types", "content": "Subject (who), Object (what), Action (how), Environment (when/where). Access = logic(Subject AND/OR Object AND/OR Action AND/OR Environment)."},
        {"title": "AAA Framework", "content": "Authentication = Verify IDENTITY. Authorization = Grant/Deny PERMISSIONS. Auditing = Review LOGS independently (using SIEM)."}
    ],
    "mcqs": [
        {
            "id": 1,
            "q": "Which of the three principal objectives of Access Control ensures that authorized users can still perform legitimate work?",
            "options": [
                "Keep outsiders out.",
                "Keep insiders in-bounds.",
                "Enable legitimate work.",
                "Enforce mandatory clearance levels."
            ],
            "ans": "C",
            "explanation": "The third objective — Enable Legitimate Work — ensures that access control does not over-restrict authorized users from performing their actual business tasks."
        },
        {
            "id": 2,
            "q": "In the AAA framework, what does 'Authorization' specifically mean?",
            "options": [
                "Verifying that the user's credentials are valid and their identity is established.",
                "Reviewing system logs to detect policy violations.",
                "Granting or denying permissions to access a specific resource based on the authenticated identity.",
                "Encrypting the user's session tokens to prevent replay attacks."
            ],
            "ans": "C",
            "explanation": "Authorization occurs after authentication and determines WHAT an authenticated entity is permitted to access or do, based on defined policies."
        },
        {
            "id": 3,
            "q": "In access control terminology, what is a 'Subject'?",
            "options": [
                "A protected resource such as a file or database.",
                "The specific operation being performed (Read, Write, Execute).",
                "The active entity requesting access, such as a user account, process, or application.",
                "The security label attached to classified data."
            ],
            "ans": "C",
            "explanation": "A Subject is the active entity that initiates an access request. Objects are the passive resources. Access Rights define the allowed operations."
        },
        {
            "id": 4,
            "q": "Which system component intercepts every resource access request and queries the decision function?",
            "options": [
                "The Security Certificate Authority (CA).",
                "The Enforcement Mechanism.",
                "The SIEM Platform.",
                "The Authorization Table."
            ],
            "ans": "B",
            "explanation": "The Enforcement Mechanism is the reference monitor that intercepts all access attempts and enforces the security policy decisions."
        },
        {
            "id": 5,
            "q": "In DAC, who controls access to a resource?",
            "options": [
                "The operating system kernel based on mandatory security labels.",
                "The network firewall based on port numbers.",
                "The data or resource owner, based on user identity.",
                "A centralized authority that cannot be overridden by individuals."
            ],
            "ans": "C",
            "explanation": "DAC = Discretionary. The owner of the data has the discretion to decide who can and cannot access their resources."
        },
        {
            "id": 6,
            "q": "Which of the following structures provides column-wise storage attached to each object, answering 'Who can access this resource?'",
            "options": [
                "Access Matrix",
                "Capability List",
                "Authorization Table",
                "Access Control List (ACL)"
            ],
            "ans": "D",
            "explanation": "An ACL is associated with an Object and lists the subjects authorized to access it. It is essentially a column of the full access matrix."
        },
        {
            "id": 7,
            "q": "What does 'WITH GRANT OPTION' accomplish in a SQL GRANT statement?",
            "options": [
                "It grants access with a time-limited expiry date.",
                "It allows the recipient to further grant those same privileges to other users.",
                "It enforces row-level security on the granted table.",
                "It triggers CASCADE revocation when the original grantor's access is removed."
            ],
            "ans": "B",
            "explanation": "WITH GRANT OPTION allows the grantee to propagate the granted privilege to other users, extending the chain of access control."
        },
        {
            "id": 8,
            "q": "What happens when REVOKE is used with the RESTRICT option and dependent grants exist?",
            "options": [
                "RESTRICT silently deletes all dependent grants automatically.",
                "RESTRICT causes the revocation to FAIL to prevent unintentional broad access removal.",
                "RESTRICT revokes the original grant and all dependent grants in a cascade.",
                "RESTRICT limits the revocation to read-only permissions only."
            ],
            "ans": "B",
            "explanation": "RESTRICT is the safe option: if dependent grants exist (the grantee passed the privilege on), the REVOKE operation fails rather than cause unexpected access changes."
        },
        {
            "id": 9,
            "q": "How is Row-Level Security typically implemented in SQL using DAC?",
            "options": [
                "Using stored procedures with IF/ELSE guards per row.",
                "By creating filtered Views and granting access to those Views instead of the base table.",
                "By assigning security labels to each row in the table.",
                "By writing custom RBAC roles for each individual data row."
            ],
            "ans": "B",
            "explanation": "Row-level security is implemented by creating a VIEW with a WHERE clause that filters rows, then granting access to the view rather than the full base table."
        },
        {
            "id": 10,
            "q": "The Bell-LaPadula (BLP) model was developed to enforce security for which organization?",
            "options": [
                "The European Union's GDPR compliance body.",
                "The U.S. Department of Defense (DoD) for classified data handling.",
                "The National Institute of Standards and Technology (NIST) for commercial enterprises.",
                "The Internet Engineering Task Force (IETF) for network protocol security."
            ],
            "ans": "B",
            "explanation": "BLP was developed by David Bell and Leonard LaPadula in a U.S. DoD-funded research effort to formalize multi-level security for military information handling."
        },
        {
            "id": 11,
            "q": "According to the Bell-LaPadula Simple Security Property ('No Read Up'), which access is PERMITTED?",
            "options": [
                "A CONFIDENTIAL-cleared user reads a TOP SECRET document.",
                "A SECRET-cleared user reads an UNCLASSIFIED document.",
                "A RESTRICTED-cleared user reads a SECRET document.",
                "An UNCLASSIFIED-cleared user reads a CONFIDENTIAL document."
            ],
            "ans": "B",
            "explanation": "No Read Up: class(Subject) ≥ class(Object). SECRET ≥ UNCLASSIFIED → allowed. Any scenario where the user reads a HIGHER classified document is DENIED."
        },
        {
            "id": 12,
            "q": "According to the Bell-LaPadula *-Property ('No Write Down'), why is a SECRET-cleared subject prevented from writing to a CONFIDENTIAL object?",
            "options": [
                "It violates availability — the CONFIDENTIAL object would become unavailable.",
                "It would leak higher-classified (SECRET) information into a lower classification level (CONFIDENTIAL), violating confidentiality.",
                "It triggers a CWE-78 OS injection vulnerability.",
                "It violates the Separation of Duties constraint in RBAC."
            ],
            "ans": "B",
            "explanation": "*-Property prevents writing DOWN in classification to stop classified information from leaking downward to unauthorized recipients at lower clearance levels."
        },
        {
            "id": 13,
            "q": "What is the primary advantage of RBAC over DAC in a large enterprise?",
            "options": [
                "RBAC eliminates the need for any authentication.",
                "RBAC makes access decisions based on network packet headers.",
                "RBAC absorbs volatile user changes (hires/fires) into a stable role layer, simplifying administration.",
                "RBAC stores access decisions in a Blockchain for audit."
            ],
            "ans": "C",
            "explanation": "With RBAC, granting/revoking access only requires adding/removing users from roles. The permissions themselves stay with the role, reducing administrative overhead enormously."
        },
        {
            "id": 14,
            "q": "In RBAC, what does 'Separation of Duties' (mutually exclusive constraint) prevent?",
            "options": [
                "Users from holding more than one role at any time.",
                "A single user from simultaneously holding two conflicting roles that together could enable fraud.",
                "Administrators from modifying role definitions without audit logs.",
                "Role inheritance in hierarchical RBAC structures."
            ],
            "ans": "B",
            "explanation": "Separation of Duties prevents concentration of conflicting powers. E.g., one person cannot be both 'Invoice Creator' AND 'Invoice Approver' — that would enable fraud."
        },
        {
            "id": 15,
            "q": "What does the 'Cardinality' constraint in RBAC limit?",
            "options": [
                "The number of objects a subject can access in a single session.",
                "The maximum number of users assignable to a role or roles assignable to a user.",
                "The length of a user's authentication session token.",
                "The number of SQL GRANT statements allowed per database."
            ],
            "ans": "B",
            "explanation": "Cardinality limits role size (e.g., max 1 'CISO' role holder) or how many roles one user can hold, preventing excessive privilege accumulation."
        },
        {
            "id": 16,
            "q": "Which SQL statement correctly creates a new named role in an RBAC implementation?",
            "options": [
                "ASSIGN ROLE Finance_Analyst;",
                "ADD ROLE Finance_Analyst;",
                "CREATE ROLE Finance_Analyst;",
                "INSERT INTO Roles VALUES ('Finance_Analyst');"
            ],
            "ans": "C",
            "explanation": "Standard SQL DCL uses CREATE ROLE to create a named role, GRANT to assign privileges/users to roles, and DROP ROLE to remove a role."
        },
        {
            "id": 17,
            "q": "What is the defining feature that distinguishes ABAC from DAC, MAC, and RBAC?",
            "options": [
                "ABAC makes access decisions based solely on the user's password strength.",
                "ABAC evaluates combinations of Subject, Object, Action, and Environment attributes dynamically at runtime.",
                "ABAC uses only physical security badges for access decisions.",
                "ABAC mandates that only OS kernels can enforce access decisions."
            ],
            "ans": "B",
            "explanation": "ABAC's key differentiator is dynamic, context-aware policy evaluation combining attributes from subjects, objects, actions, and the environment at the moment of the access request."
        },
        {
            "id": 18,
            "q": "Which policy language is an XML-based OASIS standard commonly used for implementing ABAC policies?",
            "options": [
                "LDAP (Lightweight Directory Access Protocol)",
                "XACML (eXtensible Access Control Markup Language)",
                "SNMP (Simple Network Management Protocol)",
                "SAML (Security Assertion Markup Language)"
            ],
            "ans": "B",
            "explanation": "XACML (eXtensible Access Control Markup Language) is the XML-based OASIS standard specifically designed for expressing ABAC policies."
        },
        {
            "id": 19,
            "q": "An ABAC policy denies access to financial records outside of business hours (08:00–18:00) even for authorized employees. Which ABAC attribute category does the time restriction fall under?",
            "options": [
                "Subject attributes",
                "Object attributes",
                "Action attributes",
                "Environment attributes"
            ],
            "ans": "D",
            "explanation": "Time of day, date, location, network zone, and device type are all Environment attributes in ABAC — they describe the context in which the access request occurs."
        },
        {
            "id": 20,
            "q": "What is the main disadvantage of ABAC compared to RBAC?",
            "options": [
                "ABAC cannot enforce the principle of least privilege.",
                "ABAC requires a unique hardware token per user.",
                "ABAC policies are complex to manage and debug, and require accurate standardized attributes.",
                "ABAC only works with SQL databases."
            ],
            "ans": "C",
            "explanation": "ABAC's power creates complexity: policy authoring, debugging, and maintenance are significantly harder than RBAC, and it requires all attribute data to be accurate and consistently standardized."
        }
    ]
}

