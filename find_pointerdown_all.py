with open("/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/_astro/demoFormula.NlMP6xZ0.js", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'\.addEventListener\(\s*["\'](pointer|mouse|touch)', content)]
print(f"Occurrences: {len(matches)}")
for p in matches:
    print(content[max(0, p-50):min(len(content), p+250)])
    print("-" * 50)
