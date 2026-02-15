// Theme management based on local time
(function() {
  // Get current hour (0-23)
  function getLocalHour() {
    try {
      return new Date().getHours();
    } catch (e) {
      return null;
    }
  }

  // Determine if it should be dark theme based on local time
  // Dark: 18:00 - 06:00, Light: 06:00 - 18:00
  // Default to light if cannot determine
  function isDarkByTime() {
    const hour = getLocalHour();
    if (hour === null) return false; // Default to light
    return hour < 6 || hour >= 18;
  }

  // Apply theme
  function applyTheme() {
    const html = document.documentElement;
    const isDark = isDarkByTime();
    
    if (isDark) {
      html.classList.add('dark');
    } else {
      html.classList.remove('dark');
      // html.classList.add('dark');
    }
  }

  // Initialize
  function init() {
    applyTheme();
  }

  // Expose to global
  window.themeManager = {
    apply: applyTheme
  };

  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
