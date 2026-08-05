with open("/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/_astro/_demo_.BH5Ol2L6.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
matches = [m.start() for m in re.finditer(r'z-index:\s*\d+', css)]
print(f"Occurrences of z-index: {len(matches)}")
for p in matches:
    print(css[max(0, p-40):min(len(css), p+80)])
    print("-" * 50)
