// PCS Academy Quiz App - Enhanced Version

// Quiz Database
const quizDatabase = {
    "Math": {
        "Easy": [
            {
                id: 1,
                question: "What is 15 + 27?",
                options: ["42", "41", "43", "40"],
                correct: 0,
                explanation: "15 + 27 = 42. This is basic addition."
            },
            {
                id: 2,
                question: "What is the square root of 144?",
                options: ["11", "12", "13", "14"],
                correct: 1,
                explanation: "√144 = 12, because 12 × 12 = 144"
            },
            {
                id: 3,
                question: "What is 100 - 37?",
                options: ["63", "62", "64", "61"],
                correct: 0,
                explanation: "100 - 37 = 63. This is basic subtraction."
            },
            {
                id: 10,
                question: "What is 8 × 7?",
                options: ["54", "56", "58", "52"],
                correct: 1,
                explanation: "8 × 7 = 56. This is basic multiplication."
            },
            {
                id: 11,
                question: "What is 81 ÷ 9?",
                options: ["8", "9", "7", "10"],
                correct: 1,
                explanation: "81 ÷ 9 = 9. This is basic division."
            }
        ],
        "Medium": [
            {
                id: 12,
                question: "What is 15% of 200?",
                options: ["30", "25", "35", "20"],
                correct: 0,
                explanation: "15% of 200 = 0.15 × 200 = 30"
            },
            {
                id: 13,
                question: "If x + 5 = 12, what is x?",
                options: ["7", "6", "8", "17"],
                correct: 0,
                explanation: "x = 12 - 5 = 7"
            }
        ],
        "Hard": [
            {
                id: 14,
                question: "What is the derivative of x²?",
                options: ["2x", "x", "2", "x²"],
                correct: 0,
                explanation: "The derivative of x² is 2x using the power rule."
            }
        ]
    },
    "Science": {
        "Easy": [
            {
                id: 4,
                question: "What gas do plants absorb during photosynthesis?",
                options: ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
                correct: 2,
                explanation: "Plants absorb CO2 from the air and use sunlight to convert it into glucose and oxygen."
            },
            {
                id: 5,
                question: "How many bones are there in an adult human body?",
                options: ["206", "205", "207", "204"],
                correct: 0,
                explanation: "An adult human skeleton has 206 bones."
            },
            {
                id: 15,
                question: "What is the chemical symbol for water?",
                options: ["H2O", "CO2", "O2", "H2SO4"],
                correct: 0,
                explanation: "Water is H2O - two hydrogen atoms and one oxygen atom."
            }
        ],
        "Medium": [
            {
                id: 16,
                question: "What is the speed of light in vacuum?",
                options: ["300,000 km/s", "150,000 km/s", "450,000 km/s", "200,000 km/s"],
                correct: 0,
                explanation: "The speed of light in vacuum is approximately 300,000 km/s."
            }
        ],
        "Hard": [
            {
                id: 17,
                question: "What is the atomic number of Carbon?",
                options: ["6", "8", "12", "14"],
                correct: 0,
                explanation: "Carbon has 6 protons, making its atomic number 6."
            }
        ]
    },
    "History": {
        "Easy": [
            {
                id: 6,
                question: "Who was the first President of India?",
                options: ["Jawaharlal Nehru", "Dr. Rajendra Prasad", "Mahatma Gandhi", "Sardar Patel"],
                correct: 1,
                explanation: "Dr. Rajendra Prasad was India's first President from 1950 to 1962."
            },
            {
                id: 7,
                question: "In which year did India gain independence?",
                options: ["1945", "1946", "1947", "1948"],
                correct: 2,
                explanation: "India gained independence from British rule on August 15, 1947."
            },
            {
                id: 18,
                question: "Who built the Taj Mahal?",
                options: ["Akbar", "Shah Jahan", "Aurangzeb", "Humayun"],
                correct: 1,
                explanation: "Shah Jahan built the Taj Mahal in memory of his wife Mumtaz Mahal."
            }
        ],
        "Medium": [
            {
                id: 19,
                question: "When did World War II end?",
                options: ["1944", "1945", "1946", "1947"],
                correct: 1,
                explanation: "World War II ended in 1945 with the surrender of Japan."
            }
        ],
        "Hard": [
            {
                id: 20,
                question: "Who was the first Governor-General of Bengal?",
                options: ["Warren Hastings", "Lord Cornwallis", "Robert Clive", "Lord Dalhousie"],
                correct: 0,
                explanation: "Warren Hastings was the first Governor-General of Bengal (1773-1785)."
            }
        ]
    },
    "General Knowledge": {
        "Easy": [
            {
                id: 8,
                question: "What is the capital of France?",
                options: ["London", "Berlin", "Paris", "Madrid"],
                correct: 2,
                explanation: "Paris is the capital and largest city of France."
            },
            {
                id: 9,
                question: "What is the largest mammal in the world?",
                options: ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                correct: 1,
                explanation: "The Blue Whale is the largest animal ever known to have lived on Earth."
            },
            {
                id: 21,
                question: "How many continents are there?",
                options: ["5", "6", "7", "8"],
                correct: 2,
                explanation: "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia."
            }
        ],
        "Medium": [
            {
                id: 22,
                question: "Which country has the most time zones?",
                options: ["Russia", "USA", "China", "Canada"],
                correct: 0,
                explanation: "Russia has 11 time zones, the most of any country."
            }
        ],
        "Hard": [
            {
                id: 23,
                question: "What is the smallest country in the world?",
                options: ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
                correct: 1,
                explanation: "Vatican City is the smallest country in the world with an area of 0.17 square miles."
            }
        ]
    }
};

// Achievements System
const achievements = [
    {
        name: "First Steps",
        description: "Complete your first quiz",
        icon: "🎯",
        condition: "first_quiz",
        unlocked: false
    },
    {
        name: "Perfect Score",
        description: "Get 100% on any quiz",
        icon: "🏆",
        condition: "perfect_score",
        unlocked: false
    },
    {
        name: "Math Master",
        description: "Excel in mathematics questions",
        icon: "🔢",
        condition: "math_expert",
        unlocked: false
    },
    {
        name: "Science Scholar",
        description: "Excel in science questions",
        icon: "🔬",
        condition: "science_expert",
        unlocked: false
    },
    {
        name: "Speed Runner",
        description: "Complete a quiz in under 2 minutes",
        icon: "⚡",
        condition: "speed_runner",
        unlocked: false
    },
    {
        name: "Streak Master",
        description: "Get 5 questions right in a row",
        icon: "🔥",
        condition: "streak_master",
        unlocked: false
    },
    {
        name: "Quiz Veteran",
        description: "Complete 10 quizzes",
        icon: "🎖️",
        condition: "quiz_veteran",
        unlocked: false
    },
    {
        name: "Knowledge Seeker",
        description: "Try all categories",
        icon: "📚",
        condition: "all_categories",
        unlocked: false
    }
];

// Application State
let appState = {
    currentScreen: 'loadingScreen',
    user: {
        name: 'Guest',
        avatar: '👤'
    },
    settings: {
        sound: false,
        vibration: false,
        explanations: true,
        autoAdvance: false
    },
    stats: {
        totalQuizzes: 0,
        totalQuestions: 0,
        correctAnswers: 0,
        currentStreak: 0,
        bestStreak: 0,
        categoryStats: {
            'Math': { attempted: 0, correct: 0 },
            'Science': { attempted: 0, correct: 0 },
            'History': { attempted: 0, correct: 0 },
            'General Knowledge': { attempted: 0, correct: 0 }
        },
        categoriesAttempted: new Set()
    },
    currentQuiz: {
        questions: [],
        currentQuestionIndex: 0,
        score: 0,
        correctCount: 0,
        startTime: null,
        category: 'all',
        difficulty: 'Easy',
        timeLimit: 30,
        answers: []
    },
    achievements: [...achievements],
    timer: null,
    timeLeft: 30
};

// Initialize App
function initApp() {
    // Load saved data
    loadUserData();
    
    // Start loading sequence
    setTimeout(() => {
        hideLoadingScreen();
        showScreen('splashScreen');
    }, 2000);
    
    // Setup keyboard navigation
    setupKeyboardNavigation();
    
    // Update UI
    updateStats();
    updateAchievements();
}

// Enhanced Navigation Functions
function enterApp() {
    document.getElementById('mainNav').style.display = 'block';
    document.getElementById('mainFooter').style.display = 'block';
    showPage('home');
}

function showPage(pageId) {
    // Hide all screens and pages
    document.querySelectorAll('.screen').forEach(screen => {
        screen.style.display = 'none';
        screen.classList.remove('active');
    });
    
    // Show target page
    const targetPage = document.getElementById(pageId + 'Page');
    if (targetPage) {
        targetPage.style.display = 'flex';
        targetPage.classList.add('active');
        appState.currentScreen = pageId + 'Page';
        
        // Update navigation active state
        updateNavigation(pageId);
        
        // Page-specific updates
        if (pageId === 'home') {
            updateHomeScreen();
        } else if (pageId === 'quiz') {
            updateStatsForQuizPage();
        }
        
        // Scroll to top
        window.scrollTo(0, 0);
    } else {
        // Fallback to screen system for quiz functionality
        showScreen(pageId + 'Screen');
    }
}

function updateNavigation(activePageId) {
    // Remove active class from all nav links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
    });
    
    // Add active class to current page nav link
    const navMap = {
        'home': 'home',
        'about': 'about', 
        'quiz': 'quiz',
        'help': 'help',
        'contact': 'contact'
    };
    
    if (navMap[activePageId]) {
        const activeLink = document.querySelector(`[onclick="showPage('${navMap[activePageId]}')"]`);
        if (activeLink) {
            activeLink.classList.add('active');
        }
    }
}

function toggleMobileMenu() {
    const navMenu = document.getElementById('navMenu');
    navMenu.classList.toggle('active');
}

function updateStatsForQuizPage() {
    // Update the stats on quiz page
    updateStats();
}

// Form submission functions
function submitContactForm(event) {
    event.preventDefault();
    
    const name = document.getElementById('contactName').value;
    const email = document.getElementById('contactEmail').value;
    const phone = document.getElementById('contactPhone').value;
    const subject = document.getElementById('contactSubject').value;
    const message = document.getElementById('contactMessage').value;
    
    if (!name || !email || !subject || !message) {
        alert('Please fill in all required fields.');
        return;
    }
    
    // Create email body
    let emailBody = `Name: ${name}\nEmail: ${email}`;
    if (phone) emailBody += `\nPhone: ${phone}`;
    emailBody += `\nSubject: ${subject}\nMessage:\n${message}`;
    
    // Create mailto link
    const mailtoLink = `mailto:pcsacademyschool@gmail.com?subject=Contact Form: ${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;
    
    // Try to open email client
    window.open(mailtoLink);
    
    // Show success message
    alert(`Thank you, ${name}! Your message is ready to send to pcsacademyschool@gmail.com. We'll respond within 24-48 hours.`);
    
    // Reset form
    document.getElementById('contactForm').reset();
}

function subscribeNewsletter() {
    const email = document.getElementById('newsletterEmail').value;
    
    if (!email || !email.includes('@')) {
        alert('Please enter a valid email address.');
        return;
    }
    
    // Create newsletter subscription email
    const mailtoLink = `mailto:pcsacademyschool@gmail.com?subject=Newsletter Subscription&body=Please subscribe ${encodeURIComponent(email)} to the PCS Academy newsletter.`;
    window.open(mailtoLink);
    
    alert(`Thank you for subscribing! We'll add ${email} to our newsletter list. Contact us at pcsacademyschool@gmail.com for any questions.`);
    document.getElementById('newsletterEmail').value = '';
}

// Search functions
function searchHelp() {
    const searchTerm = document.getElementById('helpSearch').value;
    if (searchTerm.trim()) {
        alert(`Searching for: "${searchTerm}". This would normally show filtered help results.`);
    }
}

function searchFAQ() {
    const searchTerm = document.getElementById('faqSearch').value;
    if (searchTerm.trim()) {
        alert(`Searching FAQ for: "${searchTerm}". This would normally show filtered FAQ results.`);
    }
}

// Quiz category navigation
function showQuizCategory(category) {
    showPage('quiz');
    setTimeout(() => {
        document.getElementById('categorySelect').value = category;
    }, 100);
}

// Loading Screen
function hideLoadingScreen() {
    const loadingScreen = document.getElementById('loadingScreen');
    loadingScreen.style.opacity = '0';
    setTimeout(() => {
        loadingScreen.style.display = 'none';
    }, 500);
}

// Screen Management (Enhanced for multi-page structure)
function showScreen(screenId) {
    // Hide all pages first
    document.querySelectorAll('.screen').forEach(screen => {
        screen.style.display = 'none';
        screen.classList.remove('active');
    });
    
    // Show target screen
    const targetScreen = document.getElementById(screenId);
    if (targetScreen) {
        targetScreen.style.display = 'flex';
        targetScreen.classList.add('active');
        appState.currentScreen = screenId;
        
        // Ensure navigation and footer are hidden for quiz screens
        if (screenId === 'quizScreen' || screenId === 'resultsScreen' || screenId === 'splashScreen') {
            document.getElementById('mainNav').style.display = 'none';
            document.getElementById('mainFooter').style.display = 'none';
        }
        
        // Update screen-specific content
        if (screenId === 'homeScreen') {
            updateHomeScreen();
        } else if (screenId === 'statsScreen') {
            updateStatsScreen();
        } else if (screenId === 'achievementsScreen') {
            updateAchievementsScreen();
        }
    }
}

// Quiz Functions
function startQuickQuiz() {
    // Get random questions from all categories
    const allQuestions = [];
    Object.keys(quizDatabase).forEach(category => {
        Object.keys(quizDatabase[category]).forEach(difficulty => {
            quizDatabase[category][difficulty].forEach(q => {
                allQuestions.push({...q, category, difficulty});
            });
        });
    });
    
    // Shuffle and select 10 questions
    const shuffled = shuffleArray(allQuestions);
    appState.currentQuiz.questions = shuffled.slice(0, 10);
    appState.currentQuiz.category = 'all';
    appState.currentQuiz.difficulty = 'Mixed';
    appState.currentQuiz.timeLimit = 30;
    
    startQuiz();
}

function startCustomQuiz() {
    const category = document.getElementById('categorySelect').value;
    const difficulty = document.getElementById('difficultySelect').value;
    const questionCount = parseInt(document.getElementById('questionsCount').value);
    const timeLimit = parseInt(document.getElementById('timeLimit').value);
    
    let questions = [];
    
    if (category === 'all') {
        // Get questions from all categories
        Object.keys(quizDatabase).forEach(cat => {
            if (quizDatabase[cat][difficulty]) {
                quizDatabase[cat][difficulty].forEach(q => {
                    questions.push({...q, category: cat, difficulty});
                });
            }
        });
    } else {
        // Get questions from specific category
        if (quizDatabase[category] && quizDatabase[category][difficulty]) {
            questions = quizDatabase[category][difficulty].map(q => ({...q, category, difficulty}));
        }
    }
    
    if (questions.length === 0) {
        alert('No questions available for the selected criteria. Please try different settings.');
        return;
    }
    
    // Shuffle and limit questions
    questions = shuffleArray(questions).slice(0, questionCount);
    
    appState.currentQuiz = {
        questions,
        currentQuestionIndex: 0,
        score: 0,
        correctCount: 0,
        startTime: null,
        category,
        difficulty,
        timeLimit,
        answers: []
    };
    
    startQuiz();
}

function startQuiz() {
    appState.currentQuiz.currentQuestionIndex = 0;
    appState.currentQuiz.score = 0;
    appState.currentQuiz.correctCount = 0;
    appState.currentQuiz.startTime = Date.now();
    appState.currentQuiz.answers = [];
    
    showScreen('quizScreen');
    loadQuestion();
}

function loadQuestion() {
    const quiz = appState.currentQuiz;
    const question = quiz.questions[quiz.currentQuestionIndex];
    
    if (!question) {
        endQuiz();
        return;
    }
    
    // Update question counter
    document.getElementById('questionCounter').textContent = 
        `${quiz.currentQuestionIndex + 1} / ${quiz.questions.length}`;
    
    // Update progress bar
    const progress = ((quiz.currentQuestionIndex + 1) / quiz.questions.length) * 100;
    document.getElementById('progressBar').style.width = `${progress}%`;
    
    // Display question
    document.getElementById('questionNumber').textContent = 
        `Question ${quiz.currentQuestionIndex + 1}`;
    document.getElementById('questionText').textContent = question.question;
    
    // Generate options
    const optionsContainer = document.getElementById('optionsContainer');
    optionsContainer.innerHTML = '';
    
    question.options.forEach((option, index) => {
        const optionElement = document.createElement('div');
        optionElement.className = 'option';
        optionElement.innerHTML = `
            <div class="option-letter">${String.fromCharCode(65 + index)}</div>
            <span>${option}</span>
        `;
        optionElement.onclick = () => selectAnswer(index);
        optionElement.tabIndex = 0;
        optionElement.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                selectAnswer(index);
            }
        });
        optionsContainer.appendChild(optionElement);
    });
    
    // Start timer if enabled
    if (quiz.timeLimit > 0) {
        startTimer();
    } else {
        document.getElementById('timer').style.display = 'none';
    }
    
    // Reset next button
    document.getElementById('nextButton').disabled = true;
    
    // Animate question card
    const questionCard = document.getElementById('questionCard');
    questionCard.style.animation = 'none';
    setTimeout(() => {
        questionCard.style.animation = 'slideIn 0.5s ease';
    }, 10);
}

function selectAnswer(selectedIndex) {
    const options = document.querySelectorAll('.option');
    const question = appState.currentQuiz.questions[appState.currentQuiz.currentQuestionIndex];
    
    // Clear previous selections
    options.forEach(option => {
        option.classList.remove('selected', 'correct', 'incorrect');
    });
    
    // Mark selected option
    options[selectedIndex].classList.add('selected');
    
    // Stop timer
    if (appState.timer) {
        clearInterval(appState.timer);
        appState.timer = null;
    }
    
    // Check answer after a brief delay for visual feedback
    setTimeout(() => {
        checkAnswer(selectedIndex);
    }, 500);
}

function checkAnswer(selectedIndex) {
    const question = appState.currentQuiz.questions[appState.currentQuiz.currentQuestionIndex];
    const options = document.querySelectorAll('.option');
    const isCorrect = selectedIndex === question.correct;
    
    // Show correct/incorrect styling
    options[question.correct].classList.add('correct');
    if (!isCorrect) {
        options[selectedIndex].classList.add('incorrect');
    }
    
    // Update score and stats
    if (isCorrect) {
        appState.currentQuiz.correctCount++;
        appState.stats.currentStreak++;
        appState.stats.correctAnswers++;
        
        if (appState.stats.currentStreak > appState.stats.bestStreak) {
            appState.stats.bestStreak = appState.stats.currentStreak;
        }
        
        // Haptic feedback
        if (appState.settings.vibration) {
            vibrate(100);
        }
    } else {
        appState.stats.currentStreak = 0;
        
        if (appState.settings.vibration) {
            vibrate([100, 50, 100]);
        }
    }
    
    // Update category stats
    const category = question.category || appState.currentQuiz.category;
    if (category !== 'all' && appState.stats.categoryStats[category]) {
        appState.stats.categoryStats[category].attempted++;
        if (isCorrect) {
            appState.stats.categoryStats[category].correct++;
        }
    }
    
    appState.stats.categoriesAttempted.add(category);
    appState.stats.totalQuestions++;
    
    // Store answer
    appState.currentQuiz.answers.push({
        question: question.question,
        selected: selectedIndex,
        correct: question.correct,
        isCorrect,
        explanation: question.explanation
    });
    
    // Show explanation if enabled
    if (appState.settings.explanations && question.explanation) {
        showExplanation(question.explanation, isCorrect);
    }
    
    // Enable next button
    document.getElementById('nextButton').disabled = false;
    
    // Auto-advance if enabled
    if (appState.settings.autoAdvance) {
        setTimeout(nextQuestion, 2000);
    }
}

function showExplanation(explanation, isCorrect) {
    const questionCard = document.getElementById('questionCard');
    
    // Create explanation element
    const explanationEl = document.createElement('div');
    explanationEl.className = `explanation ${isCorrect ? 'correct' : 'incorrect'}`;
    explanationEl.style.cssText = `
        margin-top: var(--space-4);
        padding: var(--space-4);
        border-radius: var(--radius-lg);
        background: ${isCorrect ? 'rgba(5, 150, 105, 0.1)' : 'rgba(220, 38, 38, 0.1)'};
        border: 2px solid ${isCorrect ? 'var(--success)' : 'var(--error)'};
        color: var(--color-text);
    `;
    explanationEl.innerHTML = `
        <div style="font-weight: 600; margin-bottom: var(--space-2); color: ${isCorrect ? 'var(--success)' : 'var(--error)'};">
            ${isCorrect ? '✅ Correct!' : '❌ Incorrect'}
        </div>
        <div>${explanation}</div>
    `;
    
    questionCard.appendChild(explanationEl);
}

function nextQuestion() {
    appState.currentQuiz.currentQuestionIndex++;
    
    // Remove explanation if present
    const explanation = document.querySelector('.explanation');
    if (explanation) {
        explanation.remove();
    }
    
    loadQuestion();
}

function startTimer() {
    appState.timeLeft = appState.currentQuiz.timeLimit;
    document.getElementById('timeLeft').textContent = appState.timeLeft;
    
    appState.timer = setInterval(() => {
        appState.timeLeft--;
        document.getElementById('timeLeft').textContent = appState.timeLeft;
        
        // Change color when time is running out
        const timerElement = document.getElementById('timer');
        if (appState.timeLeft <= 5) {
            timerElement.style.color = 'var(--error)';
        } else if (appState.timeLeft <= 10) {
            timerElement.style.color = 'var(--warning)';
        } else {
            timerElement.style.color = 'var(--accent)';
        }
        
        if (appState.timeLeft <= 0) {
            clearInterval(appState.timer);
            appState.timer = null;
            
            // Auto-select random answer if no answer selected
            const selectedOption = document.querySelector('.option.selected');
            if (!selectedOption) {
                const randomIndex = Math.floor(Math.random() * 4);
                selectAnswer(randomIndex);
            }
        }
    }, 1000);
}

function endQuiz() {
    // Stop timer
    if (appState.timer) {
        clearInterval(appState.timer);
        appState.timer = null;
    }
    
    // Calculate final score
    const totalQuestions = appState.currentQuiz.questions.length;
    const correctAnswers = appState.currentQuiz.correctCount;
    const scorePercentage = Math.round((correctAnswers / totalQuestions) * 100);
    const timeTaken = Math.round((Date.now() - appState.currentQuiz.startTime) / 1000);
    
    // Update global stats
    appState.stats.totalQuizzes++;
    
    // Check for achievements
    const newAchievements = checkAchievements(scorePercentage, timeTaken, correctAnswers, totalQuestions);
    
    // Update results screen
    document.getElementById('scoreCircle').textContent = `${scorePercentage}%`;
    document.getElementById('correctAnswers').textContent = correctAnswers;
    document.getElementById('incorrectAnswers').textContent = totalQuestions - correctAnswers;
    document.getElementById('timeTaken').textContent = `${timeTaken}s`;
    document.getElementById('streakCount').textContent = appState.stats.currentStreak;
    
    // Update result title and description
    const resultTitle = document.getElementById('resultTitle');
    const resultDescription = document.getElementById('resultDescription');
    
    if (scorePercentage === 100) {
        resultTitle.textContent = '🏆 Perfect Score!';
        resultDescription.textContent = `Congratulations! You answered all ${totalQuestions} questions correctly!`;
    } else if (scorePercentage >= 80) {
        resultTitle.textContent = '🌟 Excellent Work!';
        resultDescription.textContent = `Great job! You scored ${correctAnswers} out of ${totalQuestions} questions correctly.`;
    } else if (scorePercentage >= 60) {
        resultTitle.textContent = '👍 Good Effort!';
        resultDescription.textContent = `Nice work! You got ${correctAnswers} out of ${totalQuestions} questions right.`;
    } else {
        resultTitle.textContent = '📚 Keep Learning!';
        resultDescription.textContent = `You scored ${correctAnswers} out of ${totalQuestions}. Practice makes perfect!`;
    }
    
    // Show new achievements
    const newAchievementsContainer = document.getElementById('newAchievements');
    newAchievementsContainer.innerHTML = '';
    newAchievements.forEach(achievement => {
        const achievementEl = document.createElement('div');
        achievementEl.className = 'achievement';
        achievementEl.innerHTML = `${achievement.icon} ${achievement.name}`;
        newAchievementsContainer.appendChild(achievementEl);
    });
    
    // Save progress
    saveUserData();
    
    showScreen('resultsScreen');
}

// Achievement System
function checkAchievements(scorePercentage, timeTaken, correctAnswers, totalQuestions) {
    const newAchievements = [];
    
    appState.achievements.forEach(achievement => {
        if (achievement.unlocked) return;
        
        let shouldUnlock = false;
        
        switch (achievement.condition) {
            case 'first_quiz':
                shouldUnlock = appState.stats.totalQuizzes === 1;
                break;
            case 'perfect_score':
                shouldUnlock = scorePercentage === 100;
                break;
            case 'math_expert':
                const mathStats = appState.stats.categoryStats['Math'];
                shouldUnlock = mathStats.attempted >= 5 && mathStats.correct / mathStats.attempted >= 0.8;
                break;
            case 'science_expert':
                const scienceStats = appState.stats.categoryStats['Science'];
                shouldUnlock = scienceStats.attempted >= 5 && scienceStats.correct / scienceStats.attempted >= 0.8;
                break;
            case 'speed_runner':
                shouldUnlock = timeTaken < 120 && totalQuestions >= 10;
                break;
            case 'streak_master':
                shouldUnlock = appState.stats.currentStreak >= 5;
                break;
            case 'quiz_veteran':
                shouldUnlock = appState.stats.totalQuizzes >= 10;
                break;
            case 'all_categories':
                shouldUnlock = appState.stats.categoriesAttempted.size >= 4;
                break;
        }
        
        if (shouldUnlock) {
            achievement.unlocked = true;
            newAchievements.push(achievement);
        }
    });
    
    return newAchievements;
}

// Settings Functions
function toggleSetting(settingName) {
    const toggle = document.getElementById(settingName + 'Toggle');
    const isActive = toggle.classList.contains('active');
    
    if (isActive) {
        toggle.classList.remove('active');
        appState.settings[settingName] = false;
    } else {
        toggle.classList.add('active');
        appState.settings[settingName] = true;
    }
}

function saveSettings() {
    // Update user name and avatar
    const displayName = document.getElementById('displayName').value;
    const avatarSelect = document.getElementById('avatarSelect').value;
    
    if (displayName.trim()) {
        appState.user.name = displayName.trim();
    }
    
    appState.user.avatar = avatarSelect;
    
    // Save to storage
    saveUserData();
    
    // Update UI
    updateHomeScreen();
    
    alert('Settings saved successfully!');
}

// Update Functions
function updateHomeScreen() {
    document.getElementById('userName').textContent = appState.user.name;
    document.getElementById('userAvatar').textContent = appState.user.avatar;
    updateStats();
}

function updateStats() {
    const totalQuestions = appState.stats.totalQuestions;
    const correctAnswers = appState.stats.correctAnswers;
    const avgScore = totalQuestions > 0 ? Math.round((correctAnswers / totalQuestions) * 100) : 0;
    const unlockedAchievements = appState.achievements.filter(a => a.unlocked).length;
    
    document.getElementById('totalQuizzes').textContent = appState.stats.totalQuizzes;
    document.getElementById('averageScore').textContent = `${avgScore}%`;
    document.getElementById('streak').textContent = appState.stats.currentStreak;
    document.getElementById('achievements').textContent = unlockedAchievements;
}

function updateStatsScreen() {
    const totalQuestions = appState.stats.totalQuestions;
    const correctAnswers = appState.stats.correctAnswers;
    const accuracy = totalQuestions > 0 ? Math.round((correctAnswers / totalQuestions) * 100) : 0;
    
    document.getElementById('totalQuizzesStats').textContent = appState.stats.totalQuizzes;
    document.getElementById('totalQuestionsStats').textContent = totalQuestions;
    document.getElementById('accuracyStats').textContent = `${accuracy}%`;
    document.getElementById('bestStreakStats').textContent = appState.stats.bestStreak;
    
    // Update category stats
    const categoryStatsContainer = document.getElementById('categoryStats');
    categoryStatsContainer.innerHTML = '';
    
    Object.entries(appState.stats.categoryStats).forEach(([category, stats]) => {
        const accuracy = stats.attempted > 0 ? Math.round((stats.correct / stats.attempted) * 100) : 0;
        
        const categoryEl = document.createElement('div');
        categoryEl.className = 'setting-item';
        categoryEl.innerHTML = `
            <span>${category}</span>
            <div style="text-align: right;">
                <div style="font-weight: 600;">${accuracy}%</div>
                <div style="font-size: var(--font-size-xs); color: var(--color-text-secondary);">
                    ${stats.correct}/${stats.attempted}
                </div>
            </div>
        `;
        categoryStatsContainer.appendChild(categoryEl);
    });
}

function updateAchievementsScreen() {
    const achievementsList = document.getElementById('achievementsList');
    achievementsList.innerHTML = '';
    
    appState.achievements.forEach(achievement => {
        const achievementEl = document.createElement('div');
        achievementEl.className = `card ${achievement.unlocked ? '' : 'locked'}`;
        achievementEl.style.cssText = `
            opacity: ${achievement.unlocked ? '1' : '0.5'};
            margin-bottom: var(--space-3);
        `;
        
        achievementEl.innerHTML = `
            <div style="display: flex; align-items: center; gap: var(--space-4);">
                <div style="font-size: var(--font-size-3xl);">${achievement.icon}</div>
                <div style="flex: 1;">
                    <h3 style="margin-bottom: var(--space-1);">${achievement.name}</h3>
                    <p style="color: var(--color-text-secondary); margin: 0;">${achievement.description}</p>
                </div>
                <div style="font-size: var(--font-size-lg);">
                    ${achievement.unlocked ? '✅' : '🔒'}
                </div>
            </div>
        `;
        
        achievementsList.appendChild(achievementEl);
    });
}

// Keyboard Navigation
function setupKeyboardNavigation() {
    document.addEventListener('keydown', (e) => {
        if (appState.currentScreen === 'quizScreen') {
            // A, B, C, D keys for answers
            if (e.key.toLowerCase() >= 'a' && e.key.toLowerCase() <= 'd') {
                const index = e.key.toLowerCase().charCodeAt(0) - 'a'.charCodeAt(0);
                const options = document.querySelectorAll('.option');
                if (options[index] && !options[index].classList.contains('selected')) {
                    selectAnswer(index);
                }
            }
            
            // Enter key for next question
            if (e.key === 'Enter') {
                const nextButton = document.getElementById('nextButton');
                if (!nextButton.disabled) {
                    nextQuestion();
                }
            }
        }
        
        // Escape key to go back
        if (e.key === 'Escape') {
            if (appState.currentScreen !== 'homeScreen' && appState.currentScreen !== 'splashScreen') {
                showScreen('homeScreen');
            }
        }
    });
}

// Utility Functions
function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

function vibrate(pattern) {
    if (navigator.vibrate && appState.settings.vibration) {
        navigator.vibrate(pattern);
    }
}

function shareResults() {
    const scorePercentage = Math.round((appState.currentQuiz.correctCount / appState.currentQuiz.questions.length) * 100);
    const shareText = `I just scored ${scorePercentage}% on PCS Academy Quiz! 🎓 Can you beat my score? #PCSAcademy #Quiz #Learning`;
    
    if (navigator.share) {
        navigator.share({
            title: 'PCS Academy Quiz Results',
            text: shareText,
            url: window.location.href
        });
    } else {
        // Fallback to clipboard
        navigator.clipboard.writeText(shareText).then(() => {
            alert('Results copied to clipboard! Share with your friends!');
        }).catch(() => {
            alert(`Share your results: ${shareText}`);
        });
    }
}

// Enhanced quiz navigation to handle both screen and page transitions
function backToHome() {
    document.getElementById('mainNav').style.display = 'block';
    document.getElementById('mainFooter').style.display = 'block';
    showPage('home');
}

// Update quiz screen navigation to use backToHome
function enhanceQuizNavigation() {
    // Update quit quiz buttons to go back to home page instead of homeScreen
    const quitButtons = document.querySelectorAll('button[onclick="showScreen(\'homeScreen\')"],[onclick="showScreen(\'homeScreen\')"');
    quitButtons.forEach(button => {
        button.onclick = backToHome;
    });
}

// Enhanced keyboard navigation for pages
function enhanceKeyboardNavigation() {
    document.addEventListener('keydown', (e) => {
        // Page navigation with number keys
        if (e.altKey) {
            switch(e.key) {
                case '1': showPage('home'); break;
                case '2': showPage('about'); break;
                case '3': showPage('quiz'); break;
                case '4': showPage('help'); break;
                case '5': showPage('contact'); break;
            }
        }
        
        // ESC to go back to home
        if (e.key === 'Escape' && !appState.currentScreen.includes('quiz')) {
            showPage('home');
        }
    });
}

// Data Persistence (using variables since localStorage is not available)
function saveUserData() {
    // In a real app, this would save to localStorage or a backend
    // For now, we keep everything in memory
    console.log('User data saved (in memory)');
}

function loadUserData() {
    // In a real app, this would load from localStorage or a backend
    // For now, we start with default data
    console.log('User data loaded (default values)');
}

// Initialize app when page loads
document.addEventListener('DOMContentLoaded', () => {
    initApp();
    enhanceQuizNavigation();
    enhanceKeyboardNavigation();
    
    // Add click handlers for mobile menu
    document.addEventListener('click', (e) => {
        const navMenu = document.getElementById('navMenu');
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        
        if (navMenu.classList.contains('active') && 
            !navMenu.contains(e.target) && 
            !mobileMenuBtn.contains(e.target)) {
            navMenu.classList.remove('active');
        }
    });
});

// Additional quiz questions for better variety
const additionalQuestions = {
    "Math": {
        "Easy": [
            {
                id: 24,
                question: "What is 9 × 6?",
                options: ["52", "54", "56", "48"],
                correct: 1,
                explanation: "9 × 6 = 54"
            },
            {
                id: 25,
                question: "What is 25 + 38?",
                options: ["63", "62", "64", "61"],
                correct: 0,
                explanation: "25 + 38 = 63"
            }
        ],
        "Medium": [
            {
                id: 26,
                question: "What is 144 ÷ 12?",
                options: ["11", "12", "13", "10"],
                correct: 1,
                explanation: "144 ÷ 12 = 12"
            }
        ]
    },
    "Science": {
        "Easy": [
            {
                id: 27,
                question: "What is the hardest natural substance?",
                options: ["Gold", "Iron", "Diamond", "Silver"],
                correct: 2,
                explanation: "Diamond is the hardest naturally occurring substance."
            }
        ],
        "Medium": [
            {
                id: 28,
                question: "What is the chemical formula for table salt?",
                options: ["NaCl", "KCl", "CaCl2", "MgCl2"],
                correct: 0,
                explanation: "Table salt is sodium chloride (NaCl)."
            }
        ]
    },
    "History": {
        "Easy": [
            {
                id: 29,
                question: "Who discovered America?",
                options: ["Vasco da Gama", "Christopher Columbus", "Ferdinand Magellan", "Marco Polo"],
                correct: 1,
                explanation: "Christopher Columbus reached the Americas in 1492."
            }
        ]
    },
    "General Knowledge": {
        "Easy": [
            {
                id: 30,
                question: "Which planet is known as the Red Planet?",
                options: ["Venus", "Mars", "Jupiter", "Saturn"],
                correct: 1,
                explanation: "Mars is called the Red Planet due to its reddish appearance."
            }
        ]
    }
};

// Merge additional questions into main database
Object.keys(additionalQuestions).forEach(category => {
    Object.keys(additionalQuestions[category]).forEach(difficulty => {
        if (!quizDatabase[category][difficulty]) {
            quizDatabase[category][difficulty] = [];
        }
        quizDatabase[category][difficulty] = quizDatabase[category][difficulty].concat(
            additionalQuestions[category][difficulty]
        );
    });
});