html_content = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anvesha Khandelwal - Portfolio</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">
  
  <!-- Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <style>
    /* Theme Variables */
    :root {
      --bg-base: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: #f1f5f9;
      --text-main: #0f172a;
      --text-secondary: #475569;
      --text-tertiary: #94a3b8;
      --accent-main: #2563eb;
      --accent-hover: #1d4ed8;
      --border-color: #e2e8f0;
      
      --particle-color: rgba(37, 99, 235, 0.4);
      --particle-line: rgba(37, 99, 235, 0.15);
    }

    html.dark {
      --bg-base: #0f172a;
      --bg-surface: #1e293b;
      --bg-card: #334155;
      --text-main: #f8fafc;
      --text-secondary: #cbd5e1;
      --text-tertiary: #64748b;
      --accent-main: #3b82f6;
      --accent-hover: #60a5fa;
      --border-color: #334155;
      
      --particle-color: rgba(96, 165, 250, 0.4);
      --particle-line: rgba(96, 165, 250, 0.15);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Inter', sans-serif;
      background-color: var(--bg-base);
      color: var(--text-main);
      line-height: 1.6;
      transition: background-color 0.4s, color 0.4s;
      overflow-x: hidden;
    }

    h1, h2, h3, h4, .logo { font-family: 'Outfit', sans-serif; }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 2rem;
    }

    /* Navigation */
    nav {
      position: fixed;
      top: 0;
      width: 100%;
      background: rgba(var(--bg-base), 0.8);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      z-index: 1000;
      border-bottom: 1px solid var(--border-color);
      transition: background-color 0.4s, border-color 0.4s;
    }

    nav .container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 80px;
    }

    .logo {
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--text-main);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .logo-icon { color: var(--accent-main); }

    .nav-menus {
        display: flex;
        align-items: center;
        gap: 2rem;
    }

    .nav-links {
      display: flex;
      gap: 2rem;
      list-style: none;
    }

    .nav-links a {
      color: var(--text-secondary);
      text-decoration: none;
      font-weight: 500;
      font-size: 0.95rem;
      transition: color 0.3s;
      cursor: pointer;
    }

    .nav-links a:hover { color: var(--accent-main); }

    .theme-toggle {
        background: var(--bg-surface);
        border: 1px solid var(--border-color);
        color: var(--text-main);
        width: 40px; height: 40px;
        border-radius: 50%;
        display: flex; justify-content: center; align-items: center;
        cursor: pointer;
        transition: all 0.3s;
    }
    .theme-toggle:hover {
        background: var(--bg-card);
        transform: scale(1.05);
    }

    /* Hero Section */
    .hero {
      position: relative;
      min-height: 100vh;
      display: grid;
      grid-template-columns: 1fr 1fr;
      align-items: center;
      padding-top: 80px;
      max-width: 1200px;
      margin: 0 auto;
      gap: 4rem;
      padding-inline: 2rem;
    }

    .hero-content {
        z-index: 10;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        background: var(--bg-surface);
        border: 1px solid var(--border-color);
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        color: var(--text-secondary);
        margin-bottom: 1.5rem;
    }

    .ping {
        width: 8px; height: 8px;
        background: #10b981;
        border-radius: 50%;
        position: relative;
    }
    .ping::after {
        content: '';
        position: absolute;
        top: -4px; left: -4px; right: -4px; bottom: -4px;
        border-radius: 50%;
        background: #10b981;
        animation: ping 2s cubic-bezier(0, 0, 0.2, 1) infinite;
    }

    .hero-title {
      font-size: 4.5rem;
      font-weight: 800;
      line-height: 1.1;
      margin-bottom: 1.5rem;
      color: var(--text-main);
    }

    .hero-title span { color: var(--accent-main); }

    .hero-desc {
      font-size: 1.1rem;
      color: var(--text-secondary);
      margin-bottom: 2.5rem;
      max-width: 500px;
    }

    .hero-actions {
      display: flex;
      gap: 1rem;
    }

    .btn {
      padding: 0.8rem 1.8rem;
      border-radius: 8px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s;
      font-size: 0.95rem;
    }

    .btn-primary {
      background: var(--accent-main);
      color: #ffffff;
      border: 1px solid var(--accent-main);
      box-shadow: 0 4px 14px 0 rgba(37, 99, 235, 0.39);
    }

    .btn-primary:hover {
      background: var(--accent-hover);
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.23);
      transform: translateY(-2px);
    }

    .btn-secondary {
      background: var(--bg-surface);
      color: var(--text-main);
      border: 1px solid var(--border-color);
    }

    .btn-secondary:hover {
      background: var(--bg-card);
      transform: translateY(-2px);
    }

    .hero-visual {
        position: relative;
        width: 100%;
        height: 500px;
        border-radius: 24px;
        background: var(--bg-surface);
        border: 1px solid var(--border-color);
        overflow: hidden;
        box-shadow: 0 20px 40px -15px rgba(0,0,0,0.05);
    }

    #particle-canvas {
        width: 100%; height: 100%;
    }

    /* Sections Shared */
    section {
      padding: 8rem 0;
    }
    
    .section-header {
        margin-bottom: 4rem;
        text-align: center;
    }
    
    .section-header p {
        color: var(--accent-main);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.85rem;
        margin-bottom: 0.5rem;
    }
    
    .section-header h2 {
        font-size: 3rem;
        color: var(--text-main);
    }

    /* About Section */
    .about {
        background: var(--bg-surface);
        border-top: 1px solid var(--border-color);
        border-bottom: 1px solid var(--border-color);
    }

    .about-content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 5rem;
        align-items: center;
    }

    .about-image {
        position: relative;
        border-radius: 24px;
        background: var(--bg-card);
        aspect-ratio: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid var(--border-color);
    }

    .about-image i {
        font-size: 6rem;
        color: var(--accent-main);
        opacity: 0.5;
    }

    .about-floating-card {
        position: absolute;
        bottom: -20px;
        right: -20px;
        background: var(--bg-surface);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid var(--border-color);
        text-align: center;
    }
    .about-floating-card h3 {
        color: var(--accent-main);
        font-size: 2rem;
    }
    .about-floating-card p {
        color: var(--text-secondary);
        font-size: 0.85rem;
        font-weight: 600;
    }

    .about-text h3 {
        font-size: 2rem;
        margin-bottom: 1.5rem;
        color: var(--text-main);
    }

    .about-text p {
        color: var(--text-secondary);
        margin-bottom: 1.5rem;
        font-size: 1.05rem;
    }

    .about-list {
        list-style: none;
        margin-top: 2rem;
    }
    .about-list li {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
        color: var(--text-main);
        font-weight: 500;
    }
    .about-list li i {
        color: #10b981;
    }

    /* Skills / Capabilities */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
    }

    .skill-category-card {
        background: var(--bg-surface);
        border: 1px solid var(--border-color);
        border-radius: 20px;
        padding: 2.5rem;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    
    .skill-icon-wrap {
        width: 60px; height: 60px;
        background: var(--bg-card);
        border-radius: 12px;
        display: flex; justify-content: center; align-items: center;
        margin-bottom: 1.5rem;
        font-size: 1.5rem;
        color: var(--accent-main);
    }

    .skill-category-card h3 {
        font-size: 1.3rem;
        margin-bottom: 1.5rem;
    }

    .tags-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.75rem;
    }

    .tag {
        padding: 0.4rem 0.8rem;
        background: var(--bg-card);
        color: var(--text-secondary);
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 500;
        border: 1px solid var(--border-color);
        transition: all 0.3s;
    }
    .skill-category-card:hover .tag {
        background: var(--accent-main);
        color: white;
        border-color: var(--accent-main);
    }

    /* Projects */
    .projects {
        background: var(--bg-surface);
        border-top: 1px solid var(--border-color);
    }

    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
    }

    .project-card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 20px;
        overflow: hidden;
        transition: all 0.4s;
    }

    .project-visual {
        height: 220px;
        background: var(--border-color);
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 3rem;
        color: var(--text-tertiary);
    }

    .project-info {
        padding: 2rem;
    }

    .project-info h3 {
        font-size: 1.4rem;
        margin-bottom: 0.8rem;
    }

    .project-info p {
        color: var(--text-secondary);
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }

    .project-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-top: 1px solid var(--border-color);
        padding-top: 1.5rem;
        margin-top: 1rem;
    }

    .project-links a {
        color: var(--text-main);
        text-decoration: none;
        font-size: 1.2rem;
        transition: color 0.3s;
    }
    .project-links a:hover {
        color: var(--accent-main);
    }

    /* Contact Section */
    .contact-content {
        display: grid;
        grid-template-columns: 1fr 1.5fr;
        gap: 4rem;
        background: var(--bg-surface);
        border: 1px solid var(--border-color);
        border-radius: 24px;
        padding: 4rem;
    }

    .contact-info h3 {
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    .contact-info p {
        color: var(--text-secondary);
        margin-bottom: 2rem;
    }

    .social-links {
        display: flex;
        gap: 1rem; margin-top: 2rem;
    }
    .social-btn {
        width: 45px; height: 45px;
        border-radius: 50%;
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        display: flex; justify-content: center; align-items: center;
        color: var(--text-main);
        text-decoration: none;
        transition: all 0.3s;
    }
    .social-btn:hover {
        background: var(--accent-main);
        color: white;
        border-color: var(--accent-main);
        transform: translateY(-3px);
    }

    .form-group {
        margin-bottom: 1.5rem;
    }
    .form-group label {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 500;
        color: var(--text-main);
        font-size: 0.9rem;
    }
    .form-control {
        width: 100%;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        background: var(--bg-base);
        color: var(--text-main);
        font-family: inherit;
        transition: border-color 0.3s;
    }
    .form-control:focus {
        outline: none;
        border-color: var(--accent-main);
    }
    textarea.form-control {
        min-height: 150px;
        resize: vertical;
    }

    footer {
        padding: 2rem 0;
        text-align: center;
        border-top: 1px solid var(--border-color);
        color: var(--text-tertiary);
        font-size: 0.9rem;
    }

    /* Core Cool Effects */
    .typing-text {
      border-right: 3px solid var(--accent-main);
      white-space: nowrap;
      overflow: hidden;
      animation: typing 4s steps(40, end), blink-caret 0.75s step-end infinite;
      display: inline-block;
      max-width: fit-content;
    }

    @keyframes typing {
      from { width: 0; }
      to { width: 100%; }
    }

    @keyframes blink-caret {
      from, to { border-right-color: var(--accent-main); }
      50% { border-right-color: transparent; }
    }
    
    .fun-emoji {
      display: inline-block;
      transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      cursor: default;
    }
    .fun-emoji:hover {
      transform: rotate(20deg) scale(1.4);
    }
    
    .confetti {
      position: fixed;
      width: 10px;
      height: 10px;
      pointer-events: none;
      z-index: 9999;
    }
    @keyframes confetti-fall {
      0% { transform: translateY(0) rotateZ(0deg); opacity: 1; }
      100% { transform: translateY(100vh) rotateZ(360deg); opacity: 0; }
    }
    
    .easter-egg {
      position: fixed;
      pointer-events: none;
      font-size: 2.5rem;
      z-index: 9999;
      animation: float-away 2s ease-out forwards;
    }
    @keyframes float-away {
      0% { opacity: 1; transform: translateY(0) translateX(0) scale(1); }
      100% { opacity: 0; transform: translateY(-100px) translateX(50px) scale(1.5); }
    }
    
    .pulse {
      animation: pulse 1s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.05); opacity: 0.8; }
    }

    .wobble {
      animation: wobble 0.5s ease-in-out;
    }
    @keyframes wobble {
      0%, 100% { transform: translateX(0); }
      25% { transform: translateX(-8px) rotate(-3deg); }
      75% { transform: translateX(8px) rotate(3deg); }
    }
    
    .tilt-card {
        transform-style: preserve-3d;
        transform: perspective(1000px);
    }
    .tilt-card > * {
        transform: translateZ(30px);
    }

    .fade-in-section {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    }
    .fade-in-section.is-visible {
        opacity: 1;
        transform: none;
    }
    @keyframes ping {
        75%, 100% { transform: scale(2); opacity: 0; }
    }

    /* Responsive */
    @media (max-width: 900px) {
      .hero, .about-content, .contact-content {
        grid-template-columns: 1fr;
        gap: 3rem;
      }
      .nav-links { display: none; }
      .hero-title { font-size: 3.2rem; }
      .hero-content {text-align: center;}
      .typing-text { margin: 0 auto 2.5rem; }
      .hero-badge { margin: 0 auto 2rem; }
      .hero-actions { justify-content: center; }
      .hero-visual { height: 300px; }
      section { padding: 5rem 0; }
      .contact-content { padding: 2rem; }
    }
  </style>
</head>
<body class="light">

  <nav id="navbar">
    <div class="container">
      <div class="logo" id="main-logo" style="cursor: pointer; user-select: none;">
          <i class="fas fa-code logo-icon"></i>
          Anvesha
      </div>
      
      <div class="nav-menus">
          <ul class="nav-links">
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Capabilities</a></li>
            <li><a href="#projects">Work</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
          <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Dark Mode">
              <i class="fas fa-moon"></i>
          </button>
      </div>
    </div>
  </nav>

  <main>
      <section id="home" class="hero">
        <div class="hero-content">
          <div class="hero-badge">
              <div class="ping"></div>
              Available for opportunities
          </div>
          <h1 class="hero-title">
              Crafting Digital<br>
              <span>Experiences.</span>
          </h1>
          <p class="hero-desc typing-text" style="margin-bottom: 2.5rem;">Web Developer • AI Engineer • Builder</p>
          <p class="hero-desc">I am a Computer Science engineer specializing in intelligent web experiences and AI-powered solutions. From timetable automation to safety platforms, I engineer products that matter. <span class="fun-emoji">✨</span></p>
          
          <div class="hero-actions">
            <a href="#projects" class="btn btn-primary">Explore Work</a>
            <a href="#contact" class="btn btn-secondary">Contact Me</a>
          </div>
        </div>
        <div class="hero-visual">
            <canvas id="particle-canvas"></canvas>
        </div>
      </section>

      <section id="about" class="about">
        <div class="container">
            <div class="about-content fade-in-section">
                <div class="about-image">
                    <i class="fas fa-terminal"></i>
                    <div class="about-floating-card" style="cursor: pointer;" id="stat-card-1">
                        <h3>9.55</h3>
                        <p>CGPA</p>
                    </div>
                </div>
                <div class="about-text">
                    <div class="section-header" style="text-align: left; margin-bottom: 2rem;">
                        <p>Discover</p>
                        <h2>About Me</h2>
                    </div>
                    <p>I'm a second-year Computer Science Engineering student passionate about turning ideas into reality. My journey sits at the intersection of modern web development and artificial intelligence.</p>
                    <p>I believe in learning by building, prioritizing clean code, and iterating until the product truly shines.</p>
                    
                    <ul class="about-list">
                        <li><i class="fas fa-check-circle"></i> Building intelligent scheduling algorithms.</li>
                        <li><i class="fas fa-check-circle"></i> Developing accessible AI tools for visual impairment.</li>
                        <li><i class="fas fa-check-circle"></i> Creating functional, user-centric web applications.</li>
                    </ul>
                </div>
            </div>
        </div>
      </section>

      <section id="skills" class="skills">
        <div class="container">
            <div class="section-header fade-in-section">
                <p>Expertise</p>
                <h2>Technical Capabilities</h2>
            </div>
            <div class="skills-grid fade-in-section">
                <div class="skill-category-card tilt-card">
                    <div class="skill-icon-wrap"><i class="fas fa-laptop-code"></i></div>
                    <h3>Frontend Engineering</h3>
                    <div class="tags-container">
                        <span class="tag">HTML5</span>
                        <span class="tag">CSS3</span>
                        <span class="tag">JavaScript</span>
                        <span class="tag">React</span>
                        <span class="tag">UI/UX</span>
                    </div>
                </div>
                <div class="skill-category-card tilt-card">
                    <div class="skill-icon-wrap"><i class="fas fa-server"></i></div>
                    <h3>Backend & Systems</h3>
                    <div class="tags-container">
                        <span class="tag">Python</span>
                        <span class="tag">Node.js</span>
                        <span class="tag">Databases</span>
                        <span class="tag">APIs</span>
                        <span class="tag">Git</span>
                    </div>
                </div>
                <div class="skill-category-card tilt-card">
                    <div class="skill-icon-wrap"><i class="fas fa-brain"></i></div>
                    <h3>Artificial Intelligence</h3>
                    <div class="tags-container">
                        <span class="tag">Machine Learning</span>
                        <span class="tag">Computer Vision</span>
                        <span class="tag">NLP</span>
                        <span class="tag">Genetic Algorithms</span>
                    </div>
                </div>
            </div>
        </div>
      </section>

      <section id="projects" class="projects">
        <div class="container">
            <div class="section-header fade-in-section">
                <p>Portfolio</p>
                <h2>Selected Work</h2>
            </div>
            <div class="projects-grid fade-in-section">
                <div class="project-card tilt-card">
                    <div class="project-visual"><i class="fas fa-calendar-alt"></i></div>
                    <div class="project-info">
                        <h3>Samaya</h3>
                        <p>Intelligent timetable generation system using genetic algorithms to automate complex scheduling with constraints.</p>
                        <div class="tags-container" style="margin-bottom: 1.5rem;">
                            <span class="tag">AI</span><span class="tag">Automation</span>
                        </div>
                        <div class="project-footer">
                            <a href="#" class="btn btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.85rem;">View Details</a>
                            <div class="project-links"><a href="#"><i class="fab fa-github"></i></a></div>
                        </div>
                    </div>
                </div>

                <div class="project-card tilt-card">
                    <div class="project-visual"><i class="fas fa-shield-alt"></i></div>
                    <div class="project-info">
                        <h3>SafeLink</h3>
                        <p>Women's safety platform with real-time location sharing, SOS alerts, and a trusted contact network module.</p>
                        <div class="tags-container" style="margin-bottom: 1.5rem;">
                            <span class="tag">Safety</span><span class="tag">Real-time</span>
                        </div>
                        <div class="project-footer">
                             <a href="#" class="btn btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.85rem;">View Details</a>
                            <div class="project-links"><a href="#"><i class="fas fa-lock"></i></a></div>
                        </div>
                    </div>
                </div>

                <div class="project-card tilt-card">
                    <div class="project-visual"><i class="fas fa-eye"></i></div>
                    <div class="project-info">
                        <h3>VisionVani</h3>
                        <p>AI-powered visual assistance tool for visually impaired users. Utilizes Computer Vision and NLP for surroundings description.</p>
                        <div class="tags-container" style="margin-bottom: 1.5rem;">
                            <span class="tag">AI</span><span class="tag">Computer Vision</span>
                        </div>
                        <div class="project-footer">
                             <a href="#" class="btn btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.85rem;">View Details</a>
                            <div class="project-links"><a href="#"><i class="fab fa-github"></i></a></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </section>

      <section id="contact">
        <div class="container">
            <div class="contact-content fade-in-section">
                <div class="contact-info">
                    <h3>Let's Connect</h3>
                    <p>I'm currently looking for new opportunities. Whether you have a question or just want to say hi, I'll try my best to get back to you!</p>
                    <div class="social-links">
                        <a href="#" class="social-btn"><i class="fab fa-github"></i></a>
                        <a href="#" class="social-btn"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#" class="social-btn"><i class="fas fa-envelope"></i></a>
                    </div>
                </div>
                <div class="contact-form">
                    <div class="form-group">
                        <label>Name</label>
                        <input type="text" class="form-control" placeholder="John Doe">
                    </div>
                    <div class="form-group">
                        <label>Email</label>
                        <input type="email" class="form-control" placeholder="john@example.com">
                    </div>
                    <div class="form-group">
                        <label>Message</label>
                        <textarea class="form-control" placeholder="Hello Anvesha..."></textarea>
                    </div>
                    <button class="btn btn-primary" style="width: 100%;">Send Message</button>
                </div>
            </div>
        </div>
      </section>
  </main>

  <footer>
      <div class="container">
          <p>&copy; 2026 Anvesha Khandelwal. Built with professional aesthetics and a touch of coolness.</p>
      </div>
  </footer>

  <script>
    // 1. Theme Logic
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    const bodyElement = document.body;
    
    // Check local storage or system preference
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
        htmlElement.classList.add('dark');
        themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    } else {
        htmlElement.classList.remove('dark');
        themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
    }

    themeToggle.addEventListener('click', () => {
        htmlElement.classList.toggle('dark');
        
        if (htmlElement.classList.contains('dark')) {
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
            localStorage.setItem('theme', 'dark');
            themeToggle.classList.add('wobble');
        } else {
            themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
            localStorage.setItem('theme', 'light');
            themeToggle.classList.add('wobble');
        }
        setTimeout(() => themeToggle.classList.remove('wobble'), 500);
    });

    // 2. Scroll Animation Observer
    const observerOptions = { root: null, rootMargin: '0px', threshold: 0.1 };
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, observerOptions);

    document.querySelectorAll('.fade-in-section').forEach(section => { observer.observe(section); });

    // 3. Smooth scrolling for nav
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
        });
    });

    // 4. Abstract Particle Canvas Functionality adapting to CSS variables
    function initCanvasAnimation() {
      const canvas = document.getElementById('particle-canvas');
      if (!canvas) return;
      
      const ctx = canvas.getContext('2d');
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;

      let particles = [];
      const particleCount = 45;
      const connectionDistance = 120;

      class Particle {
          constructor() {
              this.x = Math.random() * canvas.width;
              this.y = Math.random() * canvas.height;
              this.vx = (Math.random() - 0.5) * 1.5;
              this.vy = (Math.random() - 0.5) * 1.5;
              this.radius = Math.random() * 2 + 1;
          }
          update() {
              this.x += this.vx; this.y += this.vy;
              if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
              if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
          }
      }

      for (let i = 0; i < particleCount; i++) { particles.push(new Particle()); }

      function animate() {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          const currentStyles = getComputedStyle(document.documentElement);
          const particleColor = currentStyles.getPropertyValue('--particle-color').trim() || 'rgba(37, 99, 235, 0.4)';
          let baseRgb = htmlElement.classList.contains('dark') ? '96, 165, 250' : '37, 99, 235';

          for (let i = 0; i < particles.length; i++) {
              particles[i].update();
              ctx.beginPath();
              ctx.arc(particles[i].x, particles[i].y, particles[i].radius, 0, Math.PI * 2);
              ctx.fillStyle = particleColor;
              ctx.fill();

              for (let j = i + 1; j < particles.length; j++) {
                  const dx = particles[i].x - particles[j].x;
                  const dy = particles[i].y - particles[j].y;
                  const distance = Math.sqrt(dx * dx + dy * dy);

                  if (distance < connectionDistance) {
                      ctx.beginPath();
                      ctx.strokeStyle = `rgba(${baseRgb}, ${0.4 * (1 - distance / connectionDistance)})`;
                      ctx.lineWidth = 1;
                      ctx.moveTo(particles[i].x, particles[i].y);
                      ctx.lineTo(particles[j].x, particles[j].y);
                      ctx.stroke();
                  }
              }
          }
          requestAnimationFrame(animate);
      }
      animate();
      window.addEventListener('resize', () => {
          canvas.width = canvas.parentElement.clientWidth;
          canvas.height = canvas.parentElement.clientHeight;
      });
    }

    // 5. Setup Cool Effects (Professional iteration)
    function setupCoolEffects() {
        // Confetti
        function createConfetti(x, y) {
            const colors = ['#2563eb', '#3b82f6', '#60a5fa', '#f8fafc', '#0f172a'];
            for (let i = 0; i < 40; i++) {
                const confetti = document.createElement('div');
                confetti.className = 'confetti';
                confetti.style.left = x + 'px';
                confetti.style.top = y + 'px';
                confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                confetti.style.borderRadius = Math.random() > 0.5 ? '50%' : '0px';
                confetti.style.animation = `confetti-fall ${1.5 + Math.random() * 1.5}s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards`;
                confetti.style.transform = `rotateZ(${Math.random() * 360}deg)`;
                document.body.appendChild(confetti);
                setTimeout(() => confetti.remove(), 3000);
            }
        }

        // Stat Card Confetti
        const statCard = document.getElementById('stat-card-1');
        if(statCard) {
            statCard.addEventListener('click', (e) => {
                statCard.classList.add('pulse');
                createConfetti(e.clientX, e.clientY);
                setTimeout(() => statCard.classList.remove('pulse'), 1000);
            });
        }

        // Easter Egg Logo
        const mainLogo = document.getElementById('main-logo');
        let clickCount = 0;
        if(mainLogo) {
            mainLogo.addEventListener('click', (e) => {
                clickCount++;
                const emojis = ['👨‍💻', '🎉', '✨', '🚀', '💡', '🎯', '🏆'];
                const easterEgg = document.createElement('div');
                easterEgg.className = 'easter-egg';
                easterEgg.textContent = emojis[Math.floor(Math.random() * emojis.length)];
                easterEgg.style.left = (e.clientX - 20) + 'px';
                easterEgg.style.top = (e.clientY) + 'px';
                document.body.appendChild(easterEgg);
                setTimeout(() => easterEgg.remove(), 2000);

                mainLogo.style.transform = 'scale(0.8) translateY(10px)';
                setTimeout(() => {
                    mainLogo.style.transform = 'scale(1.1) translateY(-10px)';
                    setTimeout(() => { mainLogo.style.transform = 'scale(1) translateY(0)'; }, 150);
                }, 150);

                if (clickCount % 5 === 0) createConfetti(window.innerWidth/2, window.innerHeight/2);
            });
        }

        // Micro-Interactions
        document.querySelectorAll('.btn, .social-btn').forEach(btn => {
            btn.addEventListener('mousedown', function() {
                this.classList.add('wobble');
                setTimeout(() => this.classList.remove('wobble'), 500);
            });
        });
    }

    // Lightweight VanillaTilt
    class SimpleTilt {
        constructor(element, settings = {}) {
            this.element = element;
            this.settings = Object.assign({ max: 10, perspective: 1000, scale: 1.02, speed: 400 }, settings);
            this.element.classList.add('tilt-card');
            this.bindEvents();
        }
        bindEvents() {
            this.element.addEventListener("mouseenter", this.onMouseEnter.bind(this));
            this.element.addEventListener("mousemove", this.onMouseMove.bind(this));
            this.element.addEventListener("mouseleave", this.onMouseLeave.bind(this));
        }
        onMouseEnter() {
            let rect = this.element.getBoundingClientRect();
            this.width = this.element.offsetWidth; this.height = this.element.offsetHeight;
            this.left = rect.left; this.top = rect.top;
            this.element.style.willChange = "transform";
            this.setTransition();
        }
        onMouseMove(e) {
            let x = Math.min(Math.max((e.clientX - this.left) / this.width, 0), 1);
            let y = Math.min(Math.max((e.clientY - this.top) / this.height, 0), 1);
            let tiltX = (this.settings.max / 2 - x * this.settings.max).toFixed(2);
            let tiltY = (y * this.settings.max - this.settings.max / 2).toFixed(2);
            this.element.style.transform = `perspective(${this.settings.perspective}px) rotateX(${tiltY}deg) rotateY(${tiltX}deg) scale3d(${this.settings.scale}, ${this.settings.scale}, ${this.settings.scale})`;
        }
        onMouseLeave() {
            this.setTransition();
            this.element.style.transform = `perspective(${this.settings.perspective}px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
        }
        setTransition() {
            this.element.style.transition = `${this.settings.speed}ms cubic-bezier(.03,.98,.52,.99)`;
            setTimeout(() => this.element.style.transition = "", this.settings.speed);
        }
    }

    window.addEventListener('load', () => {
        initCanvasAnimation();
        setupCoolEffects();
        if(window.innerWidth > 768) {
            document.querySelectorAll('.project-card, .skill-category-card').forEach(card => new SimpleTilt(card, { max: 7, scale: 1.03 }));
        }
    });

  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("index.html generated successfully!")
