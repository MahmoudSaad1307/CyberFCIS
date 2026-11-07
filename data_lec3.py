# -*- coding: utf-8 -*-

LEC3_DATA = {
    "id": "lec3",
    "number": 3,
    "title": "Fundamentals of Cryptography",
    "instructor": "Dr. Alshaimaa Abo-alian",
    "faculty": "Faculty of Computer & Information Sciences, Ain Shams University",
    "badge": "L3: Crypto Concepts & Algorithms",
    "summary_html": """
    <div class="space-y-6">
        <!-- Section: Why Cryptography -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🔐</span> 1. Why Cryptography? Applications & Core Services
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300 mb-4">
                <div>
                    <strong class="text-white block mb-1">Real-World Applications:</strong>
                    <ul class="space-y-1 list-disc list-inside text-slate-300">
                        <li>Secure communications: <strong class="text-cyan-300">HTTPS / TLS</strong>, end-to-end messaging (Signal, WhatsApp)</li>
                        <li>Banking & fintech transactions</li>
                        <li>Virtual Private Networks (VPNs)</li>
                        <li>Blockchain & cryptocurrencies</li>
                        <li>Password storage (hashing)</li>
                        <li>Cloud storage encryption</li>
                        <li>Digital signatures & certificate authorities</li>
                    </ul>
                </div>
                <div>
                    <strong class="text-white block mb-1">4 Core Security Services Provided:</strong>
                    <div class="space-y-2">
                        <div class="p-2 bg-slate-800/60 rounded border border-slate-700">
                            <span class="text-cyan-300 font-bold">1. Data Integrity:</span> Guarantees the message was NOT altered in transit.
                        </div>
                        <div class="p-2 bg-slate-800/60 rounded border border-slate-700">
                            <span class="text-cyan-300 font-bold">2. Origin Authentication:</span> Guarantees the message is not forged and comes from the stated sender.
                        </div>
                        <div class="p-2 bg-slate-800/60 rounded border border-slate-700">
                            <span class="text-cyan-300 font-bold">3. Data Confidentiality:</span> Guarantees only authorized parties can read the data.
                        </div>
                        <div class="p-2 bg-slate-800/60 rounded border border-slate-700">
                            <span class="text-cyan-300 font-bold">4. Data Non-Repudiation:</span> Guarantees the sender cannot deny having sent the message.
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section: Definitions -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>📖</span> 2. Core Definitions: Cryptography vs. Steganography vs. Cryptanalysis
            </h3>
            <div class="overflow-x-auto text-xs">
                <table class="w-full text-left border border-slate-800">
                    <thead class="bg-slate-800 text-slate-300">
                        <tr>
                            <th class="p-2 border border-slate-700">Term</th>
                            <th class="p-2 border border-slate-700">Etymology</th>
                            <th class="p-2 border border-slate-700">What It Hides</th>
                            <th class="p-2 border border-slate-700">Definition</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800 text-slate-300">
                        <tr>
                            <td class="p-2 font-bold text-cyan-300">Cryptography</td>
                            <td class="p-2 font-mono">"krypto" + "graphene"<br/>(hidden writing)</td>
                            <td class="p-2">The <strong>meaning</strong> of a message</td>
                            <td class="p-2">Science of protecting information by transforming it into an unreadable format for unauthorized parties.</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-cyan-300">Steganography</td>
                            <td class="p-2 font-mono">"steganos" + "graphia"<br/>(covered writing)</td>
                            <td class="p-2">The <strong>existence</strong> of a message</td>
                            <td class="p-2">Concealing secret messages inside innocuous cover media (images, audio, video) via metadata embedding.</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-cyan-300">Cryptanalysis</td>
                            <td class="p-2 font-mono">Analysis of hidden writing</td>
                            <td class="p-2">N/A — Breaks protection</td>
                            <td class="p-2">Mathematical techniques to defeat or break cryptographic mechanisms and recover the original plaintext.</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-cyan-300">Cryptology</td>
                            <td class="p-2 font-mono">Study of hidden writing</td>
                            <td class="p-2">Umbrella discipline</td>
                            <td class="p-2">The combined scientific study of both Cryptography and Cryptanalysis.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Section: Taxonomy of Algorithms -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🌳</span> 3. Taxonomy of Cryptographic Algorithms
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs text-slate-300">
                <!-- Keyless -->
                <div class="p-4 bg-slate-800/50 rounded-lg border border-slate-700">
                    <h4 class="text-white font-bold text-sm mb-2">🔑 Keyless Algorithms</h4>
                    <ul class="space-y-1 list-disc list-inside">
                        <li>Hash Functions (SHA-256, MD5)</li>
                        <li>Pseudo-Random Number Generators (PRNGs)</li>
                    </ul>
                    <p class="mt-2 text-slate-400">No key required. Used for integrity checks and randomness generation.</p>
                </div>
                <!-- Single Key (Symmetric) -->
                <div class="p-4 bg-blue-950/30 rounded-lg border border-blue-800/50">
                    <h4 class="text-blue-300 font-bold text-sm mb-2">🔑 Single-Key (Symmetric)</h4>
                    <p class="mb-2">Same secret key used for both encryption AND decryption.</p>
                    <ul class="space-y-1 list-disc list-inside">
                        <li><strong>Block ciphers:</strong> AES, DES, 3DES</li>
                        <li><strong>Stream ciphers:</strong> RC4, ChaCha20, OTP</li>
                    </ul>
                    <p class="mt-2 text-slate-400">Fast. Best for bulk data encryption.</p>
                </div>
                <!-- Two-Key (Asymmetric) -->
                <div class="p-4 bg-purple-950/30 rounded-lg border border-purple-800/50">
                    <h4 class="text-purple-300 font-bold text-sm mb-2">🔑🔑 Two-Key (Asymmetric)</h4>
                    <p class="mb-2">Uses mathematically linked Public/Private key pair.</p>
                    <ul class="space-y-1 list-disc list-inside">
                        <li>RSA, DSA, ECDSA, Diffie-Hellman</li>
                    </ul>
                    <p class="mt-2 text-slate-400">Slower. Used for key exchange & digital signatures.</p>
                </div>
            </div>
            <div class="mt-4 p-3 bg-slate-800/40 rounded border border-slate-700 text-xs text-slate-300">
                <strong class="text-white">By Reversibility:</strong>
                <span class="ml-2 text-cyan-300">Reversible Algorithms</span> (Encryption/Decryption, allow data recovery) vs.
                <span class="ml-2 text-amber-300">Irreversible/One-Way Algorithms</span> (Hash functions, MACs — no decryption, used for integrity verification).
            </div>
        </div>

        <!-- Section: Hash Functions -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>#️⃣</span> 4. Cryptographic Hash Functions & PRNG
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <strong class="text-white block mb-2">Hash Functions:</strong>
                    <p class="mb-2">Takes a <strong>variable-length input</strong> (file, message) and produces a <strong>fixed-length hash/digest</strong>.</p>
                    <div class="p-2 bg-slate-800/60 rounded font-mono text-cyan-300 mb-2">
                        H(variable input) → fixed-size digest
                    </div>
                    <strong class="text-white block mb-1">Required Properties:</strong>
                    <ul class="space-y-1 list-disc list-inside">
                        <li><strong>One-Way (Pre-image resistance):</strong> Computationally infeasible to reverse.</li>
                        <li><strong>Collision-Free (Collision resistance):</strong> Infeasible for two different inputs to produce the same hash.</li>
                        <li><strong>Avalanche Effect:</strong> Even a 1-bit change in input dramatically alters the entire output hash.</li>
                    </ul>
                    <div class="mt-3 overflow-x-auto">
                        <table class="w-full border border-slate-700 text-[11px]">
                            <thead class="bg-slate-800"><tr><th class="p-1.5 border border-slate-700">Algorithm</th><th class="p-1.5 border border-slate-700">Output Size</th><th class="p-1.5 border border-slate-700">Status</th></tr></thead>
                            <tbody class="divide-y divide-slate-800">
                                <tr><td class="p-1.5 font-mono">MD5</td><td class="p-1.5">128-bit</td><td class="p-1.5 text-rose-400">Broken / Legacy Only</td></tr>
                                <tr><td class="p-1.5 font-mono">SHA-1</td><td class="p-1.5">160-bit</td><td class="p-1.5 text-amber-400">Deprecated / Weak</td></tr>
                                <tr><td class="p-1.5 font-mono">SHA-256</td><td class="p-1.5">256-bit</td><td class="p-1.5 text-emerald-400">Current Standard</td></tr>
                                <tr><td class="p-1.5 font-mono">SHA-384</td><td class="p-1.5">384-bit</td><td class="p-1.5 text-emerald-400">Current Standard</td></tr>
                                <tr><td class="p-1.5 font-mono">SHA-512</td><td class="p-1.5">512-bit</td><td class="p-1.5 text-emerald-400">Current Standard</td></tr>
                                <tr><td class="p-1.5 font-mono">SHA-3</td><td class="p-1.5">Variable</td><td class="p-1.5 text-emerald-400">Keccak Algorithm</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div>
                    <strong class="text-white block mb-2">PRNG vs. CSPRNG:</strong>
                    <p class="mb-2"><strong>PRNG</strong>: Pseudorandom Number Generator — produces deterministic sequences from an initial seed. Not suitable for cryptography alone.</p>
                    <p class="mb-2"><strong>CSPRNG</strong>: Cryptographically Secure PRNG — must meet additional security criteria:</p>
                    <ul class="space-y-1 list-disc list-inside mb-3">
                        <li><strong>Unpredictability:</strong> Future outputs cannot be predicted even knowing past outputs.</li>
                        <li><strong>Backtracking Resistance:</strong> Knowing the current state does not reveal past output states.</li>
                        <li><strong>Forward Security:</strong> Compromise of current state does not compromise future outputs.</li>
                    </ul>
                    <strong class="text-white block mb-2">HMAC:</strong>
                    <p class="mb-1"><strong class="text-cyan-300">HMAC (Hash-based MAC)</strong> combines a cryptographic hash function with a secret key to provide <em>both</em>:</p>
                    <ul class="list-disc list-inside">
                        <li>Data Integrity (message wasn't altered)</li>
                        <li>Origin Authentication (message is from key holder)</li>
                    </ul>
                    <div class="mt-2 p-2 bg-slate-800/60 rounded font-mono text-xs text-cyan-300">
                        HMAC(K, m) = H( (K ⊕ opad) || H((K ⊕ ipad) || m) )
                    </div>
                    <p class="mt-1 text-slate-400 text-[11px]">K = secret key, m = message. Prevents MITM tampering.</p>
                </div>
            </div>
        </div>

        <!-- Section: Symmetric Encryption -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🔄</span> 5. Symmetric Encryption: Block Ciphers & Stream Ciphers
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div class="p-4 bg-blue-950/20 border border-blue-800/40 rounded-lg">
                    <h4 class="text-blue-300 font-bold mb-2">Block Cipher</h4>
                    <p class="mb-2">Encrypts data in fixed-size blocks.</p>
                    <ul class="list-disc list-inside space-y-1">
                        <li>Block sizes: <strong>64-bit</strong> (DES/3DES), <strong>128-bit</strong> (AES)</li>
                        <li>AES key sizes: 128, 192, or 256 bits</li>
                        <li>DES key: 56-bit (obsolete — broken)</li>
                        <li>3DES: applies DES cipher 3× in sequence</li>
                    </ul>
                    <p class="mt-2 text-slate-400">Best for: Files, databases, disk encryption, stored data.</p>
                </div>
                <div class="p-4 bg-teal-950/20 border border-teal-800/40 rounded-lg">
                    <h4 class="text-teal-300 font-bold mb-2">Stream Cipher</h4>
                    <p class="mb-2">Encrypts data continuously one bit or byte at a time using a keystream (XOR operation).</p>
                    <ul class="list-disc list-inside space-y-1">
                        <li>Examples: <strong>RC4</strong> (deprecated), <strong>ChaCha20</strong> (modern), One-Time Pad (OTP)</li>
                        <li>Key operation: Plaintext ⊕ Keystream = Ciphertext</li>
                    </ul>
                    <p class="mt-2 text-slate-400">Best for: Real-time streaming data, VoIP, wireless comms.</p>
                </div>
            </div>
            <div class="mt-3 p-4 bg-amber-950/20 border border-amber-700/50 rounded-lg text-xs text-slate-300">
                <h4 class="text-amber-300 font-bold mb-2">One-Time Pad (OTP / Vernam Cipher) — Perfect Secrecy</h4>
                <p class="mb-1">Provides <strong>unconditional / information-theoretic security</strong> (perfect secrecy) when:</p>
                <ul class="list-disc list-inside space-y-1">
                    <li>The key is <strong>truly random</strong> (not pseudorandom)</li>
                    <li>The key is <strong>as long as or longer than</strong> the plaintext</li>
                    <li>The key is <strong>never reused</strong> (used only once)</li>
                    <li>The key is kept <strong>completely secret</strong></li>
                </ul>
                <p class="mt-2 text-slate-400"><strong>Practical Limitations:</strong> Key generation randomness is hard to guarantee; distribution and storage overhead is enormous at scale (key = message length).</p>
            </div>
        </div>

        <!-- Section: Asymmetric Encryption -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>🔑🔑</span> 6. Asymmetric Encryption: Public & Private Keys
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div class="p-4 bg-purple-950/20 border border-purple-800/40 rounded-lg">
                    <h4 class="text-purple-300 font-bold mb-2">For Confidentiality</h4>
                    <p class="mb-2 text-slate-400">Goal: Only the intended recipient can read the message.</p>
                    <div class="space-y-2">
                        <div class="p-2 bg-slate-800/60 rounded">
                            <span class="text-cyan-300">Encrypt with:</span> Recipient's <strong>Public Key</strong>
                        </div>
                        <div class="p-2 bg-slate-800/60 rounded">
                            <span class="text-emerald-300">Decrypt with:</span> Recipient's <strong>Private Key</strong>
                        </div>
                    </div>
                    <p class="mt-2 text-slate-400 text-[11px]">Only the private key holder (recipient) can decrypt what was encrypted with their public key.</p>
                </div>
                <div class="p-4 bg-rose-950/20 border border-rose-800/40 rounded-lg">
                    <h4 class="text-rose-300 font-bold mb-2">For Authentication (Digital Signature)</h4>
                    <p class="mb-2 text-slate-400">Goal: Prove who sent the message (non-repudiation).</p>
                    <div class="space-y-2">
                        <div class="p-2 bg-slate-800/60 rounded">
                            <span class="text-rose-300">Sign/Encrypt with:</span> Sender's <strong>Private Key</strong>
                        </div>
                        <div class="p-2 bg-slate-800/60 rounded">
                            <span class="text-amber-300">Verify/Decrypt with:</span> Sender's <strong>Public Key</strong>
                        </div>
                    </div>
                    <p class="mt-2 text-slate-400 text-[11px]">Only the private key holder (sender) can create a signature their public key successfully verifies.</p>
                </div>
            </div>
            <div class="mt-3 p-3 bg-slate-800/40 rounded border border-cyan-500/30 text-xs">
                <span class="text-cyan-300 font-bold">Golden Rule Summary Table:</span>
                <div class="overflow-x-auto mt-2">
                    <table class="w-full border border-slate-700 text-[11px]">
                        <thead class="bg-slate-800 text-slate-300">
                            <tr><th class="p-1.5 border border-slate-700">Goal</th><th class="p-1.5 border border-slate-700">Operation</th><th class="p-1.5 border border-slate-700">Key Used</th><th class="p-1.5 border border-slate-700">Whose Key?</th></tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800 text-slate-300">
                            <tr><td class="p-1.5">Confidentiality</td><td class="p-1.5">Encrypt</td><td class="p-1.5 text-cyan-300">Public Key</td><td class="p-1.5">Recipient's</td></tr>
                            <tr><td class="p-1.5">Confidentiality</td><td class="p-1.5">Decrypt</td><td class="p-1.5 text-cyan-300">Private Key</td><td class="p-1.5">Recipient's</td></tr>
                            <tr><td class="p-1.5">Authentication/Sig</td><td class="p-1.5">Sign (Encrypt)</td><td class="p-1.5 text-rose-300">Private Key</td><td class="p-1.5">Sender's</td></tr>
                            <tr><td class="p-1.5">Authentication/Sig</td><td class="p-1.5">Verify (Decrypt)</td><td class="p-1.5 text-rose-300">Public Key</td><td class="p-1.5">Sender's</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- Section: Attacks & Evaluation Criteria -->
        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800">
            <h3 class="text-xl font-bold text-cyan-400 mb-3 flex items-center gap-2">
                <span>⚡</span> 7. Attacks on Cryptography & Evaluation Criteria
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs text-slate-300">
                <div>
                    <strong class="text-white block mb-2">Attack Types:</strong>
                    <div class="space-y-2">
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-rose-300">Brute-Force Attack:</strong> Exhaustive trial-and-error search over the entire key space until the correct key is found.
                            <span class="block text-slate-400 mt-1">Countermeasure: Increase key length (doubling bits → exponential work increase).</span>
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <strong class="text-rose-300">Cryptanalysis Attack:</strong> Exploits mathematical patterns, structural weaknesses, or statistical biases in the cryptographic algorithm itself.
                            <span class="block text-slate-400 mt-1">Examples: Differential/linear cryptanalysis, birthday attacks, padding oracle attacks.</span>
                        </div>
                    </div>
                </div>
                <div>
                    <strong class="text-white block mb-2">Evaluation Criteria for Cryptographic Algorithms:</strong>
                    <div class="space-y-2">
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <span class="text-cyan-300 font-bold">1. Level of Security:</span> Upper bound of work required to defeat it; resistance to known attacks.
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <span class="text-cyan-300 font-bold">2. Functionality:</span> Does it effectively serve the intended security objective?
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <span class="text-cyan-300 font-bold">3. Performance:</span> Time, memory, computation, and storage efficiency.
                        </div>
                        <div class="p-2 bg-slate-800/50 rounded border border-slate-700">
                            <span class="text-cyan-300 font-bold">4. Ease of Implementation:</span> Complexity of deploying in both software and hardware environments.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,
    "memory_aids": [
        {"title": "Crypto vs Stego", "content": "Cryptography hides the MEANING (scrambles content). Steganography hides the EXISTENCE (hides the fact a message is there at all)."},
        {"title": "Hash Function Properties", "content": "One-Way (can't reverse), Collision-Free (no two inputs → same hash), Avalanche Effect (1 bit change → totally different hash)."},
        {"title": "Symmetric vs Asymmetric", "content": "Symmetric = 1 shared secret key, fast, great for bulk data (AES). Asymmetric = Public/Private key pair, slower, great for key exchange & signatures (RSA)."},
        {"title": "Asymmetric Key Rules", "content": "Encrypt with RECIPIENT's PUBLIC KEY. Sign with SENDER's PRIVATE KEY. Decrypt with RECIPIENT's PRIVATE KEY. Verify with SENDER's PUBLIC KEY."},
        {"title": "Block vs Stream Cipher", "content": "Block = processes chunks of fixed size (AES 128-bit blocks). Stream = encrypts 1 bit/byte at a time using XOR keystream (RC4, ChaCha20)."},
        {"title": "OTP Perfect Secrecy", "content": "One-Time Pad provides perfect secrecy when: key is truly random, as long as plaintext, used only once, and kept absolutely secret."},
        {"title": "HMAC provides", "content": "HMAC gives you BOTH Data Integrity (message unchanged) AND Origin Authentication (message came from key holder) in one operation."},
        {"title": "Hash Algorithms by Output Size", "content": "MD5=128bit(broken), SHA-1=160bit(deprecated), SHA-256=256bit(current), SHA-512=512bit(current), SHA-3=variable(Keccak)."}
    ],
    "mcqs": [
        {
            "id": 1,
            "q": "What is the fundamental difference between Cryptography and Steganography?",
            "options": [
                "Cryptography is used offline; Steganography is used online only.",
                "Cryptography hides the meaning of a message; Steganography hides the existence of a message.",
                "Cryptography uses images; Steganography uses text.",
                "Steganography is a form of encryption while Cryptography is decryption."
            ],
            "ans": "B",
            "explanation": "Cryptography transforms a message so its meaning is unreadable. Steganography hides the fact that a secret message even exists inside a carrier file."
        },
        {
            "id": 2,
            "q": "What is 'Cryptology'?",
            "options": [
                "A synonym for encryption algorithms only.",
                "The practice of hiding messages inside image metadata.",
                "The combined scientific study of both Cryptography and Cryptanalysis.",
                "A key management protocol used in TLS."
            ],
            "ans": "C",
            "explanation": "Cryptology is the broader umbrella discipline encompassing both Cryptography (protecting information) and Cryptanalysis (breaking cryptographic schemes)."
        },
        {
            "id": 3,
            "q": "Which of the four core security services provided by cryptography guarantees the sender cannot deny having transmitted a message?",
            "options": ["Data Integrity", "Origin Authentication", "Data Confidentiality", "Data Non-Repudiation"],
            "ans": "D",
            "explanation": "Data Non-repudiation ensures a sender cannot later deny transmitting a message, often enforced through digital signatures."
        },
        {
            "id": 4,
            "q": "Which cryptographic property describes the phenomenon where a single bit change in input produces a drastically different output hash?",
            "options": ["Pre-image resistance", "Collision resistance", "Avalanche Effect", "Key diffusion"],
            "ans": "C",
            "explanation": "The Avalanche Effect is a desired property where any small change to the input results in an unpredictably large and different output, preventing pattern analysis."
        },
        {
            "id": 5,
            "q": "What is the output (digest) size of the SHA-256 algorithm?",
            "options": ["128 bits", "160 bits", "256 bits", "512 bits"],
            "ans": "C",
            "explanation": "SHA-256 belongs to the SHA-2 family and produces a 256-bit (32-byte) fixed-length hash digest."
        },
        {
            "id": 6,
            "q": "Which hash algorithm is considered broken and should only be used for legacy / non-security purposes?",
            "options": ["SHA-512", "SHA-3", "SHA-256", "MD5"],
            "ans": "D",
            "explanation": "MD5 produces a 128-bit digest and has been considered cryptographically broken (collision attacks feasible) and unsuitable for security-critical applications."
        },
        {
            "id": 7,
            "q": "Which additional requirement distinguishes a CSPRNG from a standard PRNG?",
            "options": [
                "It must use only 32-bit seed values.",
                "It must provide unpredictability, backtracking resistance, and forward security.",
                "It must produce the same output given the same seed every time.",
                "It must be seeded exclusively with timestamps."
            ],
            "ans": "B",
            "explanation": "CSPRNGs require unpredictability (outputs cannot be predicted), backtracking resistance (past states cannot be derived), and forward security (future states safe even if current is compromised)."
        },
        {
            "id": 8,
            "q": "What security services does HMAC provide?",
            "options": [
                "Data Confidentiality only.",
                "Non-repudiation and Availability.",
                "Data Integrity and Origin Authentication simultaneously.",
                "Data Compression and Encryption."
            ],
            "ans": "C",
            "explanation": "HMAC combines a hash function with a shared secret key to provide both integrity (message wasn't altered) and origin authentication (sender holds the secret key)."
        },
        {
            "id": 9,
            "q": "In a block cipher system, what block size does AES (Advanced Encryption Standard) use?",
            "options": ["56 bits", "64 bits", "128 bits", "256 bits"],
            "ans": "C",
            "explanation": "AES always uses a fixed 128-bit block size, though the key may be 128, 192, or 256 bits."
        },
        {
            "id": 10,
            "q": "How does a stream cipher process data?",
            "options": [
                "In fixed-size 128-bit blocks with S-box substitutions.",
                "By encrypting data bit-by-bit or byte-by-byte using XOR with a generated keystream.",
                "By using public and private key pairs for each byte.",
                "By compressing data before applying a hash function."
            ],
            "ans": "B",
            "explanation": "Stream ciphers encrypt data continuously one bit or byte at a time by XOR-ing with a pseudorandom keystream generated from the key."
        },
        {
            "id": 11,
            "q": "What conditions must ALL be met for a One-Time Pad to achieve perfect (unconditional) secrecy?",
            "options": [
                "Key must be a 256-bit AES key, used for every session.",
                "Key must be truly random, at least as long as the plaintext, used only once, and kept completely secret.",
                "Key must be shared over a TLS-protected channel and stored hashed.",
                "Key must be a reusable passphrase derived from PBKDF2."
            ],
            "ans": "B",
            "explanation": "Perfect secrecy via OTP requires all four conditions: truly random key, key length ≥ message length, key used only once (never reused), and complete key secrecy."
        },
        {
            "id": 12,
            "q": "Alice wants to send Bob a confidential message. Using asymmetric encryption, what key does she use to encrypt?",
            "options": [
                "Alice's private key.",
                "Alice's public key.",
                "Bob's public key.",
                "Bob's private key."
            ],
            "ans": "C",
            "explanation": "For confidentiality, Alice encrypts with the RECIPIENT's public key (Bob's public key). Only Bob's private key can then decrypt it."
        },
        {
            "id": 13,
            "q": "To create a digital signature for authentication purposes, what key does the sender use?",
            "options": [
                "Receiver's public key.",
                "Receiver's private key.",
                "Sender's public key.",
                "Sender's private key."
            ],
            "ans": "D",
            "explanation": "Digital signatures are created with the SENDER's private key. Anyone with the sender's public key can verify it, proving the sender's identity."
        },
        {
            "id": 14,
            "q": "Which cryptographic algorithm type is best suited for encrypting large files or bulk data efficiently?",
            "options": [
                "Asymmetric algorithms like RSA.",
                "One-time pads.",
                "Symmetric algorithms like AES.",
                "Hash functions like SHA-512."
            ],
            "ans": "C",
            "explanation": "Symmetric algorithms are computationally faster than asymmetric ones, making them ideal for encrypting large volumes of data."
        },
        {
            "id": 15,
            "q": "What is the primary countermeasure against a brute-force cryptographic attack?",
            "options": [
                "Using a longer, complex password on the encryption tool.",
                "Switching to a stream cipher from a block cipher.",
                "Increasing the key length to exponentially expand the key search space.",
                "Storing the encrypted file in a hidden directory."
            ],
            "ans": "C",
            "explanation": "Brute force exhaustively searches the key space. Each additional bit doubles the search space, so increasing key length is the primary countermeasure."
        },
        {
            "id": 16,
            "q": "Which hash algorithm is part of the SHA-2 family and produces a 384-bit output?",
            "options": ["SHA-1", "SHA-256", "SHA-384", "SHA-3"],
            "ans": "C",
            "explanation": "SHA-384 is a member of the SHA-2 family producing a 384-bit (48-byte) digest. SHA-3 (Keccak) is an entirely separate algorithm."
        },
        {
            "id": 17,
            "q": "What type of cryptographic algorithm is used in HTTPS/TLS for symmetric session key exchange?",
            "options": [
                "Hash function only.",
                "Asymmetric algorithm (e.g., RSA or ECDH) for key exchange, then symmetric for bulk data encryption.",
                "Only symmetric block ciphers for everything.",
                "Stream ciphers for key exchange, block ciphers for data integrity."
            ],
            "ans": "B",
            "explanation": "TLS uses a hybrid approach: asymmetric cryptography (RSA, ECDH) to securely establish a shared symmetric session key, then symmetric encryption (AES) for fast data encryption."
        },
        {
            "id": 18,
            "q": "RC4 is an example of which type of encryption algorithm?",
            "options": ["Block cipher", "Asymmetric cipher", "Stream cipher", "Hash function"],
            "ans": "C",
            "explanation": "RC4 is a stream cipher that generates a keystream to XOR with plaintext. It has been deprecated due to known biases and vulnerabilities."
        },
        {
            "id": 19,
            "q": "What is the main practical limitation preventing widespread adoption of One-Time Pads (OTP)?",
            "options": [
                "They can only encrypt messages shorter than 64 characters.",
                "Modern computers can break OTP encryption in under 1 second.",
                "The key must be as long as the message and can never be reused, creating massive key distribution overhead.",
                "OTP is only compatible with symmetric key infrastructure."
            ],
            "ans": "C",
            "explanation": "The fundamental impracticality of OTP is that the key must be as long as the plaintext, used only once, and securely distributed — impossible to scale."
        },
        {
            "id": 20,
            "q": "According to the lecture, which is NOT a valid evaluation criterion for a cryptographic algorithm?",
            "options": [
                "Level of security (resistance to attacks).",
                "Performance (speed, memory, storage).",
                "Color of the user interface displaying encrypted data.",
                "Ease of implementation in hardware and software."
            ],
            "ans": "C",
            "explanation": "The four evaluation criteria are: Level of Security, Functionality, Performance, and Ease of Implementation. UI aesthetics are irrelevant."
        }
    ]
}

