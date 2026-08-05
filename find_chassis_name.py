with open("/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/_astro/demoFormula.NlMP6xZ0.js", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'chassis', content, re.IGNORECASE)]
print(f"Occurrences of 'chassis': {len(matches)}")
for p in matches:
    print(content[max(0, p-50):min(len(content), p+150)])
    print("-" * 50)
