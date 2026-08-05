import urllib.request

url = "https://lab.patrickheintzmann.com/_astro/rapier.DBjBuyhF.js"
dest = "/Users/dhruvgupta/.gemini/antigravity/scratch/demo-formula/_astro/rapier.DBjBuyhF.js"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://lab.patrickheintzmann.com/demo/demoFormula"
}

print(f"Downloading {url} -> {dest}")
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        with open(dest, "wb") as f:
            f.write(response.read())
    print("Success!")
except Exception as e:
    print(f"Failed to download: {e}")
