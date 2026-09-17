const menuButton = document.querySelector('.menu-button');
const siteNav = document.querySelector('#site-nav');

if (menuButton && siteNav) {
  document.documentElement.classList.add('menu-ready');
  const setMenuOpen = (open) => {
    siteNav.classList.toggle('open', open);
    menuButton.setAttribute('aria-expanded', String(open));
  };
  menuButton.addEventListener('click', () => {
    setMenuOpen(menuButton.getAttribute('aria-expanded') !== 'true');
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
      setMenuOpen(false);
      menuButton.focus();
    }
  });
  siteNav.addEventListener('click', (event) => {
    if (event.target.closest('a')) setMenuOpen(false);
  });
}

const path = window.location.pathname;
document.querySelectorAll('.site-nav a').forEach((link) => {
  const href = link.getAttribute('href');
  if (href !== '/' && path.startsWith(href)) link.setAttribute('aria-current', 'page');
});

document.querySelectorAll('[data-year]').forEach((node) => {
  node.textContent = new Date().getFullYear();
});
