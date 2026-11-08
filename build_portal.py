# -*- coding: utf-8 -*-
"""
Builds the complete single-page CyberTutor portal in d:\\Tech\\Summariez\\index.html
Features:
- Instant feedback on every question selection across all lectures
- Dedicated "🎲 All-Lectures Simulator (100 Qs Shuffled)" mode with randomizer & filters
- Dedicated "📝 Solved Previous Exams" tab with step-by-step solutions for:
    * Math: 62^8 SHA-256 Precomputed Hash Table Storage (8.73 Petabytes) & Rainbow Tables
    * Database DAC Access Control Matrix, ACLs, and SQL DCL statements
    * University File System Access Control & Bell-LaPadula (BLP) MAC Multi-Level Table
    * 10 Official Exam MCQs with instant evaluation & distractor breakdowns
- Senior UI/UX overhaul: sticky live HUD, 100-question jump matrix, flashcard mastery tracking, dark cyber theme.
"""
import json
import html
from data_lec1 import LEC1_DATA
from data_lec2 import LEC2_DATA
from data_lec3 import LEC3_DATA
from data_lec4 import LEC4_DATA
from data_lec5 import LEC5_DATA
from data_previous_exams import EXAM_MCQS, generate_exams_html

LECTURES = [LEC1_DATA, LEC2_DATA, LEC3_DATA, LEC4_DATA, LEC5_DATA]

def generate_html():
    lectures_json = json.dumps(LECTURES, ensure_ascii=False)
    exam_mcqs_json = json.dumps(EXAM_MCQS, ensure_ascii=False)
    exams_sections_html = generate_exams_html()
    
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
                            950: '#050811',
                            900: '#090f1f',
                            850: '#0d152b',
                            800: '#121d3a',
                            750: '#182548',
                            700: '#1e2e58',
                            cyan: '#00f0ff',
                            rose: '#ff3366',
                            emerald: '#00ffaa',
                            amber: '#ffb703',
                            indigo: '#818cf8',
                            purple: '#a855f7'
                        }}
                    }},
                    fontFamily: {{
                        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
                        sans: ['"Inter"', 'system-ui', 'sans-serif']
                    }},
                    animation: {{
                        'pulse-glow': 'pulseGlow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                        'slide-down': 'slideDown 0.25s ease-out forwards',
                        'pop-in': 'popIn 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards',
                    }},
                    keyframes: {{
                        pulseGlow: {{
                            '0%, 100%': {{ opacity: '1', filter: 'drop-shadow(0 0 12px rgba(0,240,255,0.4))' }},
                            '50%': {{ opacity: '.7', filter: 'drop-shadow(0 0 4px rgba(0,240,255,0.15))' }},
                        }},
                        slideDown: {{
                            '0%': {{ opacity: '0', transform: 'translateY(-8px)' }},
                            '100%': {{ opacity: '1', transform: 'translateY(0)' }},
                        }},
                        popIn: {{
                            '0%': {{ opacity: '0', transform: 'scale(0.96)' }},
                            '100%': {{ opacity: '1', transform: 'scale(1)' }},
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            color-scheme: dark;
        }}
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #050811;
            color: #e2e8f0;
            overflow-x: hidden;
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
        /* Cyber glow & border utilities */
        .glow-cyan {{
            box-shadow: 0 0 25px -4px rgba(0, 240, 255, 0.28);
        }}
        .glow-purple {{
            box-shadow: 0 0 25px -4px rgba(168, 85, 247, 0.3);
        }}
        .glow-emerald {{
            box-shadow: 0 0 20px -3px rgba(0, 255, 170, 0.25);
        }}
        .glow-border-cyan {{
            border-color: rgba(0, 240, 255, 0.45);
            box-shadow: 0 0 15px -3px rgba(0, 240, 255, 0.2);
        }}
        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 7px;
            height: 7px;
        }}
        ::-webkit-scrollbar-track {{
            background: #090f1f;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #1e293b;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #0ea5e9;
        }}
        /* Option radio styling */
        .option-card {{
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .option-card:hover:not(.locked) {{
            transform: translateY(-1px);
        }}
        /* Floating HUD animation */
        #floatingHUD {{
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
        }}
        /* Print styles */
        @media print {{
            header, #floatingHUD, .lec-nav-btn, .tab-btn, button {{
                display: none !important;
            }}
            body {{
                background: white !important;
                color: black !important;
            }}
            .tab-panel {{
                display: block !important;
            }}
        }}
    </style>
</head>
<body class="bg-[#050811] text-slate-200 min-h-screen flex flex-col antialiased selection:bg-cyan-500/30 selection:text-cyan-200">

    <!-- Top Sticky Header -->
    <header class="sticky top-0 z-50 bg-[#050811]/90 backdrop-blur-xl border-b border-slate-800/80 shadow-lg shadow-black/40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Brand / Logo -->
                <div class="flex items-center gap-3 cursor-pointer" onclick="switchLecture(0)">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 via-blue-600 to-indigo-600 flex items-center justify-center font-bold text-white shadow-lg shadow-cyan-500/25 font-mono text-lg border border-cyan-300/40 transform hover:scale-105 transition-transform">
                        🛡️
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="font-extrabold text-lg tracking-tight text-white font-mono">Cyber<span class="text-cyan-400">Tutor</span></span>
                            <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-cyan-950/90 border border-cyan-500/50 text-cyan-300">Exam Coach</span>
                        </div>
                        <p class="text-[11px] text-slate-400 hidden sm:block">Ain Shams University · Dr. Alshaimaa Abo-alian</p>
                    </div>
                </div>

                <!-- Navigation Tabs (5 Lectures + 100Q Simulator + Solved Past Exams) -->
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
                    
                    <!-- SPECIAL SHUFFLE SIMULATOR TAB -->
                    <button onclick="switchToSimulator()" id="nav-btn-sim" class="lec-nav-btn relative px-3 py-1.5 rounded-lg text-xs font-mono font-semibold transition-all duration-200 text-purple-300 hover:text-white bg-purple-950/40 hover:bg-purple-900/60 border border-purple-500/40 flex items-center gap-1.5 ml-1">
                        <span class="inline-block animate-spin" style="animation-duration: 6s;">🎲</span>
                        <span>100Q Simulator</span>
                        <span class="w-1.5 h-1.5 rounded-full bg-purple-400 animate-pulse"></span>
                    </button>

                    <!-- SPECIAL PREVIOUS EXAMS SOLVED TAB -->
                    <button onclick="switchToExams()" id="nav-btn-exams" class="lec-nav-btn relative px-3 py-1.5 rounded-lg text-xs font-mono font-semibold transition-all duration-200 text-emerald-300 hover:text-white bg-emerald-950/40 hover:bg-emerald-900/60 border border-emerald-500/40 flex items-center gap-1.5 ml-1">
                        <span>📝</span>
                        <span>Solved Exams</span>
                        <span class="px-1.5 py-0.2 rounded bg-emerald-500 text-slate-950 text-[10px] font-bold">NEW</span>
                    </button>
                </nav>

                <!-- Search and Live Global Score -->
                <div class="flex items-center gap-3">
                    <div class="relative hidden lg:block w-48 xl:w-56">
                        <input type="text" id="globalSearch" placeholder="Search (BLP, FAR, CVE)..." 
                            class="w-full bg-slate-900/90 border border-slate-700/80 rounded-lg pl-3 pr-8 py-1.5 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500/50 font-mono"
                            oninput="handleSearch(this.value)">
                        <span class="absolute right-2.5 top-2 text-slate-500 text-xs">🔍</span>
                    </div>

                    <!-- Live Overall Answered Counter -->
                    <div id="headerOverallStats" class="px-3 py-1 bg-slate-900/90 rounded-lg border border-slate-800 text-[11px] font-mono flex items-center gap-2 cursor-pointer" onclick="switchToSimulator()" title="Click to view full exam simulator">
                        <span class="flex items-center gap-1 text-emerald-400 font-bold" id="headerScoreLive">
                            <span>⚡</span> <span id="headerCorrectCount">0</span>/100
                        </span>
                        <span class="text-slate-500">|</span>
                        <span class="text-cyan-400 font-medium" id="headerAccuracyLive">0% Acc</span>
                    </div>
                </div>
            </div>

            <!-- Mobile lecture scroll bar -->
            <div class="flex md:hidden overflow-x-auto py-2.5 gap-2 border-t border-slate-800/60 -mx-4 px-4 scrollbar-none" id="mobileLectureNav">
                <button onclick="switchLecture(0)" id="m-nav-btn-0" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">L1: Intro</button>
                <button onclick="switchLecture(1)" id="m-nav-btn-1" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800">L2: Threats</button>
                <button onclick="switchLecture(2)" id="m-nav-btn-2" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800">L3: Crypto</button>
                <button onclick="switchLecture(3)" id="m-nav-btn-3" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800">L4: Auth</button>
                <button onclick="switchLecture(4)" id="m-nav-btn-4" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800">L5: Access</button>
                <button onclick="switchToSimulator()" id="m-nav-btn-sim" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-purple-950/60 text-purple-300 border border-purple-500/40 font-semibold">🎲 100Q Exam</button>
                <button onclick="switchToExams()" id="m-nav-btn-exams" class="m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-emerald-950/60 text-emerald-300 border border-emerald-500/40 font-semibold">📝 Solved Exams</button>
            </div>
        </div>
    </header>

    <!-- Hero / Course Banner -->
    <div class="relative bg-gradient-to-b from-[#090f1f] via-[#070c1a] to-[#050811] border-b border-slate-800/80 py-7 px-4 sm:px-6 lg:px-8 overflow-hidden">
        <div class="absolute -right-20 -top-20 w-80 h-80 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute -left-20 -bottom-20 w-80 h-80 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="max-w-7xl mx-auto relative z-10">
            <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
                <div>
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950/70 border border-cyan-500/40 text-cyan-300 text-xs font-mono mb-2.5">
                        <span class="w-2 h-2 rounded-full bg-cyan-400 animate-ping"></span>
                        <span>🎓 Ain Shams University · Faculty of Computers & Information Sciences</span>
                    </div>
                    <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold tracking-tight text-white mb-2">
                        Cybersecurity <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-indigo-400">Mastery & Exam Coach</span>
                    </h1>
                    <p class="text-slate-400 text-xs sm:text-sm max-w-3xl leading-relaxed">
                        Complete curriculum guides, high-speed flashcards, 100 rigorous MCQs, and <strong class="text-emerald-400">official solved past papers</strong> based strictly on Dr. Alshaimaa Abo-alian & Prof. Walaa Khaled's exams.
                    </p>
                </div>

                <!-- Quick Exam Metrics Cards -->
                <div class="grid grid-cols-4 gap-2 text-center shrink-0">
                    <div class="p-2.5 sm:p-3 bg-slate-900/80 border border-slate-800 rounded-xl hover:border-cyan-500/40 transition-colors">
                        <div class="text-lg sm:text-xl font-bold font-mono text-cyan-400">5</div>
                        <div class="text-[9px] sm:text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">Lectures</div>
                    </div>
                    <div class="p-2.5 sm:p-3 bg-slate-900/80 border border-slate-800 rounded-xl hover:border-emerald-500/40 transition-colors">
                        <div class="text-lg sm:text-xl font-bold font-mono text-emerald-400">110</div>
                        <div class="text-[9px] sm:text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">Total MCQs</div>
                    </div>
                    <div class="p-2.5 sm:p-3 bg-slate-900/80 border border-slate-800 rounded-xl hover:border-purple-500/40 transition-colors">
                        <div class="text-lg sm:text-xl font-bold font-mono text-purple-400" id="heroStreakDisplay">🔥 0</div>
                        <div class="text-[9px] sm:text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">Best Streak</div>
                    </div>
                    <div class="p-2.5 sm:p-3 bg-slate-900/80 border border-slate-800 rounded-xl hover:border-amber-500/40 transition-colors">
                        <div class="text-lg sm:text-xl font-bold font-mono text-amber-400" id="heroMasteredCount">0/42</div>
                        <div class="text-[9px] sm:text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">Mastered</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-7">

        <!-- ========================================== -->
        <!-- VIEW 1: INDIVIDUAL LECTURE MODE (L1 - L5)  -->
        <!-- ========================================== -->
        <div id="view-lecture" class="space-y-6">
            
            <!-- Current Lecture Header Card -->
            <div class="p-5 sm:p-6 rounded-2xl bg-gradient-to-r from-slate-900 via-slate-900/90 to-[#0d162d] border border-slate-800 glow-border-cyan relative overflow-hidden">
                <div class="absolute right-0 top-0 bottom-0 w-1/3 bg-gradient-to-l from-cyan-500/10 to-transparent pointer-events-none"></div>
                
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-5 relative z-10">
                    <div>
                        <span id="currentLecBadge" class="inline-block px-3 py-1 rounded-md bg-cyan-950/80 border border-cyan-500/50 text-cyan-300 font-mono text-xs font-semibold mb-2">
                            L1: Foundations & Core Concepts
                        </span>
                        <h2 id="currentLecTitle" class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                            Lecture 1: Introduction to Cybersecurity
                        </h2>
                        <p id="currentLecMeta" class="text-xs text-slate-400 font-mono mt-1">
                            Instructor: Dr. Alshaimaa Abo-alian · Ain Shams University
                        </p>
                    </div>

                    <!-- Lecture Content Switcher Tabs (Summary / Memory / Quiz) -->
                    <div class="flex items-center gap-1.5 p-1.5 bg-slate-950/80 border border-slate-800 rounded-xl shrink-0 self-start md:self-auto">
                        <button onclick="switchTab('summary')" id="tab-btn-summary" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold transition-all duration-200 bg-cyan-500 text-slate-950 shadow-md">
                            📖 Summary
                        </button>
                        <button onclick="switchTab('memory')" id="tab-btn-memory" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold transition-all duration-200 text-slate-300 hover:text-white hover:bg-slate-800">
                            🧠 Memory Aids
                        </button>
                        <button onclick="switchTab('mcq')" id="tab-btn-mcq" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold transition-all duration-200 text-slate-300 hover:text-white hover:bg-slate-800 flex items-center gap-1.5">
                            <span>🎯 Quiz</span>
                            <span id="tabQuizPill" class="px-1.5 py-0.2 bg-cyan-950 text-cyan-300 border border-cyan-600/40 rounded text-[10px] font-mono">20 Qs</span>
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
                <!-- Flashcard Controls Toolbar -->
                <div class="p-4 sm:p-5 rounded-2xl bg-slate-900/90 border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div>
                        <div class="flex items-center gap-2">
                            <h3 class="text-lg font-bold text-cyan-400 flex items-center gap-2">
                                <span>⚡</span> High-Speed Recall Flashcards
                            </h3>
                            <span id="flashcardMasteryPill" class="px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-amber-950/80 text-amber-300 border border-amber-500/40">
                                0 Mastered
                            </span>
                        </div>
                        <p class="text-xs text-slate-400 mt-0.5">Click any card to flip. Click the ⭐ star to mark concepts as mastered.</p>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="flipAllCards()" class="px-3.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-mono text-cyan-300 border border-slate-700 transition-colors">
                            🔄 Flip All
                        </button>
                        <button onclick="resetAllCards()" class="px-3.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-mono text-slate-300 border border-slate-700 transition-colors">
                            ↩️ Reset Flips
                        </button>
                    </div>
                </div>

                <!-- Flashcards Grid -->
                <div id="flashcardsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                    <!-- Injected via JavaScript -->
                </div>
            </section>

            <!-- TAB 3: MULTIPLE CHOICE QUESTIONS (MCQ QUIZ WITH INSTANT FEEDBACK) -->
            <section id="panel-mcq" class="tab-panel hidden space-y-6">
                <!-- Lecture Quiz Header & Stats HUD -->
                <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                        <div class="flex items-center gap-3">
                            <h3 class="text-xl font-bold text-white flex items-center gap-2">
                                <span class="text-cyan-400">20 High-Yield MCQs</span>
                            </h3>
                            <span id="lecQuizLiveScore" class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-emerald-950/80 text-emerald-300 border border-emerald-500/40">
                                0 / 20 Correct (0%)
                            </span>
                        </div>
                        <p class="text-xs text-slate-400 mt-1">
                            <span class="text-emerald-400 font-semibold">⚡ Instant Feedback Enabled:</span> Select any answer and it immediately reveals correctness with detailed justification.
                        </p>
                    </div>
                    <div class="flex items-center gap-2">
                        <button onclick="resetCurrentLectureQuiz()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 font-semibold text-slate-300 text-xs font-mono border border-slate-700 transition-colors flex items-center gap-1.5">
                            <span>🔄 Reset Quiz</span>
                        </button>
                        <button onclick="revealAllLectureExplanations()" class="px-4 py-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 font-semibold text-cyan-300 text-xs font-mono border border-cyan-500/30 transition-colors flex items-center gap-1.5">
                            <span>👀 Reveal All Explanations</span>
                        </button>
                    </div>
                </div>

                <!-- Quick Jump Question Navigator Pills (1 to 20) -->
                <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800">
                    <div class="flex items-center justify-between mb-2.5">
                        <span class="text-xs font-mono text-slate-400 uppercase tracking-wider font-semibold">Quick Jump Navigator (20 Questions):</span>
                        <div class="flex items-center gap-3 text-[11px] font-mono">
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block"></span> Correct</span>
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-rose-500 inline-block"></span> Incorrect</span>
                            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-slate-700 inline-block"></span> Unanswered</span>
                        </div>
                    </div>
                    <div id="lecQuestionNavGrid" class="flex flex-wrap gap-1.5">
                        <!-- Numbered pills 1..20 injected via JS -->
                    </div>
                </div>

                <!-- Questions Container -->
                <div id="questionsContainer" class="space-y-4">
                    <!-- 20 Question Cards Injected via JS -->
                </div>
            </section>
        </div>

        <!-- ============================================================== -->
        <!-- VIEW 2: GLOBAL 100-QUESTION SHUFFLED EXAM SIMULATOR (ALL LECS) -->
        <!-- ============================================================== -->
        <div id="view-simulator" class="hidden space-y-6">

            <!-- Simulator Header Card -->
            <div class="p-6 rounded-2xl bg-gradient-to-r from-purple-950/60 via-slate-900 to-indigo-950/50 border border-purple-500/40 glow-purple relative overflow-hidden">
                <div class="absolute right-0 top-0 bottom-0 w-1/3 bg-gradient-to-l from-purple-500/10 to-transparent pointer-events-none"></div>

                <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-5 relative z-10">
                    <div>
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-purple-950/90 border border-purple-500/50 text-purple-300 font-mono text-xs font-semibold mb-2">
                            <span>🎲 All 5 Lectures Aggregated</span>
                            <span>•</span>
                            <span id="simulatorSeedBadge">Randomized Exam Order</span>
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight flex items-center gap-3">
                            <span>All-Lectures Grand Exam Simulator</span>
                        </h2>
                        <p class="text-xs sm:text-sm text-slate-300 font-mono mt-1 max-w-2xl">
                            100 high-yield questions sampled randomly across Lectures 1 through 5. Every question provides instant visual feedback, lecture citations, and full justifications.
                        </p>
                    </div>

                    <!-- Simulator Main Controls -->
                    <div class="flex items-center gap-2.5 shrink-0 self-start lg:self-auto">
                        <button onclick="reshuffleSimulatorQuestions()" class="px-4 py-2.5 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold text-xs font-mono shadow-lg shadow-purple-600/25 transition-all flex items-center gap-2">
                            <span>🔀 Reshuffle Order</span>
                        </button>
                        <button onclick="resetSimulatorProgress()" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs font-mono border border-slate-700 transition-colors flex items-center gap-1.5">
                            <span>🔄 Reset All</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Simulator Filter & Stats Toolbar -->
            <div class="p-4 sm:p-5 rounded-2xl bg-slate-900/90 border border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-4">
                <!-- Status Filter Chips -->
                <div class="flex flex-wrap items-center gap-1.5" id="simFilterChips">
                    <button onclick="setSimFilter('all')" id="sim-flt-all" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all bg-cyan-500 text-slate-950 font-bold">
                        All (<span id="simCountAll">100</span>)
                    </button>
                    <button onclick="setSimFilter('unanswered')" id="sim-flt-unanswered" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all text-slate-400 hover:bg-slate-800 border border-slate-800">
                        Unanswered (<span id="simCountUnanswered">100</span>)
                    </button>
                    <button onclick="setSimFilter('incorrect')" id="sim-flt-incorrect" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all text-rose-400 hover:bg-slate-800 border border-slate-800">
                        Missed / Review (<span id="simCountIncorrect">0</span>)
                    </button>
                    <button onclick="setSimFilter('correct')" id="sim-flt-correct" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all text-emerald-400 hover:bg-slate-800 border border-slate-800">
                        Correct (<span id="simCountCorrect">0</span>)
                    </button>
                </div>

                <!-- Lecture Filter Dropdown -->
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono text-slate-400">Source:</span>
                    <select id="simLecFilterSelect" onchange="setSimLectureFilter(this.value)" class="bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs font-mono text-slate-200 focus:outline-none focus:border-cyan-500">
                        <option value="all">All Lectures (1 - 5)</option>
                        <option value="1">Lecture 1: Intro</option>
                        <option value="2">Lecture 2: Threats</option>
                        <option value="3">Lecture 3: Crypto</option>
                        <option value="4">Lecture 4: Auth</option>
                        <option value="5">Lecture 5: Access</option>
                    </select>
                </div>
            </div>

            <!-- Simulator 100-Question Jump Matrix (Collapsible) -->
            <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800">
                <div class="flex items-center justify-between mb-3">
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-mono text-slate-300 font-semibold uppercase tracking-wider">Exam Matrix (100 Questions):</span>
                        <span id="simMatrixProgress" class="text-xs font-mono text-cyan-400">0 answered</span>
                    </div>
                    <button onclick="toggleMatrixExpand()" id="matrixToggleBtn" class="text-xs font-mono text-slate-400 hover:text-cyan-300">
                        ▲ Collapse Matrix
                    </button>
                </div>
                <div id="simMatrixContainer" class="flex flex-wrap gap-1 max-h-48 overflow-y-auto pr-1">
                    <!-- 100 mini pills injected via JS -->
                </div>
            </div>

            <!-- Shuffled Questions List -->
            <div id="simQuestionsContainer" class="space-y-4">
                <!-- 100 Shuffled Question Cards Injected via JS -->
            </div>
        </div>

        <!-- ============================================================== -->
        <!-- VIEW 3: OFFICIAL PREVIOUS EXAMS & PAST PAPERS SOLVED HUB       -->
        <!-- ============================================================== -->
        <div id="view-exams" class="hidden space-y-6">

            <!-- Exam Header Card -->
            <div class="p-6 sm:p-7 rounded-2xl bg-gradient-to-r from-emerald-950/70 via-slate-900 to-cyan-950/60 border border-emerald-500/40 glow-emerald relative overflow-hidden">
                <div class="absolute right-0 top-0 bottom-0 w-1/3 bg-gradient-to-l from-emerald-500/10 to-transparent pointer-events-none"></div>

                <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-5 relative z-10">
                    <div>
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-emerald-950/90 border border-emerald-500/50 text-emerald-300 font-mono text-xs font-semibold mb-2.5">
                            <span>🎓 Ain Shams University · Faculty of Computers & Information Sciences</span>
                            <span>•</span>
                            <span>Official Exam Archives</span>
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight flex items-center gap-3">
                            <span>Previous Exams & Past Papers — Step-by-Step Solutions</span>
                        </h2>
                        <p class="text-xs sm:text-sm text-slate-300 font-mono mt-1 max-w-3xl leading-relaxed">
                            Complete step-by-step solutions for official university exam papers: storage calculations (62⁸ SHA-256), Rainbow tables, database DAC & SQL DCL, Bell-LaPadula multi-level tables, and 10 high-yield MCQs.
                        </p>
                        <div class="flex flex-wrap items-center gap-3 mt-3 text-xs font-mono text-slate-400">
                            <span>Examiners: <strong class="text-slate-200">Prof. Walaa Khaled & Dr. Alshaimaa Abo-alian</strong></span>
                            <span>•</span>
                            <span>Course: <strong class="text-slate-200">INF423 Cyber Security</strong></span>
                        </div>
                    </div>

                    <!-- Quick Highlights Badge Grid -->
                    <div class="grid grid-cols-3 gap-2.5 text-center shrink-0">
                        <div class="p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
                            <div class="text-xl font-bold font-mono text-emerald-400">3</div>
                            <div class="text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">Written Tasks</div>
                        </div>
                        <div class="p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
                            <div class="text-xl font-bold font-mono text-cyan-400">10</div>
                            <div class="text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">Official MCQs</div>
                        </div>
                        <div class="p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
                            <div class="text-xl font-bold font-mono text-amber-400">100%</div>
                            <div class="text-[10px] text-slate-400 uppercase tracking-wider mt-0.5">Step-by-Step</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Quick Jump Anchor Pills -->
            <div class="sticky top-16 z-30 bg-[#050811]/95 backdrop-blur-md p-2.5 rounded-xl border border-slate-800 flex flex-wrap items-center gap-2">
                <span class="text-xs font-mono text-slate-400 px-2 font-semibold">Jump to:</span>
                <a href="#exam-sec-math" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-colors bg-slate-900 hover:bg-slate-800 text-cyan-300 border border-slate-800 hover:border-cyan-500/40">
                    🧮 1. Password Storage (62⁸ SHA-256)
                </a>
                <a href="#exam-sec-db-dac" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-colors bg-slate-900 hover:bg-slate-800 text-purple-300 border border-slate-800 hover:border-purple-500/40">
                    🛡️ 2. Database DAC & SQL DCL
                </a>
                <a href="#exam-sec-blp" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-colors bg-slate-900 hover:bg-slate-800 text-emerald-300 border border-slate-800 hover:border-emerald-500/40">
                    🏛️ 3. University BLP Matrix (MAC)
                </a>
                <a href="#exam-sec-mcqs" class="px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-colors bg-slate-900 hover:bg-slate-800 text-amber-300 border border-slate-800 hover:border-amber-500/40">
                    🎯 4. 10 Official Exam MCQs
                </a>
            </div>

            <!-- All 4 Sections Rendered from data_previous_exams -->
            {exams_sections_html}
        </div>

    </main>

    <!-- FLOATING REAL-TIME HUD (Appears when taking quizzes) -->
    <div id="floatingHUD" class="fixed bottom-4 left-1/2 -translate-x-1/2 z-40 bg-slate-950/95 backdrop-blur-md border border-slate-800 rounded-2xl px-5 py-3 shadow-2xl shadow-black/80 flex items-center gap-4 sm:gap-6 max-w-[95vw]">
        <div class="flex items-center gap-2 font-mono text-xs">
            <span class="text-slate-400">Solved:</span>
            <span id="hudAnswered" class="font-bold text-white">0/20</span>
        </div>
        <div class="w-px h-5 bg-slate-800"></div>
        <div class="flex items-center gap-2 font-mono text-xs">
            <span class="text-slate-400">Score:</span>
            <span id="hudScore" class="font-bold text-emerald-400">0</span>
            <span id="hudAccuracy" class="text-cyan-400 text-[11px]">(0%)</span>
        </div>
        <div class="w-px h-5 bg-slate-800"></div>
        <div class="flex items-center gap-1.5 font-mono text-xs">
            <span id="hudStreakFlame" class="text-sm">🔥</span>
            <span id="hudStreak" class="font-bold text-amber-400">0 Streak</span>
        </div>
        <div class="w-px h-5 bg-slate-800 hidden sm:block"></div>
        <button onclick="scrollToTop()" class="hidden sm:flex items-center gap-1 text-[11px] font-mono text-slate-400 hover:text-cyan-300 transition-colors">
            <span>↑ Top</span>
        </button>
    </div>

    <!-- Footer -->
    <footer class="mt-16 border-t border-slate-800/80 bg-slate-950/90 py-8 px-4 sm:px-6 lg:px-8 text-xs text-slate-400">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-2">
                <span class="font-mono text-cyan-400 font-bold">CyberTutor Portal</span>
                <span>•</span>
                <span>Faculty of Computers & Information Sciences, Ain Shams University</span>
            </div>
            <div>
                Lectures strictly from <strong class="text-slate-300">Dr. Alshaimaa Abo-alian & Prof. Walaa Khaled</strong>
            </div>
        </div>
    </footer>

    <!-- INLINE APPLICATION LOGIC -->
    <script>
        const LECTURES_DATA = {lectures_json};
        const EXAM_MCQS = {exam_mcqs_json};
        
        // Application State
        let currentMode = 'lecture'; // 'lecture', 'simulator', or 'exams'
        let currentLecIndex = 0;
        let currentTab = 'summary'; // 'summary', 'memory', 'mcq'
        
        // Storage keys
        const STORAGE_KEY_ANSWERS = 'cybertutor_v2_answers';
        const STORAGE_KEY_MASTERED = 'cybertutor_v2_mastered';
        const STORAGE_KEY_EXAM_MCQ = 'cybertutor_v2_exam_mcq';
        
        // userAnswers: {{ "globalKey": {{ ans: "A", isCorrect: true }} }}
        let userAnswers = JSON.parse(localStorage.getItem(STORAGE_KEY_ANSWERS) || '{{}}');
        // masteredCards: {{ "cardKey": true }}
        let masteredCards = JSON.parse(localStorage.getItem(STORAGE_KEY_MASTERED) || '{{}}');
        // examMCQAnswers: {{ "idx": {{ ans: "A", isCorrect: true }} }}
        let examMCQAnswers = JSON.parse(localStorage.getItem(STORAGE_KEY_EXAM_MCQ) || '{{}}');
        
        // Streak counter
        let currentStreak = 0;
        let bestStreak = 0;

        // Simulator State
        let simulatorQuestions = [];
        let simCurrentFilter = 'all'; // 'all', 'unanswered', 'incorrect', 'correct'
        let simCurrentLecFilter = 'all'; // 'all', '1'..'5'
        let matrixExpanded = true;

        // Initialize Simulator Questions Array
        function initSimulatorData() {{
            simulatorQuestions = [];
            LECTURES_DATA.forEach((lec, lIdx) => {{
                lec.mcqs.forEach((mcq, qIdx) => {{
                    simulatorQuestions.push({{
                        ...mcq,
                        lecIndex: lIdx,
                        qIndex: qIdx,
                        globalKey: `${{lIdx}}_${{qIdx}}`,
                        lecNumber: lec.number,
                        lecTitle: lec.title,
                        lecBadge: lec.badge
                    }});
                }});
            }});
        }}

        // Fisher-Yates Shuffle
        function shuffleArray(arr) {{
            const shuffled = [...arr];
            for (let i = shuffled.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
            }}
            return shuffled;
        }}

        // ==========================================
        // NAVIGATION & VIEW SWITCHING
        // ==========================================

        function switchLecture(index) {{
            currentMode = 'lecture';
            currentLecIndex = index;
            const lec = LECTURES_DATA[index];

            // Show Lecture view, hide simulator and exams
            document.getElementById('view-lecture').classList.remove('hidden');
            document.getElementById('view-simulator').classList.add('hidden');
            document.getElementById('view-exams').classList.add('hidden');

            // Update Header Title & Meta
            document.getElementById('currentLecBadge').innerText = lec.badge;
            document.getElementById('currentLecTitle').innerText = `Lecture ${{lec.number}}: ${{lec.title}}`;
            document.getElementById('currentLecMeta').innerText = `Instructor: ${{lec.instructor}} · ${{lec.faculty}}`;

            // Update Nav styling
            updateNavPills();

            // Render sub-sections
            renderSummary();
            renderFlashcards();
            renderLectureMCQs();
            updateAllStats();

            // Scroll top smoothly
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function switchToSimulator() {{
            currentMode = 'simulator';
            
            // Show Simulator view, hide others
            document.getElementById('view-lecture').classList.add('hidden');
            document.getElementById('view-simulator').classList.remove('hidden');
            document.getElementById('view-exams').classList.add('hidden');

            updateNavPills();

            if (simulatorQuestions.length === 0) {{
                initSimulatorData();
                simulatorQuestions = shuffleArray(simulatorQuestions);
            }}

            renderSimulatorView();
            updateAllStats();
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function switchToExams() {{
            currentMode = 'exams';

            // Show Exams view, hide others
            document.getElementById('view-lecture').classList.add('hidden');
            document.getElementById('view-simulator').classList.add('hidden');
            document.getElementById('view-exams').classList.remove('hidden');

            updateNavPills();
            renderExamMCQs();
            updateAllStats();
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function updateNavPills() {{
            // Desktop lecture nav buttons
            for (let i = 0; i < 5; i++) {{
                const btn = document.getElementById(`nav-btn-${{i}}`);
                const mBtn = document.getElementById(`m-nav-btn-${{i}}`);
                if (currentMode === 'lecture' && i === currentLecIndex) {{
                    btn.className = "lec-nav-btn px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all duration-200 bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 shadow-sm";
                    if (mBtn) mBtn.className = "m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/40";
                }} else {{
                    btn.className = "lec-nav-btn px-3 py-1.5 rounded-lg text-xs font-mono font-medium transition-all duration-200 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 border border-transparent";
                    if (mBtn) mBtn.className = "m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono text-slate-400 hover:bg-slate-800";
                }}
            }}

            // Simulator button
            const simBtn = document.getElementById('nav-btn-sim');
            const mSimBtn = document.getElementById('m-nav-btn-sim');
            if (currentMode === 'simulator') {{
                simBtn.className = "lec-nav-btn relative px-3 py-1.5 rounded-lg text-xs font-mono font-bold transition-all duration-200 text-white bg-purple-600 border border-purple-400 shadow-md shadow-purple-500/30 flex items-center gap-1.5 ml-1";
                if (mSimBtn) mSimBtn.className = "m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-purple-600 text-white border border-purple-400 font-bold";
            }} else {{
                simBtn.className = "lec-nav-btn relative px-3 py-1.5 rounded-lg text-xs font-mono font-semibold transition-all duration-200 text-purple-300 hover:text-white bg-purple-950/40 hover:bg-purple-900/60 border border-purple-500/40 flex items-center gap-1.5 ml-1";
                if (mSimBtn) mSimBtn.className = "m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-purple-950/60 text-purple-300 border border-purple-500/40 font-semibold";
            }}

            // Previous Exams button
            const examsBtn = document.getElementById('nav-btn-exams');
            const mExamsBtn = document.getElementById('m-nav-btn-exams');
            if (currentMode === 'exams') {{
                examsBtn.className = "lec-nav-btn relative px-3 py-1.5 rounded-lg text-xs font-mono font-bold transition-all duration-200 text-white bg-emerald-600 border border-emerald-400 shadow-md shadow-emerald-500/30 flex items-center gap-1.5 ml-1";
                if (mExamsBtn) mExamsBtn.className = "m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-emerald-600 text-white border border-emerald-400 font-bold";
            }} else {{
                examsBtn.className = "lec-nav-btn relative px-3 py-1.5 rounded-lg text-xs font-mono font-semibold transition-all duration-200 text-emerald-300 hover:text-white bg-emerald-950/40 hover:bg-emerald-900/60 border border-emerald-500/40 flex items-center gap-1.5 ml-1";
                if (mExamsBtn) mExamsBtn.className = "m-lec-btn whitespace-nowrap px-3 py-1 rounded-md text-xs font-mono bg-emerald-950/60 text-emerald-300 border border-emerald-500/40 font-semibold";
            }}
        }}

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
            updateFloatingHUD();
        }}

        // ==========================================
        // SUMMARY TAB
        // ==========================================

        function renderSummary() {{
            const lec = LECTURES_DATA[currentLecIndex];
            document.getElementById('summaryContainer').innerHTML = lec.summary_html;
        }}

        // ==========================================
        // FLASHCARDS & MEMORY AIDS
        // ==========================================

        function renderFlashcards() {{
            const lec = LECTURES_DATA[currentLecIndex];
            const container = document.getElementById('flashcardsGrid');
            container.innerHTML = '';

            let masteredCount = 0;

            lec.memory_aids.forEach((aid, idx) => {{
                const cardKey = `${{currentLecIndex}}_${{idx}}`;
                const isMastered = !!masteredCards[cardKey];
                if (isMastered) masteredCount++;

                const card = document.createElement('div');
                card.className = "perspective-1000 h-56 cursor-pointer select-none group relative";
                card.id = `flashcard-${{cardKey}}`;

                card.innerHTML = `
                    <div class="card-inner relative w-full h-full duration-500 transform-style-3d rounded-xl transition-transform border ${{isMastered ? 'border-amber-500/60' : 'border-slate-800'}} group-hover:border-cyan-500/50">
                        <!-- Front -->
                        <div class="absolute inset-0 w-full h-full bg-slate-900/90 rounded-xl p-5 flex flex-col justify-between backface-hidden border border-slate-800" onclick="toggleCardFlip(this.parentElement)">
                            <div>
                                <div class="flex items-center justify-between mb-2">
                                    <span class="text-[10px] font-mono text-cyan-400 uppercase tracking-widest">Rule #${{idx + 1}}</span>
                                    <button onclick="event.stopPropagation(); toggleMasterCard('${{cardKey}}')" class="text-xs p-1 rounded hover:bg-slate-800 transition-colors" title="${{isMastered ? 'Unmark Mastered' : 'Mark as Mastered'}}">
                                        <span class="${{isMastered ? 'text-amber-400' : 'text-slate-600 hover:text-amber-300'}}">★</span>
                                    </button>
                                </div>
                                <h4 class="text-sm font-bold text-white group-hover:text-cyan-300 transition-colors">${{aid.title}}</h4>
                            </div>
                            <div class="text-[11px] text-slate-500 font-mono flex items-center justify-between">
                                <span>Click to flip</span>
                                <span>↻</span>
                            </div>
                        </div>
                        <!-- Back -->
                        <div class="absolute inset-0 w-full h-full bg-[#091224] rounded-xl p-5 flex flex-col justify-between rotate-y-180 backface-hidden border border-cyan-500/40 glow-border-cyan" onclick="toggleCardFlip(this.parentElement)">
                            <div>
                                <div class="flex items-center justify-between mb-1.5">
                                    <span class="text-[10px] font-mono text-emerald-400 uppercase tracking-widest font-semibold">Key Takeaway</span>
                                    <button onclick="event.stopPropagation(); toggleMasterCard('${{cardKey}}')" class="text-xs p-1 rounded hover:bg-slate-800 transition-colors">
                                        <span class="${{isMastered ? 'text-amber-400' : 'text-slate-600 hover:text-amber-300'}}">★</span>
                                    </button>
                                </div>
                                <p class="text-xs text-slate-200 leading-relaxed font-sans">${{aid.content}}</p>
                            </div>
                            <div class="text-[10px] text-slate-500 font-mono text-right">Click to flip back ↻</div>
                        </div>
                    </div>
                `;
                container.appendChild(card);
            }});

            document.getElementById('flashcardMasteryPill').innerText = `${{masteredCount}} / ${{lec.memory_aids.length}} Mastered`;
            updateTotalMasteredHero();
        }}

        function toggleCardFlip(innerEl) {{
            innerEl.classList.toggle('flipped');
        }}

        function flipAllCards() {{
            const cards = document.querySelectorAll('#flashcardsGrid .card-inner');
            cards.forEach(c => c.classList.toggle('flipped'));
        }}

        function resetAllCards() {{
            const cards = document.querySelectorAll('#flashcardsGrid .card-inner');
            cards.forEach(c => c.classList.remove('flipped'));
        }}

        function toggleMasterCard(cardKey) {{
            if (masteredCards[cardKey]) {{
                delete masteredCards[cardKey];
            }} else {{
                masteredCards[cardKey] = true;
            }}
            localStorage.setItem(STORAGE_KEY_MASTERED, JSON.stringify(masteredCards));
            renderFlashcards();
        }}

        function updateTotalMasteredHero() {{
            let count = Object.keys(masteredCards).length;
            const el = document.getElementById('heroMasteredCount');
            if (el) el.innerText = `${{count}}/42`;
        }}

        // ==========================================
        // INSTANT FEEDBACK MCQ ENGINE (CORE FEATURE)
        // ==========================================

        function renderLectureMCQs() {{
            const lec = LECTURES_DATA[currentLecIndex];
            const container = document.getElementById('questionsContainer');
            const navGrid = document.getElementById('lecQuestionNavGrid');
            container.innerHTML = '';
            navGrid.innerHTML = '';

            lec.mcqs.forEach((mcq, qIdx) => {{
                const globalKey = `${{currentLecIndex}}_${{qIdx}}`;
                const answeredData = userAnswers[globalKey];

                const qCard = buildQuestionCardHtml({{
                    globalKey: globalKey,
                    displayNum: qIdx + 1,
                    mcq: mcq,
                    answeredData: answeredData,
                    sourceBadge: `Question #${{mcq.id}}`,
                    cardPrefix: `lec_q_${{currentLecIndex}}_${{qIdx}}`
                }});
                container.appendChild(qCard);

                const navBtn = document.createElement('button');
                navBtn.id = `lec-nav-pill-${{qIdx}}`;
                let pillColor = "bg-slate-800 text-slate-400 hover:bg-slate-700";
                if (answeredData) {{
                    pillColor = answeredData.isCorrect ? "bg-emerald-600 text-white font-bold" : "bg-rose-600 text-white font-bold";
                }}
                navBtn.className = `w-8 h-8 rounded-lg text-xs font-mono flex items-center justify-center transition-all ${{pillColor}}`;
                navBtn.innerText = qIdx + 1;
                navBtn.onclick = () => {{
                    document.getElementById(`lec_q_${{currentLecIndex}}_${{qIdx}}`).scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                }};
                navGrid.appendChild(navBtn);
            }});

            updateLectureQuizScoreBadge();
        }}

        function buildQuestionCardHtml(props) {{
            const {{ globalKey, displayNum, mcq, answeredData, sourceBadge, cardPrefix }} = props;
            const card = document.createElement('div');
            card.id = cardPrefix;
            card.className = "p-5 rounded-2xl bg-slate-900/90 border border-slate-800 transition-all duration-300 relative";

            const letters = ['A', 'B', 'C', 'D'];
            let optionsHtml = '';

            letters.forEach((letter, optIdx) => {{
                const optText = mcq.options[optIdx];
                let cardStyle = "border-slate-800 bg-slate-800/40 text-slate-300 hover:border-slate-700 hover:bg-slate-800/80";
                let badgeHtml = `<span class="w-6 h-6 rounded-md bg-slate-800 border border-slate-700 font-mono text-xs flex items-center justify-center font-bold text-slate-400">${{letter}}</span>`;
                let cursorStyle = "cursor-pointer";

                if (answeredData) {{
                    cursorStyle = "cursor-default pointer-events-none";
                    if (letter === mcq.ans) {{
                        cardStyle = "border-emerald-500 bg-emerald-950/60 text-emerald-200 font-medium ring-1 ring-emerald-500/60 glow-emerald";
                        badgeHtml = `<span class="w-6 h-6 rounded-md bg-emerald-500 text-slate-950 font-mono text-xs flex items-center justify-center font-bold">✓</span>`;
                    }} else if (answeredData.ans === letter && !answeredData.isCorrect) {{
                        cardStyle = "border-rose-500 bg-rose-950/60 text-rose-200 ring-1 ring-rose-500/60";
                        badgeHtml = `<span class="w-6 h-6 rounded-md bg-rose-500 text-white font-mono text-xs flex items-center justify-center font-bold">✗</span>`;
                    }} else {{
                        cardStyle = "border-slate-850 bg-slate-900/40 text-slate-500 opacity-60";
                    }}
                }}

                optionsHtml += `
                    <div onclick="handleInstantAnswer('${{globalKey}}', '${{letter}}', '${{cardPrefix}}')" 
                         class="option-card p-3 rounded-xl border ${{cardStyle}} ${{cursorStyle}} flex items-center gap-3 text-xs sm:text-sm select-none">
                        ${{badgeHtml}}
                        <span class="flex-1">${{optText}}</span>
                        ${{answeredData && letter === mcq.ans ? '<span class="text-[10px] font-mono uppercase bg-emerald-500 text-slate-950 px-2 py-0.5 rounded font-bold">Correct</span>' : ''}}
                        ${{answeredData && answeredData.ans === letter && !answeredData.isCorrect ? '<span class="text-[10px] font-mono uppercase bg-rose-500 text-white px-2 py-0.5 rounded font-bold">Your Choice</span>' : ''}}
                    </div>
                `;
            }});

            let explanationHtml = '';
            if (answeredData) {{
                const isCorrect = answeredData.isCorrect;
                explanationHtml = `
                    <div class="mt-4 p-4 rounded-xl ${{isCorrect ? 'bg-emerald-950/30 border border-emerald-500/40' : 'bg-rose-950/30 border border-rose-500/40'}} animate-slide-down text-xs sm:text-sm">
                        <div class="flex items-center justify-between gap-2 mb-1.5">
                            <span class="font-mono font-bold ${{isCorrect ? 'text-emerald-400' : 'text-rose-400'}} flex items-center gap-1.5">
                                <span>${{isCorrect ? '✅ Correct!' : '❌ Incorrect.'}}</span>
                                <span>Correct Answer: [${{mcq.ans}}]</span>
                            </span>
                            <button onclick="retryQuestion('${{globalKey}}', '${{cardPrefix}}')" class="text-[11px] font-mono text-slate-400 hover:text-cyan-300 underline">
                                Try Again
                            </button>
                        </div>
                        <p class="text-slate-200 leading-relaxed font-sans">${{mcq.explanation}}</p>
                    </div>
                `;
            }}

            card.innerHTML = `
                <div class="flex items-start justify-between gap-3 mb-3">
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded bg-slate-800 border border-slate-700 font-mono text-xs font-bold text-cyan-400">
                            #${{displayNum}}
                        </span>
                        <span class="text-[11px] font-mono text-slate-400">${{sourceBadge}}</span>
                    </div>
                    ${{answeredData ? (answeredData.isCorrect ? '<span class="text-xs font-mono text-emerald-400 font-bold bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-500/40">✓ Solved</span>' : '<span class="text-xs font-mono text-rose-400 font-bold bg-rose-950/80 px-2 py-0.5 rounded border border-rose-500/40">✗ Missed</span>') : '<span class="text-[10px] font-mono text-slate-500">Not Answered</span>'}}
                </div>
                <h4 class="text-sm sm:text-base font-semibold text-slate-100 mb-3 leading-snug">${{mcq.q}}</h4>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                    ${{optionsHtml}}
                </div>
                ${{explanationHtml}}
            `;

            return card;
        }}

        function handleInstantAnswer(globalKey, selectedLetter, cardPrefix) {{
            const parts = globalKey.split('_');
            const lecIdx = parseInt(parts[0]);
            const qIdx = parseInt(parts[1]);
            const mcq = LECTURES_DATA[lecIdx].mcqs[qIdx];

            const isCorrect = selectedLetter === mcq.ans;

            userAnswers[globalKey] = {{
                ans: selectedLetter,
                isCorrect: isCorrect,
                time: Date.now()
            }};
            localStorage.setItem(STORAGE_KEY_ANSWERS, JSON.stringify(userAnswers));

            if (isCorrect) {{
                currentStreak++;
                if (currentStreak > bestStreak) bestStreak = currentStreak;
            }} else {{
                currentStreak = 0;
            }}

            const oldCard = document.getElementById(cardPrefix);
            if (oldCard) {{
                const displayNum = oldCard.querySelector('span.text-cyan-400')?.innerText?.replace('#', '') || (qIdx + 1);
                const sourceBadge = oldCard.querySelector('span.text-slate-400')?.innerText || `Question #${{mcq.id}}`;
                const newCard = buildQuestionCardHtml({{
                    globalKey: globalKey,
                    displayNum: displayNum,
                    mcq: mcq,
                    answeredData: userAnswers[globalKey],
                    sourceBadge: sourceBadge,
                    cardPrefix: cardPrefix
                }});
                oldCard.replaceWith(newCard);
            }}

            if (currentMode === 'lecture') {{
                const pill = document.getElementById(`lec-nav-pill-${{qIdx}}`);
                if (pill) {{
                    pill.className = `w-8 h-8 rounded-lg text-xs font-mono flex items-center justify-center transition-all ${{isCorrect ? 'bg-emerald-600 text-white font-bold' : 'bg-rose-600 text-white font-bold'}}`;
                }}
                updateLectureQuizScoreBadge();
            }} else if (currentMode === 'simulator') {{
                const simPill = document.getElementById(`sim-matrix-pill-${{globalKey}}`);
                if (simPill) {{
                    simPill.className = `w-7 h-7 rounded text-[10px] font-mono flex items-center justify-center transition-all ${{isCorrect ? 'bg-emerald-600 text-white font-bold' : 'bg-rose-600 text-white font-bold'}}`;
                }}
                updateSimulatorStats();
            }}

            updateAllStats();
        }}

        function retryQuestion(globalKey, cardPrefix) {{
            delete userAnswers[globalKey];
            localStorage.setItem(STORAGE_KEY_ANSWERS, JSON.stringify(userAnswers));

            const parts = globalKey.split('_');
            const lecIdx = parseInt(parts[0]);
            const qIdx = parseInt(parts[1]);
            const mcq = LECTURES_DATA[lecIdx].mcqs[qIdx];

            const oldCard = document.getElementById(cardPrefix);
            if (oldCard) {{
                const displayNum = oldCard.querySelector('span.text-cyan-400')?.innerText?.replace('#', '') || (qIdx + 1);
                const sourceBadge = oldCard.querySelector('span.text-slate-400')?.innerText || `Question #${{mcq.id}}`;
                const newCard = buildQuestionCardHtml({{
                    globalKey: globalKey,
                    displayNum: displayNum,
                    mcq: mcq,
                    answeredData: null,
                    sourceBadge: sourceBadge,
                    cardPrefix: cardPrefix
                }});
                oldCard.replaceWith(newCard);
            }}

            if (currentMode === 'lecture') {{
                const pill = document.getElementById(`lec-nav-pill-${{qIdx}}`);
                if (pill) pill.className = "w-8 h-8 rounded-lg text-xs font-mono flex items-center justify-center transition-all bg-slate-800 text-slate-400 hover:bg-slate-700";
                updateLectureQuizScoreBadge();
            }} else if (currentMode === 'simulator') {{
                const simPill = document.getElementById(`sim-matrix-pill-${{globalKey}}`);
                if (simPill) simPill.className = "w-7 h-7 rounded text-[10px] font-mono flex items-center justify-center transition-all bg-slate-800 text-slate-400 hover:bg-slate-700";
                updateSimulatorStats();
            }}
            updateAllStats();
        }}

        function resetCurrentLectureQuiz() {{
            if (!confirm(`Reset all answers for Lecture ${{LECTURES_DATA[currentLecIndex].number}}?`)) return;
            const lec = LECTURES_DATA[currentLecIndex];
            lec.mcqs.forEach((_, qIdx) => {{
                delete userAnswers[`${{currentLecIndex}}_${{qIdx}}`];
            }});
            localStorage.setItem(STORAGE_KEY_ANSWERS, JSON.stringify(userAnswers));
            renderLectureMCQs();
            updateAllStats();
        }}

        function revealAllLectureExplanations() {{
            const lec = LECTURES_DATA[currentLecIndex];
            lec.mcqs.forEach((mcq, qIdx) => {{
                const k = `${{currentLecIndex}}_${{qIdx}}`;
                if (!userAnswers[k]) {{
                    userAnswers[k] = {{ ans: mcq.ans, isCorrect: true, time: Date.now() }};
                }}
            }});
            localStorage.setItem(STORAGE_KEY_ANSWERS, JSON.stringify(userAnswers));
            renderLectureMCQs();
            updateAllStats();
        }}

        function updateLectureQuizScoreBadge() {{
            const lec = LECTURES_DATA[currentLecIndex];
            let answered = 0;
            let correct = 0;
            lec.mcqs.forEach((_, qIdx) => {{
                const ans = userAnswers[`${{currentLecIndex}}_${{qIdx}}`];
                if (ans) {{
                    answered++;
                    if (ans.isCorrect) correct++;
                }}
            }});
            const pct = answered > 0 ? Math.round((correct / 20) * 100) : 0;
            const scoreEl = document.getElementById('lecQuizLiveScore');
            if (scoreEl) {{
                scoreEl.innerText = `${{correct}} / 20 Correct (${{pct}}%) · ${{answered}}/20 Answered`;
            }}
        }}

        // ==========================================
        // 100-QUESTION SHUFFLED SIMULATOR LOGIC
        // ==========================================

        function renderSimulatorView() {{
            const container = document.getElementById('simQuestionsContainer');
            const matrix = document.getElementById('simMatrixContainer');
            container.innerHTML = '';
            matrix.innerHTML = '';

            let filteredList = simulatorQuestions.filter(item => {{
                const ans = userAnswers[item.globalKey];
                if (simCurrentFilter === 'unanswered' && ans) return false;
                if (simCurrentFilter === 'correct' && (!ans || !ans.isCorrect)) return false;
                if (simCurrentFilter === 'incorrect' && (!ans || ans.isCorrect)) return false;

                if (simCurrentLecFilter !== 'all' && item.lecNumber.toString() !== simCurrentLecFilter) return false;
                return true;
            }});

            filteredList.forEach((item, index) => {{
                const answeredData = userAnswers[item.globalKey];
                const card = buildQuestionCardHtml({{
                    globalKey: item.globalKey,
                    displayNum: index + 1,
                    mcq: item,
                    answeredData: answeredData,
                    sourceBadge: `L${{item.lecNumber}}: ${{item.lecTitle.split(':')[0]}}`,
                    cardPrefix: `sim_card_${{item.globalKey}}`
                }});
                container.appendChild(card);
            }});

            simulatorQuestions.forEach((item, idx) => {{
                const answeredData = userAnswers[item.globalKey];
                let pillColor = "bg-slate-850 text-slate-500 border border-slate-800";
                if (answeredData) {{
                    pillColor = answeredData.isCorrect ? "bg-emerald-600 text-white font-bold" : "bg-rose-600 text-white font-bold";
                }}
                const pill = document.createElement('button');
                pill.id = `sim-matrix-pill-${{item.globalKey}}`;
                pill.className = `w-7 h-7 rounded text-[10px] font-mono flex items-center justify-center transition-all ${{pillColor}} hover:scale-110`;
                pill.innerText = idx + 1;
                pill.title = `Q${{idx + 1}} (L${{item.lecNumber}}): ${{item.q.substring(0, 45)}}...`;
                pill.onclick = () => {{
                    const cardEl = document.getElementById(`sim_card_${{item.globalKey}}`);
                    if (!cardEl) {{
                        simCurrentFilter = 'all';
                        simCurrentLecFilter = 'all';
                        document.getElementById('simLecFilterSelect').value = 'all';
                        renderSimulatorView();
                    }}
                    setTimeout(() => {{
                        document.getElementById(`sim_card_${{item.globalKey}}`)?.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    }}, 50);
                }};
                matrix.appendChild(pill);
            }});

            updateSimulatorStats();
        }}

        function reshuffleSimulatorQuestions() {{
            simulatorQuestions = shuffleArray(simulatorQuestions);
            const seedBadge = document.getElementById('simulatorSeedBadge');
            if (seedBadge) seedBadge.innerText = `Reshuffled #${{Math.floor(Math.random() * 9000 + 1000)}}`;
            renderSimulatorView();
        }}

        function resetSimulatorProgress() {{
            if (!confirm("Are you sure you want to clear your answers across all 100 questions for a fresh exam?")) return;
            userAnswers = {{}};
            currentStreak = 0;
            localStorage.setItem(STORAGE_KEY_ANSWERS, JSON.stringify(userAnswers));
            renderSimulatorView();
            updateAllStats();
        }}

        function setSimFilter(filterType) {{
            simCurrentFilter = filterType;
            const chips = ['all', 'unanswered', 'incorrect', 'correct'];
            chips.forEach(t => {{
                const btn = document.getElementById(`sim-flt-${{t}}`);
                if (t === filterType) {{
                    btn.className = "px-3 py-1.5 rounded-lg text-xs font-mono transition-all bg-cyan-500 text-slate-950 font-bold shadow-md";
                }} else {{
                    btn.className = "px-3 py-1.5 rounded-lg text-xs font-mono transition-all text-slate-400 hover:bg-slate-800 border border-slate-800";
                }}
            }});
            renderSimulatorView();
        }}

        function setSimLectureFilter(val) {{
            simCurrentLecFilter = val;
            renderSimulatorView();
        }}

        function toggleMatrixExpand() {{
            const mat = document.getElementById('simMatrixContainer');
            const btn = document.getElementById('matrixToggleBtn');
            matrixExpanded = !matrixExpanded;
            if (matrixExpanded) {{
                mat.classList.remove('hidden');
                btn.innerText = "▲ Collapse Matrix";
            }} else {{
                mat.classList.add('hidden');
                btn.innerText = "▼ Expand Matrix";
            }}
        }}

        function updateSimulatorStats() {{
            let total = 100;
            let answered = 0;
            let correct = 0;
            let incorrect = 0;

            simulatorQuestions.forEach(q => {{
                const ans = userAnswers[q.globalKey];
                if (ans) {{
                    answered++;
                    if (ans.isCorrect) correct++;
                    else incorrect++;
                }}
            }});

            const unanswered = total - answered;

            document.getElementById('simCountAll').innerText = total;
            document.getElementById('simCountUnanswered').innerText = unanswered;
            document.getElementById('simCountIncorrect').innerText = incorrect;
            document.getElementById('simCountCorrect').innerText = correct;
            document.getElementById('simMatrixProgress').innerText = `${{answered}}/100 Answered (${{answered > 0 ? Math.round(correct/answered*100) : 0}}% Acc)`;
        }}

        // ==========================================
        // SECTION 4: 10 EXAM MCQS EVALUATION LOGIC
        // ==========================================

        function renderExamMCQs() {{
            const container = document.getElementById('examMCQContainer');
            if (!container) return;
            container.innerHTML = '';

            EXAM_MCQS.forEach((mcq, idx) => {{
                const answeredData = examMCQAnswers[idx];
                const card = document.createElement('div');
                card.id = `exam_mcq_card_${{idx}}`;
                card.className = "p-5 rounded-2xl bg-slate-950/80 border border-slate-800 transition-all duration-300";

                const letters = ['A', 'B', 'C', 'D'];
                let optionsHtml = '';

                letters.forEach((letter, optIdx) => {{
                    const optText = mcq.options[optIdx];
                    let cardStyle = "border-slate-800 bg-slate-900/60 text-slate-300 hover:border-slate-700 hover:bg-slate-850";
                    let badgeHtml = `<span class="w-6 h-6 rounded-md bg-slate-800 border border-slate-700 font-mono text-xs flex items-center justify-center font-bold text-slate-400">${{letter}}</span>`;
                    let cursorStyle = "cursor-pointer";

                    if (answeredData) {{
                        cursorStyle = "cursor-default pointer-events-none";
                        if (letter === mcq.ans) {{
                            cardStyle = "border-emerald-500 bg-emerald-950/60 text-emerald-200 font-medium ring-1 ring-emerald-500/60 glow-emerald";
                            badgeHtml = `<span class="w-6 h-6 rounded-md bg-emerald-500 text-slate-950 font-mono text-xs flex items-center justify-center font-bold">✓</span>`;
                        }} else if (answeredData.ans === letter && !answeredData.isCorrect) {{
                            cardStyle = "border-rose-500 bg-rose-950/60 text-rose-200 ring-1 ring-rose-500/60";
                            badgeHtml = `<span class="w-6 h-6 rounded-md bg-rose-500 text-white font-mono text-xs flex items-center justify-center font-bold">✗</span>`;
                        }} else {{
                            cardStyle = "border-slate-850 bg-slate-900/30 text-slate-500 opacity-60";
                        }}
                    }}

                    optionsHtml += `
                        <div onclick="handleExamMCQSelect(${{idx}}, '${{letter}}')" 
                             class="option-card p-3 rounded-xl border ${{cardStyle}} ${{cursorStyle}} flex items-center gap-3 text-xs sm:text-sm select-none">
                            ${{badgeHtml}}
                            <span class="flex-1">${{optText}}</span>
                            ${{answeredData && letter === mcq.ans ? '<span class="text-[10px] font-mono uppercase bg-emerald-500 text-slate-950 px-2 py-0.5 rounded font-bold">Correct</span>' : ''}}
                            ${{answeredData && answeredData.ans === letter && !answeredData.isCorrect ? '<span class="text-[10px] font-mono uppercase bg-rose-500 text-white px-2 py-0.5 rounded font-bold">Your Choice</span>' : ''}}
                        </div>
                    `;
                }});

                let explanationHtml = '';
                if (answeredData) {{
                    const isCorrect = answeredData.isCorrect;
                    explanationHtml = `
                        <div class="mt-4 p-4 rounded-xl ${{isCorrect ? 'bg-emerald-950/30 border border-emerald-500/40' : 'bg-rose-950/30 border border-rose-500/40'}} animate-slide-down text-xs sm:text-sm">
                            <div class="flex items-center justify-between gap-2 mb-2">
                                <span class="font-mono font-bold ${{isCorrect ? 'text-emerald-400' : 'text-rose-400'}} flex items-center gap-1.5">
                                    <span>${{isCorrect ? '✅ Correct Answer!' : '❌ Incorrect.'}}</span>
                                    <span>(Official Answer: [${{mcq.ans}}])</span>
                                </span>
                                <button onclick="retryExamMCQ(${{idx}})" class="text-[11px] font-mono text-slate-400 hover:text-cyan-300 underline">
                                    Try Again
                                </button>
                            </div>
                            <div class="text-slate-200 leading-relaxed font-sans mb-2">${{mcq.explanation}}</div>
                            <div class="text-[11px] font-mono text-cyan-400 bg-cyan-950/50 p-2 rounded border border-cyan-800/40">
                                <strong>Tested Concept:</strong> ${{mcq.concept}}
                            </div>
                        </div>
                    `;
                }}

                card.innerHTML = `
                    <div class="flex items-start justify-between gap-3 mb-2">
                        <div class="flex items-center gap-2">
                            <span class="px-2 py-0.5 rounded bg-slate-800 border border-slate-700 font-mono text-xs font-bold text-amber-400">
                                Exam Q#${{mcq.id}}
                            </span>
                            <span class="text-[11px] font-mono text-slate-400">${{mcq.concept}}</span>
                        </div>
                        ${{answeredData ? (answeredData.isCorrect ? '<span class="text-xs font-mono text-emerald-400 font-bold bg-emerald-950 px-2 py-0.5 rounded border border-emerald-500/40">✓ Solved</span>' : '<span class="text-xs font-mono text-rose-400 font-bold bg-rose-950 px-2 py-0.5 rounded border border-rose-500/40">✗ Missed</span>') : '<span class="text-[10px] font-mono text-slate-500">Not Answered</span>'}}
                    </div>
                    <h4 class="text-sm sm:text-base font-semibold text-slate-100 mb-3 leading-snug">${{mcq.q}}</h4>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                        ${{optionsHtml}}
                    </div>
                    ${{explanationHtml}}
                `;

                container.appendChild(card);
            }});

            updateExamMCQScoreBadge();
        }}

        function handleExamMCQSelect(idx, selectedLetter) {{
            const mcq = EXAM_MCQS[idx];
            const isCorrect = selectedLetter === mcq.ans;
            examMCQAnswers[idx] = {{ ans: selectedLetter, isCorrect: isCorrect }};
            localStorage.setItem(STORAGE_KEY_EXAM_MCQ, JSON.stringify(examMCQAnswers));
            renderExamMCQs();
        }}

        function retryExamMCQ(idx) {{
            delete examMCQAnswers[idx];
            localStorage.setItem(STORAGE_KEY_EXAM_MCQ, JSON.stringify(examMCQAnswers));
            renderExamMCQs();
        }}

        function revealAllExamMCQSolutions() {{
            EXAM_MCQS.forEach((mcq, idx) => {{
                examMCQAnswers[idx] = {{ ans: mcq.ans, isCorrect: true }};
            }});
            localStorage.setItem(STORAGE_KEY_EXAM_MCQ, JSON.stringify(examMCQAnswers));
            renderExamMCQs();
        }}

        function updateExamMCQScoreBadge() {{
            let answered = 0;
            let correct = 0;
            EXAM_MCQS.forEach((mcq, idx) => {{
                const a = examMCQAnswers[idx];
                if (a) {{
                    answered++;
                    if (a.isCorrect) correct++;
                }}
            }});
            const el = document.getElementById('examMCQScoreBadge');
            if (el) el.innerText = `${{correct}} / 10 Correct (${{answered}}/10 Solved)`;
        }}

        // ==========================================
        // GLOBAL LIVE STATS & FLOATING HUD
        // ==========================================

        function updateAllStats() {{
            let total = 100;
            let answered = 0;
            let correct = 0;

            for (let l = 0; l < 5; l++) {{
                for (let q = 0; q < 20; q++) {{
                    const a = userAnswers[`${{l}}_${{q}}`];
                    if (a) {{
                        answered++;
                        if (a.isCorrect) correct++;
                    }}
                }}
            }}

            const accuracy = answered > 0 ? Math.round((correct / answered) * 100) : 0;

            document.getElementById('headerCorrectCount').innerText = correct;
            document.getElementById('headerAccuracyLive').innerText = `${{accuracy}}% Acc`;
            document.getElementById('heroStreakDisplay').innerText = `🔥 ${{currentStreak}}`;

            updateFloatingHUD();
        }}

        function updateFloatingHUD() {{
            const hud = document.getElementById('floatingHUD');
            
            let answered = 0;
            let correct = 0;
            let maxCount = 20;

            if (currentMode === 'lecture') {{
                maxCount = 20;
                for (let q = 0; q < 20; q++) {{
                    const a = userAnswers[`${{currentLecIndex}}_${{q}}`];
                    if (a) {{
                        answered++;
                        if (a.isCorrect) correct++;
                    }}
                }}
            }} else if (currentMode === 'simulator') {{
                maxCount = 100;
                for (let l = 0; l < 5; l++) {{
                    for (let q = 0; q < 20; q++) {{
                        const a = userAnswers[`${{l}}_${{q}}`];
                        if (a) {{
                            answered++;
                            if (a.isCorrect) correct++;
                        }}
                    }}
                }}
            }} else {{
                // Exams Mode HUD
                maxCount = 10;
                EXAM_MCQS.forEach((mcq, idx) => {{
                    const a = examMCQAnswers[idx];
                    if (a) {{
                        answered++;
                        if (a.isCorrect) correct++;
                    }}
                }});
            }}

            const acc = answered > 0 ? Math.round((correct / answered) * 100) : 0;

            document.getElementById('hudAnswered').innerText = `${{answered}}/${{maxCount}}`;
            document.getElementById('hudScore').innerText = `${{correct}}`;
            document.getElementById('hudAccuracy').innerText = `(${{acc}}%)`;
            document.getElementById('hudStreak').innerText = `${{currentStreak}} Streak`;

            const flame = document.getElementById('hudStreakFlame');
            if (currentStreak >= 5) {{
                flame.className = "text-base animate-bounce";
            }} else {{
                flame.className = "text-sm";
            }}
        }}

        function scrollToTop() {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        // Quick Search Filter across summary, MCQs, and Exam solutions
        function handleSearch(term) {{
            term = term.toLowerCase().trim();
            if (!term) return;

            // Search in Exam Solutions first if matching key exam terms
            const examKeywords = ['rainbow', '62^8', '62', 'sha-256', 'petabyte', 'cascade', 'restrict', 'blp', 'bell-lapadula', 'top secret', 'unclassified', 'acls', 'table1', 'table2', 'table3', 'smith'];
            for (let kw of examKeywords) {{
                if (term.includes(kw)) {{
                    switchToExams();
                    return;
                }}
            }}

            // Search in which lecture it appears most
            for (let i = 0; i < LECTURES_DATA.length; i++) {{
                const lec = LECTURES_DATA[i];
                const content = (lec.title + " " + lec.summary_html).toLowerCase();
                if (content.includes(term)) {{
                    if (currentMode !== 'lecture' || currentLecIndex !== i) {{
                        switchLecture(i);
                    }}
                    break;
                }}
            }}
        }}

        window.addEventListener('keydown', (e) => {{
            if ((e.ctrlKey && e.key === 'k') || (e.key === '/' && document.activeElement.tagName !== 'INPUT')) {{
                e.preventDefault();
                document.getElementById('globalSearch')?.focus();
            }}
        }});

        window.addEventListener('DOMContentLoaded', () => {{
            initSimulatorData();
            switchLecture(0);
            updateTotalMasteredHero();
            updateAllStats();
        }});
    </script>
</body>
</html>
"""
    with open("d:\\Tech\\Summariez\\index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Successfully built index.html with Solved Previous Exams tab!")

if __name__ == "__main__":
    generate_html()
