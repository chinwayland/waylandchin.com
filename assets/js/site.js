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

// Stretch the main native link across each card; keep secondary controls usable.
document.querySelectorAll('.project-card, .route-card, .document-card, .sidebar-card, .evolution-card, .evidence-grid figure, .evidence-feature').forEach((card) => {
  const links = [...card.querySelectorAll('a[href]')];
  if (!links.length) return;
  const primary = links.find((link) => !link.hasAttribute('download')) || links[0];
  card.classList.add('linked-card');
  primary.classList.add('card-primary-link');
  const heading = card.querySelector('h2, h3');
  if (heading && !primary.hasAttribute('aria-label')) {
    primary.setAttribute('aria-label', `${primary.textContent.trim()} — ${heading.textContent.trim()}`);
  }
  card.querySelectorAll('a, button, input, select, textarea, summary').forEach((control) => {
    if (control !== primary) control.classList.add('card-secondary-control');
  });
});
