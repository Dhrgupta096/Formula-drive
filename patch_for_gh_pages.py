import os

# 1. Patch index.html
html_path = "/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/index.html"
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Replace absolute root paths with relative dot paths
    html = html.replace('href="/_astro/', 'href="./_astro/')
    html = html.replace('src="/_astro/', 'src="./_astro/')
    html = html.replace('href="/assets/', 'href="./assets/')
    html = html.replace('src="/assets/', 'src="./assets/')
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Patched index.html with relative dot paths.")

# 2. Patch demoFormula.NlMP6xZ0.js
js_path = "/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/_astro/demoFormula.NlMP6xZ0.js"
if os.path.exists(js_path):
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()
        
    # We replaced it with baseURL="/" earlier. Let's change it to baseURL="./"
    js = js.replace('baseURL="/"', 'baseURL="./"')
    # Just in case:
    js = js.replace("baseURL='/'", "baseURL='./'")
    
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("Patched demoFormula.NlMP6xZ0.js baseURL to relative './'.")
