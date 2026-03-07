<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grace · work-from-home</title>
    <!-- Font Awesome for icons (free) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        /* ----- GLOBAL & CUSTOM CURSOR ----- */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            cursor: none; /* hide default */
        }
        body {
            font-family: 'Segoe UI', Roboto, system-ui, sans-serif;
            background: #faf9f8;
            color: #1e1e1e;
            line-height: 1.6;
            padding: 2rem 1rem;
            min-height: 100vh;
        }
        #cat-cursor {
            position: fixed;
            width: 32px; height: 32px;
            pointer-events: none;
            z-index: 9999;
            font-size: 28px;
            transform: translate(-50%, -50%);
            transition: transform 0.1s ease;
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2));
            display: none;
        }
        /* all text turns green on hover */
        *:hover {
            color: #4CAF50 !important;
        }
        /* but keep button background intact */
        .btn:hover {
            background-color: inherit;
            border-color: #4CAF50;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        section { margin-bottom: 4rem; }
        h1 { font-size: 2.5rem; margin-bottom: 1rem; color: #2c3e50; }
        h2 {
            font-size: 2rem;
            margin-bottom: 2rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e0e0e0;
            color: #2c3e50;
        }
        /* about card */
        .about-card {
            background: white;
            border-radius: 24px;
            padding: 2rem;
            box-shadow: 0 10px 30px -10px rgba(0,0,0,0.1);
            margin-bottom: 3rem;
            border: 1px solid #f0f0f0;
        }
        .about-items {
            display: flex;
            flex-wrap: wrap;
            gap: 1.5rem;
            margin-top: 1.5rem;
        }
        .about-item {
            flex: 1 1 200px;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            background: #f5f5f5;
            padding: 1rem 1.5rem;
            border-radius: 50px;
            font-size: 1.1rem;
            color: #2c3e50;
        }
        .about-item span:first-child { font-size: 1.8rem; }

        /* project cards grid */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }
        .card {
            background: white;
            border-radius: 28px;
            padding: 1.8rem;
            box-shadow: 0 10px 25px -8px rgba(0,0,0,0.07);
            transition: all 0.25s ease;
            border: 1px solid #f5f0f0;
            display: flex;
            flex-direction: column;
        }
        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 25px 35px -12px rgba(76, 175, 80, 0.2);
            border-color: #c8e6c9;
        }
        .card h3 {
            font-size: 1.6rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .card .description {
            color: #4a4a4a;
            margin-bottom: 1.5rem;
            flex: 1;
        }
        .card .links {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
            margin-top: auto;
            align-items: center;
        }

        /* button style (replaces shields.io badges) */
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background-color: #f0f0f0;
            color: #1e1e1e;
            padding: 0.6rem 1.2rem;
            border-radius: 40px;
            font-size: 0.9rem;
            font-weight: 500;
            text-decoration: none;
            border: 1px solid transparent;
            transition: all 0.2s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        .btn i { font-size: 1.2rem; }
        /* color variants */
        .btn.linkedin { background-color: #90CAF9; color: #0a66c2; }
        .btn.play { background-color: #F8BBD0; color: #b0003a; }
        .btn.chart { background-color: #FFAB91; color: #bf360c; }
        .btn.wiki { background-color: #CE93D8; color: #4a148c; }
        .btn.gov { background-color: #9FA8DA; color: #1a237e; }
        .btn.safety { background-color: #B39DDB; color: #311b92; }
        .btn.portfolio { background-color: #9FA8DA; color: #283593; }

        /* collaboration area */
        .collab {
            text-align: center;
            background: #e8f0fe;
            border-radius: 60px;
            padding: 3rem;
            margin-top: 3rem;
            border: 1px dashed #90CAF9;
        }
        .collab h2 { border-bottom: none; margin-bottom: 1rem; }

        /* responsive */
        @media (max-width: 600px) {
            body { padding: 1rem; }
            h1 { font-size: 2rem; }
            .about-item { flex: 1 1 100%; }
        }
        /* hide custom cursor on touch devices */
        @media (hover: none) and (pointer: coarse) {
            * { cursor: auto; }
            #cat-cursor { display: none !important; }
        }
    </style>
</head>
<body>
    <div id="cat-cursor">🐱</div>
    <div class="container">

        <!-- ABOUT (top) -->
        <section id="about">
            <h1>👩‍💻 work-from-home-</h1>
            <div class="about-card">
                <h2>🌸 about me</h2>
                <div class="about-items">
                    <div class="about-item"><span>🎓</span> <span>Recently Graduated</span></div>
                    <div class="about-item"><span>🧠</span> <span>Human-AI Relationships, Transformative Impacts of AI</span></div>
                    <div class="about-item"><span>🌱</span> <span>Always exploring new technologies & interdisciplinary projects</span></div>
                </div>
            </div>
        </section>

        <!-- PROJECTS -->
        <section id="projects">
            <h2>🌐 AI-co-created projects</h2>
            <div class="projects-grid">

                <!-- 1. Manus Cat -->
                <div class="card">
                    <h3> Manus Cat · LinkedIn Newsletter</h3>
                    <div class="description">
                        Weekly insights on macro forces, tech news, society, and of course AI. Scroll down to see my AI employee.
                    </div>
                    <div class="links">
                        <a href="https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7422191016994217984" target="_blank" class="btn linkedin"><i class="fab fa-linkedin"></i> Follow Newsletter</a>
                    </div>
                </div>

                <!-- 2. Momentum Dashboard -->
                <div class="card">
                    <h3> Momentum Dashboard</h3>
                    <div class="description">
                        <em>(account needed)</em><br>
                        A gentle life management tool to visualize and manage energy through small, science‑backed recovery actions. Rest is part of your momentum.<br>
                        <small>Ideas for improvement? Collaboration welcome!</small>
                    </div>
                    <div class="links">
                        <a href="https://screenapp.io/app/v/YzJV1A2nJl" target="_blank" class="btn play"><i class="fas fa-play"></i> Demo</a>
                        <a href="https://rugged-build-your-momentum.base44.app/Home" target="_blank" class="btn chart"><i class="fas fa-chart-bar"></i> Dashboard</a>
                    </div>
                </div>

                <!-- 3. AI Wiki (card 1) -->
                <div class="card">
                    <h3>📖 AI Wiki</h3>
                    <div class="description">
                        <strong>Focus:</strong> Knowledge Base · Comprehensive LLM concepts and AI fundamentals.
                    </div>
                    <div class="links">
                        <a href="https://rcnd1qqt63cw.feishu.cn/wiki/UfMaw8HkmiQR8JkdZwjcmQNjnyc?from=from_copylink" target="_blank" class="btn wiki"><i class="fas fa-book-open"></i> Open Wiki</a>
                    </div>
                </div>

                <!-- 4. Chinese AI Governance -->
                <div class="card">
                    <h3>📋 Chinese AI Governance</h3>
                    <div class="description">
                        <strong>Focus:</strong> Policy & Governance · Framework for understanding AI governance in China.
                    </div>
                    <div class="links">
                        <a href="https://rcnd1qqt63cw.feishu.cn/wiki/P5O8w8uENiE6RGkVrw2c5pUunTc?from=from_copylink" target="_blank" class="btn gov"><i class="fas fa-gavel"></i> Read More</a>
                    </div>
                </div>

                <!-- 5. Prompt Red Teaming -->
                <div class="card">
                    <h3>⚠️ Prompt Red Teaming</h3>
                    <div class="description">
                        <strong>Focus:</strong> Safety & Ethics · Moral evaluations and safety testing of AI systems.
                    </div>
                    <div class="links">
                        <a href="https://rcnd1qqt63cw.feishu.cn/wiki/Ep3ewlDZligXJMkiZnxcQsDDnNc?from=from_copylink" target="_blank" class="btn safety"><i class="fas fa-shield-alt"></i> View Research</a>
                    </div>
                </div>

                <!-- 6. Academic Portfolio -->
                <div class="card">
                    <h3>🎓 Academic Portfolio</h3>
                    <div class="description">
                        Personal research showcase, study tools, AI sources, and your everyday quote.<br>
                        <em>"𝒰𝓃𝒸𝒽𝒶𝒾𝓃𝑒𝒹 𝑀𝑒𝓁𝑜𝒹𝓎" — take your time.</em>
                    </div>
                    <div class="links">
                        <a href="https://app--graces-kiosk-a4c1d845.base44.app/" target="_blank" class="btn portfolio"><i class="fas fa-globe"></i> Grace's Kiosk</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- COLLABORATE -->
        <section id="collaborate">
            <div class="collab">
                <h2>💡 Let's Collaborate!</h2>
                <p style="font-size: 1.2rem; margin-bottom: 1rem;">Interested in any project? Have an idea? Let's connect.</p>
                <div class="links" style="justify-content: center;">
                    <a href="#" class="btn linkedin"><i class="fab fa-linkedin"></i> LinkedIn</a>
                    <a href="#" class="btn wiki"><i class="fas fa-envelope"></i> Email</a>
                </div>
            </div>
        </section>

        <hr>
        <footer style="text-align: center; color: #aaa; padding: 2rem 0 1rem;">✦ built with curiosity ✦</footer>
    </div>

    <!-- kitten cursor script -->
    <script>
        (function() {
            const cursor = document.getElementById('cat-cursor');
            if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
                cursor.style.display = 'block';
                document.addEventListener('mousemove', e => {
                    cursor.style.left = e.clientX + 'px';
                    cursor.style.top = e.clientY + 'px';
                });
                document.querySelectorAll('a, button, .btn, .card').forEach(el => {
                    el.addEventListener('mouseenter', () => cursor.style.transform = 'translate(-50%, -50%) scale(1.2)');
                    el.addEventListener('mouseleave', () => cursor.style.transform = 'translate(-50%, -50%) scale(1)');
                });
            } else {
                cursor.style.display = 'none';
                document.body.style.cursor = 'auto';
            }
        })();
    </script>
</body>
</html>
