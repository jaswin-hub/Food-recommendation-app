import requests
import re

filepath = r'c:\for 2nd sem related things\New folder (2)\app\backend\src\main\java\com\foodapp\data\RecipeDataStore.java'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all imageUrls
urls = re.findall(r'"(https?://.*?)"', content)

broken_urls = []
for url in urls:
    try:
        # Check if URL ends with jpg, png, etc.
        if not any(url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp']):
             # If it doesn't end with image extension, it might be a page URL
             broken_urls.append(url)
             continue
             
        response = requests.head(url, timeout=5, allow_redirects=True)
        if response.status_code != 200:
            broken_urls.append(url)
        else:
            content_type = response.headers.get('Content-Type', '')
            if 'image' not in content_type:
                broken_urls.append(url)
    except Exception:
        broken_urls.append(url)

print(f"Total URLs found: {len(urls)}")
print(f"Broken/Invalid URLs found: {len(broken_urls)}")
for url in broken_urls:
    print(url)
