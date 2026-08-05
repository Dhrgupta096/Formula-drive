import os
import re

print("Applying custom branding for Dhruv Gupta...")

# 1. Update index.html
html_path = "/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/index.html"
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    # Replace description meta
    desc_regex = r'<meta name="description" content="[^"]*">'
    new_desc = '<meta name="description" content="An interactive 3D WebGL Formula 1 model kit and driving simulation playground, built by Dhruv Gupta using Three.js.">'
    html = re.sub(desc_regex, new_desc, html)
    
    # Replace title
    title_regex = r'<title>[^<]*</title>'
    new_title = '<title>Dhruv\'s Lab - 3D Formula 1 Simulator</title>'
    html = re.sub(title_regex, new_title, html)
    
    # Remove Google Tag Manager scripts
    gtag_regex = r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-VPCB4QL004"></script><script>\s*window\.dataLayer = window\.dataLayer \|\| \[\];\s*function gtag\(\)\{dataLayer\.push\(arguments\);\}[^<]*gtag\(\'config\', \'G-VPCB4QL004\'\);\s*</script>'
    html = re.sub(gtag_regex, '', html)
    
    # Replace loader title
    html = html.replace('<p>[04] Formula</p>', '<p>DHRUV\'S PLAYGROUND</p>')
    
    # Replace Header Logo/Lab tag with DHRUV tag
    old_logo = '<a href="/"> <p id="demoMenu-content-header-lab"> <span>L</span> <span>A</span> <span>B</span> </p> </a>'
    new_logo = '<a href="https://github.com/Dhrgupta096" target="_blank" style="text-decoration: none;"><p id="demoMenu-content-header-lab" style="font-size: 14px; font-weight: 800; border: 1px solid rgba(255,255,255,0.4); padding: 4px 10px; border-radius: 4px; display: inline-block; margin: 0; color: #fff; letter-spacing: 0.15em;">DHRUV</p></a>'
    html = html.replace(old_logo, new_logo)
    
    # Replace Menu Title
    old_menu_title = '[04] Formula </p>'
    new_menu_title = 'FORMULA 1 PLAYGROUND </p><p class="demoMenu-content-copy letterSpacing" style="opacity: 0.6; font-size: 9px; margin-top: 4px;">Created by Dhruv Gupta</p>'
    html = html.replace(old_menu_title, new_menu_title)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(" index.html branded successfully.")

# 2. Update Console Log Credit inside bundle script
js_path = "/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/_astro/_demo_.astro_astro_type_script_index_0_lang.CI7kkfYG.js"
if os.path.exists(js_path):
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()
        
    old_log = 'console.log("%cCreated by www.patrickheintzmann.com","background-color:#000000; color:#ffffff; padding:6px; font-size:10px; border-radius: 2px;")'
    new_log = 'console.log("%cCreated by Dhruv Gupta - https://github.com/Dhrgupta096","background-color:#E10600; color:#ffffff; padding:6px; font-size:10px; border-radius: 2px;")'
    
    if old_log in js:
        js = js.replace(old_log, new_log)
    else:
        # Fallback search if spacing or quotes slightly differ
        js = re.sub(r'console\.log\("%cCreated by[^"]*","background-color:#000000;[^"]*"\)', new_log, js)
        
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print(" JS console log branded successfully.")

print("Branding application complete.")
