// Header scroll behavior
document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('header');
    if (!header) return;
    
    // Add necessary CSS for transitions
    const style = document.createElement('style');
    style.textContent = `
      header {
        position: sticky;
        top: 0;
        transition: transform 0.3s ease;
        z-index: 1000;
      }
      
      header.header-hidden {
        transform: translateY(-100%);
      }
    `;
    document.head.appendChild(style);
    
    let lastScrollTop = 0;
    let scrollThreshold = 50; // Amount of scroll before triggering header show/hide
    
    window.addEventListener('scroll', function() {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      
      // Only apply the effect after scrolling down past the header height
      if (scrollTop > header.offsetHeight) {
        // Scrolling down
        if (scrollTop > lastScrollTop + scrollThreshold) {
          header.classList.add('header-hidden');
          lastScrollTop = scrollTop;
        } 
        // Scrolling up
        else if (scrollTop < lastScrollTop - scrollThreshold) {
          header.classList.remove('header-hidden');
          lastScrollTop = scrollTop;
        }
      } else {
        // At the top of the page
        header.classList.remove('header-hidden');
      }
    }, { passive: true });
  });