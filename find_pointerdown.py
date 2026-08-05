with open("/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/_astro/demoFormula.NlMP6xZ0.js", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'pointerdown', content, re.IGNORECASE)]
print(f"Occurrences of 'pointerdown': {len(matches)}")
for p in matches:
    print(content[max(0, p-100):min(len(content), p+900)])
    print("-" * 50)
