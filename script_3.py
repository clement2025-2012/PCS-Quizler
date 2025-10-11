# Create comprehensive JavaScript with quiz functionality
js_content = '''// PCS Academy Quiz Application - Complete JavaScript
class PCSQuizApp {
    constructor() {
        this.currentScreen = 'splash-screen';
        this.currentQuestion = 0;
        this.quizQuestions = [];
        this.userAnswers = [];
        this.score = 0;
        this.timer = null;
        this.timeLeft = 30;
        this.selectedAnswer = null;
        
        // Question database
        this.questionDB = [
            {
                id: 1,
                category: "Math",
                difficulty: "Easy",
                question: "What is 15 + 27?",
                options: ["42", "41", "43", "40"],
                correct: 0,
                explanation: "15 + 27 = 42. This is basic addition."
            },
            {
                id: 2,
                category: "Math",
                difficulty: "Easy", 
                question: "What is the square root of 144?",
                options: ["11", "12", "13", "14"],
                correct: 1,
                explanation: "√144 = 12, because 12 × 12 = 144"
            },
            {
                id: 3,
                category: "Science",
                difficulty: "Easy",
                question: "What gas do plants absorb during photosynthesis?",
                options: ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
                correct: 2,
                explanation: "Plants absorb CO₂ from the air and use sunlight to convert it into glucose and oxygen."
            },
            {
                id: 4,
                category: "Science",
                difficulty: "Easy",
                question: "How many bones are there in an adult human body?",
                options: ["206", "205", "207", "204"],
                correct: 0,
                explanation: "An adult human skeleton has 206 bones."
            },
            {
                id: 5,
                category: "History",
                difficulty: "Easy",
                question: "Who was the first President of India?",
                options: ["Jawaharlal Nehru", "Dr. Rajendra Prasad", "Mahatma Gandhi", "Sardar Patel"],
                correct: 1,
                explanation: "Dr. Rajendra Prasad was India's first President from 1950 to 1962."
            },
            {
                id: 6,
                category: "History",
                difficulty: "Easy",
                question: "In which year did India gain independence?",
                options: ["1945", "1946", "1947", "1948"],
                correct: 2,
                explanation: "India gained independence from British rule on August 15, 1947."
            },
            {
                id: 7,
                category: "General Knowledge",
                difficulty: "Easy",
                question: "What is the capital of France?",
                options: ["London", "Berlin", "Paris", "Madrid"],
                correct: 2,
                explanation: "Paris is the capital and largest city of France."
            },
            {
                id: 8,
                category: "General Knowledge",
                difficulty: "Easy",
                question: "What is the largest mammal in the world?",
                options: ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                correct: 1,
                explanation: "The Blue Whale is the largest animal ever known to have lived on Earth."
            },
            {
                id: 9,
                category: "Math",
                difficulty: "Medium",
                question: "What is 12 × 15?",
                options: ["180", "175", "185", "170"],
                correct: 0,
                explanation: "12 × 15 = 180. You can calculate this as (12 × 10) + (12 × 5) = 120 + 60 = 180."
            },
            {
                id: 10,
                category: "Science",
                difficulty: "Medium",
                question: "What is the chemical symbol for gold?",
                options: ["Go", "Gd", "Au", "Ag"],
                correct: 2,
                explanation: "The chemical symbol for gold is Au, from the Latin word 'aurum'."
            },
            {
                id: 11,
                category: "Math",
                difficulty: "Easy",
                question: "What is 100 - 37?",
                options: ["63", "62", "64", "61"],
                correct: 0,
                explanation: "100 - 37 = 63. This is basic subtraction."
            },
            {
                id: 12,
                category: "Science",
                difficulty: "Easy",
                question: "Which planet is known as the Red Planet?",
                options: ["Venus", "Mars", "Jupiter", "Saturn"],
                correct: 1,
                explanation: "Mars is known as the Red Planet due to its reddish appearance caused by iron oxide on its surface."
            },
            {
                id: 13,
                category: "General Knowledge",
                difficulty: "Easy",
                question: "How many continents are there on Earth?",
                options: ["5", "6", "7", "8"],
                correct: 2,
                explanation: "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia."
            },
            {
                id: 14,
                category: "History",
                difficulty: "Medium",
                question: "Who built the Taj Mahal?",
                options: ["Akbar", "Shah Jahan", "Humayun", "Aurangzeb"],
                correct: 1,
                explanation: "The Taj Mahal was built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal."
            },
            {
                id: 15,
                category: "Math",
                difficulty: "Medium",
                question: "What is 25% of 80?",
                options: ["15", "20", "25", "30"],
                correct: 1,
                explanation: "25% of 80 = (25/100) × 80 = 0.25 × 80 = 20."
            }
        ];
        
        this.init();
    }
    
    init() {
        // Show splash screen for 3 seconds
        setTimeout(() => {
            this.showScreen('home-screen');
        }, 3000);
        
        // Set up event listeners
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        // Quiz button listeners
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('option-button')) {
                this.selectAnswer(e.target);
            }
        });
        
        const submitButton = document.getElementById('submit-answer');
        const nextButton = document.getElementById('next-question');
        
        if (submitButton) {
            submitButton.addEventListener('click', () => this.submitAnswer());
        }
        
        if (nextButton) {
            nextButton.addEventListener('click', () => this.nextQuestion());
        }
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (this.currentScreen === 'quiz-screen') {
                switch(e.key) {
                    case 'a':
                    case 'A':
                        this.selectAnswerByIndex(0);
                        break;
                    case 'b':
                    case 'B':
                        this.selectAnswerByIndex(1);
                        break;
                    case 'c':
                    case 'C':
                        this.selectAnswerByIndex(2);
                        break;
                    case 'd':
                    case 'D':
                        this.selectAnswerByIndex(3);
                        break;
                    case 'Enter':
                        if (this.selectedAnswer !== null) {
                            this.submitAnswer();
                        }
                        break;
                }
            }
        });
    }
    
    showScreen(screenId) {
        // Hide all screens
        const screens = document.querySelectorAll('.screen');
        screens.forEach(screen => {
            screen.classList.remove('active');
        });
        
        // Show target screen
        const targetScreen = document.getElementById(screenId);
        if (targetScreen) {
            targetScreen.classList.add('active');
            this.currentScreen = screenId;
            
            // Initialize quiz if entering quiz screen
            if (screenId === 'quiz-screen') {
                this.startQuiz();
            }
        }
    }
    
    startQuiz() {
        // Reset quiz state
        this.currentQuestion = 0;
        this.userAnswers = [];
        this.score = 0;
        this.selectedAnswer = null;
        
        // Shuffle questions
        this.quizQuestions = this.shuffleArray([...this.questionDB]).slice(0, 10);
        
        // Show first question
        this.displayQuestion();
        this.startTimer();
    }
    
    displayQuestion() {
        const question = this.quizQuestions[this.currentQuestion];
        
        // Update question counter
        document.getElementById('question-counter').textContent = 
            `Question ${this.currentQuestion + 1} of ${this.quizQuestions.length}`;
        
        // Update question text
        document.getElementById('question-text').textContent = question.question;
        
        // Update options
        const optionsContainer = document.getElementById('options-container');
        optionsContainer.innerHTML = '';
        
        question.options.forEach((option, index) => {
            const button = document.createElement('button');
            button.className = 'option-button';
            button.textContent = `${String.fromCharCode(65 + index)}. ${option}`;
            button.dataset.index = index;
            optionsContainer.appendChild(button);
        });
        
        // Reset selected answer
        this.selectedAnswer = null;
        
        // Show submit button, hide next button
        document.getElementById('submit-answer').style.display = 'inline-block';
        document.getElementById('next-question').style.display = 'none';
        
        // Reset timer
        this.timeLeft = 30;
        this.startTimer();
    }
    
    selectAnswer(button) {
        // Remove previous selection
        const options = document.querySelectorAll('.option-button');
        options.forEach(opt => opt.classList.remove('selected'));
        
        // Add selection to clicked button
        button.classList.add('selected');
        this.selectedAnswer = parseInt(button.dataset.index);
    }
    
    selectAnswerByIndex(index) {
        const options = document.querySelectorAll('.option-button');
        if (options[index]) {
            this.selectAnswer(options[index]);
        }
    }
    
    submitAnswer() {
        if (this.selectedAnswer === null) {
            alert('Please select an answer before submitting!');
            return;
        }
        
        const question = this.quizQuestions[this.currentQuestion];
        const options = document.querySelectorAll('.option-button');
        
        // Stop timer
        clearInterval(this.timer);
        
        // Show correct/incorrect answers
        options.forEach((option, index) => {
            if (index === question.correct) {
                option.classList.add('correct');
            } else if (index === this.selectedAnswer && index !== question.correct) {
                option.classList.add('incorrect');
            }
            option.disabled = true;
        });
        
        // Record answer
        const isCorrect = this.selectedAnswer === question.correct;
        this.userAnswers.push({
            question: question.question,
            selected: this.selectedAnswer,
            correct: question.correct,
            isCorrect: isCorrect
        });
        
        if (isCorrect) {
            this.score++;
        }
        
        // Show explanation
        this.showExplanation(question.explanation, isCorrect);
        
        // Hide submit button, show next button
        document.getElementById('submit-answer').style.display = 'none';
        document.getElementById('next-question').style.display = 'inline-block';
    }
    
    showExplanation(explanation, isCorrect) {
        // Create explanation element
        const explanationDiv = document.createElement('div');
        explanationDiv.className = 'explanation';
        explanationDiv.innerHTML = `
            <div class="explanation-header ${isCorrect ? 'correct' : 'incorrect'}">
                ${isCorrect ? '✓ Correct!' : '✗ Incorrect'}
            </div>
            <div class="explanation-text">${explanation}</div>
        `;
        
        // Add to question container
        const questionContainer = document.querySelector('.question-container');
        questionContainer.appendChild(explanationDiv);
        
        // Style the explanation
        explanationDiv.style.cssText = `
            margin-top: 1rem;
            padding: 1rem;
            border-radius: 8px;
            background: ${isCorrect ? '#dcfce7' : '#fef2f2'};
            border-left: 4px solid ${isCorrect ? '#16a34a' : '#dc2626'};
        `;
        
        const header = explanationDiv.querySelector('.explanation-header');
        header.style.cssText = `
            font-weight: bold;
            color: ${isCorrect ? '#16a34a' : '#dc2626'};
            margin-bottom: 0.5rem;
        `;
    }
    
    nextQuestion() {
        this.currentQuestion++;
        
        if (this.currentQuestion < this.quizQuestions.length) {
            // Remove explanation
            const explanation = document.querySelector('.explanation');
            if (explanation) {
                explanation.remove();
            }
            
            this.displayQuestion();
        } else {
            this.showResults();
        }
    }
    
    showResults() {
        const percentage = Math.round((this.score / this.quizQuestions.length) * 100);
        let message = '';
        
        if (percentage >= 90) {
            message = 'Excellent! Outstanding performance! 🏆';
        } else if (percentage >= 75) {
            message = 'Great job! Well done! 🎉';
        } else if (percentage >= 60) {
            message = 'Good work! Keep practicing! 👍';
        } else {
            message = 'Keep studying and try again! 📚';
        }
        
        const quizContainer = document.querySelector('.quiz-container');
        quizContainer.innerHTML = `
            <div class="results-container">
                <h2>Quiz Complete!</h2>
                <div class="score-display">
                    <div class="score-circle">
                        <span class="score-number">${percentage}%</span>
                    </div>
                    <p class="score-text">You scored ${this.score} out of ${this.quizQuestions.length}</p>
                    <p class="score-message">${message}</p>
                </div>
                <div class="results-actions">
                    <button onclick="quizApp.startQuiz()" class="quiz-button">Try Again</button>
                    <button onclick="quizApp.showScreen('home-screen')" class="quiz-button">Back to Home</button>
                </div>
            </div>
        `;
        
        // Style the results
        const style = document.createElement('style');
        style.textContent = `
            .results-container {
                text-align: center;
                padding: 2rem;
                background: white;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .score-display {
                margin: 2rem 0;
            }
            .score-circle {
                width: 120px;
                height: 120px;
                border-radius: 50%;
                background: linear-gradient(135deg, #dc2626, #ef4444);
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 1rem;
                box-shadow: 0 8px 16px rgba(220,38,38,0.3);
            }
            .score-number {
                font-size: 2rem;
                font-weight: bold;
                color: white;
            }
            .score-text {
                font-size: 1.2rem;
                color: #374151;
                margin-bottom: 0.5rem;
            }
            .score-message {
                font-size: 1.1rem;
                color: #dc2626;
                font-weight: 600;
            }
            .results-actions {
                margin-top: 2rem;
                display: flex;
                gap: 1rem;
                justify-content: center;
                flex-wrap: wrap;
            }
        `;
        document.head.appendChild(style);
    }
    
    startTimer() {
        clearInterval(this.timer);
        this.timeLeft = 30;
        
        this.timer = setInterval(() => {
            this.timeLeft--;
            const timerElement = document.getElementById('timer');
            
            if (timerElement) {
                timerElement.textContent = this.timeLeft;
                
                // Change color based on time remaining
                if (this.timeLeft <= 5) {
                    timerElement.style.background = '#ef4444';
                    timerElement.style.animation = 'pulse 0.5s infinite';
                } else if (this.timeLeft <= 10) {
                    timerElement.style.background = '#f59e0b';
                } else {
                    timerElement.style.background = '#dc2626';
                    timerElement.style.animation = 'pulse 1s infinite';
                }
            }
            
            if (this.timeLeft <= 0) {
                clearInterval(this.timer);
                // Auto-submit if no answer selected
                if (this.selectedAnswer === null) {
                    alert('Time\\'s up! Moving to next question.');
                    this.nextQuestion();
                } else {
                    this.submitAnswer();
                }
            }
        }, 1000);
    }
    
    shuffleArray(array) {
        const shuffled = [...array];
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }
        return shuffled;
    }
}

// Global functions for HTML onclick handlers
function showScreen(screenId) {
    if (window.quizApp) {
        window.quizApp.showScreen(screenId);
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.quizApp = new PCSQuizApp();
});

// Add smooth scrolling for anchor links
document.addEventListener('click', function(e) {
    if (e.target.tagName === 'A' && e.target.getAttribute('href')?.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(e.target.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }
});

// Add loading animation
window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});

// Performance optimization: Lazy load images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}'''

with open(f"{project_dir}/app.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Created comprehensive app.js")