# -*- coding: utf-8 -*-
"""
Builds the complete single-page CyberTutor portal in d:\\Tech\\Summariez\\index.html
"""
import json
import html
from data_lec1 import LEC1_DATA
from data_lec2 import LEC2_DATA
from data_lec3 import LEC3_DATA
from data_lec4 import LEC4_DATA
from data_lec5 import LEC5_DATA

LECTURES = [LEC1_DATA, LEC2_DATA, LEC3_DATA, LEC4_DATA, LEC5_DATA]

def generate_html():
    lectures_json = json.dumps(LECTURES, ensure_ascii=False)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberTutor — Cybersecurity Exam Coach & Memory Portal</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        cyber: {{
                            950: '#070b13',
                            900: '#0a0f1d',
                            800: '#11182c',
                            700: '#1b2545',
                            cyan: '#00f0ff',
                            rose: '#ff3366',
                            emerald: '#00ffaa',
                            amber: '#ffb703'
                        }}
                    }},
                    fontFamily: {{
                        mono: ['"JetBrains Mono"', 'monospace'],
                        sans: ['"Inter"', 'system-ui', 'sans-serif']
                    }}
                }}
            }}
        }}
    </script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #070b13;
            color: #e2e8f0;
        }}
        .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}
        /* Perspective for 3D flip card */
        .perspective-1000 {{
            perspective: 1000px;
        }}
        .transform-style-3d {{
            transform-style: preserve-3d;
        }}
        .backface-hidden {{
            backface-visibility: hidden;
            -webkit-backface-visibility: hidden;
        }}
        .rotate-y-180 {{
            transform: rotateY(180deg);
        }}
        .flipped {{
            transform: rotateY(180deg);
        }}
        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #0a0f1d;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #1e293b;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #0284c7;
        }}
        .glow-cyan {{
            box-shadow: 0 0 20px -3px rgba(0, 240, 255, 0.25);
        }}
        .glow-border-cyan {{
            border-color: rgba(0, 240, 255, 0.4);
            box-shadow: 0 0 15px -3px rgba(0, 240, 255, 0.15);
        }}
    </style>
</head>
<body class="bg-[#070b13] text-slate-200 min-h-screen flex flex-col antialiased selection:bg-cyan-500/30 selection:text-cyan-200">

    <!-- Top Sticky Header -->
    <header class="sticky top-0 z-50 bg-[#070b13]/90 backdrop-blur-md border-b border-slate-800/80">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Brand / Logo -->
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center font-bold text-white shadow-lg shadow-cyan-500/20 font-mono text-lg border border-cyan-400/40">
                        🛡️
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="font-bold text-lg tracking-tight text-white font-mono">Cyber<span class="text-cyan-400">Tutor</span></span>
                            <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-cyan-950/80 border border-cyan-500/40 text-cyan-300">Exam Coach</span>
                        </div>
                        <p class="text-[11px] text-slate-400 hidden sm:block">Ain Shams University · Dr. Alshaimaa Abo-alian</p>
                    </div>
                </div>

                <!-- Lecture Selector Navigation -->
                <nav class="hidden md:flex items-center gap-1.5 bg-slate-900/90 p-1 rounded-xl border border-slate-800" id="lectureNav">
                    <button onclick="switchLecture(0)" id="nav-btn-0" class="lec-nav-btn px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all duration-200 bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 shadow-sm">
                        L1: Intro
                    </button>
                    <button onclick="switchLecture(1)" id="nav-btn-1" class="lec-nav-btn px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all duration-200 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
                        L2: Threats
                    </button>
                    <button onclick="switchLecture(2)" id="nav-btn-2" class="lec-nav-btn px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all duration-200 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
                        L3: Crypto
                    </button>
                    <button onclick="switchLecture(3)" id="nav-btn-3" class="lec-nav-btn px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all duration-200 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
                        L4: Auth
                    </button>
                    <button onclick="switchLecture(4)" id="nav-btn-4" class="lec-nav-btn px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all duration-200 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent">
                        L5: Access
                    </button>
                </nav>

                <!-- Search and Stats Badge -->
                <div class="flex items-center gap-3">
                    <div class="relative hidden lg:block w-48 xl:w-60">
                        <input type="text" id="globalSearch" placeholder="Search concept (e.g. BLP, FAR, CVE)..." 
                            class="w-full bg-slate-900 border border-slate-700/80 rounded-lg px-3 py-1.5 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500/50 font-mono"
                            oninput="handleSearch(this.value)">
                        <span class="absolute right-2.5 top-2 text-slate-500 text-xs">🔍</span>
                    </div>
                    <div class="px-2.5 py-1 bg-slate-900 rounded-lg border border-slate-800 text-[11px] font-mono text-cyan-400 hidden sm:flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        <span>100 MCQs Total</span>
                    </div>
                </div>
            </div>

            <!-- Mobile lecture scroll bar -->
            <div class="flex md:hidden overflow-x-auto py-2 gap-2 border-t border-slate-800/60 -mx-4 px-4 scrollbar-none" id="mobileLectureNav">
                <button onclick="switchLecture(0)" id="m-nav-btn-0" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">L1: Intro</button>
                <button onclick="switchLecture(1)" id="m-nav-btn-1" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800">L2: Threats</button>
                <button onclick="switchLecture(2)" id="m-nav-btn-2" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800">L3: Crypto</button>
                <button onclick="switchLecture(3)" id="m-nav-btn-3" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800">L4: Auth</button>
                <button onclick="switchLecture(4)" id="m-nav-btn-4" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800">L5: Access</button>
            </div>
        </div>
    </header>

    <!-- Hero / Course Banner -->
    <div class="relative bg-gradient-to-b from-[#0a0f1d] to-[#070b13] border-b border-slate-800/80 py-8 px-4 sm:px-6 lg:px-8">
        <div class="max-w-7xl mx-auto">
            <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
                <div>
                    <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full bg-cyan-950/60 border border-cyan-500/40 text-cyan-300 text-xs font-mono mb-3">
                        <span>🎓 Ain Shams University</span>
                        <span>•</span>
                        <span>Faculty of Computers & Information Sciences</span>
                    </div>
                    <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold tracking-tight text-white mb-2">
                        Cybersecurity <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-indigo-400">Mastery & Exam Coach</span>
                    </h1>
                    <p class="text-slate-400 text-sm max-w-3xl leading-relaxed">
                        Complete university lecture guides, fast-track memory aids, and 100 high-yield multiple-choice questions (20 per lecture) based strictly on Dr. Alshaimaa Abo-alian's curriculum.
                    </p>
                </div>
                <!-- Quick Exam Metrics Cards -->
                <div class="grid grid-cols-3 gap-2.5 text-center shrink-0">
                    <div class="p-3 bg-slate-900/80 border border-slate-800 rounded-xl">
                        <div class="text-xl font-bold font-mono text-cyan-400">5</div>
                        <div class="text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">Lectures</div>
                    </div>
                    <div class="p-3 bg-slate-900/80 border border-slate-800 rounded-xl">
                        <div class="text-xl font-bold font-mono text-emerald-400">100</div>
                        <div class="text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">MCQ Tests</div>
                    </div>
                    <div class="p-3 bg-slate-900/80 border border-slate-800 rounded-xl">
                        <div class="text-xl font-bold font-mono text-amber-400">40+</div>
                        <div class="text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">Flashcards</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        <!-- Current Lecture Header Card -->
        <div class="mb-6 p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-slate-900/90 to-[#0c1527] border border-slate-800 glow-border-cyan relative overflow-hidden">
            <div class="absolute right-0 top-0 bottom-0 w-1/3 bg-gradient-to-l from-cyan-500/5 to-transparent pointer-events-none"></div>
            
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div>
                    <span id="currentLecBadge" class="inline-block px-3 py-1 rounded-md bg-cyan-950/80 border border-cyan-500/50 text-cyan-300 font-mono text-xs font-semibold mb-2">
                        L1: Foundations & Core Concepts
                    </span>
                    <h2 id="currentLecTitle" class="text-2xl sm:text-3xl font-bold text-white tracking-tight">
                        Lecture 1: Introduction to Cybersecurity
                    </h2>
                    <p id="currentLecMeta" class="text-xs text-slate-400 font-mono mt-1">
                        Instructor: Dr. Alshaimaa Abo-alian · Ain Shams University
                    </p>
                </div>

                <!-- Lecture Content Switcher Tabs (Summary / Memory / Quiz) -->
                <div class="flex items-center gap-1.5 p-1.5 bg-slate-950/80 border border-slate-800 rounded-xl shrink-0">
                    <button onclick="switchTab('summary')" id="tab-btn-summary" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold transition-all duration-200 bg-cyan-500 text-slate-950 shadow-md">
                        📖 Summary
                    </button>
                    <button onclick="switchTab('memory')" id="tab-btn-memory" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold transition-all duration-200 text-slate-300 hover:text-white hover:bg-slate-800">
                        🧠 Memory Aids
                    </button>
                    <button onclick="switchTab('mcq')" id="tab-btn-mcq" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold transition-all duration-200 text-slate-300 hover:text-white hover:bg-slate-800 flex items-center gap-1.5">
                        <span>🎯 Quiz</span>
                        <span class="px-1.5 py-0.2 bg-cyan-950 text-cyan-300 border border-cyan-600/40 rounded text-[10px] font-mono">20 Qs</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- TAB 1: SIMPLIFIED SUMMARY -->
        <section id="panel-summary" class="tab-panel">
            <div id="summaryContainer">
                <!-- Dynamically injected summary HTML -->
            </div>
        </section>

        <!-- TAB 2: MEMORY & MEMORIZATION AIDS -->
        <section id="panel-memory" class="tab-panel hidden space-y-6">
            <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
                <div>
                    <h3 class="text-lg font-bold text-cyan-400 flex items-center gap-2">
                        <span>⚡</span> Fast-Recall Flashcards
                    </h3>
                    <p class="text-xs text-slate-400">Click any card to flip and reveal the golden rule / core definition.</p>
                </div>
                <button onclick="flipAllCards()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-mono text-cyan-300 border border-slate-700">
                    🔄 Flip All
                </button>
            </div>

            <!-- Flashcards Grid -->
            <div id="flashcardsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <!-- Injected via JavaScript -->
            </div>
        </section>

        <!-- TAB 3: MULTIPLE CHOICE QUESTIONS (MCQ QUIZ) -->
        <section id="panel-mcq" class="tab-panel hidden space-y-6">
            <!-- Quiz Controls Header -->
            <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <div class="flex items-center gap-2">
                        <h3 class="text-xl font-bold text-cyan-400">20 High-Yield Exam MCQs</h3>
                        <span id="quizScoreBadge" class="hidden px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-emerald-950 text-emerald-400 border border-emerald-600/50">
                            Score: 0/20
                        </span>
                    </div>
                    <p class="text-xs text-slate-400 mt-1">Select your answers below and click "Grade Quiz" to view detailed explanations.</p>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="gradeCurrentQuiz()" class="px-5 py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 font-bold text-slate-950 text-xs font-mono transition-all shadow-lg shadow-cyan-500/20">
                        ⚡ Grade Quiz & Show Explanations
                    </button>
                    <button onclick="resetCurrentQuiz()" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 font-semibold text-slate-300 text-xs font-mono border border-slate-700">
                        Reset
                    </button>
                </div>
            </div>

            <!-- Questions Container -->
            <div id="questionsContainer" class="space-y-4">
                <!-- 20 Question Cards Injected via JS -->
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="mt-16 border-t border-slate-800/80 bg-slate-950/80 py-8 px-4 sm:px-6 lg:px-8 text-xs text-slate-400">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-2">
                <span class="font-mono text-cyan-400 font-bold">CyberTutor Portal</span>
                <span>•</span>
                <span>Faculty of Computers & Information Sciences, Ain Shams University</span>
            </div>
            <div>
                Lectures by <strong class="text-slate-300">Dr. Alshaimaa Abo-alian</strong>
            </div>
        </div>
    </footer>

    <!-- INLINE APPLICATION LOGIC -->
    <script>
        const LECTURES_DATA = {lectures_json};
        
        let currentLecIndex = 0;
        let currentTab = 'summary';
        let userAnswers = {{}}; // format: {{ "lecIndex_qIndex": "A" }}
        let quizGraded = {{}}; // format: {{ "lecIndex": true/false }}

        // Switch active lecture
        function switchLecture(index) {{
            currentLecIndex = index;
            const lec = LECTURES_DATA[index];

            // Update Header
            document.getElementById('currentLecBadge').innerText = lec.badge;
            document.getElementById('currentLecTitle').innerText = `Lecture ${{lec.number}}: ${{lec.title}}`;
            document.getElementById('currentLecMeta').innerText = `Instructor: ${{lec.instructor}} · ${{lec.faculty}}`;

            // Update Nav Buttons desktop & mobile
            for (let i = 0; i < 5; i++) {{
                const btn = document.getElementById(`nav-btn-${{i}}`);
                const mBtn = document.getElementById(`m-nav-btn-${{i}}`);
                if (i === index) {{
                    btn.className = "lec-nav-btn px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all duration-200 bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 shadow-sm";
                    if (mBtn) mBtn.className = "m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/40";
                }} else {{
                    btn.className = "lec-nav-btn px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all duration-200 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent";
                    if (mBtn) mBtn.className = "m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800";
                }}
            }}

            // Render Content
            renderSummary();
            renderFlashcards();
            renderMCQs();
            updateQuizBadge();

            // Scroll top slightly
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        // Switch active tab (summary, memory, mcq)
        function switchTab(tabId) {{
            currentTab = tabId;
            const tabs = ['summary', 'memory', 'mcq'];
            tabs.forEach(t => {{
                const panel = document.getElementById(`panel-${{t}}`);
                const btn = document.getElementById(`tab-btn-${{t}}`);
                if (t === tabId) {{
                    panel.classList.remove('hidden');
                    btn.className = "tab-btn px-4 py-2 rounded-lg text-xs font-semibold transition-all duration-200 bg-cyan-500 text-slate-950 shadow-md";
                }} else {{
                    panel.classList.add('hidden');
                    btn.className = "tab-btn px-4 py-2 rounded-lg text-xs font-semibold transition-all duration-200 text-slate-300 hover:text-white hover:bg-slate-800";
                }}
            }});
        }}

        // Render Summary
        function renderSummary() {{
            const lec = LECTURES_DATA[currentLecIndex];
            document.getElementById('summaryContainer').innerHTML = lec.summary_html;
        }}

        // Render Flashcards
        function renderFlashcards() {{
            const lec = LECTURES_DATA[currentLecIndex];
            const container = document.getElementById('flashcardsGrid');
            container.innerHTML = '';

            lec.memory_aids.forEach((aid, idx) => {{
                const card = document.createElement('div');
                card.className = "perspective-1000 h-52 cursor-pointer select-none group";
                card.onclick = () => toggleCardFlip(card);

                card.innerHTML = `
                    <div class="card-inner relative w-full h-full duration-500 transform-style-3d rounded-xl transition-transform border border-slate-800 group-hover:border-cyan-500/50">
                        <!-- Front -->
                        <div class="absolute inset-0 w-full h-full bg-slate-900/90 rounded-xl p-5 flex flex-col justify-between backface-hidden border border-slate-800">
                            <div>
                                <span class="text-[10px] font-mono text-cyan-400 uppercase tracking-widest block mb-2">Rule #${{idx + 1}}</span>
                                <h4 class="text-sm font-bold text-white group-hover:text-cyan-300 transition-colors">${{aid.title}}</h4>
                            </div>
                            <div class="text-[11px] text-slate-500 font-mono flex items-center justify-between">
                                <span>Click to flip</span>
                                <span>↻</span>
                            </div>
                        </div>
                        <!-- Back -->
                        <div class="absolute inset-0 w-full h-full bg-[#0d162a] rounded-xl p-5 flex flex-col justify-between rotate-y-180 backface-hidden border border-cyan-500/40 glow-border-cyan">
                            <div>
                                <span class="text-[10px] font-mono text-emerald-400 uppercase tracking-widest block mb-1">Key Definition</span>
                                <p class="text-xs text-slate-200 leading-relaxed">${{aid.content}}</p>
                            </div>
                            <div class="text-[10px] text-slate-500 font-mono text-right">Click to flip back</div>
                        </div>
                    </div>
                `;
                container.appendChild(card);
            }});
        }}

        function toggleCardFlip(card) {{
            const inner = card.querySelector('.card-inner');
            inner.classList.toggle('flipped');
        }}

        function flipAllCards() {{
            const cards = document.querySelectorAll('.card-inner');
            cards.forEach(c => c.classList.toggle('flipped'));
        }}

        // Render MCQs
        function renderMCQs() {{
            const lec = LECTURES_DATA[currentLecIndex];
            const container = document.getElementById('questionsContainer');
            container.innerHTML = '';

            const isGraded = quizGraded[currentLecIndex] || false;

            lec.mcqs.forEach((mcq, qIdx) => {{
                const qKey = `${{currentLecIndex}}_${{qIdx}}`;
                const selectedAns = userAnswers[qKey];
                const isCorrect = selectedAns === mcq.ans;

                let cardBorder = "border-slate-800";
                if (isGraded) {{
                    cardBorder = isCorrect ? "border-emerald-500/50 bg-emerald-950/10" : "border-rose-500/50 bg-rose-950/10";
                }}

                const qCard = document.createElement('div');
                qCard.className = `p-5 rounded-xl bg-slate-900/80 border ${{cardBorder}} transition-all`;

                let optionsHtml = '';
                const letters = ['A', 'B', 'C', 'D'];
                mcq.options.forEach((opt, optIdx) => {{
                    const letter = letters[optIdx];
                    const isChecked = selectedAns === letter;
                    
                    let optStyle = "border-slate-800 hover:border-slate-700 bg-slate-800/40 text-slate-300";
                    if (isChecked) {{
                        optStyle = "border-cyan-500 bg-cyan-950/30 text-white font-medium";
                    }}
                    if (isGraded) {{
                        if (letter === mcq.ans) {{
                            optStyle = "border-emerald-500 bg-emerald-950/40 text-emerald-200 font-semibold";
                        }} else if (isChecked && letter !== mcq.ans) {{
                            optStyle = "border-rose-500 bg-rose-950/40 text-rose-200";
                        }}
                    }}

                    optionsHtml += `
                        <label class="flex items-center gap-3 p-3 rounded-lg border ${{optStyle}} cursor-pointer transition-all text-xs">
                            <input type="radio" name="q_${{currentLecIndex}}_${{qIdx}}" value="${{letter}}" 
                                ${{isChecked ? 'checked' : ''}} 
                                onchange="selectAnswer(${{currentLecIndex}}, ${{qIdx}}, '${{letter}}')" 
                                class="w-4 h-4 text-cyan-500 bg-slate-800 border-slate-700 focus:ring-cyan-500 focus:ring-1">
                            <span class="font-mono font-bold text-slate-400">${{letter}}.</span>
                            <span class="flex-1">${{opt}}</span>
                        </label>
                    `;
                }});

                let explanationHtml = '';
                if (isGraded) {{
                    explanationHtml = `
                        <div class="mt-4 p-3 rounded-lg bg-slate-950 border border-slate-800 text-xs">
                            <div class="flex items-center gap-2 mb-1">
                                <span class="font-mono font-bold ${{isCorrect ? 'text-emerald-400' : 'text-rose-400'}}">
                                    ${{isCorrect ? '✅ Correct' : '❌ Incorrect (Correct: ' + mcq.ans + ')'}}
                                </span>
                            </div>
                            <p class="text-slate-300 leading-relaxed">${{mcq.explanation}}</p>
                        </div>
                    `;
                }}

                qCard.innerHTML = `
                    <div class="flex items-start justify-between gap-4 mb-3">
                        <div class="flex items-center gap-2">
                            <span class="w-6 h-6 rounded bg-slate-800 border border-slate-700 font-mono text-xs flex items-center justify-center font-bold text-cyan-400">
                                ${{mcq.id}}
                            </span>
                            <h4 class="text-sm font-semibold text-slate-100">${{mcq.q}}</h4>
                        </div>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-2">
                        ${{optionsHtml}}
                    </div>
                    ${{explanationHtml}}
                `;

                container.appendChild(qCard);
            }});
        }}

        function selectAnswer(lecIdx, qIdx, answer) {{
            userAnswers[`${{lecIdx}}_${{qIdx}}`] = answer;
        }}

        function gradeCurrentQuiz() {{
            quizGraded[currentLecIndex] = true;
            renderMCQs();
            updateQuizBadge();
        }}

        function resetCurrentQuiz() {{
            const lec = LECTURES_DATA[currentLecIndex];
            lec.mcqs.forEach((_, qIdx) => {{
                delete userAnswers[`${{currentLecIndex}}_${{qIdx}}`];
            }});
            quizGraded[currentLecIndex] = false;
            renderMCQs();
            updateQuizBadge();
        }}

        function updateQuizBadge() {{
            const badge = document.getElementById('quizScoreBadge');
            if (quizGraded[currentLecIndex]) {{
                const lec = LECTURES_DATA[currentLecIndex];
                let score = 0;
                lec.mcqs.forEach((mcq, qIdx) => {{
                    if (userAnswers[`${{currentLecIndex}}_${{qIdx}}`] === mcq.ans) {{
                        score++;
                    }}
                }});
                badge.innerText = `Score: ${{score}} / 20 (${{Math.round(score/20*100)}}%)`;
                badge.classList.remove('hidden');
            }} else {{
                badge.classList.add('hidden');
            }}
        }}

        // Quick Search Filter across summary and MCQs
        function handleSearch(term) {{
            term = term.toLowerCase().trim();
            if (!term) return;

            // Search in which lecture it appears most
            for (let i = 0; i < LECTURES_DATA.length; i++) {{
                const lec = LECTURES_DATA[i];
                const content = (lec.title + " " + lec.summary_html).toLowerCase();
                if (content.includes(term)) {{
                    if (currentLecIndex !== i) {{
                        switchLecture(i);
                    }}
                    break;
                }}
            }}
        }}

        // Initialize on load
        window.addEventListener('DOMContentLoaded', () => {{
            switchLecture(0);
        }});
    </script>
</body>
</html>
"""
    with open("d:\\Tech\\Summariez\\index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Successfully created d:\\Tech\\Summariez\\index.html")

if __name__ == "__main__":
    generate_html()
