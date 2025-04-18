#!/bin/bash

# Navigate to the blog directory
cd /Users/home/Desktop/hvacpasadena/blog

# Process each HTML file in the directory
for file in *.html; do
    echo "Processing $file..."
    
    # Use sed to replace links that don't already have ../ prefix
    # 1. Replace href="index.html" with href="../index.html"
    # 2. Replace href="ac-repair.html" with href="../ac-repair.html"
    # 3. Skip links that already have proper paths (e.g., href="../something" or href="http://")
    
    sed -i.bak '
    s/href="index.html"/href="..\/index.html"/g;
    s/href="about.html"/href="..\/about.html"/g;
    s/href="testimonials.html"/href="..\/testimonials.html"/g;
    s/href="financing.html"/href="..\/financing.html"/g;
    s/href="contact.html"/href="..\/contact.html"/g;
    s/href="ac-repair.html"/href="..\/ac-repair.html"/g;
    s/href="heating.html"/href="..\/heating.html"/g;
    s/href="hvac-maintenance.html"/href="..\/hvac-maintenance.html"/g;
    s/href="commercial-hvac.html"/href="..\/commercial-hvac.html"/g;
    s/href="air-quality.html"/href="..\/air-quality.html"/g;
    s/href="emergency-service.html"/href="..\/emergency-service.html"/g;
    s/href="furnace-installation.html"/href="..\/furnace-installation.html"/g;
    s/href="pasadena-hvac.html"/href="..\/pasadena-hvac.html"/g;
    s/href="north-pasadena-hvac.html"/href="..\/north-pasadena-hvac.html"/g;
    s/href="south-pasadena-hvac.html"/href="..\/south-pasadena-hvac.html"/g;
    s/href="altadena-hvac.html"/href="..\/altadena-hvac.html"/g;
    s/href="san-marino-hvac.html"/href="..\/san-marino-hvac.html"/g;
    s/href="sierra-madre-hvac.html"/href="..\/sierra-madre-hvac.html"/g;
    ' "$file"
    
    # Remove backup files
    rm "$file.bak"
done

echo "All blog HTML files updated successfully!"