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
