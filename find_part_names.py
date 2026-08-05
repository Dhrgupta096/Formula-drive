with open("/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/_astro/demoFormula.NlMP6xZ0.js", "r", encoding="utf-8") as f:
    content = f.read()

target = "FRONT_WHEEL_PART_NAMES"
pos = content.find(target)
if pos != -1:
    print("Found FRONT_WHEEL_PART_NAMES!")
    print(content[pos-100:pos+800])
else:
    print("Not found")
