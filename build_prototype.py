import json

# Load base64 images
with open(r'c:\Users\dudam\OneDrive\Desktop\songs\assets\images_b64.json', 'r') as f:
    img_data = json.load(f)

img_floor_wide = img_data['floorWide']
img_hack_squat = img_data['hackSquat']
img_cardio_arena = img_data['cardioArena']
img_selectorized = img_data['selectorized']

html_content = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Midtown Fitness | Worli, Mumbai — Apex Training & Performance Destination</title>
  <meta name="description" content="Worli's premier athletic fitness destination. Heavy iron bay, cobalt neon cardio arena, MMA cage, Zumba sound stage, and executive eucalyptus steam suites. Dr. Annie Besant Rd, Worli, Mumbai.">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Oswald:wght@500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            obsidian: '#07090e',
            carbon: '#0f131c',
            'carbon-card': '#141824',
            'carbon-hover': '#1d2233',
            'cobalt-neon': '#2563eb',
            'cobalt-bright': '#38bdf8',
            'cobalt-glow': 'rgba(37, 99, 235, 0.45)',
            'cove-blue': '#1d4ed8',
            'neon-violet': '#8b5cf6',
            'neon-magenta': '#ec4899',
            'ash-wood': '#ded6c8',
            chrome: '#94a3b8',
            titanium: '#f8fafc',
          }},
          fontFamily: {{
            syne: ['Syne', 'sans-serif'],
            oswald: ['Oswald', 'sans-serif'],
            sans: ['Inter', 'sans-serif'],
          }},
          animation: {{
            'pulse-glow': 'pulseGlow 2.5s infinite',
            'scanline': 'scanline 8s linear infinite',
            'steam-drift': 'steamDrift 4s ease-in-out infinite alternate',
          }},
          keyframes: {{
            pulseGlow: {{
              '0%, 100%': {{ opacity: '0.6', filter: 'drop-shadow(0 0 15px rgba(37, 99, 235, 0.5))' }},
              '50%': {{ opacity: '1', filter: 'drop-shadow(0 0 30px rgba(56, 189, 248, 0.85))' }},
            }},
            scanline: {{
              '0%': {{ transform: 'translateY(-100%)' }},
              '100%': {{ transform: 'translateY(1000%)' }},
            }},
            steamDrift: {{
              '0%': {{ transform: 'translateY(0) scale(1)', opacity: '0.4' }},
              '100%': {{ transform: 'translateY(-15px) scale(1.08)', opacity: '0.8' }},
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 7px;
    }}
    ::-webkit-scrollbar-track {{
      background: #07090e;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #1e293b;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #2563eb;
    }}

    /* Kinetic Glassmorphism with Cobalt Coves */
    .glass-panel {{
      background: rgba(15, 19, 28, 0.75);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .glass-panel-cobalt {{
      background: rgba(15, 19, 28, 0.84);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(37, 99, 235, 0.35);
      box-shadow: 0 0 30px rgba(37, 99, 235, 0.12);
    }}
    .glass-panel-violet {{
      background: rgba(15, 19, 28, 0.84);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(139, 92, 246, 0.35);
      box-shadow: 0 0 30px rgba(139, 92, 246, 0.12);
    }}
    .text-glow-cobalt {{
      text-shadow: 0 0 20px rgba(56, 189, 248, 0.65);
    }}

    /* Architectural Ceiling Cove Glow Box (Matches Midtown Fitness Ceiling Photos) */
    .cove-border {{
      border: 2px solid rgba(37, 99, 235, 0.6);
      box-shadow: 0 0 25px rgba(37, 99, 235, 0.35), inset 0 0 20px rgba(37, 99, 235, 0.2);
    }}
    .cove-border-violet {{
      border: 2px solid rgba(139, 92, 246, 0.6);
      box-shadow: 0 0 25px rgba(139, 92, 246, 0.35), inset 0 0 20px rgba(139, 92, 246, 0.2);
    }}

    /* Subtle Architectural Cyber Grid */
    .cyber-grid {{
      background-size: 40px 40px;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    }}

    /* Interactive Transformation Comparison Slider */
    .comparison-container {{
      position: relative;
      overflow: hidden;
      user-select: none;
    }}
    .comparison-before {{
      position: absolute;
      top: 0;
      left: 0;
      height: 100%;
      overflow: hidden;
      width: 50%;
      border-right: 2px solid #38bdf8;
      box-shadow: 5px 0 25px rgba(56, 189, 248, 0.4);
    }}

    /* Slider input */
    input[type=range] {{
      -webkit-appearance: none;
      background: #141824;
      border-radius: 9999px;
      height: 6px;
    }}
    input[type=range]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #38bdf8;
      cursor: pointer;
      box-shadow: 0 0 12px #2563eb;
      border: 2px solid #ffffff;
    }}
  </style>
</head>

<body class="bg-obsidian text-titanium font-sans antialiased selection:bg-cobalt-bright selection:text-obsidian min-h-screen relative overflow-x-hidden cyber-grid pb-24 md:pb-0">

  <!-- Ambient Blue & Indigo Architectural Halos (Matching Midtown Lighting) -->
  <div class="fixed top-0 left-1/4 w-[600px] h-[600px] bg-blue-600/12 rounded-full blur-[160px] pointer-events-none -z-10"></div>
  <div class="fixed bottom-1/3 right-10 w-[650px] h-[650px] bg-indigo-600/12 rounded-full blur-[180px] pointer-events-none -z-10"></div>
  <div class="fixed top-2/3 left-10 w-[500px] h-[500px] bg-violet-600/10 rounded-full blur-[150px] pointer-events-none -z-10"></div>

  <!-- Top Announcement Bar (Live Facility Telemetry) -->
  <div class="bg-carbon/95 border-b border-white/10 px-4 py-2 text-xs backdrop-blur-md sticky top-0 z-50">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <!-- Live Status & Mumbai Time -->
      <div class="flex items-center gap-3">
        <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 font-medium border border-emerald-500/30">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 -ml-2.5"></span>
          OPEN TODAY TILL 11:00 PM
        </span>
        <span class="hidden sm:inline text-chrome/70">|</span>
        <span class="hidden sm:inline text-chrome/90 flex items-center gap-1">
          <i data-lucide="map-pin" class="w-3 h-3 text-cobalt-bright"></i>
          Dr. Annie Besant Rd, opp. Old Passport Office, Worli
        </span>
      </div>

      <!-- Quick Action Contacts -->
      <div class="flex items-center gap-4 text-xs">
        <a href="tel:9819999103" class="flex items-center gap-1.5 text-titanium hover:text-cobalt-bright transition-colors font-semibold">
          <i data-lucide="phone-call" class="w-3.5 h-3.5 text-cobalt-bright"></i>
          <span>+91 9819999103</span>
        </a>
        <a href="https://wa.me/919819999103?text=Hi%20Midtown%20Fitness%2C%20I%20want%20to%20book%20my%20free%20workout%20session%20and%20trial%20pass." 
           target="_blank" 
           class="hidden md:flex items-center gap-1 text-emerald-400 hover:text-emerald-300 font-medium transition-colors">
          <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
          <span>WhatsApp VIP Desk</span>
        </a>
      </div>
    </div>
  </div>

  <!-- Primary Navigation -->
  <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between relative z-40">
    <div class="flex items-center gap-3">
      <!-- High-tech Logo Icon matching Blue Neon Cove -->
      <div class="relative w-11 h-11 rounded-xl bg-gradient-to-br from-cobalt-bright via-cobalt-neon to-neon-violet p-[1.5px] shadow-[0_0_20px_rgba(37,99,235,0.5)]">
        <div class="w-full h-full bg-obsidian rounded-[10px] flex items-center justify-center">
          <i data-lucide="dumbbell" class="w-6 h-6 text-cobalt-bright"></i>
        </div>
      </div>
      <div>
        <div class="font-syne font-extrabold text-xl tracking-wider text-titanium flex items-center gap-1">
          MIDTOWN <span class="text-transparent bg-clip-text bg-gradient-to-r from-cobalt-bright via-cobalt-neon to-neon-violet">FITNESS</span>
        </div>
        <div class="text-[10px] font-mono tracking-widest text-chrome uppercase">WORLI • MUMBAI 400030</div>
      </div>
    </div>

    <!-- Desktop Navigation Links -->
    <div class="hidden xl:flex items-center gap-6 text-xs font-semibold text-chrome">
      <a href="#gallery" class="hover:text-cobalt-bright transition-colors flex items-center gap-1">
        <span class="w-1.5 h-1.5 rounded-full bg-cobalt-bright"></span> Gym Tour
      </a>
      <a href="#zones" class="hover:text-cobalt-bright transition-colors">Training Zones</a>
      <a href="#combat-zumba" class="hover:text-cobalt-bright transition-colors">MMA & Zumba</a>
      <a href="#trainers" class="hover:text-cobalt-bright transition-colors">Master Trainers</a>
      <a href="#transformations" class="hover:text-cobalt-bright transition-colors">Transformations</a>
      <a href="#steam" class="hover:text-cobalt-bright transition-colors">Steam Sanctuary</a>
      <a href="#calculator" class="hover:text-cobalt-bright transition-colors">AI Macro Split</a>
      <a href="#schedule" class="hover:text-cobalt-bright transition-colors">Classes</a>
      <a href="#pricing" class="hover:text-cobalt-bright transition-colors">Passes</a>
    </div>

    <!-- Header Actions -->
    <div class="flex items-center gap-3">
      <button id="sfx-toggle-btn" onclick="toggleAudioFx()" title="Toggle Interface SFX" 
              class="w-9 h-9 rounded-lg glass-panel flex items-center justify-center text-chrome hover:text-cobalt-bright hover:border-cobalt-bright/40 transition-all">
        <i id="sfx-icon" data-lucide="volume-2" class="w-4 h-4"></i>
      </button>

      <button onclick="openModal('passModal')" 
              class="relative group overflow-hidden px-4 sm:px-5 py-2.5 rounded-xl font-oswald tracking-wider uppercase text-sm font-bold bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_20px_rgba(37,99,235,0.4)] hover:shadow-[0_0_30px_rgba(56,189,248,0.7)] transition-all duration-300 transform hover:-translate-y-0.5">
        <span class="relative z-10 flex items-center gap-1.5">
          <i data-lucide="zap" class="w-4 h-4 fill-current"></i>
          CLAIM 1-DAY PASS
        </span>
        <div class="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
      </button>
    </div>
  </nav>

  <!-- Hero Section with Architectural Blue Neon Ceiling Theme & Live Pulse -->
  <section class="relative pt-6 pb-16 md:py-20 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        
        <!-- Left Hero Content -->
        <div class="lg:col-span-7 space-y-6">
          
          <div class="flex flex-wrap items-center gap-2">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full glass-panel border border-cobalt-neon/40 text-xs text-titanium">
              <div class="flex items-center text-amber-400">
                <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                <i data-lucide="star" class="w-3.5 h-3.5 fill-current"></i>
                <i data-lucide="star" class="w-3.5 h-3.5 text-chrome"></i>
              </div>
              <span class="font-bold text-white">4.0 ★ Verified</span>
              <span class="text-chrome/80">| 210+ Google Reviews</span>
            </div>

            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-500/10 text-cobalt-bright text-xs font-mono border border-blue-500/30">
              <i data-lucide="camera" class="w-3 h-3"></i>
              AUTHENTIC WORLI FACILITY PHOTOS
            </span>
          </div>

          <h1 class="text-4xl sm:text-6xl xl:text-7xl font-syne font-extrabold tracking-tight leading-[1.05] text-titanium">
            THE APEX OF <br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-cobalt-bright via-blue-400 to-neon-violet text-glow-cobalt">
              WORLI ATHLETICS.
            </span>
          </h1>

          <p class="text-base sm:text-lg text-chrome max-w-xl font-normal leading-relaxed">
            South Mumbai's hardcore high-tech training temple. Submerged in architectural cobalt neon coves, heavy Arsenal plate-loaded machinery, dedicated MMA cage, Zumba sound stage, and executive eucalyptus steam suites on Dr. Annie Besant Road.
          </p>

          <div class="flex flex-wrap gap-2 pt-1 text-xs">
            <span class="px-3 py-1.5 rounded-lg bg-carbon border border-white/10 text-white flex items-center gap-1.5">
              <i data-lucide="check" class="w-3.5 h-3.5 text-cobalt-bright"></i> Heavy Plate Iron Bay
            </span>
            <span class="px-3 py-1.5 rounded-lg bg-carbon border border-white/10 text-white flex items-center gap-1.5">
              <i data-lucide="check" class="w-3.5 h-3.5 text-cobalt-bright"></i> MMA & Muay Thai Cage
            </span>
            <span class="px-3 py-1.5 rounded-lg bg-carbon border border-white/10 text-white flex items-center gap-1.5">
              <i data-lucide="check" class="w-3.5 h-3.5 text-neon-magenta"></i> Zumba & Dance Stage
            </span>
            <span class="px-3 py-1.5 rounded-lg bg-carbon border border-white/10 text-white flex items-center gap-1.5">
              <i data-lucide="check" class="w-3.5 h-3.5 text-emerald-400"></i> Eucalyptus Steam Suite
            </span>
          </div>

          <div class="flex flex-wrap items-center gap-4 pt-3">
            <button onclick="openModal('passModal')" 
                    class="px-7 py-3.5 rounded-xl font-oswald text-base tracking-wider uppercase font-bold bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_25px_rgba(37,99,235,0.45)] hover:shadow-[0_0_35px_rgba(56,189,248,0.7)] transition-all transform hover:-translate-y-0.5 flex items-center gap-2">
              <i data-lucide="flame" class="w-5 h-5 fill-current"></i>
              BOOK FREE TRIAL PASS
            </button>
            <a href="https://wa.me/919819999103?text=Hi%20Midtown%20Fitness%2C%20I%20want%20to%20book%20my%20free%20workout%20session%20and%20trial%20pass." 
               target="_blank"
               class="px-6 py-3.5 rounded-xl font-oswald text-base tracking-wider uppercase font-bold glass-panel text-white hover:border-emerald-500/60 hover:text-emerald-400 transition-all flex items-center gap-2">
              <i data-lucide="message-square" class="w-4 h-4 text-emerald-400"></i>
              WHATSAPP CONCIERGE
            </a>
          </div>

          <div class="pt-4 grid grid-cols-3 gap-3 border-t border-white/10 max-w-lg text-xs text-chrome">
            <div class="flex items-center gap-2">
              <i data-lucide="car" class="w-4 h-4 text-cobalt-bright"></i>
              <span>Free On-Site Parking</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="shower-head" class="w-4 h-4 text-cobalt-bright"></i>
              <span>Steam & Showers</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="users" class="w-4 h-4 text-neon-violet"></i>
              <span>Certified Master PTs</span>
            </div>
          </div>
        </div>

        <!-- Right Hero: Live Gym Pulse -->
        <div id="pulse" class="lg:col-span-5 relative">
          <div class="relative glass-panel-cobalt rounded-3xl p-6 sm:p-7 overflow-hidden cove-border">
            <div class="absolute inset-0 bg-gradient-to-b from-transparent via-blue-400/5 to-transparent h-20 animate-scanline pointer-events-none"></div>

            <div class="flex items-center justify-between border-b border-white/10 pb-4 mb-5">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-cobalt-bright animate-pulse"></span>
                <span class="font-oswald tracking-wider uppercase text-sm font-bold text-white">LIVE WORLI GYM PULSE</span>
              </div>
              <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-cobalt-neon/20 text-cobalt-bright border border-cobalt-bright/30">
                SENSORS ONLINE
              </span>
            </div>

            <div class="space-y-3 mb-6">
              <div class="flex items-end justify-between">
                <div>
                  <div class="text-xs uppercase font-mono tracking-wider text-chrome">Current Floor Density</div>
                  <div id="live-density-pct" class="text-4xl sm:text-5xl font-syne font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cobalt-bright to-white">
                    38%
                  </div>
                </div>
                <div class="text-right">
                  <span id="live-density-badge" class="px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/15 text-emerald-400 border border-emerald-500/30">
                    Smooth Flow & Peak Energy
                  </span>
                  <div id="live-clock" class="text-[11px] font-mono text-chrome/80 mt-1">Local Time: Worli, Mumbai</div>
                </div>
              </div>

              <div class="w-full h-3 bg-carbon rounded-full overflow-hidden p-0.5 border border-white/10 relative">
                <div id="live-density-bar" class="h-full bg-gradient-to-r from-cobalt-bright via-cobalt-neon to-neon-violet rounded-full transition-all duration-700 w-[38%] shadow-[0_0_12px_#2563eb]"></div>
              </div>
            </div>

            <div class="space-y-3 pt-2 border-t border-white/10">
              <div class="flex items-center justify-between text-xs">
                <span class="font-semibold text-titanium flex items-center gap-1.5">
                  <i data-lucide="sliders" class="w-3.5 h-3.5 text-cobalt-bright"></i>
                  Scrub Hourly Crowding:
                </span>
                <span id="scrub-hour-display" class="font-mono text-cobalt-bright font-bold text-sm bg-obsidian/80 px-2 py-0.5 rounded border border-white/10">
                  3:30 PM (Midday Chill)
                </span>
              </div>

              <input type="range" id="hour-slider" min="6" max="23" step="0.5" value="15.5" class="w-full cursor-pointer accent-cobalt-bright" oninput="updateGymPulse(this.value)">

              <div class="grid grid-cols-18 gap-1 h-14 items-end pt-2 px-1" id="hourly-bars-container"></div>
              <div class="flex justify-between text-[10px] font-mono text-chrome/60 px-1">
                <span>06:00 AM</span>
                <span>12:00 PM</span>
                <span>06:00 PM</span>
                <span>11:00 PM</span>
              </div>
            </div>

            <div class="grid grid-cols-3 gap-2 mt-5 pt-4 border-t border-white/10 text-center">
              <div class="p-2 rounded-xl bg-obsidian/60 border border-white/5">
                <div class="text-[10px] font-mono text-chrome">Soundtrack</div>
                <div id="vibe-bpm" class="text-xs font-bold text-cobalt-bright mt-0.5">132 BPM Phonk</div>
              </div>
              <div class="p-2 rounded-xl bg-obsidian/60 border border-white/5">
                <div class="text-[10px] font-mono text-chrome">AC Climate</div>
                <div class="text-xs font-bold text-white mt-0.5">20.5°C Chilled</div>
              </div>
              <div class="p-2 rounded-xl bg-obsidian/60 border border-white/5">
                <div class="text-[10px] font-mono text-chrome">Steam Ready</div>
                <div class="text-xs font-bold text-emerald-400 mt-0.5">48°C Active</div>
              </div>
            </div>

          </div>
          <div class="absolute -bottom-4 -right-4 -z-10 w-full h-full rounded-3xl bg-gradient-to-r from-blue-600/25 to-purple-600/25 blur-xl"></div>
        </div>

      </div>
    </div>
  </section>

  <!-- AUTHENTIC GYM FACILITY GALLERY (Using Actual Uploaded Photos) -->
  <section id="gallery" class="py-16 bg-carbon/60 relative border-t border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-4">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cobalt-neon/15 border border-cobalt-bright/30 text-cobalt-bright text-xs font-mono mb-2">
            <i data-lucide="eye" class="w-3.5 h-3.5"></i>
            AUTHENTIC FACILITY TOUR
          </div>
          <h2 class="text-3xl sm:text-4xl font-syne font-extrabold text-titanium">
            INSIDE MIDTOWN WORLI HQ
          </h2>
          <p class="text-chrome text-xs sm:text-sm mt-1 max-w-xl">
            Real untouched photography of our Adarsh Nagar facility: signature architectural blue neon ceiling coves, Scandinavian ash wood floors, and commercial strength bays.
          </p>
        </div>

        <div class="flex items-center gap-2 text-xs font-mono text-chrome">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>Photos from Midtown Fitness, Shop 01 Madhu Hans</span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
        
        <!-- Photo 1: Cardio Arena -->
        <div class="group relative rounded-2xl overflow-hidden cove-border bg-obsidian flex flex-col">
          <div class="h-56 overflow-hidden relative">
            <img src="{img_cardio_arena}" alt="Midtown Fitness Neon Cardio Arena" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian via-transparent to-transparent"></div>
            <span class="absolute top-3 left-3 px-2 py-0.5 rounded bg-black/80 backdrop-blur-md text-[10px] font-mono text-cobalt-bright border border-cobalt-bright/40">
              CARDIO ARENA
            </span>
          </div>
          <div class="p-4 space-y-1.5 flex-1 flex flex-col justify-between">
            <div>
              <div class="text-sm font-bold font-syne text-white">Neon Cardio & Spin Fleet</div>
              <p class="text-xs text-chrome mt-1">Matrix ClimbMill stairmasters and Bluetooth spin cycles under vibrant cobalt ceiling lights.</p>
            </div>
            <div class="text-[11px] font-mono text-cobalt-bright pt-2 border-t border-white/10">
              ● High-Velocity Air-Wash Climate
            </div>
          </div>
        </div>

        <!-- Photo 2: Plate-Loaded Hack Squat -->
        <div class="group relative rounded-2xl overflow-hidden cove-border-violet bg-obsidian flex flex-col">
          <div class="h-56 overflow-hidden relative">
            <img src="{img_hack_squat}" alt="Midtown Fitness Plate Hack Squat Bay" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian via-transparent to-transparent"></div>
            <span class="absolute top-3 left-3 px-2 py-0.5 rounded bg-black/80 backdrop-blur-md text-[10px] font-mono text-neon-violet border border-neon-violet/40">
              HEAVY IRON BAY
            </span>
          </div>
          <div class="p-4 space-y-1.5 flex-1 flex flex-col justify-between">
            <div>
              <div class="text-sm font-bold font-syne text-white">Heavy Plate Hack Squat</div>
              <p class="text-xs text-chrome mt-1">45° linear bearing hack squat, heavy leg press, and Olympic power racks for heavy compound lifting.</p>
            </div>
            <div class="text-[11px] font-mono text-neon-violet pt-2 border-t border-white/10">
              ● Up to 600kg Load Capacity
            </div>
          </div>
        </div>

        <!-- Photo 3: Main Floor & Branded Pillars -->
        <div class="group relative rounded-2xl overflow-hidden cove-border bg-obsidian flex flex-col">
          <div class="h-56 overflow-hidden relative">
            <img src="{img_floor_wide}" alt="Midtown Fitness Main Deck & Pillars" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian via-transparent to-transparent"></div>
            <span class="absolute top-3 left-3 px-2 py-0.5 rounded bg-black/80 backdrop-blur-md text-[10px] font-mono text-cobalt-bright border border-cobalt-bright/40">
              MAIN TRAINING DECK
            </span>
          </div>
          <div class="p-4 space-y-1.5 flex-1 flex flex-col justify-between">
            <div>
              <div class="text-sm font-bold font-syne text-white">Ash Wood Deck & Pillars</div>
              <p class="text-xs text-chrome mt-1">High-traction Scandinavian ash wood flooring, branded Midtown columns, and expansive free weights bay.</p>
            </div>
            <div class="text-[11px] font-mono text-cobalt-bright pt-2 border-t border-white/10">
              ● Heavy Rubber Dampening Layer
            </div>
          </div>
        </div>

        <!-- Photo 4: Selectorized Cable Crossovers -->
        <div class="group relative rounded-2xl overflow-hidden cove-border-violet bg-obsidian flex flex-col">
          <div class="h-56 overflow-hidden relative">
            <img src="{img_selectorized}" alt="Midtown Fitness Cable Towers" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian via-transparent to-transparent"></div>
            <span class="absolute top-3 left-3 px-2 py-0.5 rounded bg-black/80 backdrop-blur-md text-[10px] font-mono text-neon-violet border border-neon-violet/40">
              SELECTORIZED BAY
            </span>
          </div>
          <div class="p-4 space-y-1.5 flex-1 flex flex-col justify-between">
            <div>
              <div class="text-sm font-bold font-syne text-white">Cable Towers & Isolation</div>
              <p class="text-xs text-chrome mt-1">Dual adjustable pulley systems, seated cable rows, mirrored walls, and precision isolation stations.</p>
            </div>
            <div class="text-[11px] font-mono text-neon-violet pt-2 border-t border-white/10">
              ● Full Biomechanical Cable Arc
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Interactive 3D Floorplan & Equipment Zone Deck -->
  <section id="zones" class="py-20 bg-obsidian relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
        <div>
          <div class="text-xs font-mono font-bold uppercase tracking-widest text-cobalt-bright mb-2 flex items-center gap-2">
            <span class="w-2 h-0.5 bg-cobalt-bright"></span> FLOORPLAN & TRAINING ZONES
          </div>
          <h2 class="text-3xl sm:text-5xl font-syne font-extrabold text-titanium">
            ENGINEERED <span class="text-transparent bg-clip-text bg-gradient-to-r from-cobalt-bright via-blue-400 to-neon-violet">WAR ZONES.</span>
          </h2>
          <p class="text-chrome text-sm sm:text-base mt-2 max-w-xl">
            Explore Midtown's specialized sectors engineered for maximum hypertrophy, high-tempo combat, dance conditioning, and cardio endurance.
          </p>
        </div>

        <div class="flex flex-wrap gap-2 p-1.5 rounded-2xl bg-carbon border border-white/10 self-start md:self-auto">
          <button onclick="switchZone('iron')" id="tab-iron" class="zone-tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_15px_rgba(37,99,235,0.4)]">
            ZONE A: IRON BAY
          </button>
          <button onclick="switchZone('cardio')" id="tab-cardio" class="zone-tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all text-chrome hover:text-white">
            ZONE B: NEON CARDIO
          </button>
          <button onclick="switchZone('combat')" id="tab-combat" class="zone-tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all text-chrome hover:text-white">
            ZONE C: MMA & COMBAT
          </button>
          <button onclick="switchZone('zumba')" id="tab-zumba" class="zone-tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all text-chrome hover:text-white">
            ZONE D: ZUMBA STUDIO
          </button>
        </div>
      </div>

      <!-- Active Zone Interactive Showcase Deck -->
      <div id="zone-display-container" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center glass-panel-cobalt rounded-3xl p-6 sm:p-8 cove-border transition-all duration-500">
        
        <div class="lg:col-span-7 relative group overflow-hidden rounded-2xl border border-white/15 h-[340px] sm:h-[420px]">
          <img id="zone-image" 
               src="{img_hack_squat}" 
               alt="Midtown Fitness Zone" 
               class="w-full h-full object-cover object-center transform group-hover:scale-105 transition-transform duration-700">
          
          <div class="absolute inset-0 bg-gradient-to-t from-obsidian via-obsidian/30 to-transparent"></div>
          
          <div id="zone-glow-ambient" class="absolute inset-0 border-2 border-cobalt-bright/40 rounded-2xl pointer-events-none shadow-[inset_0_0_30px_rgba(37,99,235,0.3)]"></div>

          <div class="absolute top-4 left-4 glass-panel px-3 py-1.5 rounded-lg border border-white/20 text-xs font-mono text-cobalt-bright flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-cobalt-bright animate-ping"></span>
            <span id="zone-code-tag">WORLI HQ // ZONE-A</span>
          </div>

          <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between glass-panel p-3 rounded-xl border border-white/20">
            <div>
              <div class="text-[10px] font-mono text-chrome">BIOMECHANICAL FOCUS</div>
              <div id="zone-focus-text" class="text-sm font-bold text-white">Compound Overload & Heavy Hypertrophy</div>
            </div>
            <button onclick="openModal('passModal')" class="px-3.5 py-1.5 rounded-lg bg-cobalt-bright text-obsidian text-xs font-oswald font-bold tracking-wider hover:bg-white transition-colors">
              TEST THIS ZONE
            </button>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6">
          
          <div>
            <div id="zone-subtitle" class="text-xs font-mono text-cobalt-bright uppercase tracking-wider">HARDCORE HYPERTROPHY HUB</div>
            <h3 id="zone-title" class="text-2xl sm:text-3xl font-syne font-extrabold text-titanium mt-1">
              Plate-Loaded Iron Bay
            </h3>
            <p id="zone-description" class="text-chrome text-sm mt-2 leading-relaxed">
              Designed for serious lifters in Worli. Zero queueing on leg day with heavy-duty 45° hack squats, Olympic power racks, calibrated steel plates, and dumbbells up to 50kg.
            </p>
          </div>

          <div class="space-y-2">
            <div class="text-xs font-mono uppercase text-chrome">Target Muscle Primaries:</div>
            <div id="zone-muscles-list" class="flex flex-wrap gap-2">
              <span class="px-2.5 py-1 rounded-md bg-cobalt-neon/15 border border-cobalt-bright/30 text-cobalt-bright text-xs font-medium">Quadriceps</span>
              <span class="px-2.5 py-1 rounded-md bg-cobalt-neon/15 border border-cobalt-bright/30 text-cobalt-bright text-xs font-medium">Hamstrings & Glutes</span>
              <span class="px-2.5 py-1 rounded-md bg-cobalt-neon/15 border border-cobalt-bright/30 text-cobalt-bright text-xs font-medium">Pectorals</span>
              <span class="px-2.5 py-1 rounded-md bg-cobalt-neon/15 border border-cobalt-bright/30 text-cobalt-bright text-xs font-medium">Latissimus Dorsi</span>
            </div>
          </div>

          <div class="space-y-3">
            <div class="text-xs font-mono uppercase text-chrome flex justify-between">
              <span>Verified Machine Inventory</span>
              <span class="text-cobalt-bright">100% Calibrated</span>
            </div>
            <div id="zone-equipment-grid" class="grid grid-cols-2 gap-2 text-xs">
              <div class="p-2.5 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-cobalt-bright flex-shrink-0"></i>
                <span class="text-titanium">45° Plate Hack Squat</span>
              </div>
              <div class="p-2.5 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-cobalt-bright flex-shrink-0"></i>
                <span class="text-titanium">Olympic Power Racks</span>
              </div>
              <div class="p-2.5 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-cobalt-bright flex-shrink-0"></i>
                <span class="text-titanium">Heavy Leg Press 600kg</span>
              </div>
              <div class="p-2.5 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-cobalt-bright flex-shrink-0"></i>
                <span class="text-titanium">Dumbbells 2.5kg - 50kg</span>
              </div>
            </div>
          </div>

          <div class="flex items-center justify-between p-3 rounded-xl bg-obsidian/50 border border-white/5 text-xs text-chrome font-mono">
            <span>FLOOR SURFACE: High-Traction Ash Wood & Rubber</span>
            <span class="text-cobalt-bright">ISO CERTIFIED</span>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- DEDICATED MMA COMBAT & ZUMBA SHOWCASE SECTION -->
  <section id="combat-zumba" class="py-20 bg-carbon/50 relative border-t border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-14">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-neon-violet/15 border border-neon-violet/30 text-neon-violet text-xs font-mono mb-3">
          <i data-lucide="swords" class="w-3.5 h-3.5"></i>
          DUAL ENERGY SPECIALIZATION
        </div>
        <h2 class="text-3xl sm:text-5xl font-syne font-extrabold text-titanium">
          MMA COMBAT ARENA & <span class="text-transparent bg-clip-text bg-gradient-to-r from-neon-violet via-pink-400 to-cobalt-bright">ZUMBA SOUND STAGE</span>
        </h2>
        <p class="text-chrome text-sm sm:text-base mt-3">
          Whether you want high-velocity striking and grappling power or high-calorie rhythmic Latin dance conditioning, Midtown Worli has certified masters on the deck.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        
        <!-- Left: MMA Combat Arena -->
        <div class="glass-panel rounded-3xl p-6 sm:p-8 cove-border-violet flex flex-col justify-between relative overflow-hidden group">
          <div class="space-y-5">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-purple-500/20 text-neon-violet border border-purple-500/40">
                COMBAT & STRIKING
              </span>
              <span class="text-xs font-mono text-chrome">LED BY KRU SIDDHARTH</span>
            </div>

            <div>
              <h3 class="text-2xl sm:text-3xl font-syne font-extrabold text-white">
                Midtown MMA & Fight Camp
              </h3>
              <p class="text-xs sm:text-sm text-chrome mt-2 leading-relaxed">
                Full-contact combat conditioning engineered for functional power, agility, and mental tenacity. Train striking combinations, Muay Thai low kicks, clinch defense, and high-intensity bag rounds.
              </p>
            </div>

            <div class="grid grid-cols-2 gap-3 text-xs">
              <div class="p-3 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="shield" class="w-4 h-4 text-neon-violet flex-shrink-0"></i>
                <span class="text-white">Fairtex 6ft Heavy Bags</span>
              </div>
              <div class="p-3 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="activity" class="w-4 h-4 text-neon-violet flex-shrink-0"></i>
                <span class="text-white">Pro Ring Countdown Timers</span>
              </div>
              <div class="p-3 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="zap" class="w-4 h-4 text-neon-violet flex-shrink-0"></i>
                <span class="text-white">Muay Thai Thai Pads</span>
              </div>
              <div class="p-3 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="target" class="w-4 h-4 text-neon-violet flex-shrink-0"></i>
                <span class="text-white">Grappling & Sparring Mats</span>
              </div>
            </div>

            <div class="p-4 rounded-2xl bg-obsidian/50 border border-white/10 flex items-center justify-between text-xs">
              <div>
                <div class="font-bold text-white">Next Fight Camp Session:</div>
                <div class="text-chrome font-mono">Today • 11:00 AM & 07:30 PM</div>
              </div>
              <span class="px-2.5 py-1 rounded bg-neon-violet/20 text-neon-violet font-mono font-bold">Only 2 Spots Left</span>
            </div>
          </div>

          <div class="pt-6">
            <button onclick="openBookingModal('kickboxing-01')" class="w-full py-3 rounded-xl font-oswald text-sm uppercase tracking-wider font-bold bg-neon-violet hover:bg-violet-400 text-white transition-all shadow-[0_0_20px_rgba(139,92,246,0.3)]">
              RESERVE MMA & FIGHT PASS
            </button>
          </div>
        </div>

        <!-- Right: Zumba Sound Stage -->
        <div class="glass-panel rounded-3xl p-6 sm:p-8 cove-border flex flex-col justify-between relative overflow-hidden group">
          <div class="space-y-5">
            <div class="flex items-center justify-between">
              <span class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-pink-500/20 text-neon-magenta border border-pink-500/40">
                DANCE FITNESS & HIGH-CALORIE
              </span>
              <span class="text-xs font-mono text-chrome">LED BY COACH NATASHA</span>
            </div>

            <div>
              <h3 class="text-2xl sm:text-3xl font-syne font-extrabold text-white">
                Zumba & Dance Sound Stage
              </h3>
              <p class="text-xs sm:text-sm text-chrome mt-2 leading-relaxed">
                South Mumbai's most electric group sweat session. Incinerate 600-800 calories in 60 minutes with high-tempo Latin beats, Bollywood cardio remixes, and joint-friendly sprung floor acoustics.
              </p>
            </div>

            <div class="grid grid-cols-2 gap-3 text-xs">
              <div class="p-3 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="music" class="w-4 h-4 text-neon-magenta flex-shrink-0"></i>
                <span class="text-white">Concert Grade Audio Rig</span>
              </div>
              <div class="p-3 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="sparkles" class="w-4 h-4 text-neon-magenta flex-shrink-0"></i>
                <span class="text-white">Atmospheric Laser Strobes</span>
              </div>
              <div class="p-3 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="flame" class="w-4 h-4 text-neon-magenta flex-shrink-0"></i>
                <span class="text-white">650+ kcal Caloric Output</span>
              </div>
              <div class="p-3 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2">
                <i data-lucide="layers" class="w-4 h-4 text-neon-magenta flex-shrink-0"></i>
                <span class="text-white">Shock-Absorbing Wood Floor</span>
              </div>
            </div>

            <div class="p-4 rounded-2xl bg-obsidian/50 border border-white/10 flex items-center justify-between text-xs">
              <div>
                <div class="font-bold text-white">Next Zumba Beat Stage:</div>
                <div class="text-chrome font-mono">Today • 06:00 PM (Prime Time)</div>
              </div>
              <span class="px-2.5 py-1 rounded bg-pink-500/20 text-neon-magenta font-mono font-bold">3 Spots Remaining</span>
            </div>
          </div>

          <div class="pt-6">
            <button onclick="openBookingModal('zumba-01')" class="w-full py-3 rounded-xl font-oswald text-sm uppercase tracking-wider font-bold bg-gradient-to-r from-pink-500 to-cobalt-bright text-white transition-all shadow-[0_0_20px_rgba(236,72,153,0.3)]">
              RESERVE ZUMBA STAGE PASS
            </button>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- MASTER COACHES & TRAINER ROSTER -->
  <section id="trainers" class="py-20 relative bg-obsidian">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
        <div>
          <div class="text-xs font-mono font-bold uppercase tracking-widest text-cobalt-bright mb-2 flex items-center gap-2">
            <span class="w-2 h-0.5 bg-cobalt-bright"></span> CERTIFIED BIOMECHANICS & COACHING STAFF
          </div>
          <h2 class="text-3xl sm:text-5xl font-syne font-extrabold text-titanium">
            MIDTOWN MASTER <span class="text-transparent bg-clip-text bg-gradient-to-r from-cobalt-bright to-neon-violet">TRAINERS</span>
          </h2>
          <p class="text-chrome text-sm sm:text-base mt-2 max-w-xl">
            Certified elite trainers who understand anatomical torque, progressive overload, and personalized nutritional biochemistry.
          </p>
        </div>

        <a href="https://wa.me/919819999103?text=Hi%20Midtown%20Fitness%2C%20I%20want%20to%20book%20a%20personal%20trainer%20consultation." target="_blank"
           class="px-5 py-2.5 rounded-xl glass-panel text-xs text-white hover:text-cobalt-bright border border-white/15 flex items-center gap-2 self-start md:self-auto font-mono">
          <i data-lucide="message-circle" class="w-4 h-4 text-emerald-400"></i>
          Request 1-on-1 PT Evaluation
        </a>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- Trainer 1: Coach Aryan Sawant -->
        <div class="glass-panel rounded-3xl p-6 cove-border flex flex-col justify-between hover:scale-[1.02] transition-transform duration-300">
          <div class="space-y-4">
            <div class="flex items-center gap-3">
              <div class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-cobalt-bright to-cobalt-neon p-0.5 shadow-[0_0_15px_rgba(37,99,235,0.4)]">
                <div class="w-full h-full bg-carbon rounded-[14px] flex items-center justify-center font-syne font-extrabold text-lg text-white">
                  AS
                </div>
              </div>
              <div>
                <h4 class="text-base font-bold font-syne text-white">Aryan Sawant</h4>
                <div class="text-xs text-cobalt-bright font-mono">Head Biomechanics & PT</div>
              </div>
            </div>

            <div class="space-y-2 text-xs">
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Credentials:</span>
                <span class="font-bold text-white font-mono">CSCS • ISSA Elite • K11</span>
              </div>
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Experience:</span>
                <span class="font-bold text-white font-mono">9+ Years</span>
              </div>
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Athletes Transformed:</span>
                <span class="font-bold text-emerald-400 font-mono">320+ Clients</span>
              </div>
            </div>

            <p class="text-xs text-chrome leading-relaxed">
              Specialist in compound powerlifting, heavy plate hypertrophy, and structural posture restoration.
            </p>
          </div>

          <div class="pt-5 border-t border-white/10 mt-4">
            <button onclick="bookTrainer('Coach Aryan Sawant', 'Strength & Biomechanics')" class="w-full py-2.5 rounded-xl text-xs font-oswald uppercase tracking-wider font-bold bg-white/10 hover:bg-cobalt-bright hover:text-obsidian text-white transition-all flex items-center justify-center gap-1.5">
              <span>BOOK 1-ON-1 PT</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- Trainer 2: Kru Siddharth Verma -->
        <div class="glass-panel rounded-3xl p-6 cove-border-violet flex flex-col justify-between hover:scale-[1.02] transition-transform duration-300">
          <div class="space-y-4">
            <div class="flex items-center gap-3">
              <div class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-neon-violet to-pink-500 p-0.5 shadow-[0_0_15px_rgba(139,92,246,0.4)]">
                <div class="w-full h-full bg-carbon rounded-[14px] flex items-center justify-center font-syne font-extrabold text-lg text-white">
                  SV
                </div>
              </div>
              <div>
                <h4 class="text-base font-bold font-syne text-white">Siddharth Verma</h4>
                <div class="text-xs text-neon-violet font-mono">MMA & Combat Director</div>
              </div>
            </div>

            <div class="space-y-2 text-xs">
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Credentials:</span>
                <span class="font-bold text-white font-mono">WMC Muay Thai • Pro MMA</span>
              </div>
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Experience:</span>
                <span class="font-bold text-white font-mono">8+ Years</span>
              </div>
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Combat Rounds:</span>
                <span class="font-bold text-emerald-400 font-mono">1,500+ Coached</span>
              </div>
            </div>

            <p class="text-xs text-chrome leading-relaxed">
              National MMA Gold Medalist specializing in fight conditioning, Muay Thai clinch, and high-velocity bag drills.
            </p>
          </div>

          <div class="pt-5 border-t border-white/10 mt-4">
            <button onclick="bookTrainer('Kru Siddharth Verma', 'MMA & Striking')" class="w-full py-2.5 rounded-xl text-xs font-oswald uppercase tracking-wider font-bold bg-white/10 hover:bg-neon-violet hover:text-white text-white transition-all flex items-center justify-center gap-1.5">
              <span>BOOK MMA SESSION</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- Trainer 3: Coach Natasha Fernandez -->
        <div class="glass-panel rounded-3xl p-6 cove-border flex flex-col justify-between hover:scale-[1.02] transition-transform duration-300">
          <div class="space-y-4">
            <div class="flex items-center gap-3">
              <div class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-pink-500 to-cobalt-bright p-0.5 shadow-[0_0_15px_rgba(236,72,153,0.4)]">
                <div class="w-full h-full bg-carbon rounded-[14px] flex items-center justify-center font-syne font-extrabold text-lg text-white">
                  NF
                </div>
              </div>
              <div>
                <h4 class="text-base font-bold font-syne text-white">Natasha Fernandez</h4>
                <div class="text-xs text-neon-magenta font-mono">Zumba & Dance Director</div>
              </div>
            </div>

            <div class="space-y-2 text-xs">
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Credentials:</span>
                <span class="font-bold text-white font-mono">ZIN™ Licensed • ACE Group</span>
              </div>
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Experience:</span>
                <span class="font-bold text-white font-mono">7+ Years</span>
              </div>
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Avg Calorie Burn:</span>
                <span class="font-bold text-emerald-400 font-mono">650+ kcal/class</span>
              </div>
            </div>

            <p class="text-xs text-chrome leading-relaxed">
              Certified choreography maestro blending Latin rhythms, energetic Bollywood beats, and joint-safe cardio flow.
            </p>
          </div>

          <div class="pt-5 border-t border-white/10 mt-4">
            <button onclick="bookTrainer('Coach Natasha Fernandez', 'Zumba & Dance Fitness')" class="w-full py-2.5 rounded-xl text-xs font-oswald uppercase tracking-wider font-bold bg-white/10 hover:bg-pink-500 hover:text-white text-white transition-all flex items-center justify-center gap-1.5">
              <span>JOIN ZUMBA CLASS</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- Trainer 4: Coach Dev Malhotra -->
        <div class="glass-panel rounded-3xl p-6 cove-border-violet flex flex-col justify-between hover:scale-[1.02] transition-transform duration-300">
          <div class="space-y-4">
            <div class="flex items-center gap-3">
              <div class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-cobalt-neon to-emerald-400 p-0.5 shadow-[0_0_15px_rgba(16,185,129,0.4)]">
                <div class="w-full h-full bg-carbon rounded-[14px] flex items-center justify-center font-syne font-extrabold text-lg text-white">
                  DM
                </div>
              </div>
              <div>
                <h4 class="text-base font-bold font-syne text-white">Dev Malhotra</h4>
                <div class="text-xs text-emerald-400 font-mono">Physique Recomp & Nutrition</div>
              </div>
            </div>

            <div class="space-y-2 text-xs">
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Credentials:</span>
                <span class="font-bold text-white font-mono">Crossfit L2 • PN2 Nutrition</span>
              </div>
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Experience:</span>
                <span class="font-bold text-white font-mono">6+ Years</span>
              </div>
              <div class="flex justify-between border-b border-white/5 pb-1">
                <span class="text-chrome">Fat Recomp Success:</span>
                <span class="font-bold text-emerald-400 font-mono">210+ Clients</span>
              </div>
            </div>

            <p class="text-xs text-chrome leading-relaxed">
              Metabolic conditioning specialist helping clients shred fat while sustaining heavy strength gains and lean muscle.
            </p>
          </div>

          <div class="pt-5 border-t border-white/10 mt-4">
            <button onclick="bookTrainer('Coach Dev Malhotra', 'Physique Recomp & Nutrition')" class="w-full py-2.5 rounded-xl text-xs font-oswald uppercase tracking-wider font-bold bg-white/10 hover:bg-emerald-400 hover:text-obsidian text-white transition-all flex items-center justify-center gap-1.5">
              <span>GET RECOMP PLAN</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- INTERACTIVE BEFORE & AFTER TRANSFORMATION SHOWCASE -->
  <section id="transformations" class="py-20 bg-carbon/50 relative border-t border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-14">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 text-xs font-mono mb-3">
          <i data-lucide="award" class="w-3.5 h-3.5"></i>
          VERIFIED ATHLETE TRANSFORMATIONS
        </div>
        <h2 class="text-3xl sm:text-5xl font-syne font-extrabold text-titanium">
          REAL WORLI MEMBERS. <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-cobalt-bright to-white">PROVEN PHYSIQUES.</span>
        </h2>
        <p class="text-chrome text-sm sm:text-base mt-3">
          Drag the interactive slider below to inspect actual body recomposition achieved right here on Dr. Annie Besant Road.
        </p>
      </div>

      <div class="max-w-4xl mx-auto glass-panel-cobalt rounded-3xl p-6 sm:p-8 cove-border mb-12">
        <div class="flex items-center justify-between mb-4">
          <div>
            <span class="text-xs font-mono text-cobalt-bright font-bold uppercase">FEATURED TRANSFORMATION // KUNAL PAREKH</span>
            <div class="text-lg font-syne font-bold text-white">16-Week Complete Athletic Body Recomposition</div>
          </div>
          <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 font-mono text-xs font-bold">
            -18 KG FAT SHRED
          </span>
        </div>

        <div class="relative w-full h-[320px] sm:h-[420px] rounded-2xl overflow-hidden comparison-container border border-white/15">
          
          <div class="absolute inset-0 w-full h-full bg-carbon flex items-center justify-center overflow-hidden">
            <img src="https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=1470&auto=format&fit=crop" 
                 alt="After Transformation Physique" 
                 class="w-full h-full object-cover">
            <div class="absolute bottom-4 right-4 bg-obsidian/85 backdrop-blur-md px-3 py-1.5 rounded-lg border border-emerald-500/40 text-xs font-mono text-emerald-400 font-bold">
              AFTER: 74 KG (11.2% BF)
            </div>
          </div>

          <div id="comparison-clip" class="comparison-before">
            <div class="w-full h-full min-w-[700px] sm:min-w-[900px] relative">
              <img src="https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?q=80&w=1470&auto=format&fit=crop" 
                   alt="Before Transformation Physique" 
                   class="w-full h-full object-cover filter contrast-90 brightness-75">
              <div class="absolute bottom-4 left-4 bg-obsidian/85 backdrop-blur-md px-3 py-1.5 rounded-lg border border-white/20 text-xs font-mono text-chrome font-bold">
                BEFORE: 92 KG (28.5% BF)
              </div>
            </div>
          </div>

          <div id="comparison-handle" class="absolute top-0 bottom-0 left-1/2 -ml-4 w-8 flex items-center justify-center pointer-events-none z-20">
            <div class="w-8 h-8 rounded-full bg-cobalt-bright text-obsidian shadow-[0_0_15px_#38bdf8] flex items-center justify-center font-bold text-xs">
              ↔
            </div>
          </div>

          <input type="range" id="transform-range" min="0" max="100" value="50" 
                 class="absolute inset-0 w-full h-full opacity-0 cursor-ew-resize z-30" 
                 oninput="updateComparisonSlider(this.value)">
        </div>

        <div class="flex items-center justify-between text-xs font-mono text-chrome mt-3 px-1">
          <span>◀ DRAG LEFT FOR AFTER</span>
          <span class="text-cobalt-bright">INTERACTIVE COMPARISON VIEWER</span>
          <span>DRAG RIGHT FOR BEFORE ▶</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-6 pt-5 border-t border-white/10 text-center text-xs">
          <div class="p-2.5 rounded-xl bg-obsidian/70 border border-white/5">
            <div class="text-[10px] font-mono text-chrome">Total Loss</div>
            <div class="text-sm font-bold text-white mt-0.5">-18.2 Kilograms</div>
          </div>
          <div class="p-2.5 rounded-xl bg-obsidian/70 border border-white/5">
            <div class="text-[10px] font-mono text-chrome">Body Fat Drop</div>
            <div class="text-sm font-bold text-emerald-400 mt-0.5">28.5% ➔ 11.2%</div>
          </div>
          <div class="p-2.5 rounded-xl bg-obsidian/70 border border-white/5">
            <div class="text-[10px] font-mono text-chrome">Timeframe</div>
            <div class="text-sm font-bold text-cobalt-bright mt-0.5">16 Dedicated Weeks</div>
          </div>
          <div class="p-2.5 rounded-xl bg-obsidian/70 border border-white/5">
            <div class="text-[10px] font-mono text-chrome">Assigned Coach</div>
            <div class="text-sm font-bold text-white mt-0.5">Coach Aryan Sawant</div>
          </div>
        </div>

      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        
        <div class="glass-panel p-6 rounded-3xl border border-white/10 space-y-4">
          <div class="flex items-center justify-between">
            <div>
              <span class="text-[11px] font-mono text-neon-magenta uppercase font-bold">CASE STUDY // PRIYA MERCHANT</span>
              <h4 class="text-lg font-syne font-bold text-white">Post-Pregnancy Core & Lean Recomp</h4>
            </div>
            <span class="px-2.5 py-1 rounded bg-pink-500/20 text-neon-magenta font-mono text-xs font-bold">-11 KG</span>
          </div>
          <div class="grid grid-cols-3 gap-2 text-center text-xs">
            <div class="p-2 bg-obsidian rounded-xl border border-white/5">
              <span class="text-chrome block text-[10px]">BEFORE</span>
              <span class="font-bold text-white">68 kg (31% BF)</span>
            </div>
            <div class="p-2 bg-obsidian rounded-xl border border-white/5">
              <span class="text-chrome block text-[10px]">AFTER</span>
              <span class="font-bold text-emerald-400">57 kg (19.5% BF)</span>
            </div>
            <div class="p-2 bg-obsidian rounded-xl border border-white/5">
              <span class="text-chrome block text-[10px]">PROGRAM</span>
              <span class="font-bold text-neon-magenta">Zumba + PT</span>
            </div>
          </div>
          <p class="text-xs text-chrome leading-relaxed">
            "Coach Natasha and Dev structured a clean calorie deficit with 3 days of Zumba Sound Stage and 2 days of strength training. Dropped 4 dress sizes in 12 weeks."
          </p>
        </div>

        <div class="glass-panel p-6 rounded-3xl border border-white/10 space-y-4">
          <div class="flex items-center justify-between">
            <div>
              <span class="text-[11px] font-mono text-cobalt-bright uppercase font-bold">CASE STUDY // ADITYA SEN</span>
              <h4 class="text-lg font-syne font-bold text-white">Skinny to Dense Powerlifter Frame</h4>
            </div>
            <span class="px-2.5 py-1 rounded bg-blue-500/20 text-cobalt-bright font-mono text-xs font-bold">+14 KG MUSCLE</span>
          </div>
          <div class="grid grid-cols-3 gap-2 text-center text-xs">
            <div class="p-2 bg-obsidian rounded-xl border border-white/5">
              <span class="text-chrome block text-[10px]">BEFORE</span>
              <span class="font-bold text-white">61 kg</span>
            </div>
            <div class="p-2 bg-obsidian rounded-xl border border-white/5">
              <span class="text-chrome block text-[10px]">AFTER</span>
              <span class="font-bold text-cobalt-bright">75 kg Lean Mass</span>
            </div>
            <div class="p-2 bg-obsidian rounded-xl border border-white/5">
              <span class="text-chrome block text-[10px]">SQUAT RECORD</span>
              <span class="font-bold text-emerald-400">150 kg PR</span>
            </div>
          </div>
          <p class="text-xs text-chrome leading-relaxed">
            "Started with zero power rack experience. Coach Aryan taught me proper bracing and biomechanics on the heavy iron bay. My squat went from 70kg to 150kg."
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- EXECUTIVE HYDRO-THERMAL EUCALYPTUS STEAM SANCTUARY -->
  <section id="steam" class="py-20 relative bg-obsidian">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        
        <!-- Left: Steam Sanctuary Description & Specs -->
        <div class="lg:col-span-6 space-y-6">
          <div>
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 text-xs font-mono mb-2">
              <i data-lucide="droplet" class="w-3.5 h-3.5"></i>
              HYDRO-THERMAL RECOVERY SUITE
            </div>
            <h2 class="text-3xl sm:text-5xl font-syne font-extrabold text-titanium">
              EUCALYPTUS STEAM <br>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cobalt-bright">
                SANCTUARY.
              </span>
            </h2>
            <p class="text-chrome text-sm sm:text-base mt-3 leading-relaxed">
              Flush metabolic waste and accelerate DOMS muscle repair. Midtown Worli features dual commercial-grade hydro-thermal steam chambers infused with organic eucalyptus aromatherapy vapor.
            </p>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
            <div class="p-3.5 rounded-2xl bg-carbon border border-white/10 flex items-start gap-3">
              <i data-lucide="zap" class="w-5 h-5 text-emerald-400 flex-shrink-0 mt-0.5"></i>
              <div>
                <div class="font-bold text-white">40% Accelerated Recovery</div>
                <div class="text-chrome mt-0.5">Enhances blood circulation, flushing lactic acid build-up after heavy leg day sessions.</div>
              </div>
            </div>

            <div class="p-3.5 rounded-2xl bg-carbon border border-white/10 flex items-start gap-3">
              <i data-lucide="wind" class="w-5 h-5 text-cobalt-bright flex-shrink-0 mt-0.5"></i>
              <div>
                <div class="font-bold text-white">Bronchial Airway Clearing</div>
                <div class="text-chrome mt-0.5">Pure Australian eucalyptus oil vapor clears respiratory passages and optimizes VO2 max.</div>
              </div>
            </div>

            <div class="p-3.5 rounded-2xl bg-carbon border border-white/10 flex items-start gap-3">
              <i data-lucide="sparkles" class="w-5 h-5 text-emerald-400 flex-shrink-0 mt-0.5"></i>
              <div>
                <div class="font-bold text-white">Cortisol Down-Regulation</div>
                <div class="text-chrome mt-0.5">Shifts the nervous system into parasympathetic relaxation, lowering systemic stress.</div>
              </div>
            </div>

            <div class="p-3.5 rounded-2xl bg-carbon border border-white/10 flex items-start gap-3">
              <i data-lucide="shower-head" class="w-5 h-5 text-cobalt-bright flex-shrink-0 mt-0.5"></i>
              <div>
                <div class="font-bold text-white">Rain Showers & Locker Suite</div>
                <div class="text-chrome mt-0.5">High-pressure rain showers, chilled citrus towels, and executive private restrooms.</div>
              </div>
            </div>
          </div>

          <div class="p-4 rounded-2xl glass-panel-cobalt cove-border flex items-center justify-between text-xs font-mono">
            <div class="flex items-center gap-3">
              <span class="w-3 h-3 rounded-full bg-emerald-400 animate-ping"></span>
              <div>
                <div class="text-white font-bold">Men's & Women's Chambers: READY</div>
                <div class="text-chrome">Current Temp: 48°C • 100% Humidity</div>
              </div>
            </div>
            <span class="px-2.5 py-1 rounded bg-emerald-500/20 text-emerald-400 font-bold">ALL PASSES INCLUDE STEAM</span>
          </div>

        </div>

        <div class="lg:col-span-6">
          <div class="relative rounded-3xl overflow-hidden cove-border glass-panel p-2">
            <div class="w-full h-[380px] rounded-2xl overflow-hidden relative bg-obsidian">
              <img src="https://images.unsplash.com/photo-1540555700478-4be289fbecef?q=80&w=1470&auto=format&fit=crop" 
                   alt="Midtown Fitness Steam Sanctuary" 
                   class="w-full h-full object-cover filter brightness-80 contrast-110">
              
              <div class="absolute inset-0 bg-gradient-to-t from-obsidian via-obsidian/40 to-transparent"></div>
              <div class="absolute inset-0 bg-gradient-to-t from-emerald-500/10 via-transparent to-blue-500/10 animate-steam-drift pointer-events-none"></div>

              <div class="absolute top-4 left-4 glass-panel px-3 py-1.5 rounded-lg border border-white/20 text-xs font-mono text-emerald-400 flex items-center gap-2">
                <i data-lucide="flame" class="w-3.5 h-3.5"></i>
                <span>THERMAL SUITE // 48°C MIST</span>
              </div>

              <div class="absolute bottom-4 left-4 right-4 glass-panel p-4 rounded-xl border border-white/20 flex items-center justify-between">
                <div>
                  <div class="text-sm font-bold text-white">Daily Steam Sanctuary Hours</div>
                  <div class="text-xs text-chrome">Open Daily: 06:00 AM - 10:30 PM (Daily Sanitization Cycles)</div>
                </div>
                <button onclick="openModal('passModal')" class="px-3.5 py-1.5 rounded-lg bg-emerald-400 text-obsidian text-xs font-oswald font-bold tracking-wider hover:bg-white transition-colors">
                  BOOK PASS
                </button>
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Smart AI Workout & Macro Split Calculator -->
  <section id="calculator" class="py-20 relative bg-carbon/40 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-14">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cobalt-neon/15 border border-cobalt-bright/30 text-cobalt-bright text-xs font-mono mb-3">
          <i data-lucide="cpu" class="w-3.5 h-3.5"></i>
          CLIENT-SIDE ALGORITHMIC ENGINE
        </div>
        <h2 class="text-3xl sm:text-5xl font-syne font-extrabold text-titanium">
          SMART AI SPLIT & <span class="text-transparent bg-clip-text bg-gradient-to-r from-cobalt-bright via-blue-400 to-neon-violet">MACRO CALCULATOR</span>
        </h2>
        <p class="text-chrome text-sm sm:text-base mt-3">
          Calculate your exact caloric baseline, protein split, and a customized workout architecture based on your biomechanical targets.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <div class="lg:col-span-5 glass-panel rounded-3xl p-6 sm:p-8 border border-white/15 space-y-5">
          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <h3 class="font-oswald text-lg font-bold tracking-wider uppercase text-white flex items-center gap-2">
              <i data-lucide="user-check" class="w-4 h-4 text-cobalt-bright"></i>
              Your Physical Parameters
            </h3>
            <span class="text-[11px] font-mono text-chrome">Precision Metric</span>
          </div>

          <form id="calc-form" onsubmit="event.preventDefault(); calculateSplit();" class="space-y-4">
            <div>
              <label class="block text-xs font-mono uppercase text-chrome mb-1.5">Gender Biological Base</label>
              <div class="grid grid-cols-2 gap-2">
                <button type="button" onclick="setGender('male')" id="gender-male" class="gender-btn py-2.5 px-3 rounded-xl border border-cobalt-bright bg-blue-500/20 text-white text-xs font-bold font-oswald tracking-wide flex items-center justify-center gap-2">
                  <i data-lucide="mars" class="w-3.5 h-3.5 text-cobalt-bright"></i> MALE
                </button>
                <button type="button" onclick="setGender('female')" id="gender-female" class="gender-btn py-2.5 px-3 rounded-xl border border-white/10 bg-obsidian text-chrome hover:text-white text-xs font-bold font-oswald tracking-wide flex items-center justify-center gap-2">
                  <i data-lucide="venus" class="w-3.5 h-3.5 text-pink-400"></i> FEMALE
                </button>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="block text-xs font-mono uppercase text-chrome mb-1.5">Age (Years)</label>
                <input type="number" id="calc-age" value="26" min="15" max="80" class="w-full bg-obsidian border border-white/15 rounded-xl px-3.5 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none transition-colors">
              </div>
              <div>
                <label class="block text-xs font-mono uppercase text-chrome mb-1.5">Weight (kg)</label>
                <input type="number" id="calc-weight" value="74" min="35" max="200" step="0.5" class="w-full bg-obsidian border border-white/15 rounded-xl px-3.5 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none transition-colors">
              </div>
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div>
                <label class="block text-xs font-mono uppercase text-chrome mb-1.5">Height (cm)</label>
                <input type="number" id="calc-height" value="176" min="120" max="230" class="w-full bg-obsidian border border-white/15 rounded-xl px-3.5 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none transition-colors">
              </div>
              <div>
                <label class="block text-xs font-mono uppercase text-chrome mb-1.5">Weekly Days</label>
                <select id="calc-days" class="w-full bg-obsidian border border-white/15 rounded-xl px-3 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none transition-colors">
                  <option value="3">3 Days (Full Body)</option>
                  <option value="4" selected>4 Days (Upper / Lower)</option>
                  <option value="5">5 Days (Push / Pull / Legs)</option>
                  <option value="6">6 Days (MMA & Iron Bay Split)</option>
                </select>
              </div>
            </div>

            <div>
              <label class="block text-xs font-mono uppercase text-chrome mb-1.5">Primary Target Objective</label>
              <select id="calc-goal" class="w-full bg-obsidian border border-white/15 rounded-xl px-3 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none transition-colors">
                <option value="muscle" selected>Hypertrophy & Lean Muscle Gain (+300 kcal)</option>
                <option value="fatloss">Rapid Fat Shred & Zumba Conditioning (-500 kcal)</option>
                <option value="power">MMA Striking & Athletic Power (Maintenance)</option>
              </select>
            </div>

            <button type="submit" class="w-full py-3 rounded-xl font-oswald tracking-wider uppercase font-bold bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_20px_rgba(37,99,235,0.35)] hover:shadow-[0_0_30px_rgba(56,189,248,0.6)] transition-all flex items-center justify-center gap-2">
              <i data-lucide="sparkles" class="w-4 h-4 fill-current"></i>
              RECALCULATE BLUEPRINT
            </button>
          </form>
        </div>

        <div class="lg:col-span-7 glass-panel-cobalt rounded-3xl p-6 sm:p-8 cove-border space-y-6">
          <div class="flex items-center justify-between border-b border-white/10 pb-4">
            <div>
              <span class="text-[11px] font-mono text-cobalt-bright uppercase">SYNTHESIZED DIAGNOSTICS</span>
              <h3 class="text-xl sm:text-2xl font-syne font-extrabold text-white">Your Midtown Custom Blueprint</h3>
            </div>
            <span class="px-2.5 py-1 rounded bg-white/10 text-white font-mono text-xs">WORLI HQ SPEC</span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="p-4 rounded-2xl bg-obsidian/70 border border-white/10">
              <div class="text-[11px] font-mono text-chrome uppercase">Calculated BMI</div>
              <div id="output-bmi" class="text-2xl sm:text-3xl font-syne font-extrabold text-cobalt-bright mt-1">23.9</div>
              <div id="output-bmi-cat" class="text-xs text-emerald-400 font-medium mt-0.5">Optimal / Normal</div>
            </div>

            <div class="p-4 rounded-2xl bg-obsidian/70 border border-white/10">
              <div class="text-[11px] font-mono text-chrome uppercase">Target Calories</div>
              <div id="output-calories" class="text-2xl sm:text-3xl font-syne font-extrabold text-white mt-1">2,480</div>
              <div class="text-xs text-chrome mt-0.5">kcal / day</div>
            </div>

            <div class="p-4 rounded-2xl bg-obsidian/70 border border-white/10">
              <div class="text-[11px] font-mono text-chrome uppercase">Daily Protein</div>
              <div id="output-protein" class="text-2xl sm:text-3xl font-syne font-extrabold text-neon-magenta mt-1">162g</div>
              <div class="text-xs text-chrome mt-0.5">2.2g / kg lean body</div>
            </div>
          </div>

          <div class="space-y-3">
            <div class="text-xs font-mono uppercase text-chrome flex items-center justify-between">
              <span>Personalized Workout Architecture:</span>
              <span class="text-cobalt-bright">Periodized Split</span>
            </div>
            <div id="output-split-container" class="space-y-2"></div>
          </div>

          <div class="pt-2">
            <button onclick="sendBlueprintWhatsApp()" 
                    class="w-full py-3.5 rounded-xl font-oswald text-base tracking-wider uppercase font-bold bg-emerald-500 hover:bg-emerald-400 text-obsidian shadow-[0_0_20px_rgba(16,185,129,0.4)] transition-all flex items-center justify-center gap-2">
              <i data-lucide="send" class="w-4 h-4"></i>
              SEND MY CUSTOM BLUEPRINT TO WHATSAPP (+91 9819999103)
            </button>
            <p class="text-center text-[11px] text-chrome/70 mt-2 font-mono">
              Instantly syncs with Coach Aryan & Dev at Worli to review your targets during your free session.
            </p>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Dynamic Class Schedule & Instant Spot Reservation Engine -->
  <section id="schedule" class="py-20 bg-obsidian relative border-t border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-6">
        <div>
          <div class="text-xs font-mono font-bold uppercase tracking-widest text-cobalt-bright mb-2 flex items-center gap-2">
            <span class="w-2 h-0.5 bg-cobalt-bright"></span> LIVE DAILY TIMETABLE
          </div>
          <h2 class="text-3xl sm:text-5xl font-syne font-extrabold text-titanium">
            HIGH-INTENSITY <span class="text-transparent bg-clip-text bg-gradient-to-r from-cobalt-bright via-blue-400 to-neon-violet">CLASS SCHEDULE</span>
          </h2>
          <p class="text-chrome text-sm sm:text-base mt-2 max-w-xl">
            MMA combat sparring, Zumba rhythm burns, Crossfit metcon, and heavy barbell powerlifting. Real-time slot availability.
          </p>
        </div>

        <div class="flex flex-wrap gap-2">
          <button onclick="filterClasses('all')" class="class-filter-btn active px-3.5 py-1.5 rounded-xl text-xs font-oswald tracking-wide font-bold bg-white text-obsidian">
            ALL CLASSES
          </button>
          <button onclick="filterClasses('mma')" class="class-filter-btn px-3.5 py-1.5 rounded-xl text-xs font-oswald tracking-wide font-bold bg-carbon text-chrome hover:text-white border border-white/10">
            MMA & KICKBOXING
          </button>
          <button onclick="filterClasses('zumba')" class="class-filter-btn px-3.5 py-1.5 rounded-xl text-xs font-oswald tracking-wide font-bold bg-carbon text-chrome hover:text-white border border-white/10">
            ZUMBA & DANCE
          </button>
          <button onclick="filterClasses('strength')" class="class-filter-btn px-3.5 py-1.5 rounded-xl text-xs font-oswald tracking-wide font-bold bg-carbon text-chrome hover:text-white border border-white/10">
            HEAVY STRENGTH
          </button>
          <button onclick="filterClasses('hiit')" class="class-filter-btn px-3.5 py-1.5 rounded-xl text-xs font-oswald tracking-wide font-bold bg-carbon text-chrome hover:text-white border border-white/10">
            HIIT & METCON
          </button>
        </div>
      </div>

      <div id="classes-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"></div>

    </div>
  </section>

  <!-- Membership Matrix with Live Price Tier & EMI Breakdown -->
  <section id="pricing" class="py-20 relative bg-carbon/50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-12">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 border border-white/20 text-white text-xs font-mono mb-3">
          <i data-lucide="shield-check" class="w-3.5 h-3.5 text-cobalt-bright"></i>
          TRANSPARENT WORLI PRICING • ALL PASSES INCLUDE STEAM ACCESS
        </div>
        <h2 class="text-3xl sm:text-5xl font-syne font-extrabold text-titanium">
          SELECT YOUR <span class="text-transparent bg-clip-text bg-gradient-to-r from-cobalt-bright to-white">TRANSFORMATION PASS</span>
        </h2>
        <p class="text-chrome text-sm sm:text-base mt-3">
          Invest in your peak physique with our flexible tenure passes and 0% interest monthly EMI options.
        </p>

        <div class="mt-8 inline-flex items-center gap-3 p-1.5 rounded-2xl bg-carbon border border-white/10">
          <button onclick="setBillingCycle('quarterly')" id="btn-monthly" class="px-5 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all text-chrome hover:text-white">
            STANDARD TENURE
          </button>
          <button onclick="setBillingCycle('annual')" id="btn-annual" class="px-5 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_15px_rgba(37,99,235,0.4)] flex items-center gap-1.5">
            <span>ANNUAL VIP (SAVE 25%)</span>
            <span class="px-1.5 py-0.5 rounded bg-obsidian text-cobalt-bright text-[10px] font-mono">POPULAR</span>
          </button>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 items-stretch">
        
        <!-- Tier 1: Starter -->
        <div class="glass-panel rounded-3xl p-6 border border-white/10 flex flex-col justify-between hover:border-white/25 transition-all">
          <div>
            <div class="text-xs font-mono text-chrome uppercase">FOUNDATION</div>
            <h3 class="text-2xl font-syne font-extrabold text-white mt-1">1 Month Starter</h3>
            <p class="text-chrome text-xs mt-2">Ideal for testing the facility, heavy lifting bays, and group sessions.</p>
            
            <div class="my-6">
              <div class="flex items-baseline gap-1">
                <span class="text-3xl font-syne font-extrabold text-white">₹3,499</span>
                <span class="text-xs text-chrome font-mono">/ month</span>
              </div>
              <div class="text-[11px] font-mono text-chrome/70 mt-1">One-time enrollment</div>
            </div>

            <ul class="space-y-3 text-xs text-titanium/90 border-t border-white/10 pt-4">
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                Full access to Iron & Cardio Zones
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                Eucalyptus Steam Suite Access
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                Free physical fitness screening
              </li>
              <li class="flex items-center gap-2 text-chrome/40 line-through">
                <i data-lucide="x" class="w-4 h-4 text-chrome/40 flex-shrink-0"></i>
                Dedicated 1-on-1 PT Sessions
              </li>
              <li class="flex items-center gap-2 text-chrome/40 line-through">
                <i data-lucide="x" class="w-4 h-4 text-chrome/40 flex-shrink-0"></i>
                VIP Guest Passes
              </li>
            </ul>
          </div>

          <div class="pt-6">
            <button onclick="selectMembership('1 Month Starter', '3499')" class="w-full py-2.5 rounded-xl font-oswald text-xs uppercase tracking-wider font-bold bg-white/10 hover:bg-white/20 text-white transition-colors">
              SELECT PASS
            </button>
          </div>
        </div>

        <!-- Tier 2: Transformation -->
        <div class="glass-panel rounded-3xl p-6 border border-white/10 flex flex-col justify-between hover:border-white/25 transition-all">
          <div>
            <div class="text-xs font-mono text-cobalt-bright uppercase">MOMENTUM</div>
            <h3 class="text-2xl font-syne font-extrabold text-white mt-1">3 Months Split</h3>
            <p class="text-chrome text-xs mt-2">Comprehensive 90-day physical recomp and nutritional guidance.</p>
            
            <div class="my-6">
              <div class="flex items-baseline gap-1">
                <span class="text-3xl font-syne font-extrabold text-white">₹8,999</span>
                <span class="text-xs text-chrome font-mono">(₹2,999/mo)</span>
              </div>
              <div class="text-[11px] font-mono text-cobalt-bright mt-1">EMI from ₹1,550/mo</div>
            </div>

            <ul class="space-y-3 text-xs text-titanium/90 border-t border-white/10 pt-4">
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                Unlimited gym & MMA floor access
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                1x Complimentary Personal Training
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                Personalized Macro & Diet Blueprint
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                Eucalyptus Steam Sanctuary Access
              </li>
              <li class="flex items-center gap-2 text-chrome/40 line-through">
                <i data-lucide="x" class="w-4 h-4 text-chrome/40 flex-shrink-0"></i>
                VIP Guest Passes
              </li>
            </ul>
          </div>

          <div class="pt-6">
            <button onclick="selectMembership('3 Months Split', '8999')" class="w-full py-2.5 rounded-xl font-oswald text-xs uppercase tracking-wider font-bold bg-white/10 hover:bg-white/20 text-white transition-colors">
              SELECT PASS
            </button>
          </div>
        </div>

        <!-- Tier 3: Pro Athlete -->
        <div class="glass-panel-cobalt rounded-3xl p-6 cove-border flex flex-col justify-between relative shadow-[0_0_30px_rgba(37,99,235,0.2)]">
          <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 px-3 py-0.5 rounded-full bg-cobalt-bright text-obsidian font-mono text-[10px] font-extrabold uppercase tracking-wider">
            MOST POPULAR IN WORLI
          </div>
          <div>
            <div class="text-xs font-mono text-cobalt-bright uppercase">ATHLETE STANDARD</div>
            <h3 class="text-2xl font-syne font-extrabold text-white mt-1">6 Months Pro</h3>
            <p class="text-chrome text-xs mt-2">The sweet spot for serious strength gains, Zumba burns, and body recomp.</p>
            
            <div class="my-6">
              <div class="flex items-baseline gap-1">
                <span class="text-3xl font-syne font-extrabold text-cobalt-bright">₹15,499</span>
                <span class="text-xs text-chrome font-mono">(₹2,583/mo)</span>
              </div>
              <div class="text-[11px] font-mono text-emerald-400 mt-1">EMI from ₹1,350/mo No-Cost</div>
            </div>

            <ul class="space-y-3 text-xs text-titanium/90 border-t border-white/10 pt-4">
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                All Access: Iron Bay, MMA Cage, Zumba
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                3x 1-on-1 Certified PT Sessions
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                Unlimited Eucalyptus Steam Access
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                2x Complimentary Guest Passes
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-cobalt-bright flex-shrink-0"></i>
                Dedicated On-Site Parking Access
              </li>
            </ul>
          </div>

          <div class="pt-6">
            <button onclick="selectMembership('6 Months Pro', '15499')" class="w-full py-3 rounded-xl font-oswald text-xs uppercase tracking-wider font-bold bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_15px_rgba(37,99,235,0.4)] hover:shadow-[0_0_25px_rgba(56,189,248,0.7)] transition-all">
              CLAIM PRO PASS
            </button>
          </div>
        </div>

        <!-- Tier 4: VIP Black Card -->
        <div class="glass-panel rounded-3xl p-6 cove-border-violet flex flex-col justify-between hover:border-purple-400/70 transition-all">
          <div>
            <div class="text-xs font-mono text-neon-violet uppercase">ELITE PRIVILEGE</div>
            <h3 class="text-2xl font-syne font-extrabold text-white mt-1">12 Mo VIP Black</h3>
            <p class="text-chrome text-xs mt-2">Unrestricted apex status with maximum savings and concierge support.</p>
            
            <div class="my-6">
              <div class="flex items-baseline gap-1">
                <span class="text-3xl font-syne font-extrabold text-neon-violet">₹23,999</span>
                <span class="text-xs text-chrome font-mono">(₹1,999/mo)</span>
              </div>
              <div class="text-[11px] font-mono text-emerald-400 mt-1">EMI from ₹2,050/mo No-Cost</div>
            </div>

            <ul class="space-y-3 text-xs text-titanium/90 border-t border-white/10 pt-4">
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-neon-violet flex-shrink-0"></i>
                Full 365 Days Unrestricted Access
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-neon-violet flex-shrink-0"></i>
                6x 1-on-1 Certified PT Sessions
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-neon-violet flex-shrink-0"></i>
                5x VIP Guest Day Passes
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-neon-violet flex-shrink-0"></i>
                Unlimited Eucalyptus Steam & Towels
              </li>
              <li class="flex items-center gap-2">
                <i data-lucide="check" class="w-4 h-4 text-neon-violet flex-shrink-0"></i>
                Reserved VIP Locker & Priority Classes
              </li>
            </ul>
          </div>

          <div class="pt-6">
            <button onclick="selectMembership('12 Mo VIP Black', '23999')" class="w-full py-2.5 rounded-xl font-oswald text-xs uppercase tracking-wider font-bold bg-neon-violet/20 hover:bg-neon-violet text-white transition-all">
              CLAIM VIP BLACK PASS
            </button>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Facility Location & Interactive Navigation Guide -->
  <section id="location" class="py-20 relative bg-obsidian">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        <div class="lg:col-span-6 space-y-6">
          <div>
            <div class="text-xs font-mono font-bold uppercase tracking-widest text-cobalt-bright mb-2">
              PRIME LOCATION & ACCESS
            </div>
            <h2 class="text-3xl sm:text-4xl font-syne font-extrabold text-titanium">
              TRAIN AT THE HEART OF WORLI, MUMBAI.
            </h2>
            <p class="text-chrome text-sm mt-3 leading-relaxed">
              Located conveniently on Dr. Annie Besant Road opposite the Old Passport Office in Adarsh Nagar. Fast access from Lower Parel, Prabhadevi, and South Mumbai.
            </p>
          </div>

          <div class="p-5 rounded-2xl glass-panel-cobalt cove-border space-y-3">
            <div class="flex items-start gap-3">
              <i data-lucide="map-pin" class="w-5 h-5 text-cobalt-bright flex-shrink-0 mt-0.5"></i>
              <div>
                <div class="text-xs font-mono text-cobalt-bright uppercase">Verified Facility Address</div>
                <div class="text-sm font-semibold text-white mt-1 leading-snug">
                  Shop No. 01, Madhu Hans, Dr. Annie Besant Rd, opp. Old Passport Office, Adarsh Nagar, Worli, Mumbai, Maharashtra 400030
                </div>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-3 pt-3 border-t border-white/10 text-xs">
              <div>
                <span class="text-chrome/70 block">Direct Hotline:</span>
                <a href="tel:9819999103" class="text-cobalt-bright font-bold hover:underline">+91 9819999103</a>
              </div>
              <div>
                <span class="text-chrome/70 block">Daily Hours:</span>
                <span class="text-emerald-400 font-bold">Open till 11:00 PM Daily</span>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs">
            <div class="p-3 rounded-xl bg-carbon border border-white/10 flex items-center gap-2">
              <i data-lucide="car" class="w-4 h-4 text-cobalt-bright"></i>
              <span>Dedicated Parking</span>
            </div>
            <div class="p-3 rounded-xl bg-carbon border border-white/10 flex items-center gap-2">
              <i data-lucide="droplet" class="w-4 h-4 text-emerald-400"></i>
              <span>Eucalyptus Steam</span>
            </div>
            <div class="p-3 rounded-xl bg-carbon border border-white/10 flex items-center gap-2">
              <i data-lucide="wifi" class="w-4 h-4 text-cobalt-bright"></i>
              <span>High-Speed WiFi</span>
            </div>
            <div class="p-3 rounded-xl bg-carbon border border-white/10 flex items-center gap-2">
              <i data-lucide="lock" class="w-4 h-4 text-cobalt-bright"></i>
              <span>Digital Lockers</span>
            </div>
            <div class="p-3 rounded-xl bg-carbon border border-white/10 flex items-center gap-2">
              <i data-lucide="music" class="w-4 h-4 text-neon-magenta"></i>
              <span>Zumba Sound Stage</span>
            </div>
            <div class="p-3 rounded-xl bg-carbon border border-white/10 flex items-center gap-2">
              <i data-lucide="shield" class="w-4 h-4 text-neon-violet"></i>
              <span>MMA Combat Arena</span>
            </div>
          </div>

          <div class="flex flex-wrap gap-4 pt-2">
            <a href="https://maps.google.com/?q=Midtown+Fitness+Worli+Mumbai" target="_blank"
               class="px-6 py-3 rounded-xl font-oswald text-sm uppercase tracking-wider font-bold bg-white text-obsidian hover:bg-cobalt-bright transition-colors flex items-center gap-2 shadow-[0_0_20px_rgba(255,255,255,0.2)]">
              <i data-lucide="navigation" class="w-4 h-4 fill-current"></i>
              OPEN GOOGLE MAPS NAVIGATION
            </a>
            <a href="tel:9819999103" 
               class="px-5 py-3 rounded-xl font-oswald text-sm uppercase tracking-wider font-bold glass-panel text-white hover:text-cobalt-bright transition-colors flex items-center gap-2">
              <i data-lucide="phone" class="w-4 h-4 text-cobalt-bright"></i>
              CALL RECEPTION
            </a>
          </div>

        </div>

        <div class="lg:col-span-6">
          <div class="relative rounded-3xl overflow-hidden cove-border glass-panel p-2 shadow-[0_0_30px_rgba(37,99,235,0.2)]">
            
            <div class="w-full h-[380px] rounded-2xl overflow-hidden relative">
              <iframe 
                title="Midtown Fitness Worli Location"
                src="https://maps.google.com/maps?q=Midtown%20Fitness%20Shop%20No.%2001%20Madhu%20Hans%20Dr.%20Annie%20Besant%20Rd%20Worli%20Mumbai&t=&z=16&ie=UTF8&iwloc=&output=embed" 
                class="w-full h-full border-0 filter contrast-125 brightness-90 grayscale-[30%]">
              </iframe>

              <div class="absolute bottom-4 left-4 right-4 glass-panel p-3.5 rounded-xl border border-white/20 flex items-center justify-between">
                <div>
                  <div class="text-xs font-bold text-white flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                    MIDTOWN FITNESS HQ
                  </div>
                  <div class="text-[11px] text-chrome">Adarsh Nagar, Opp Old Passport Office</div>
                </div>
                <a href="https://maps.google.com/?q=Midtown+Fitness+Worli+Mumbai" target="_blank"
                   class="px-3 py-1.5 rounded-lg bg-cobalt-bright text-obsidian text-xs font-oswald font-bold tracking-wider hover:bg-white transition-colors">
                  GET DIRECTIONS
                </a>
              </div>
            </div>

          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Pitch Deck High-Conversion CTA Banner -->
  <section class="py-16 relative overflow-hidden bg-gradient-to-r from-carbon via-obsidian to-carbon border-t border-white/10">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 text-center space-y-6">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-500/15 border border-cobalt-bright/40 text-cobalt-bright text-xs font-mono">
        <i data-lucide="zap" class="w-3.5 h-3.5"></i>
        ZERO RISK TRIAL PASS
      </div>
      <h2 class="text-3xl sm:text-5xl font-syne font-extrabold text-white">
        EXPERIENCE WORLI'S APEX GYM TODAY.
      </h2>
      <p class="text-chrome text-sm sm:text-base max-w-xl mx-auto">
        No sales pressure. No contracts required upfront. Experience our power racks, neon atmosphere, certified trainers, and steam sanctuary with a complimentary 1-day pass.
      </p>
      <div class="flex flex-wrap items-center justify-center gap-4 pt-2">
        <button onclick="openModal('passModal')" 
                class="px-8 py-4 rounded-xl font-oswald text-base tracking-wider uppercase font-bold bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_30px_rgba(37,99,235,0.5)] hover:shadow-[0_0_40px_rgba(56,189,248,0.8)] transition-all transform hover:-translate-y-0.5">
          CLAIM YOUR COMPLIMENTARY PASS NOW
        </button>
        <a href="tel:9819999103" 
           class="px-7 py-4 rounded-xl font-oswald text-base tracking-wider uppercase font-bold glass-panel text-white hover:text-cobalt-bright transition-colors flex items-center gap-2">
          <i data-lucide="phone" class="w-4 h-4 text-cobalt-bright"></i>
          CALL +91 9819999103
        </a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-obsidian border-t border-white/10 pt-12 pb-24 md:pb-12 text-chrome text-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-4 gap-8 mb-10">
      
      <div class="space-y-3">
        <div class="font-syne font-extrabold text-lg text-white flex items-center gap-1">
          MIDTOWN <span class="text-cobalt-bright">FITNESS</span>
        </div>
        <p class="text-chrome/80 leading-relaxed">
          Worli's premier athletic gym. Heavy plate-loaded strength bays, cobalt neon cardio arena, MMA fight camp, Zumba stage, and eucalyptus steam suite.
        </p>
        <div class="text-[11px] font-mono text-emerald-400">
          ● Open 7 Days: Mon - Sun until 11:00 PM
        </div>
      </div>

      <div>
        <div class="font-oswald uppercase text-white font-bold text-sm mb-3">Disciplines</div>
        <ul class="space-y-2">
          <li><a href="#zones" class="hover:text-cobalt-bright transition-colors">Plate-Loaded Strength Bays</a></li>
          <li><a href="#combat-zumba" class="hover:text-cobalt-bright transition-colors">MMA & Combat Fight Camp</a></li>
          <li><a href="#combat-zumba" class="hover:text-cobalt-bright transition-colors">Zumba Dance Sound Stage</a></li>
          <li><a href="#steam" class="hover:text-cobalt-bright transition-colors">Eucalyptus Steam Sanctuary</a></li>
          <li><a href="#trainers" class="hover:text-cobalt-bright transition-colors">Certified Master PT Roster</a></li>
        </ul>
      </div>

      <div>
        <div class="font-oswald uppercase text-white font-bold text-sm mb-3">Facility & Location</div>
        <address class="not-italic space-y-2 text-chrome/90">
          <div>Shop No. 01, Madhu Hans</div>
          <div>Dr. Annie Besant Rd, opp. Old Passport Office</div>
          <div>Adarsh Nagar, Worli, Mumbai 400030</div>
          <div class="pt-1">
            <a href="tel:9819999103" class="text-cobalt-bright font-bold hover:underline">Tel: +91 9819999103</a>
          </div>
        </address>
      </div>

      <div>
        <div class="font-oswald uppercase text-white font-bold text-sm mb-3">Executive Concierge</div>
        <p class="text-chrome/80 mb-3">
          Book immediate workout sessions, personal trainer consultations, or steam passes via WhatsApp.
        </p>
        <a href="https://wa.me/919819999103?text=Hi%20Midtown%20Fitness%2C%20I%20want%20to%20book%20my%20free%20workout%20session%20and%20trial%20pass." 
           target="_blank"
           class="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 font-bold hover:bg-emerald-500 hover:text-obsidian transition-colors">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          Connect via WhatsApp
        </a>
      </div>

    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-t border-white/5 pt-6 flex flex-col sm:flex-row items-center justify-between text-[11px] text-chrome/60 gap-3">
      <div>© 2026 Midtown Fitness, Worli, Mumbai. All rights reserved.</div>
      <div class="font-mono">Engineered for Peak Performance • Prototype Demo</div>
    </div>
  </footer>

  <!-- Interactive Workout Playlist & Synthesizer Player Widget (Floating Bottom-Right) -->
  <div id="audio-player-widget" class="fixed bottom-20 md:bottom-6 right-4 sm:right-6 z-40 transition-all duration-300">
    <div class="glass-panel-cobalt rounded-2xl p-3 sm:p-4 cove-border w-[300px] sm:w-[330px]">
      
      <div class="flex items-center justify-between mb-2.5">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-cobalt-bright animate-ping"></span>
          <span class="text-[11px] font-mono font-bold text-cobalt-bright uppercase tracking-wider">MIDTOWN BEATS // LIVE</span>
        </div>
        <div class="flex items-center gap-1.5">
          <button onclick="toggleAudioMin()" id="min-player-btn" class="text-chrome hover:text-white p-1">
            <i data-lucide="chevron-down" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>

      <div id="player-body" class="space-y-3">
        <div class="w-full h-8 bg-obsidian/80 rounded-lg overflow-hidden border border-white/10 flex items-center justify-center p-1">
          <canvas id="audio-visualizer" width="280" height="32" class="w-full h-full"></canvas>
        </div>

        <div class="flex items-center justify-between">
          <div class="truncate pr-2">
            <div id="track-name" class="text-xs font-bold text-white truncate">Worli Cobalt Phonk Pulse</div>
            <div id="track-bpm" class="text-[10px] font-mono text-cobalt-bright">132 BPM • Electronic Sub-Bass</div>
          </div>
          <span class="text-[10px] font-mono text-chrome" id="track-timer">00:00</span>
        </div>

        <div class="flex items-center justify-between gap-2 pt-1 border-t border-white/10">
          <button onclick="prevTrack()" class="p-1.5 text-chrome hover:text-white transition-colors">
            <i data-lucide="skip-back" class="w-3.5 h-3.5"></i>
          </button>
          
          <button id="synth-play-btn" onclick="toggleSynthMusic()" 
                  class="w-8 h-8 rounded-full bg-cobalt-bright text-obsidian flex items-center justify-center hover:scale-105 transition-transform shadow-[0_0_10px_#38bdf8]">
            <i id="synth-play-icon" data-lucide="play" class="w-4 h-4 fill-current ml-0.5"></i>
          </button>

          <button onclick="nextTrack()" class="p-1.5 text-chrome hover:text-white transition-colors">
            <i data-lucide="skip-forward" class="w-3.5 h-3.5"></i>
          </button>

          <div class="flex items-center gap-1.5 pl-2">
            <i data-lucide="volume-1" class="w-3.5 h-3.5 text-chrome"></i>
            <input type="range" id="synth-volume" min="0" max="1" step="0.05" value="0.7" class="w-16 h-1 cursor-pointer accent-cobalt-bright" oninput="setSynthVolume(this.value)">
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- Sticky Mobile Command Bar (Persistent Demo Experience on Phones) -->
  <div class="md:hidden fixed bottom-0 left-0 right-0 z-50 bg-carbon/95 border-t border-white/15 px-3 py-2 backdrop-blur-xl">
    <div class="grid grid-cols-4 gap-1.5 text-center text-[10px] font-mono">
      
      <a href="tel:9819999103" class="flex flex-col items-center justify-center py-1.5 rounded-xl bg-obsidian border border-white/10 text-white active:bg-blue-500/20">
        <i data-lucide="phone" class="w-4 h-4 text-cobalt-bright mb-1"></i>
        <span>CALL</span>
      </a>

      <a href="https://wa.me/919819999103?text=Hi%20Midtown%20Fitness%2C%20I%20want%20to%20book%20my%20free%20workout%20session%20and%20trial%20pass." 
         target="_blank" 
         class="flex flex-col items-center justify-center py-1.5 rounded-xl bg-obsidian border border-white/10 text-white active:bg-emerald-500/20">
        <i data-lucide="message-circle" class="w-4 h-4 text-emerald-400 mb-1"></i>
        <span>WHATSAPP</span>
      </a>

      <a href="https://maps.google.com/?q=Midtown+Fitness+Worli+Mumbai" target="_blank"
         class="flex flex-col items-center justify-center py-1.5 rounded-xl bg-obsidian border border-white/10 text-white active:bg-white/20">
        <i data-lucide="map-pin" class="w-4 h-4 text-neon-violet mb-1"></i>
        <span>WORLI MAP</span>
      </a>

      <button onclick="openModal('passModal')" class="flex flex-col items-center justify-center py-1.5 rounded-xl bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian font-bold font-oswald active:scale-95 transition-transform">
        <i data-lucide="zap" class="w-4 h-4 fill-current mb-0.5"></i>
        <span>FREE PASS</span>
      </button>

    </div>
  </div>

  <!-- MODAL 1: Free 1-Day Trial Pass Modal -->
  <div id="passModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-obsidian/85 backdrop-blur-md hidden opacity-0 transition-opacity duration-300">
    <div class="relative w-full max-w-md glass-panel-cobalt rounded-3xl p-6 sm:p-7 cove-border">
      
      <button onclick="closeModal('passModal')" class="absolute top-4 right-4 text-chrome hover:text-white p-2">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="space-y-4">
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-cobalt-neon/15 text-cobalt-bright text-xs font-mono border border-cobalt-bright/30">
          <i data-lucide="ticket" class="w-3.5 h-3.5"></i>
          INSTANT ACCESS PASS
        </div>

        <h3 class="text-2xl font-syne font-extrabold text-white">
          Claim 1-Day Free Pass
        </h3>
        <p class="text-xs text-chrome">
          Valid for 1 full training session + Eucalyptus Steam Suite at Midtown Fitness, Shop 01 Madhu Hans, Dr. Annie Besant Rd, Worli.
        </p>

        <form id="pass-form" onsubmit="handlePassSubmit(event)" class="space-y-3 pt-2">
          <div>
            <label class="block text-xs font-mono uppercase text-chrome mb-1">Your Full Name</label>
            <input type="text" id="pass-name" required placeholder="e.g. Vikram Malhotra" 
                   class="w-full bg-obsidian border border-white/15 rounded-xl px-3.5 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none">
          </div>

          <div>
            <label class="block text-xs font-mono uppercase text-chrome mb-1">WhatsApp / Phone Number</label>
            <input type="tel" id="pass-phone" required placeholder="+91 98199..." 
                   class="w-full bg-obsidian border border-white/15 rounded-xl px-3.5 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none">
          </div>

          <div>
            <label class="block text-xs font-mono uppercase text-chrome mb-1">Preferred Activity</label>
            <select id="pass-zone" class="w-full bg-obsidian border border-white/15 rounded-xl px-3.5 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none">
              <option value="Zone A: Heavy Plate Iron Bay">Zone A: Heavy Plate Iron Bay</option>
              <option value="Zone B: Neon Cardio Arena">Zone B: Neon Cardio Arena</option>
              <option value="Zone C: MMA & Combat Fighting Cage">Zone C: MMA & Combat Fighting Cage</option>
              <option value="Zone D: Zumba & Dance Sound Stage">Zone D: Zumba & Dance Sound Stage</option>
              <option value="Eucalyptus Steam Sanctuary">Eucalyptus Steam Sanctuary</option>
            </select>
          </div>

          <div>
            <label class="block text-xs font-mono uppercase text-chrome mb-1">Visit Date</label>
            <input type="date" id="pass-date" required class="w-full bg-obsidian border border-white/15 rounded-xl px-3.5 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none">
          </div>

          <button type="submit" 
                  class="w-full py-3 rounded-xl font-oswald text-base tracking-wider uppercase font-bold bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_20px_rgba(37,99,235,0.4)] hover:shadow-[0_0_30px_rgba(56,189,248,0.7)] transition-all">
            CONFIRM & RECEIVE PASS
          </button>
        </form>

        <div class="text-[11px] font-mono text-center text-chrome/60 pt-1">
          Pass details will be verified at our Worli reception via SMS / WhatsApp.
        </div>
      </div>

    </div>
  </div>

  <!-- MODAL 2: Spot Reservation Confirmation Modal -->
  <div id="bookingModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-obsidian/85 backdrop-blur-md hidden opacity-0 transition-opacity duration-300">
    <div class="relative w-full max-w-md glass-panel-cobalt rounded-3xl p-6 sm:p-7 cove-border">
      
      <button onclick="closeModal('bookingModal')" class="absolute top-4 right-4 text-chrome hover:text-white p-2">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div class="space-y-4">
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-neon-violet/15 text-neon-violet text-xs font-mono border border-neon-violet/30">
          <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
          CLASS RESERVATION
        </div>

        <h3 id="modal-class-title" class="text-2xl font-syne font-extrabold text-white">
          Reserve Your Spot
        </h3>
        <p id="modal-class-subtitle" class="text-xs text-chrome">
          Lock in your mat / station for today's session.
        </p>

        <form id="booking-form" onsubmit="handleBookingSubmit(event)" class="space-y-3 pt-2">
          <input type="hidden" id="booking-class-id">

          <div>
            <label class="block text-xs font-mono uppercase text-chrome mb-1">Member Name</label>
            <input type="text" id="book-name" required placeholder="Enter your name" 
                   class="w-full bg-obsidian border border-white/15 rounded-xl px-3.5 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none">
          </div>

          <div>
            <label class="block text-xs font-mono uppercase text-chrome mb-1">Phone Number</label>
            <input type="tel" id="book-phone" required placeholder="+91 98199..." 
                   class="w-full bg-obsidian border border-white/15 rounded-xl px-3.5 py-2.5 text-sm text-white focus:border-cobalt-bright focus:outline-none">
          </div>

          <div class="p-3 rounded-xl bg-obsidian/70 border border-white/10 space-y-1 text-xs">
            <div class="flex justify-between text-chrome">
              <span>Time Slot:</span>
              <span id="modal-class-time" class="font-bold text-white">07:00 AM - 08:00 AM</span>
            </div>
            <div class="flex justify-between text-chrome">
              <span>Coach:</span>
              <span id="modal-class-coach" class="font-bold text-cobalt-bright">Coach Aryan</span>
            </div>
            <div class="flex justify-between text-chrome">
              <span>Remaining Spots:</span>
              <span id="modal-class-spots" class="font-bold text-emerald-400">3 Spots Left</span>
            </div>
          </div>

          <button type="submit" 
                  class="w-full py-3 rounded-xl font-oswald text-base tracking-wider uppercase font-bold bg-gradient-to-r from-cobalt-bright to-neon-violet text-white shadow-[0_0_20px_rgba(37,99,235,0.4)] hover:shadow-[0_0_30px_rgba(56,189,248,0.7)] transition-all">
            CONFIRM SPOT RESERVATION
          </button>
        </form>
      </div>

    </div>
  </div>

  <!-- Toast Notification Alert -->
  <div id="toast" class="fixed top-6 right-6 z-50 transform translate-x-full transition-transform duration-300 pointer-events-none">
    <div class="glass-panel-cobalt px-4 py-3 rounded-2xl cove-border text-xs font-mono text-white flex items-center gap-3 shadow-[0_0_25px_rgba(37,99,235,0.4)]">
      <div id="toast-icon" class="text-cobalt-bright"><i data-lucide="check-circle" class="w-4 h-4"></i></div>
      <div id="toast-msg">Notification message here</div>
    </div>
  </div>

  <!-- Core Application Scripts -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const today = new Date().toISOString().split('T')[0];
      const dateInput = document.getElementById('pass-date');
      if (dateInput) dateInput.value = today;

      lucide.createIcons();
      renderHourlyBars();
      renderClasses('all');
      initAudioVisualizer();
      calculateSplit();

      updateMumbaiClock();
      setInterval(updateMumbaiClock, 1000);
    }});

    function updateMumbaiClock() {{
      const now = new Date();
      const options = {{ timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true }};
      const timeStr = now.toLocaleTimeString('en-US', options);
      const clockEl = document.getElementById('live-clock');
      if (clockEl) {{
        clockEl.textContent = `Mumbai Local: ${{timeStr}} IST`;
      }}
    }}

    const hourlyDensityMap = {{
      6: 22, 6.5: 35, 7: 68, 7.5: 88, 8: 92, 8.5: 82, 9: 64, 9.5: 45,
      10: 32, 10.5: 25, 11: 22, 11.5: 18, 12: 15, 12.5: 16, 13: 14, 13.5: 15,
      14: 18, 14.5: 22, 15: 28, 15.5: 38, 16: 48, 16.5: 58, 17: 72, 17.5: 84,
      18: 94, 18.5: 96, 19: 98, 19.5: 92, 20: 85, 20.5: 75, 21: 60, 21.5: 44,
      22: 28, 22.5: 18, 23: 10
    }};

    function renderHourlyBars() {{
      const container = document.getElementById('hourly-bars-container');
      if (!container) return;
      container.innerHTML = '';
      
      const hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23];
      hours.forEach(h => {{
        const val = hourlyDensityMap[h] || 30;
        const bar = document.createElement('div');
        bar.className = 'w-full bg-carbon rounded-t hover:bg-cobalt-bright transition-colors cursor-pointer relative group';
        bar.style.height = `${{val}}%`;
        bar.setAttribute('onclick', `setSliderHour(${{h}})`);
        
        let colorClass = 'bg-white/20';
        if (val > 80) colorClass = 'bg-neon-magenta';
        else if (val > 50) colorClass = 'bg-cobalt-neon';
        else colorClass = 'bg-cobalt-bright/60';
        bar.className += ` ${{colorClass}}`;

        container.appendChild(bar);
      }});
    }}

    function setSliderHour(hour) {{
      const slider = document.getElementById('hour-slider');
      if (slider) {{
        slider.value = hour;
        updateGymPulse(hour);
      }}
    }}

    function updateGymPulse(hourVal) {{
      const h = parseFloat(hourVal);
      const density = hourlyDensityMap[h] || Math.round(30 + Math.sin(h) * 20);
      
      const intHour = Math.floor(h);
      const mins = h % 1 !== 0 ? '30' : '00';
      const ampm = intHour >= 12 ? 'PM' : 'AM';
      const displayHour = intHour > 12 ? intHour - 12 : (intHour === 0 ? 12 : intHour);
      const formattedTime = `${{displayHour}}:${{mins}} ${{ampm}}`;

      const displayEl = document.getElementById('scrub-hour-display');
      const pctEl = document.getElementById('live-density-pct');
      const barEl = document.getElementById('live-density-bar');
      const badgeEl = document.getElementById('live-density-badge');
      const bpmEl = document.getElementById('vibe-bpm');

      if (pctEl) pctEl.textContent = `${{density}}%`;
      if (barEl) barEl.style.width = `${{density}}%`;

      if (density >= 85) {{
        if (badgeEl) {{
          badgeEl.textContent = 'High Energy • Prime Peak Rush';
          badgeEl.className = 'px-3 py-1 rounded-full text-xs font-bold bg-pink-500/20 text-neon-magenta border border-pink-500/40';
        }}
        if (displayEl) displayEl.textContent = `${{formattedTime}} (Apex Peak)`;
        if (bpmEl) bpmEl.textContent = '145 BPM Hardcore';
      }} else if (density >= 50) {{
        if (badgeEl) {{
          badgeEl.textContent = 'Active Momentum • Steady Flow';
          badgeEl.className = 'px-3 py-1 rounded-full text-xs font-bold bg-blue-500/20 text-blue-400 border border-blue-500/40';
        }}
        if (displayEl) displayEl.textContent = `${{formattedTime}} (Moderate Flow)`;
        if (bpmEl) bpmEl.textContent = '135 BPM Phonk';
      }} else {{
        if (badgeEl) {{
          badgeEl.textContent = 'Smooth Flow & Peak Space';
          badgeEl.className = 'px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40';
        }}
        if (displayEl) displayEl.textContent = `${{formattedTime}} (Optimal Chill)`;
        if (bpmEl) bpmEl.textContent = '125 BPM Deep Bass';
      }}
      playUiTick();
    }}

    const zonesData = {{
      iron: {{
        code: 'WORLI HQ // ZONE-A',
        title: 'Plate-Loaded Iron Bay',
        subtitle: 'HARDCORE HYPERTROPHY & HEAVY STRENGTH',
        description: 'Designed for serious lifters in Worli. Zero queueing on leg day with heavy-duty 45° hack squats, Olympic power racks, calibrated steel plates, and dumbbells up to 50kg.',
        focus: 'Compound Overload & Heavy Hypertrophy',
        image: '{img_hack_squat}',
        muscles: ['Quadriceps & Hamstrings', 'Pectorals & Delts', 'Latissimus Dorsi', 'Glutes & Spinal Erectors'],
        equipment: [
          '45° Heavy-Duty Plate Hack Squat',
          'Olympic Power Racks with Spotter Arms',
          'Heavy Leg Press (600kg capacity)',
          'Dumbbells from 2.5kg up to 50kg pairs',
          'Dual Adjustable Cable Crossover Tower',
          'T-Bar Row & Plate Incline Chest Press'
        ]
      }},
      cardio: {{
        code: 'WORLI HQ // ZONE-B',
        title: 'Cobalt Neon Cardio Arena',
        subtitle: 'AEROBIC ENDURANCE & FAT SHRED',
        description: 'Submerged in ambient cobalt-blue LED ceiling coves with high-velocity air-wash filtration. Features Matrix ClimbMill Stairmasters, Bluetooth spin cycles, and curved treadmills.',
        focus: 'VO2 Max, Cardiovascular Stamina & Caloric Burn',
        image: '{img_cardio_arena}',
        muscles: ['Cardiovascular System', 'Calves & Soleus', 'Quadriceps', 'Core Stabilizers'],
        equipment: [
          'Matrix Commercial ClimbMill Stairmasters',
          'Keiser M3i Bluetooth Spin Cycles',
          'Curved Non-Motorized Slat Treadmills',
          'Concept2 Ski-Ergs with PM5 Monitors',
          'RowErgs with Dynamic Wind Resistance',
          'Heart-Rate Telemetry Screens'
        ]
      }},
      combat: {{
        code: 'WORLI HQ // ZONE-C',
        title: 'MMA Combat Fighting Cage',
        subtitle: 'FULL-CONTACT STRIKING & MUAY THAI',
        description: 'Dedicated combat training sector equipped with Fairtex teardrop heavy bags, MMA cage flooring, Thai kick shields, and pro ring timers led by Kru Siddharth.',
        focus: 'Striking Power, Clinch Velocity & Fight Conditioning',
        image: '{img_floor_wide}',
        muscles: ['Rotational Core & Obliques', 'Shoulder Girdle', 'Hip Flexors', 'Fast-Twitch Kinetic Chain'],
        equipment: [
          'Fairtex 6ft Heavy Muay Thai Bags',
          'MMA Cage Sparring & Grappling Mats',
          'Thai Kick Pads & Leather Focus Mitts',
          'Pro Round Countdown Fight Timers',
          'Teardrop Upper-Cut Heavy Bags',
          'Hand Wrap & Speed Bag Station'
        ]
      }},
      zumba: {{
        code: 'WORLI HQ // ZONE-D',
        title: 'Zumba & Dance Sound Stage',
        subtitle: '650+ KCAL RHYTHMIC CALORIE INFERNO',
        description: 'Concert-grade acoustics with laser strobe lighting and sprung ash wood shock-absorbing flooring. Led by certified ZIN Director Coach Natasha Fernandez.',
        focus: 'High-Tempo Latin Cardio, Aerobic Stamina & Rhythm',
        image: '{img_selectorized}',
        muscles: ['Full Body Kinetic Aerobics', 'Cardiovascular Health', 'Calves & Glutes', 'Core Stability'],
        equipment: [
          'Sprung Shock-Absorbing Wood Floor',
          'Concert Grade High-Fidelity Audio Rig',
          'Laser & Ambient Color Strobe Lighting',
          'Studio Aerobic Steppers & Resistance Bands',
          'Full-Length Wall Mirrors with Perimeter Glow',
          'Chilled Air-Wash Climate Control'
        ]
      }}
    }};

    function switchZone(zoneKey) {{
      const data = zonesData[zoneKey];
      if (!data) return;

      document.querySelectorAll('.zone-tab-btn').forEach(btn => {{
        btn.className = 'zone-tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all text-chrome hover:text-white';
      }});
      const activeBtn = document.getElementById(`tab-${{zoneKey}}`);
      if (activeBtn) {{
        activeBtn.className = 'zone-tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_15px_rgba(37,99,235,0.4)]';
      }}

      document.getElementById('zone-code-tag').textContent = data.code;
      document.getElementById('zone-title').textContent = data.title;
      document.getElementById('zone-subtitle').textContent = data.subtitle;
      document.getElementById('zone-description').textContent = data.description;
      document.getElementById('zone-focus-text').textContent = data.focus;
      
      const img = document.getElementById('zone-image');
      img.style.opacity = '0';
      setTimeout(() => {{
        img.src = data.image;
        img.style.opacity = '1';
      }}, 200);

      const musclesContainer = document.getElementById('zone-muscles-list');
      musclesContainer.innerHTML = '';
      data.muscles.forEach(m => {{
        const badge = document.createElement('span');
        badge.className = 'px-2.5 py-1 rounded-md bg-cobalt-neon/15 border border-cobalt-bright/30 text-cobalt-bright text-xs font-medium';
        badge.textContent = m;
        musclesContainer.appendChild(badge);
      }});

      const eqContainer = document.getElementById('zone-equipment-grid');
      eqContainer.innerHTML = '';
      data.equipment.forEach(eq => {{
        const item = document.createElement('div');
        item.className = 'p-2.5 rounded-xl bg-obsidian/70 border border-white/10 flex items-center gap-2';
        item.innerHTML = `
          <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-cobalt-bright flex-shrink-0"></i>
          <span class="text-titanium">${{eq}}</span>
        `;
        eqContainer.appendChild(item);
      }});

      lucide.createIcons();
      playUiTick();
    }}

    function updateComparisonSlider(val) {{
      const clip = document.getElementById('comparison-clip');
      const handle = document.getElementById('comparison-handle');
      if (clip) clip.style.width = `${{val}}%`;
      if (handle) handle.style.left = `${{val}}%`;
    }}

    let selectedGender = 'male';

    function setGender(g) {{
      selectedGender = g;
      const maleBtn = document.getElementById('gender-male');
      const femaleBtn = document.getElementById('gender-female');
      if (g === 'male') {{
        maleBtn.className = 'gender-btn py-2.5 px-3 rounded-xl border border-cobalt-bright bg-blue-500/20 text-white text-xs font-bold font-oswald tracking-wide flex items-center justify-center gap-2';
        femaleBtn.className = 'gender-btn py-2.5 px-3 rounded-xl border border-white/10 bg-obsidian text-chrome hover:text-white text-xs font-bold font-oswald tracking-wide flex items-center justify-center gap-2';
      }} else {{
        femaleBtn.className = 'gender-btn py-2.5 px-3 rounded-xl border border-pink-400 bg-pink-500/20 text-white text-xs font-bold font-oswald tracking-wide flex items-center justify-center gap-2';
        maleBtn.className = 'gender-btn py-2.5 px-3 rounded-xl border border-white/10 bg-obsidian text-chrome hover:text-white text-xs font-bold font-oswald tracking-wide flex items-center justify-center gap-2';
      }}
      playUiTick();
      calculateSplit();
    }}

    function calculateSplit() {{
      const age = parseInt(document.getElementById('calc-age')?.value) || 26;
      const weight = parseFloat(document.getElementById('calc-weight')?.value) || 74;
      const height = parseFloat(document.getElementById('calc-height')?.value) || 176;
      const days = parseInt(document.getElementById('calc-days')?.value) || 4;
      const goal = document.getElementById('calc-goal')?.value || 'muscle';

      const heightInMeters = height / 100;
      const bmi = (weight / (heightInMeters * heightInMeters)).toFixed(1);
      
      let bmiCategory = 'Optimal / Normal';
      let bmiColor = 'text-emerald-400';
      if (bmi < 18.5) {{ bmiCategory = 'Underweight'; bmiColor = 'text-amber-400'; }}
      else if (bmi >= 25 && bmi < 29.9) {{ bmiCategory = 'Overweight Baseline'; bmiColor = 'text-amber-400'; }}
      else if (bmi >= 30) {{ bmiCategory = 'High Adiposity'; bmiColor = 'text-neon-magenta'; }}

      let bmr = (selectedGender === 'male')
        ? (10 * weight) + (6.25 * height) - (5 * age) + 5
        : (10 * weight) + (6.25 * height) - (5 * age) - 161;

      let multiplier = 1.375;
      if (days === 4) multiplier = 1.45;
      if (days === 5) multiplier = 1.55;
      if (days >= 6) multiplier = 1.7;

      const tdee = Math.round(bmr * multiplier);

      let targetCalories = tdee;
      let proteinPerKg = 2.0;

      if (goal === 'muscle') {{
        targetCalories = tdee + 350;
        proteinPerKg = 2.2;
      }} else if (goal === 'fatloss') {{
        targetCalories = Math.max(1400, tdee - 500);
        proteinPerKg = 2.3;
      }} else {{
        targetCalories = tdee;
        proteinPerKg = 2.0;
      }}

      const dailyProteinGrams = Math.round(weight * proteinPerKg);

      const bmiEl = document.getElementById('output-bmi');
      if (bmiEl) bmiEl.textContent = bmi;
      const bmiCatEl = document.getElementById('output-bmi-cat');
      if (bmiCatEl) {{
        bmiCatEl.textContent = bmiCategory;
        bmiCatEl.className = `text-xs font-medium mt-0.5 ${{bmiColor}}`;
      }}
      const calEl = document.getElementById('output-calories');
      if (calEl) calEl.textContent = targetCalories.toLocaleString();
      const protEl = document.getElementById('output-protein');
      if (protEl) protEl.textContent = `${{dailyProteinGrams}}g`;

      renderCustomSplitDays(days, goal);
    }}

    function renderCustomSplitDays(days, goal) {{
      const container = document.getElementById('output-split-container');
      if (!container) return;
      container.innerHTML = '';

      let splits = [];
      if (days === 3) {{
        splits = [
          {{ day: 'DAY 1', badge: 'bg-blue-500/20 text-cobalt-bright', title: 'Heavy Iron Push & Hack Squat Overload', desc: '45° Hack Squat, Incline Dumbbell Press, Standing Overhead Press, Dips' }},
          {{ day: 'DAY 2', badge: 'bg-purple-500/20 text-neon-violet', title: 'MMA Fight Bag Striking & Cable Pull', desc: 'Fairtex Heavy Bag Rounds, Weighted Pull-Ups, Cable Face Pulls, Clinch Core' }},
          {{ day: 'DAY 3', badge: 'bg-pink-500/20 text-neon-magenta', title: 'Zumba Calorie Inferno & Post-Steam Flush', desc: '60-min Latin Rhythm Beat, Dumbbell Pump, 20-min Eucalyptus Steam Recovery' }}
        ];
      }} else if (days === 4) {{
        splits = [
          {{ day: 'DAY 1', badge: 'bg-blue-500/20 text-cobalt-bright', title: 'Upper Body Heavy Iron (Pecs / Delts / Arms)', desc: 'Barbell Incline Press, Chest-Supported Rows, Cable Lateral Raises, Weighted Dips' }},
          {{ day: 'DAY 2', badge: 'bg-emerald-500/20 text-emerald-400', title: 'Lower Body Plate Hack Squat & Posterior', desc: '45° Hack Squat 4x8, Romanian Deadlifts, Bulgarian Split Squats, Steam Flush' }},
          {{ day: 'DAY 3', badge: 'bg-purple-500/20 text-neon-violet', title: 'MMA Striking & Combat Core Circuit', desc: 'Heavy Bag Combinations, Speed Ball, Thai Pad Rounds with Kru Siddharth' }},
          {{ day: 'DAY 4', badge: 'bg-pink-500/20 text-neon-magenta', title: 'Zumba High-Calorie Stage + Full Recovery', desc: '650+ kcal Zumba Choreography, Foam Roll, 25-min Eucalyptus Steam Session' }}
        ];
      }} else {{
        splits = [
          {{ day: 'DAY 1', badge: 'bg-blue-500/20 text-cobalt-bright', title: 'Heavy Push Hypertrophy (Iron Bay)', desc: 'Heavy Incline DB Press, Standing OHP, Cable Flyes, Overhead Skullcrushers' }},
          {{ day: 'DAY 2', badge: 'bg-purple-500/20 text-neon-violet', title: 'Heavy Pull & Back Thickness (Selectorized)', desc: 'Weighted Pull-Ups, Seated Cable Rows, Lat Pulldowns, Incline Bicep Curls' }},
          {{ day: 'DAY 3', badge: 'bg-emerald-500/20 text-emerald-400', title: 'Quad Dominant Legs & 45° Hack Squat', desc: 'Olympic Squats, 45° Hack Squat, Leg Extensions, Standing Calves + Steam' }},
          {{ day: 'DAY 4', badge: 'bg-purple-500/20 text-neon-violet', title: 'MMA Fight Camp Striking & Bag Conditioning', desc: 'Fairtex Teardrop Bags, Sparring Footwork, Clinch Knee Strikes, Core Planks' }},
          {{ day: 'DAY 5', badge: 'bg-pink-500/20 text-neon-magenta', title: 'Zumba Dance Sound Stage & Steam Detox', desc: 'Latin & Bollywood Cardio Fusion, Rain Shower, Eucalyptus Steam Aromatherapy' }}
        ];
      }}

      splits.forEach(s => {{
        const row = document.createElement('div');
        row.className = 'p-3.5 rounded-xl bg-obsidian/60 border border-white/10 flex items-start gap-3';
        row.innerHTML = `
          <span class="px-2 py-0.5 rounded text-xs font-mono font-bold ${{s.badge}}">${{s.day}}</span>
          <div>
            <div class="text-sm font-bold text-white">${{s.title}}</div>
            <div class="text-xs text-chrome mt-0.5">${{s.desc}}</div>
          </div>
        `;
        container.appendChild(row);
      }});
    }}

    function sendBlueprintWhatsApp() {{
      const weight = document.getElementById('calc-weight')?.value || '74';
      const height = document.getElementById('calc-height')?.value || '176';
      const bmi = document.getElementById('output-bmi')?.textContent || '23.9';
      const calories = document.getElementById('output-calories')?.textContent || '2480';
      const protein = document.getElementById('output-protein')?.textContent || '162g';
      const goalEl = document.getElementById('calc-goal');
      const goal = goalEl ? goalEl.options[goalEl.selectedIndex].text : 'Lean Muscle';

      const message = `Hi Midtown Fitness Worli! Here is my AI Workout & Macro Blueprint from your website:\n• Weight: ${{weight}}kg | Height: ${{height}}cm\n• BMI: ${{bmi}}\n• Target Calories: ${{calories}} kcal/day\n• Daily Protein: ${{protein}}\n• Goal: ${{goal}}\nI want to book my free workout session, trainer review, and steam pass.`;
      
      window.open(`https://wa.me/919819999103?text=${{encodeURIComponent(message)}}`, '_blank');
      showToast('Connecting to WhatsApp with your Custom Blueprint!');
    }}

    function bookTrainer(trainerName, specialty) {{
      const message = `Hi Midtown Fitness Worli! I would like to book a 1-on-1 consultation session with ${{trainerName}} (${{specialty}}). Please let me know available slots.`;
      window.open(`https://wa.me/919819999103?text=${{encodeURIComponent(message)}}`, '_blank');
      showToast(`Selected ${{trainerName}}! Opening WhatsApp VIP Desk.`);
    }}

    const classesData = [
      {{
        id: 'kickboxing-01',
        discipline: 'mma',
        title: 'Muay Thai Striking & Heavy Bag Camp',
        time: '11:00 AM - 12:00 PM',
        coach: 'Kru Siddharth Verma',
        sweatRating: 5,
        totalSlots: 14,
        bookedSlots: 12,
        tag: 'MMA & STRIKING',
        badgeColor: 'border-neon-violet/40 text-neon-violet'
      }},
      {{
        id: 'zumba-01',
        discipline: 'zumba',
        title: 'Zumba Calorie Inferno (650+ kcal)',
        time: '06:00 PM - 07:00 PM',
        coach: 'Coach Natasha Fernandez',
        sweatRating: 5,
        totalSlots: 20,
        bookedSlots: 17,
        tag: 'ZUMBA SOUND STAGE',
        badgeColor: 'border-pink-400/40 text-pink-400'
      }},
      {{
        id: 'strength-01',
        discipline: 'strength',
        title: 'Heavy Barbell Compound Overload',
        time: '08:30 AM - 09:30 AM',
        coach: 'Coach Aryan Sawant',
        sweatRating: 4,
        totalSlots: 12,
        bookedSlots: 10,
        tag: 'HEAVY IRON BAY',
        badgeColor: 'border-blue-400/40 text-cobalt-bright'
      }},
      {{
        id: 'hiit-01',
        discipline: 'hiit',
        title: 'MetCon Gauntlet & Core Shred',
        time: '07:00 AM - 08:00 AM',
        coach: 'Coach Dev Malhotra',
        sweatRating: 5,
        totalSlots: 16,
        bookedSlots: 13,
        tag: 'METCON HIIT',
        badgeColor: 'border-emerald-400/40 text-emerald-400'
      }},
      {{
        id: 'mma-02',
        discipline: 'mma',
        title: 'MMA Clinch Defense & Ground Sparring',
        time: '07:30 PM - 08:30 PM',
        coach: 'Kru Siddharth Verma',
        sweatRating: 5,
        totalSlots: 12,
        bookedSlots: 10,
        tag: 'COMBAT SPARRING',
        badgeColor: 'border-neon-violet/40 text-neon-violet'
      }},
      {{
        id: 'zumba-02',
        discipline: 'zumba',
        title: 'Bollywood Cardio & Rhythm Blast',
        time: '08:30 PM - 09:30 PM',
        coach: 'Coach Natasha Fernandez',
        sweatRating: 4,
        totalSlots: 18,
        bookedSlots: 14,
        tag: 'DANCE FITNESS',
        badgeColor: 'border-pink-400/40 text-pink-400'
      }}
    ];

    function renderClasses(filter) {{
      const grid = document.getElementById('classes-grid');
      if (!grid) return;
      grid.innerHTML = '';

      const filtered = filter === 'all' 
        ? classesData 
        : classesData.filter(c => c.discipline === filter);

      filtered.forEach(c => {{
        const remaining = c.totalSlots - c.bookedSlots;
        const card = document.createElement('div');
        card.className = 'glass-panel rounded-3xl p-6 border border-white/10 flex flex-col justify-between hover:border-white/25 transition-all group';

        let flames = '';
        for (let i = 0; i < 5; i++) {{
          flames += i < c.sweatRating 
            ? '<i data-lucide="flame" class="w-3.5 h-3.5 fill-current text-neon-magenta"></i>' 
            : '<i data-lucide="flame" class="w-3.5 h-3.5 text-chrome/30"></i>';
        }}

        card.innerHTML = `
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase border ${{c.badgeColor}}">
                ${{c.tag}}
              </span>
              <div class="flex items-center gap-0.5" title="Sweat Rating: ${{c.sweatRating}}/5">
                ${{flames}}
              </div>
            </div>

            <h4 class="text-lg font-syne font-bold text-white group-hover:text-cobalt-bright transition-colors">
              ${{c.title}}
            </h4>

            <div class="space-y-2 mt-4 text-xs">
              <div class="flex items-center gap-2 text-titanium font-mono">
                <i data-lucide="clock" class="w-4 h-4 text-cobalt-bright"></i>
                <span>${{c.time}}</span>
              </div>
              <div class="flex items-center gap-2 text-chrome">
                <i data-lucide="user" class="w-4 h-4 text-chrome"></i>
                <span>${{c.coach}}</span>
              </div>
            </div>
          </div>

          <div class="pt-5 mt-4 border-t border-white/10 flex items-center justify-between">
            <div>
              <div class="text-[10px] font-mono text-chrome uppercase">Available Spots</div>
              <div class="text-xs font-bold ${{remaining <= 3 ? 'text-neon-magenta animate-pulse' : 'text-emerald-400'}}">
                ${{remaining <= 3 ? `Only ${{remaining}} spots left!` : `${{remaining}} slots open`}}
              </div>
            </div>

            <button onclick="openBookingModal('${{c.id}}')" 
                    class="px-4 py-2 rounded-xl text-xs font-oswald tracking-wider uppercase font-bold bg-white/10 group-hover:bg-cobalt-bright group-hover:text-obsidian text-white transition-all flex items-center gap-1.5 shadow-[0_0_15px_transparent] group-hover:shadow-[0_0_20px_rgba(37,99,235,0.4)]">
              <span>BOOK SPOT</span>
              <i data-lucide="arrow-right" class="w-3 h-3"></i>
            </button>
          </div>
        `;

        grid.appendChild(card);
      }});

      lucide.createIcons();
    }}

    function filterClasses(type) {{
      document.querySelectorAll('.class-filter-btn').forEach(btn => {{
        btn.className = 'class-filter-btn px-3.5 py-1.5 rounded-xl text-xs font-oswald tracking-wide font-bold bg-carbon text-chrome hover:text-white border border-white/10';
      }});
      event.target.className = 'class-filter-btn px-3.5 py-1.5 rounded-xl text-xs font-oswald tracking-wide font-bold bg-white text-obsidian';
      renderClasses(type);
      playUiTick();
    }}

    function openBookingModal(classId) {{
      const c = classesData.find(item => item.id === classId);
      if (!c) return;

      document.getElementById('booking-class-id').value = c.id;
      document.getElementById('modal-class-title').textContent = c.title;
      document.getElementById('modal-class-time').textContent = c.time;
      document.getElementById('modal-class-coach').textContent = c.coach;
      const remaining = c.totalSlots - c.bookedSlots;
      document.getElementById('modal-class-spots').textContent = `${{remaining}} Spots Left Today`;

      openModal('bookingModal');
    }}

    function handleBookingSubmit(e) {{
      e.preventDefault();
      const name = document.getElementById('book-name').value;
      const classId = document.getElementById('booking-class-id').value;

      const c = classesData.find(item => item.id === classId);
      if (c && c.bookedSlots < c.totalSlots) {{
        c.bookedSlots++;
      }}

      closeModal('bookingModal');
      playUiSuccess();
      showToast(`Spot Confirmed for ${{name}}! See you at Worli HQ.`);
      renderClasses('all');
    }}

    function handlePassSubmit(e) {{
      e.preventDefault();
      const name = document.getElementById('pass-name').value;
      
      closeModal('passModal');
      playUiSuccess();
      showToast(`VIP Pass + Steam Sanctuary Generated for ${{name}}!`);
    }}

    function setBillingCycle(cycle) {{
      const btnMonthly = document.getElementById('btn-monthly');
      const btnAnnual = document.getElementById('btn-annual');

      if (cycle === 'annual') {{
        btnAnnual.className = 'px-5 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all bg-gradient-to-r from-cobalt-bright to-cobalt-neon text-obsidian shadow-[0_0_15px_rgba(37,99,235,0.4)] flex items-center gap-1.5';
        btnMonthly.className = 'px-5 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all text-chrome hover:text-white';
        showToast('Annual Discount Applied: 25% OFF all VIP Tiers');
      }} else {{
        btnMonthly.className = 'px-5 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all bg-white text-obsidian';
        btnAnnual.className = 'px-5 py-2 rounded-xl text-xs sm:text-sm font-oswald tracking-wide font-bold transition-all text-chrome hover:text-white';
      }}
      playUiTick();
    }}

    function selectMembership(tier, price) {{
      const message = `Hi Midtown Fitness Worli! I am interested in joining the ${{tier}} membership (₹${{price}}). Please share sign-up details, steam access, and EMI options.`;
      window.open(`https://wa.me/919819999103?text=${{encodeURIComponent(message)}}`, '_blank');
      showToast(`Selected ${{tier}}! Connecting to Membership Desk.`);
    }}

    let audioCtx = null;
    let isPlaying = false;
    let currentTrackIdx = 0;
    let timerInterval = null;
    let trackSeconds = 0;
    let gainNode = null;
    let synthLoopTimeout = null;

    const tracks = [
      {{ name: 'Worli Cobalt Phonk Pulse', bpm: '132 BPM • Electronic Sub-Bass', tempo: 132 }},
      {{ name: 'MMA Striking Beat Drop', bpm: '142 BPM • Combat Energy', tempo: 142 }},
      {{ name: 'Zumba Latin Electro Heat', bpm: '128 BPM • High Calorie Groove', tempo: 128 }}
    ];

    function initAudioContext() {{
      if (!audioCtx) {{
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContext();
        gainNode = audioCtx.createGain();
        gainNode.gain.value = 0.5;
        gainNode.connect(audioCtx.destination);
      }}
      if (audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}
    }}

    function toggleSynthMusic() {{
      initAudioContext();
      if (isPlaying) {{
        stopSynthMusic();
      }} else {{
        startSynthMusic();
      }}
    }}

    function startSynthMusic() {{
      isPlaying = true;
      document.getElementById('synth-play-icon').setAttribute('data-lucide', 'pause');
      lucide.createIcons();
      showToast(`Now Playing: ${{tracks[currentTrackIdx].name}}`);
      playDrumBeatLoop();
      startTimer();
    }}

    function stopSynthMusic() {{
      isPlaying = false;
      clearTimeout(synthLoopTimeout);
      clearInterval(timerInterval);
      document.getElementById('synth-play-icon').setAttribute('data-lucide', 'play');
      lucide.createIcons();
    }}

    function startTimer() {{
      clearInterval(timerInterval);
      timerInterval = setInterval(() => {{
        trackSeconds++;
        const mins = Math.floor(trackSeconds / 60).toString().padStart(2, '0');
        const secs = (trackSeconds % 60).toString().padStart(2, '0');
        document.getElementById('track-timer').textContent = `${{mins}}:${{secs}}`;
      }}, 1000);
    }}

    function prevTrack() {{
      currentTrackIdx = (currentTrackIdx - 1 + tracks.length) % tracks.length;
      updateTrackDisplay();
      if (isPlaying) {{
        stopSynthMusic();
        startSynthMusic();
      }}
    }}

    function nextTrack() {{
      currentTrackIdx = (currentTrackIdx + 1) % tracks.length;
      updateTrackDisplay();
      if (isPlaying) {{
        stopSynthMusic();
        startSynthMusic();
      }}
    }}

    function updateTrackDisplay() {{
      document.getElementById('track-name').textContent = tracks[currentTrackIdx].name;
      document.getElementById('track-bpm').textContent = tracks[currentTrackIdx].bpm;
      trackSeconds = 0;
      document.getElementById('track-timer').textContent = '00:00';
      playUiTick();
    }}

    function setSynthVolume(val) {{
      if (gainNode) {{
        gainNode.gain.value = parseFloat(val);
      }}
    }}

    function playDrumBeatLoop() {{
      if (!isPlaying || !audioCtx) return;

      const track = tracks[currentTrackIdx];
      const beatInterval = (60 / track.tempo) * 1000;

      playKick(audioCtx.currentTime);
      playHiHat(audioCtx.currentTime + (beatInterval / 2000));
      playBassNote(audioCtx.currentTime);

      synthLoopTimeout = setTimeout(() => {{
        playDrumBeatLoop();
      }}, beatInterval);
    }}

    function playKick(time) {{
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(gainNode);

      osc.frequency.setValueAtTime(150, time);
      osc.frequency.exponentialRampToValueAtTime(0.01, time + 0.35);

      gain.gain.setValueAtTime(0.8, time);
      gain.gain.exponentialRampToValueAtTime(0.01, time + 0.35);

      osc.start(time);
      osc.stop(time + 0.35);
    }}

    function playHiHat(time) {{
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'highpass';
      osc.frequency.setValueAtTime(8000, time);
      osc.connect(gain);
      gain.connect(gainNode);

      gain.gain.setValueAtTime(0.2, time);
      gain.gain.exponentialRampToValueAtTime(0.01, time + 0.08);

      osc.start(time);
      osc.stop(time + 0.08);
    }}

    function playBassNote(time) {{
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sawtooth';
      const notes = [55, 65.41, 73.42, 82.41];
      const note = notes[Math.floor(Math.random() * notes.length)];
      osc.frequency.setValueAtTime(note, time);

      osc.connect(gain);
      gain.connect(gainNode);

      gain.gain.setValueAtTime(0.3, time);
      gain.gain.exponentialRampToValueAtTime(0.01, time + 0.4);

      osc.start(time);
      osc.stop(time + 0.4);
    }}

    function initAudioVisualizer() {{
      const canvas = document.getElementById('audio-visualizer');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const numBars = 24;

      function renderFrame() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const barWidth = canvas.width / numBars - 2;

        for (let i = 0; i < numBars; i++) {{
          let height = 3;
          if (isPlaying) {{
            const t = Date.now() / 150;
            height = Math.abs(Math.sin(t + i * 0.5) * 22) + (Math.random() * 6);
          }}
          const x = i * (barWidth + 2);
          const y = canvas.height - height;

          const grad = ctx.createLinearGradient(0, canvas.height, 0, 0);
          grad.addColorStop(0, '#38bdf8');
          grad.addColorStop(1, '#8b5cf6');
          ctx.fillStyle = grad;
          ctx.fillRect(x, y, barWidth, height);
        }}
        requestAnimationFrame(renderFrame);
      }}
      renderFrame();
    }}

    function toggleAudioMin() {{
      const body = document.getElementById('player-body');
      const btn = document.getElementById('min-player-btn');
      if (body.classList.contains('hidden')) {{
        body.classList.remove('hidden');
        btn.innerHTML = '<i data-lucide="chevron-down" class="w-3.5 h-3.5"></i>';
      }} else {{
        body.classList.add('hidden');
        btn.innerHTML = '<i data-lucide="chevron-up" class="w-3.5 h-3.5"></i>';
      }}
      lucide.createIcons();
    }}

    let sfxEnabled = true;

    function toggleAudioFx() {{
      sfxEnabled = !sfxEnabled;
      const icon = document.getElementById('sfx-icon');
      if (sfxEnabled) {{
        icon.setAttribute('data-lucide', 'volume-2');
        showToast('Interface SFX Enabled');
      }} else {{
        icon.setAttribute('data-lucide', 'volume-x');
        showToast('Interface SFX Muted');
      }}
      lucide.createIcons();
    }}

    function playUiTick() {{
      if (!sfxEnabled) return;
      try {{
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        const ctx = new AudioContext();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.frequency.setValueAtTime(650, ctx.currentTime);
        gain.gain.setValueAtTime(0.04, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.03);
        osc.start();
        osc.stop(ctx.currentTime + 0.03);
      }} catch (e) {{}}
    }}

    function playUiSuccess() {{
      if (!sfxEnabled) return;
      try {{
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        const ctx = new AudioContext();
        [523.25, 783.99, 1046.50].forEach((freq, idx) => {{
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'triangle';
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.frequency.setValueAtTime(freq, ctx.currentTime + idx * 0.06);
          gain.gain.setValueAtTime(0.08, ctx.currentTime + idx * 0.06);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.06 + 0.25);
          osc.start(ctx.currentTime + idx * 0.06);
          osc.stop(ctx.currentTime + idx * 0.06 + 0.25);
        }});
      }} catch (e) {{}}
    }}

    function openModal(id) {{
      const modal = document.getElementById(id);
      if (!modal) return;
      modal.classList.remove('hidden');
      setTimeout(() => {{
        modal.classList.remove('opacity-0');
      }}, 10);
      playUiTick();
    }}

    function closeModal(id) {{
      const modal = document.getElementById(id);
      if (!modal) return;
      modal.classList.add('opacity-0');
      setTimeout(() => {{
        modal.classList.add('hidden');
      }}, 300);
      playUiTick();
    }}

    let toastTimeout;
    function showToast(msg) {{
      const toast = document.getElementById('toast');
      const msgEl = document.getElementById('toast-msg');
      if (!toast || !msgEl) return;
      
      msgEl.textContent = msg;
      toast.classList.remove('translate-x-full');
      
      clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => {{
        toast.classList.add('translate-x-full');
      }}, 3500);
    }}
  </script>
</body>
</html>
'''

with open(r'c:\Users\dudam\OneDrive\Desktop\songs\index.html', 'w', encoding='utf-8') as out_f:
    out_f.write(html_content)

print(f"Generated index.html successfully! File size: {len(html_content)} bytes")
