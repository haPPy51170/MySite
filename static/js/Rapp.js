/*==================================================
                NEBULA PORTFOLIO
                app.js
==================================================*/
console.log("🔥 Rapp.js loaded");
/*==============================
TYPING EFFECT
==============================*/

const headlinesData = document.getElementById("headlines-data");
const typing = document.querySelector(".typing");

if (headlinesData && typing) {

    const words = JSON.parse(headlinesData.textContent);

    let wordIndex = 0;
    let letterIndex = 0;
    let deleting = false;

    function typeEffect() {

        const currentWord = words[wordIndex];

        if (!deleting) {

            typing.textContent = currentWord.substring(
                0,
                letterIndex++
            );

            if (letterIndex > currentWord.length) {

                deleting = true;

                setTimeout(typeEffect, 1600);

                return;

            }

        } else {

            typing.textContent = currentWord.substring(
                0,
                letterIndex--
            );

            if (letterIndex < 0) {

                deleting = false;

                wordIndex++;

                if (wordIndex >= words.length) {

                    wordIndex = 0;

                }

            }

        }

        setTimeout(
            typeEffect,
            deleting ? 45 : 90
        );

    }

    typeEffect();

}



/*==============================
SCROLL PROGRESS
==============================*/

const progress = document.querySelector(".progress-bar");

window.addEventListener("scroll", () => {

    if (!progress) return;

    const total = document.documentElement.scrollHeight - window.innerHeight;

    const percent = (window.scrollY / total) * 100;

    progress.style.width = percent + "%";

});


/*==============================
HEADER SCROLL
==============================*/

const header = document.querySelector(".header");

window.addEventListener("scroll", () => {

    if (!header) return;

    if (window.scrollY > 40) {

        header.classList.add("scrolled");

    } else {

        header.classList.remove("scrolled");

    }

});


/*==============================
REVEAL ANIMATION
==============================*/

const reveals = document.querySelectorAll(

    ".about-card,.skill-box,.project-card,.blog-card,.contact,.section-title,.hero-stats"

);

function revealSections() {

    reveals.forEach(item => {

        const top = item.getBoundingClientRect().top;

        if (top < window.innerHeight - 120) {

            item.classList.add("reveal");
            item.classList.add("active");

        }

    });

}

window.addEventListener("scroll", revealSections);

revealSections();


/*==============================
MOBILE MENU
==============================*/

const menuBtn = document.querySelector(".menu-btn");
const navbar = document.querySelector(".navbar");

if (menuBtn && navbar) {

    menuBtn.addEventListener("click", () => {

        navbar.classList.toggle("active");
        menuBtn.classList.toggle("active");

    });

    document.querySelectorAll(".navbar a").forEach(link => {

        link.addEventListener("click", () => {

            navbar.classList.remove("active");
            menuBtn.classList.remove("active");

        });

    });

}


/*==============================
SMOOTH SCROLL
==============================*/

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        const target = document.querySelector(this.getAttribute("href"));

        if (!target) return;

        e.preventDefault();

        target.scrollIntoView({

            behavior: "smooth"

        });

    });

});


/*==============================
ACTIVE NAV LINK
==============================*/

const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".navbar a");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const top = section.offsetTop - 120;

        const height = section.offsetHeight;

        if (window.scrollY >= top) {

            current = section.getAttribute("id");

        }

    });

    navLinks.forEach(link => {

        link.classList.remove("active");

        if (link.getAttribute("href") === "#" + current) {

            link.classList.add("active");

        }

    });

});


/*==============================
PARALLAX ORBS
==============================*/

const orb1 = document.querySelector(".orb-1");
const orb2 = document.querySelector(".orb-2");

document.addEventListener("mousemove", e => {

    const x = (e.clientX / window.innerWidth - 0.5) * 20;
    const y = (e.clientY / window.innerHeight - 0.5) * 20;

    if (orb1) {

        orb1.style.transform =
            `translate(${x}px,${y}px)`;

    }

    if (orb2) {

        orb2.style.transform =
            `translate(${-x}px,${-y}px)`;

    }

});

