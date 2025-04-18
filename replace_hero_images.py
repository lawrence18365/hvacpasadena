import os
import glob

# List of HTML files to process
html_files = [
    'about.html',
    'ac-repair.html',
    'air-quality.html',
    'altadena-hvac.html',
    'commercial-hvac.html',
    'contact.html',
    'emergency-service.html',
    'financing.html',
    'furnace-installation.html',
    'heating.html',
    'hvac-maintenance.html',
    'index.html',
    'north-pasadena-hvac.html',
    'pasadena-hvac.html',
    'san-marino-hvac.html',
    'sierra-madre-hvac.html',
    'south-pasadena-hvac.html',
    'testimonials.html',
    'blog/common-ac-problems-pasadena.html',
    'blog/energy-efficient-hvac-options.html',
    'blog/index.html',
    'blog/preparing-hvac-for-summer.html',
    'blog/when-to-replace-vs-repair.html'
]

# Placeholder URL to find
placeholder_url = "/api/placeholder/1600/800"

# List of replacement image URLs
replacement_urls = [
    "https://images.unsplash.com/photo-1638790584370-d8857cfbf7d9?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1667983453881-4992fe86ab1b?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1502745785315-67f3193a7a10?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1568634699096-82c9765548a0?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1624167473693-bb5ea202957f?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1550998251-1e18917c975c?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjd8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1601993198415-19d86ae28424?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjl8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1545649311-24d0ac00ae82?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzN8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1575118025558-0677ece2e258?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzV8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1722010811002-a772b2066890?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzl8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1587996758305-47176ba7fb4c?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDN8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1647022528152-52ed9338611d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTJ8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1563623700465-1265fad258f4?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDl8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1722131646940-b821a6cc6252?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTN8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D",
    "https://images.unsplash.com/photo-1558919047-80f932b017cf?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTl8fGFpciUyMGNvbmRpdGlvbmluZ3xlbnwwfHwwfHx8Mg%3D%3D"
]

url_index = 0
files_modified = 0

print(f"Starting image replacement process...")

for file_path in html_files:
    if not os.path.exists(file_path):
        print(f"Warning: File not found, skipping: {file_path}")
        continue

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if placeholder_url in content:
            replacement_url = replacement_urls[url_index % len(replacement_urls)]
            new_content = content.replace(placeholder_url, replacement_url)

            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Replaced placeholder in: {file_path} with {replacement_url}")
                url_index += 1
                files_modified += 1
            else:
                 print(f"Placeholder found but no change needed (already replaced?): {file_path}")
        # else:
            # print(f"Placeholder not found in: {file_path}") # Optional: uncomment for more verbose logging

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

print(f"\nImage replacement process finished.")
print(f"Total files modified: {files_modified}")