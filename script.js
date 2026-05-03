// Theme Toggle
function toggleTheme() {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', newTheme);
    
    // Save preference
    localStorage.setItem('theme', newTheme);
    
    // Update button icon
    const themeToggle = document.querySelector('.theme-toggle');
    themeToggle.textContent = newTheme === 'dark' ? '☀️' : '🌙';
}

// Load saved theme preference
window.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    const themeToggle = document.querySelector('.theme-toggle');
    themeToggle.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
});

// Mobile Menu Toggle - FIXED
function toggleMobileMenu() {
    const navLinks = document.querySelector('.nav-links');
    const hamburger = document.querySelector('.mobile-menu');
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('open');
}

// Close menu when a nav link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        document.querySelector('.nav-links').classList.remove('active');
        document.querySelector('.mobile-menu').classList.remove('open');
    });
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
    const navLinks = document.querySelector('.nav-links');
    const hamburger = document.querySelector('.mobile-menu');
    if (!navLinks.contains(e.target) && !hamburger.contains(e.target)) {
        navLinks.classList.remove('active');
        hamburger.classList.remove('open');
    }
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Form submission handler
function handleSubmit(event) {
    event.preventDefault();
    
    // Get form data
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    
    // Here you would typically send the data to a server
    console.log('Form submitted:', data);
    
    // Show success message
    alert('Thank you for your message! I will get back to you soon.');
    
    // Reset form
    event.target.reset();
}

// Add scroll animation to elements
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all sections
document.querySelectorAll('section').forEach(section => {
    observer.observe(section);
});

// Navbar style update on scroll
function updateNavbarState() {
    const nav = document.querySelector('nav');
    if (!nav) {
        return;
    }

    nav.classList.toggle('scrolled', window.scrollY > 50);
}

window.addEventListener('scroll', updateNavbarState);

// Typing animation for rotating hero subtitle lines
const heroSubtitleLines = [
    'Python & Web Developer',
    'B.Tech CSE Student @ AKTU',
    'Java & DSA Enthusiast',
    'Open to Internships 🚀'
];

function initHeroSubtitleTyping() {
    const subtitle = document.querySelector('.subtitle');
    if (!subtitle || heroSubtitleLines.length === 0) {
        return;
    }

    let lineIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    const typingSpeed = 70;
    const deletingSpeed = 40;
    const holdAfterTyping = 1400;
    const holdAfterDeleting = 300;

    function tick() {
        const currentLine = heroSubtitleLines[lineIndex];
        subtitle.textContent = currentLine.slice(0, charIndex);

        if (!isDeleting && charIndex < currentLine.length) {
            charIndex++;
            setTimeout(tick, typingSpeed);
            return;
        }

        if (isDeleting && charIndex > 0) {
            charIndex--;
            setTimeout(tick, deletingSpeed);
            return;
        }

        if (!isDeleting) {
            isDeleting = true;
            setTimeout(tick, holdAfterTyping);
            return;
        }

        isDeleting = false;
        lineIndex = (lineIndex + 1) % heroSubtitleLines.length;
        setTimeout(tick, holdAfterDeleting);
    }

    tick();
}

function initInteractiveSurfaceGlow() {
    const surfaces = document.querySelectorAll('nav, section');
    if (surfaces.length === 0) {
        return;
    }

    const supportsPointerTracking = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

    surfaces.forEach((surface) => {
        surface.style.setProperty('--mouse-x', '50%');
        surface.style.setProperty('--mouse-y', '50%');
    });

    if (!supportsPointerTracking) {
        return;
    }

    surfaces.forEach((surface) => {
        surface.addEventListener('mousemove', (event) => {
            const rect = surface.getBoundingClientRect();
            const x = ((event.clientX - rect.left) / rect.width) * 100;
            const y = ((event.clientY - rect.top) / rect.height) * 100;

            surface.style.setProperty('--mouse-x', `${x}%`);
            surface.style.setProperty('--mouse-y', `${y}%`);
        });

        surface.addEventListener('mouseleave', () => {
            surface.style.setProperty('--mouse-x', '50%');
            surface.style.setProperty('--mouse-y', '50%');
        });
    });
}

// Start typing animation when page loads
window.addEventListener('load', () => {
    updateNavbarState();
    setTimeout(initHeroSubtitleTyping, 700);
    initInteractiveSurfaceGlow();
});
