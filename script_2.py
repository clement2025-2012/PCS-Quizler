# Create comprehensive CSS with modern styling
css_content = '''/* PCS Academy Quiz App - Complete Styling */

/* CSS Variables for consistent theming */
:root {
  --primary-color: #dc2626;
  --primary-light: #ef4444;
  --primary-dark: #b91c1c;
  --secondary-color: #059669;
  --accent-color: #f59e0b;
  --background-color: #f8fafc;
  --surface-color: #ffffff;
  --text-primary: #1f2937;
  --text-secondary: #6b7280;
  --border-color: #e5e7eb;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --border-radius: 8px;
  --transition: all 0.3s ease;
}

/* Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  color: var(--text-primary);
  background-color: var(--background-color);
}

/* App Container */
#app {
  min-height: 100vh;
  position: relative;
}

/* Screen Management */
.screen {
  display: none;
  min-height: 100vh;
  opacity: 0;
  transition: var(--transition);
}

.screen.active {
  display: block;
  opacity: 1;
}

/* Splash Screen Styles */
#splash-screen {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
  color: white;
  text-align: center;
}

.splash-container {
  max-width: 400px;
  padding: 2rem;
}

.splash-container .logo {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin-bottom: 2rem;
  border: 4px solid white;
  box-shadow: var(--shadow-lg);
  animation: pulse 2s infinite;
}

.splash-container h1 {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.splash-container p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.loading-bar {
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 2px;
  margin-bottom: 1rem;
  overflow: hidden;
}

.loading-progress {
  height: 100%;
  background: white;
  border-radius: 2px;
  animation: loading 3s ease-in-out;
}

.loading-text {
  font-size: 0.9rem;
  opacity: 0.8;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

@keyframes loading {
  0% { width: 0%; }
  50% { width: 70%; }
  100% { width: 100%; }
}

/* Header Styles */
.app-header {
  background: white;
  box-shadow: var(--shadow-sm);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.header-logo {
  width: 50px;
  height: 50px;
  border-radius: 8px;
}

.app-header h1 {
  font-size: 1.5rem;
  color: var(--primary-color);
  font-weight: bold;
}

.main-nav {
  display: flex;
  gap: 1.5rem;
}

.main-nav a {
  text-decoration: none;
  color: var(--text-primary);
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: var(--border-radius);
  transition: var(--transition);
}

.main-nav a:hover {
  background-color: var(--primary-color);
  color: white;
}

/* Home Content */
.home-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.hero-section {
  text-align: center;
  padding: 4rem 0;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
  color: white;
  border-radius: var(--border-radius);
  margin-bottom: 4rem;
}

.hero-section h2 {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.hero-section p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  opacity: 0.9;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.cta-button {
  background: white;
  color: var(--primary-color);
  border: none;
  padding: 1rem 2rem;
  font-size: 1.1rem;
  font-weight: bold;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: var(--transition);
  box-shadow: var(--shadow-md);
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

/* Features Grid */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-md);
  text-align: center;
  transition: var(--transition);
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.feature-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--primary-color);
}

.feature-card p {
  color: var(--text-secondary);
  line-height: 1.6;
}

/* Footer Styles */
.app-footer {
  background: var(--text-primary);
  color: white;
  padding: 3rem 0 1rem;
  margin-top: 4rem;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.footer-section h4 {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  color: var(--primary-light);
}

.footer-section p, .footer-section a {
  margin-bottom: 0.5rem;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  display: block;
}

.footer-section a:hover {
  color: var(--primary-light);
}

.footer-bottom {
  max-width: 1200px;
  margin: 2rem auto 0;
  padding: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
  color: rgba(255, 255, 255, 0.6);
}

/* Quiz Screen Styles */
.quiz-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.quiz-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border-color);
}

.back-button {
  background: var(--text-secondary);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: var(--border-radius);
  cursor: pointer;
  font-weight: 500;
  transition: var(--transition);
}

.back-button:hover {
  background: var(--text-primary);
}

.quiz-info {
  display: flex;
  gap: 2rem;
  align-items: center;
}

#question-counter {
  font-weight: 600;
  color: var(--text-secondary);
}

.timer {
  background: var(--primary-color);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 50%;
  font-weight: bold;
  min-width: 60px;
  text-align: center;
  animation: pulse 1s infinite;
}

.quiz-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.question-container {
  background: white;
  padding: 2rem;
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-md);
  margin-bottom: 2rem;
}

.question-container h2 {
  font-size: 1.5rem;
  line-height: 1.4;
  color: var(--text-primary);
}

.options-container {
  display: grid;
  gap: 1rem;
  margin-bottom: 2rem;
}

.option-button {
  background: white;
  border: 2px solid var(--border-color);
  padding: 1rem;
  border-radius: var(--border-radius);
  text-align: left;
  cursor: pointer;
  transition: var(--transition);
  font-size: 1rem;
}

.option-button:hover {
  border-color: var(--primary-color);
  background-color: rgba(220, 38, 38, 0.05);
}

.option-button.selected {
  background: var(--primary-color);
  color: white;
  border-color: var(--primary-color);
}

.option-button.correct {
  background: var(--secondary-color);
  color: white;
  border-color: var(--secondary-color);
}

.option-button.incorrect {
  background: #ef4444;
  color: white;
  border-color: #ef4444;
}

.quiz-controls {
  text-align: center;
}

.quiz-button {
  background: var(--primary-color);
  color: white;
  border: none;
  padding: 1rem 2rem;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: var(--transition);
  margin: 0 0.5rem;
}

.quiz-button:hover {
  background: var(--primary-dark);
}

.quiz-button:disabled {
  background: var(--text-secondary);
  cursor: not-allowed;
}

/* Page Container Styles */
.page-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem 1rem;
  min-height: 100vh;
}

.page-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--border-color);
}

.page-header h1 {
  font-size: 2.5rem;
  color: var(--primary-color);
  margin-top: 1rem;
}

.page-content {
  background: white;
  padding: 2rem;
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-md);
  line-height: 1.8;
}

/* About and Policy Content */
.about-section, .policy-content {
  max-width: none;
}

.about-section h2, .policy-content h2 {
  color: var(--primary-color);
  margin: 2rem 0 1rem 0;
  font-size: 1.5rem;
}

.about-section h3, .policy-content h3 {
  color: var(--text-primary);
  margin: 1.5rem 0 0.5rem 0;
}

.about-section p, .policy-content p {
  margin-bottom: 1rem;
  color: var(--text-secondary);
}

.about-section ul, .policy-content ul {
  margin: 1rem 0 1rem 2rem;
  color: var(--text-secondary);
}

.about-section li, .policy-content li {
  margin-bottom: 0.5rem;
}

.contact-info {
  background: var(--background-color);
  padding: 1.5rem;
  border-radius: var(--border-radius);
  margin: 1rem 0;
}

/* Contact Page Styles */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-top: 2rem;
}

.contact-method {
  margin-bottom: 2rem;
}

.contact-method h3 {
  color: var(--primary-color);
  margin-bottom: 0.5rem;
}

.contact-method a {
  color: var(--primary-color);
  text-decoration: none;
}

.contact-method a:hover {
  text-decoration: underline;
}

/* Contact Form */
.contact-form {
  background: var(--background-color);
  padding: 2rem;
  border-radius: var(--border-radius);
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-primary);
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid var(--border-color);
  border-radius: var(--border-radius);
  font-size: 1rem;
  transition: var(--transition);
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}

.submit-button {
  background: var(--primary-color);
  color: white;
  border: none;
  padding: 1rem 2rem;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: var(--transition);
  width: 100%;
}

.submit-button:hover {
  background: var(--primary-dark);
}

/* Responsive Design */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    text-align: center;
  }
  
  .hero-section h2 {
    font-size: 2rem;
  }
  
  .hero-section p {
    font-size: 1rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .quiz-info {
    flex-direction: column;
    gap: 1rem;
  }
  
  .main-nav {
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .page-header h1 {
    font-size: 2rem;
  }
}

@media (max-width: 480px) {
  .page-container,
  .quiz-container {
    padding: 1rem 0.5rem;
  }
  
  .hero-section {
    padding: 2rem 1rem;
  }
  
  .feature-card,
  .question-container,
  .page-content {
    padding: 1.5rem;
  }
}

/* Additional Utility Classes */
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

.mt-1 { margin-top: 0.25rem; }
.mt-2 { margin-top: 0.5rem; }
.mt-4 { margin-top: 1rem; }
.mb-1 { margin-bottom: 0.25rem; }
.mb-2 { margin-bottom: 0.5rem; }
.mb-4 { margin-bottom: 1rem; }

.hidden { display: none !important; }
.visible { display: block !important; }

/* Animation Classes */
.fade-in {
  animation: fadeIn 0.5s ease-in;
}

.slide-up {
  animation: slideUp 0.3s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from { 
    opacity: 0; 
    transform: translateY(20px); 
  }
  to { 
    opacity: 1; 
    transform: translateY(0); 
  }
}'''

with open(f"{project_dir}/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("Created comprehensive style.css")