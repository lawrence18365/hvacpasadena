const fs = require('fs');
const path = require('path');
// Updated glob import for newer versions
const { glob } = require('glob');

// New header content
const newHeaderContent = `<header>
      <div class="container">
        <div class="header-container">
          <div class="logo">
            <div class="logo-text"> HVAC <span> Pasadena </span>
            </div>
          </div>
          <div class="header-contact">
            <a class="phone-number" href="tel:+16265551234"> (626) 555-1234 </a>
            <div class="phone-text"> Free Estimates • Same-Day Service </div>
          </div>
        </div>
      </div>
      <nav>
        <div class="container nav-container">
          <ul class="nav-links">
            <li>
              <a href="index.html"> Home </a>
            </li>
            <li class="dropdown">
              <a class="dropdown-toggle" href="#"> Services </a>
              <ul class="dropdown-menu">
                <li>
                  <a href="ac-repair.html"> AC Repair </a>
                </li>
                <li>
                  <a href="heating.html"> Heating </a>
                </li>
                <li>
                  <a href="hvac-maintenance.html"> Maintenance </a>
                </li>
                <li>
                  <a href="commercial-hvac.html"> Commercial HVAC </a>
                </li>
                <li>
                  <a href="air-quality.html"> Air Quality </a>
                </li>
                <li>
                  <a href="emergency-service.html"> Emergency Service </a>
                </li>
                <li>
                  <a href="furnace-installation.html"> Furnace Installation </a>
                </li>
              </ul>
            </li>
            <li class="dropdown">
              <a class="dropdown-toggle" href="#"> Locations </a>
              <ul class="dropdown-menu">
                <li>
                  <a href="pasadena-hvac.html"> Pasadena </a>
                </li>
                <li>
                  <a href="north-pasadena-hvac.html"> North Pasadena </a>
                </li>
                <li>
                  <a href="south-pasadena-hvac.html"> South Pasadena </a>
                </li>
                <li>
                  <a href="altadena-hvac.html"> Altadena </a>
                </li>
                <li>
                  <a href="san-marino-hvac.html"> San Marino </a>
                </li>
                <li>
                  <a href="sierra-madre-hvac.html"> Sierra Madre </a>
                </li>
              </ul>
            </li>
            <li class="dropdown">
              <a class="dropdown-toggle" href="#"> Blog </a>
              <ul class="dropdown-menu">
                <li>
                  <a href="blog/index.html"> All Posts </a>
                </li>
                <li>
                  <a href="blog/common-ac-problems-pasadena.html"> Common AC Problems </a>
                </li>
                <li>
                  <a href="blog/energy-efficient-hvac-options.html"> Energy Efficient Options </a>
                </li>
                <li>
                  <a href="blog/preparing-hvac-for-summer.html"> Preparing for Summer </a>
                </li>
                <li>
                  <a href="blog/when-to-replace-vs-repair.html"> Replace vs Repair </a>
                </li>
              </ul>
            </li>
            <li>
              <a href="about.html"> About Us </a>
            </li>
            <li>
              <a href="testimonials.html"> Reviews </a>
            </li>
            <li>
              <a href="financing.html"> Financing </a>
            </li>
            <li>
              <a href="contact.html"> Contact </a>
            </li>
          </ul>
          <div class="nav-cta">
            <a href="contact.html"> Free Estimate </a>
          </div>
          <button aria-label="Toggle mobile menu" class="mobile-toggle">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </nav>
    </header>
    <div class="mobile-overlay"></div>`;

// Adjust these paths as needed
const blogDirectory = '/Users/home/Desktop/hvacpasadena/blog';

// Function to fix relative paths in the blog directory
function fixRelativePaths(htmlContent, currentFilePath) {
  // Get the depth of the current file relative to the blog directory
  const relativePath = path.relative(blogDirectory, path.dirname(currentFilePath));
  const depth = relativePath.split(path.sep).length;
  
  // If we're at the blog root (depth = 0) or in a direct subdirectory (depth = 1), no need to adjust paths
  if (depth <= 1) {
    return htmlContent;
  }
  
  // For files in deeper subdirectories, we need to add ../ for each level
  let prefix = '';
  for (let i = 1; i < depth; i++) {
    prefix += '../';
  }
  
  // Replace all href attributes that don't start with http, https, or #
  let fixedContent = htmlContent.replace(/href="(?!(http|https|#|mailto:|tel:))([^"]*)"/g, function(match, p1, p2) {
    return `href="${prefix}${p2}"`;
  });
  
  return fixedContent;
}

// Function to process a single HTML file
function processHtmlFile(filePath) {
  try {
    console.log(`Processing: ${filePath}`);
    
    // Read the file content
    let fileContent = fs.readFileSync(filePath, 'utf8');
    
    // Check if the file already has our new header (to avoid duplicate replacements)
    if (fileContent.includes(newHeaderContent.trim())) {
      console.log(`  Already updated: ${filePath}`);
      return;
    }
    
    // Replace the header
    // We'll use a regular expression to match the header and mobile overlay
    const headerRegex = /<header>[\s\S]*?<\/header>\s*<div class="mobile-overlay"><\/div>/;
    
    if (headerRegex.test(fileContent)) {
      // Adjust paths for the new header content based on file location
      let adjustedHeaderContent = fixRelativePaths(newHeaderContent, filePath);
      
      // Replace the old header with the new one
      fileContent = fileContent.replace(headerRegex, adjustedHeaderContent);
      
      // Write the modified content back to the file
      fs.writeFileSync(filePath, fileContent, 'utf8');
      console.log(`  Updated: ${filePath}`);
    } else {
      console.warn(`  No header found to replace in: ${filePath}`);
    }
  } catch (error) {
    console.error(`Error processing ${filePath}:`, error);
  }
}

// Function to recursively find all HTML files
async function findAndProcessHtmlFiles() {
  try {
    // Use glob with async/await syntax for newer versions
    const files = await glob(`${blogDirectory}/**/*.html`);
    
    console.log(`Found ${files.length} HTML files to process.`);
    
    let successCount = 0;
    
    // Process each HTML file
    files.forEach(file => {
      try {
        processHtmlFile(file);
        successCount++;
      } catch (error) {
        console.error(`Failed to process ${file}:`, error);
      }
    });
    
    console.log(`Completed: Successfully processed ${successCount} out of ${files.length} files.`);
  } catch (err) {
    console.error('Error finding HTML files:', err);
  }
}

// Create a backup of the blog directory before making changes
function createBackup() {
  const backupDir = `${path.dirname(blogDirectory)}/blog_backup_${Date.now()}`;
  
  try {
    // Create recursive directory copy function since fs.cp is not available in older Node versions
    function copyDirSync(src, dest) {
      // Create destination directory
      fs.mkdirSync(dest, { recursive: true });
      
      // Get all files and folders in the source directory
      const entries = fs.readdirSync(src, { withFileTypes: true });
      
      for (let entry of entries) {
        const srcPath = path.join(src, entry.name);
        const destPath = path.join(dest, entry.name);
        
        if (entry.isDirectory()) {
          // Recursively copy subdirectories
          copyDirSync(srcPath, destPath);
        } else {
          // Copy files
          fs.copyFileSync(srcPath, destPath);
        }
      }
    }
    
    // Create backup
    copyDirSync(blogDirectory, backupDir);
    console.log(`Backup created at: ${backupDir}`);
    return true;
  } catch (error) {
    console.error('Failed to create backup:', error);
    return false;
  }
}

// Main execution as an async IIFE (Immediately Invoked Function Expression)
(async function() {
  console.log('Starting header replacement process...');

  // Create backup first
  if (createBackup()) {
    console.log('Backup created successfully. Proceeding with header replacement...');
    await findAndProcessHtmlFiles();
  } else {
    console.error('Backup failed. Aborting header replacement for safety.');
  }
})();