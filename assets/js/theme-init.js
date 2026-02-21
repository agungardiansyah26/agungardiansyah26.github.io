(function() {
  try {
    var localTheme = localStorage.getItem('theme');
    var supportDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (localTheme === 'light' || (!localTheme && !supportDarkMode)) {
      document.documentElement.classList.add('light-mode');
    }
  } catch (e) {}
})();
