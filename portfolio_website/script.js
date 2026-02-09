document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = document.querySelectorAll('section');
    const heroImage = document.querySelector('.hero-image-container img');

    // 1. Sophisticated Navbar Transition
    window.addEventListener('scroll', () => {
        if (window.scrollY > 80) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // 2. Intentional Hero Parallax
        if (heroImage && window.scrollY < window.innerHeight) {
            const scrollValue = window.scrollY * 0.15;
            heroImage.style.transform = `translateY(${scrollValue}px)`;
        }

        // 3. Precise Active Section Tracking
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= (sectionTop - 300)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });

    // 4. Calm Reveal on Scroll
    const revealElements = document.querySelectorAll('.reveal-scroll');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 1.2s cubic-bezier(0.2, 0.8, 0.2, 1), transform 1.2s cubic-bezier(0.2, 0.8, 0.2, 1)';
        revealObserver.observe(el);
    });

    // 5. Minimal Smooth Scrolling
    navLinks.forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // 6. Professional Testimonials Logic
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    const modal = document.getElementById('review-modal');
    const modalText = document.getElementById('modal-text');
    const modalName = document.getElementById('modal-client-name');
    const modalRole = document.getElementById('modal-client-role');
    const closeModal = document.querySelector('.close-modal');

    // Detect text overflow for "Read more" link
    testimonialCards.forEach(card => {
        const textElement = card.querySelector('.review-text');
        const readMoreBtn = card.querySelector('.read-more');

        // Check if text is truncated (clamped)
        if (textElement.scrollHeight > textElement.clientHeight) {
            readMoreBtn.style.display = 'inline-block';
        }

        readMoreBtn.addEventListener('click', () => {
            const fullText = readMoreBtn.getAttribute('data-full-text');
            const name = card.querySelector('.client-name').textContent;
            const role = card.querySelector('.client-role').textContent;

            modalText.textContent = fullText;
            modalName.textContent = name;
            modalRole.textContent = role;

            modal.style.display = 'flex';
            document.body.classList.add('modal-open');
        });
    });

    // Modal Closing Logic
    const closeReviewModal = () => {
        modal.style.display = 'none';
        document.body.classList.remove('modal-open');
    };

    closeModal.addEventListener('click', closeReviewModal);

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeReviewModal();
        }
    });

    // ESC key support
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.style.display === 'flex') {
            closeReviewModal();
        }
    });
});
