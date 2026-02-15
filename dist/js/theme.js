// 主题切换功能
(function() {
  // 获取主题设置
  function getTheme() {
    return localStorage.getItem('theme') || 'auto';
  }

  // 设置主题
  function setTheme(theme) {
    localStorage.setItem('theme', theme);
    applyTheme(theme);
  }

  // 应用主题
  function applyTheme(theme) {
    const html = document.documentElement;
    
    if (theme === 'dark') {
      html.classList.add('dark');
    } else if (theme === 'light') {
      html.classList.remove('dark');
    } else {
      // auto - 跟随系统
      if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        html.classList.add('dark');
      } else {
        html.classList.remove('dark');
      }
    }
  }

  // 切换主题
  function toggleTheme() {
    const currentTheme = getTheme();
    const themes = ['light', 'dark', 'auto'];
    const currentIndex = themes.indexOf(currentTheme);
    const nextTheme = themes[(currentIndex + 1) % themes.length];
    setTheme(nextTheme);
    updateThemeIcon(nextTheme);
  }

  // 更新主题图标
  function updateThemeIcon(theme) {
    const icons = {
      light: '☀️',
      dark: '🌙',
      auto: '⚡'
    };
    const btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.textContent = icons[theme] || icons.auto;
      btn.title = `主题: ${theme}`;
    }
  }

  // 初始化
  function init() {
    const theme = getTheme();
    applyTheme(theme);
    updateThemeIcon(theme);

    // 监听系统主题变化
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
      if (getTheme() === 'auto') {
        applyTheme('auto');
      }
    });

    // 绑定切换按钮
    const toggleBtn = document.getElementById('theme-toggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', toggleTheme);
    }
  }

  // 暴露到全局
  window.themeManager = {
    get: getTheme,
    set: setTheme,
    toggle: toggleTheme
  };

  // DOM 加载完成后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
