# Plan to Fix Blog Page Header (`blog/common-ac-problems-pasadena.html`)

**Goal:** Make the header on the blog page match the standard site header by correcting file paths, removing redundant inline styles, and adding missing JavaScript.

**Analysis Summary:**

*   **Incorrect Paths:** CSS and JS files linked with relative paths (`styles.css`, `header-scroll.js`) instead of parent directory paths (`../styles.css`, `../header-scroll.js`).
*   **Redundant Inline Styles:** A large `<style>` block (lines 9-502) containing CSS likely duplicated from `styles.css` exists in the blog page's `<head>`.
*   **Missing JavaScript:** The inline JavaScript block responsible for mobile navigation and dropdowns (present in `index.html`) is missing from the blog page.

**Plan Steps:**

1.  **Modify `blog/common-ac-problems-pasadena.html`:**
    *   Replace the incorrect CSS link on line 8 (`<link href="styles.css" rel="stylesheet" />`) with the correct path: `<link href="../styles.css" rel="stylesheet" />`.
    *   Remove the inline `<style>` block (lines 9 through 502).
    *   Insert the mobile navigation JavaScript block (retrieved from `index.html` lines 3160-3252) just before the existing `<script src="header-scroll.js"></script>` tag.
    *   Correct the path for the `header-scroll.js` script tag to `<script src="../header-scroll.js"></script>`.
2.  **Implementation:** Use the `write_to_file` tool in "Code" mode to overwrite the file with the corrected content.

**Visualization of Changes:**

```mermaid
graph TD
    subgraph "blog/common-ac-problems-pasadena.html (Current)"
        A1["<head>"] --> A2["<link href='styles.css'> (Line 8)"];
        A1 --> A3["<style>...</style> (Lines 9-502)"];
        A3 --> A4["</head>"];
        A5["<body>"] --> A6["<footer>"];
        A6 --> A7["<script src='header-scroll.js'> (Line 1828)"];
        A7 --> A8["</body>"];
    end

    subgraph "blog/common-ac-problems-pasadena.html (Proposed)"
        B1["<head>"] --> B2["<link href='../styles.css'>"];
        B2 --> B3["</head>"];
        B4["<body>"] --> B5["<footer>"];
        B5 --> B6["<script>...Mobile Nav JS...</script>"];
        B6 --> B7["<script src='../header-scroll.js'>"];
        B7 --> B8["</body>"];
    end

    A2 -- Correct Path --> B2;
    A3 -- Remove --> B2;
    A7 -- Correct Path --> B7;
    A6 -- Insert Before --> B6;

    style A2 fill:#f9f,stroke:#333,stroke-width:2px
    style A3 fill:#f9f,stroke:#333,stroke-width:2px
    style A7 fill:#f9f,stroke:#333,stroke-width:2px
    style B6 fill:#ccf,stroke:#333,stroke-width:2px