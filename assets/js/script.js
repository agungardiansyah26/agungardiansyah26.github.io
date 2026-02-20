document.getElementById("year").textContent = new Date().getFullYear();

// Scroll Reveal Animation
const revealElements = document.querySelectorAll(".reveal");

const revealObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px",
  }
);

revealElements.forEach((el) => revealObserver.observe(el));

// Active Navigation Link
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-link");

const navObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute("id");
        navLinks.forEach((link) => {
          link.classList.remove("active");
          if (link.getAttribute("href") === `#${id}`) {
            link.classList.add("active");
          }
        });
      }
    });
  },
  {
    threshold: 0.3, // Trigger when 30% of the section is visible
  }
);

sections.forEach((section) => navObserver.observe(section));

// Theme Toggle
const themeToggle = document.getElementById("theme-toggle");
const body = document.body;
const sunIcon = document.getElementById("sun-icon");
const moonIcon = document.getElementById("moon-icon");

// Check for saved theme preference or system preference
const savedTheme = localStorage.getItem("theme");
const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

if (savedTheme === "light" || (!savedTheme && !systemPrefersDark)) {
  body.classList.add("light-mode");
  sunIcon.style.display = "none";
  moonIcon.style.display = "block";
}

themeToggle.addEventListener("click", () => {
  body.classList.toggle("light-mode");
  const isLight = body.classList.contains("light-mode");
  
  // Update icons
  sunIcon.style.display = isLight ? "none" : "block";
  moonIcon.style.display = isLight ? "block" : "none";

  // Save preference
  localStorage.setItem("theme", isLight ? "light" : "dark");
});

// Language Toggle
const langIdBtn = document.getElementById("lang-id");
const langEnBtn = document.getElementById("lang-en");

function getNestedTranslation(obj, path) {
  return path.split('.').reduce((prev, curr) => {
    return prev ? prev[curr] : null;
  }, obj);
}

function updateContent(lang) {
  // Update text content
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const key = element.getAttribute("data-i18n");
    const translation = getNestedTranslation(translations[lang], key);
    if (translation) {
      element.innerHTML = translation;
    }
  });

  // Update placeholders
  document.querySelectorAll("[data-i18n-placeholder]").forEach((element) => {
    const key = element.getAttribute("data-i18n-placeholder");
    const translation = getNestedTranslation(translations[lang], key);
    if (translation) {
      element.placeholder = translation;
    }
  });

  // Update toggle state
  if (lang === "id") {
    langIdBtn.classList.add("active-lang");
    langIdBtn.setAttribute("aria-pressed", "true");
    langEnBtn.classList.remove("active-lang");
    langEnBtn.setAttribute("aria-pressed", "false");
  } else {
    langEnBtn.classList.add("active-lang");
    langEnBtn.setAttribute("aria-pressed", "true");
    langIdBtn.classList.remove("active-lang");
    langIdBtn.setAttribute("aria-pressed", "false");
  }

  // Save preference
  localStorage.setItem("lang", lang);
  document.documentElement.lang = lang;
}

// Initial Load
const savedLang = localStorage.getItem("lang") || "id";
updateContent(savedLang);

// Event Listeners
langIdBtn.addEventListener("click", () => updateContent("id"));
langEnBtn.addEventListener("click", () => updateContent("en"));

// Async Contact Form Submission
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = contactForm.querySelector('button[type="submit"]');
    const btnTextSpan = btn.querySelector('[data-i18n="contact.form.btn_send"]');
    const statusDiv = document.getElementById('form-status');

    // Get current language
    const currentLang = localStorage.getItem("lang") || "id";

    // Helper to get translation text
    const t = (key) => getNestedTranslation(translations[currentLang], key);

    // Loading State
    btn.disabled = true;
    if (btnTextSpan) btnTextSpan.textContent = t('contact.form.btn_sending');
    statusDiv.textContent = '';
    statusDiv.style.color = '';

    try {
      const formData = new FormData(contactForm);
      const response = await fetch(contactForm.action, {
        method: 'POST',
        body: formData,
        headers: { 'Accept': 'application/json' }
      });

      if (response.ok) {
        // Success
        contactForm.reset();
        statusDiv.textContent = t('contact.form.success_msg');
        statusDiv.style.color = 'var(--accent)';
      } else {
        throw new Error('Form submission failed');
      }
    } catch (error) {
      // Error
      statusDiv.textContent = t('contact.form.error_msg');
      statusDiv.style.color = '#ef4444'; // Red color for error
    } finally {
      // Reset button
      btn.disabled = false;
      if (btnTextSpan) btnTextSpan.textContent = t('contact.form.btn_send');
    }
  });
}
