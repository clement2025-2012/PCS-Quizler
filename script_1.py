# Create comprehensive index.html with all features and AdSense compliance
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PCS Academy Quiz App - Educational Learning Platform</title>
    <meta name="description" content="Interactive educational quiz application by PCS Academy School. Test your knowledge in Math, Science, History and more.">
    <meta name="keywords" content="education, quiz, learning, PCS Academy, students, interactive">
    <meta name="author" content="PCS Academy School">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAQAQAABMLAAATCwAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==">
    <link rel="apple-touch-icon" sizes="180x180" href="assets/PCS-Seal.jpg">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="PCS Academy Quiz App">
    <meta property="og:description" content="Interactive educational quiz application by PCS Academy School">
    <meta property="og:type" content="website">
    
    <!-- CSS -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="app">
        <!-- Splash Screen -->
        <div id="splash-screen" class="screen active">
            <div class="splash-container">
                <img src="assets/PCS-Seal.jpg" alt="PCS Academy School" class="logo">
                <h1>PCS ACADEMY</h1>
                <p>Educational Quiz App</p>
                <div class="loading-bar">
                    <div class="loading-progress"></div>
                </div>
                <p class="loading-text">Loading...</p>
            </div>
        </div>

        <!-- Home Screen -->
        <div id="home-screen" class="screen">
            <header class="app-header">
                <div class="header-content">
                    <img src="assets/PCS-Seal.jpg" alt="PCS Academy" class="header-logo">
                    <h1>PCS ACADEMY QUIZ</h1>
                    <nav class="main-nav">
                        <a href="#" onclick="showScreen('quiz-screen')">Start Quiz</a>
                        <a href="#" onclick="showScreen('about-screen')">About</a>
                        <a href="#" onclick="showScreen('contact-screen')">Contact</a>
                        <a href="#" onclick="showScreen('privacy-screen')">Privacy</a>
                    </nav>
                </div>
            </header>

            <main class="home-content">
                <section class="hero-section">
                    <h2>Welcome to PCS Academy Educational Quiz Platform</h2>
                    <p>Test your knowledge across multiple subjects with our interactive quiz system. Learn, practice, and excel with engaging questions designed by educational experts.</p>
                    <button class="cta-button" onclick="showScreen('quiz-screen')">Start Learning Now</button>
                </section>

                <section class="features-grid">
                    <div class="feature-card">
                        <h3>🧮 Mathematics</h3>
                        <p>Enhance your mathematical skills with problems ranging from basic arithmetic to advanced concepts.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔬 Science</h3>
                        <p>Explore the wonders of Physics, Chemistry, Biology, and Earth Science through interactive questions.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📚 General Knowledge</h3>
                        <p>Broaden your understanding of the world with questions covering history, geography, and current affairs.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🏆 Achievement System</h3>
                        <p>Earn badges, track progress, and compete with friends in our comprehensive learning platform.</p>
                    </div>
                </section>
            </main>

            <footer class="app-footer">
                <div class="footer-content">
                    <div class="footer-section">
                        <h4>PCS Academy School</h4>
                        <p>Established 2022 - Excellence in Education</p>
                        <p>📍 Ambah, Madhya Pradesh, India</p>
                    </div>
                    <div class="footer-section">
                        <h4>Contact Information</h4>
                        <p>📞 <a href="tel:+919977365777">+91 9977365777</a></p>
                        <p>📞 <a href="tel:+918269950030">+91 8269950030</a></p>
                        <p>✉️ <a href="mailto:pcsacademyschool@gmail.com">pcsacademyschool@gmail.com</a></p>
                    </div>
                    <div class="footer-section">
                        <h4>Quick Links</h4>
                        <a href="#" onclick="showScreen('privacy-screen')">Privacy Policy</a>
                        <a href="#" onclick="showScreen('terms-screen')">Terms of Service</a>
                        <a href="#" onclick="showScreen('about-screen')">About Us</a>
                        <a href="#" onclick="showScreen('contact-screen')">Contact</a>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p>&copy; 2025 PCS Academy School. All rights reserved.</p>
                </div>
            </footer>
        </div>

        <!-- Quiz Screen -->
        <div id="quiz-screen" class="screen">
            <div class="quiz-container">
                <div class="quiz-header">
                    <button onclick="showScreen('home-screen')" class="back-button">← Back</button>
                    <div class="quiz-info">
                        <span id="question-counter">Question 1 of 10</span>
                        <div class="timer" id="timer">30</div>
                    </div>
                </div>
                
                <div class="quiz-content">
                    <div class="question-container">
                        <h2 id="question-text">Loading question...</h2>
                    </div>
                    
                    <div class="options-container" id="options-container">
                        <!-- Options will be populated by JavaScript -->
                    </div>
                    
                    <div class="quiz-controls">
                        <button id="submit-answer" class="quiz-button">Submit Answer</button>
                        <button id="next-question" class="quiz-button" style="display: none;">Next Question</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- About Screen -->
        <div id="about-screen" class="screen">
            <div class="page-container">
                <div class="page-header">
                    <button onclick="showScreen('home-screen')" class="back-button">← Back to Home</button>
                    <h1>About PCS Academy School</h1>
                </div>
                <div class="page-content">
                    <section class="about-section">
                        <h2>Our Mission</h2>
                        <p>PCS Academy School, established in 2022, is committed to providing quality education through innovative teaching methods and technology-enhanced learning experiences. We believe in nurturing young minds and preparing them for the challenges of tomorrow.</p>
                        
                        <h2>Educational Excellence</h2>
                        <p>Since our establishment, we have rapidly grown to become a leading educational institution in Ambah, Madhya Pradesh. Our comprehensive approach combines traditional teaching methods with modern technology to create an engaging learning environment.</p>
                        
                        <h2>Technology-Enhanced Learning</h2>
                        <p>This quiz application is part of our commitment to digital education. We provide interactive learning tools that make education accessible, engaging, and effective for students of all ages.</p>
                        
                        <h2>Contact Information</h2>
                        <div class="contact-info">
                            <p><strong>Address:</strong> PCS Academy School, Ambah, Madhya Pradesh, India</p>
                            <p><strong>Phone:</strong> +91 9977365777, +91 8269950030</p>
                            <p><strong>Email:</strong> pcsacademyschool@gmail.com</p>
                            <p><strong>Established:</strong> 2022</p>
                        </div>
                    </section>
                </div>
            </div>
        </div>

        <!-- Contact Screen -->
        <div id="contact-screen" class="screen">
            <div class="page-container">
                <div class="page-header">
                    <button onclick="showScreen('home-screen')" class="back-button">← Back to Home</button>
                    <h1>Contact Us</h1>
                </div>
                <div class="page-content">
                    <div class="contact-grid">
                        <div class="contact-info-section">
                            <h2>Get in Touch</h2>
                            <div class="contact-method">
                                <h3>📞 Phone Numbers</h3>
                                <p><a href="tel:+919977365777">+91 9977365777</a></p>
                                <p><a href="tel:+918269950030">+91 8269950030</a></p>
                            </div>
                            <div class="contact-method">
                                <h3>✉️ Email</h3>
                                <p><a href="mailto:pcsacademyschool@gmail.com">pcsacademyschool@gmail.com</a></p>
                            </div>
                            <div class="contact-method">
                                <h3>📍 Address</h3>
                                <p>PCS Academy School<br>Ambah, Madhya Pradesh, India</p>
                            </div>
                            <div class="contact-method">
                                <h3>🕒 Office Hours</h3>
                                <p>Monday - Saturday: 9:00 AM - 3:00 PM<br>Sunday: Closed</p>
                            </div>
                        </div>
                        
                        <div class="contact-form-section">
                            <h2>Send us a Message</h2>
                            <form class="contact-form" action="mailto:pcsacademyschool@gmail.com" method="post" enctype="text/plain">
                                <div class="form-group">
                                    <label for="name">Full Name</label>
                                    <input type="text" id="name" name="name" required>
                                </div>
                                <div class="form-group">
                                    <label for="email">Email Address</label>
                                    <input type="email" id="email" name="email" required>
                                </div>
                                <div class="form-group">
                                    <label for="subject">Subject</label>
                                    <select id="subject" name="subject" required>
                                        <option value="">Select a subject</option>
                                        <option value="Admission Inquiry">Admission Inquiry</option>
                                        <option value="Academic Support">Academic Support</option>
                                        <option value="Technical Issues">Technical Issues</option>
                                        <option value="General Questions">General Questions</option>
                                    </select>
                                </div>
                                <div class="form-group">
                                    <label for="message">Message</label>
                                    <textarea id="message" name="message" rows="5" required></textarea>
                                </div>
                                <button type="submit" class="submit-button">Send Message</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Privacy Policy Screen -->
        <div id="privacy-screen" class="screen">
            <div class="page-container">
                <div class="page-header">
                    <button onclick="showScreen('home-screen')" class="back-button">← Back to Home</button>
                    <h1>Privacy Policy</h1>
                </div>
                <div class="page-content">
                    <div class="policy-content">
                        <p><strong>Last Updated:</strong> October 11, 2025</p>
                        
                        <section>
                            <h2>Introduction</h2>
                            <p>PCS Academy School ("we," "our," or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our educational quiz application.</p>
                        </section>
                        
                        <section>
                            <h2>Information We Collect</h2>
                            <h3>Personal Information</h3>
                            <ul>
                                <li>Name and contact information when you register or contact us</li>
                                <li>Educational progress and quiz performance data</li>
                                <li>Device information and browser details</li>
                                <li>IP address and location data</li>
                            </ul>
                            
                            <h3>Cookies and Tracking Technologies</h3>
                            <p>We use cookies and similar technologies to enhance your experience and analyze website usage. This includes:</p>
                            <ul>
                                <li>Session cookies for website functionality</li>
                                <li>Analytics cookies to understand user behavior</li>
                                <li>Third-party advertising cookies (Google AdSense)</li>
                            </ul>
                        </section>
                        
                        <section>
                            <h2>Third-Party Services</h2>
                            <h3>Google AdSense</h3>
                            <p>We use Google AdSense to display advertisements. Google may use cookies and other technologies to serve ads based on your prior visits to our website or other websites. You can opt out of personalized advertising by visiting Google's Ad Settings.</p>
                            
                            <h3>Analytics</h3>
                            <p>We may use Google Analytics or similar services to analyze website traffic and user behavior to improve our educational services.</p>
                        </section>
                        
                        <section>
                            <h2>How We Use Your Information</h2>
                            <ul>
                                <li>To provide and maintain our educational services</li>
                                <li>To track academic progress and personalize learning experiences</li>
                                <li>To communicate with students, parents, and educators</li>
                                <li>To improve our website and educational content</li>
                                <li>To comply with legal obligations</li>
                            </ul>
                        </section>
                        
                        <section>
                            <h2>Your Rights</h2>
                            <p>Under applicable privacy laws (GDPR, CCPA), you have the right to:</p>
                            <ul>
                                <li>Access your personal data</li>
                                <li>Correct inaccurate information</li>
                                <li>Request deletion of your data</li>
                                <li>Object to data processing</li>
                                <li>Data portability</li>
                            </ul>
                        </section>
                        
                        <section>
                            <h2>Children's Privacy</h2>
                            <p>We comply with COPPA regulations. We do not knowingly collect personal information from children under 13 without parental consent. If we learn that we have collected information from a child under 13, we will delete it promptly.</p>
                        </section>
                        
                        <section>
                            <h2>Contact Us</h2>
                            <p>If you have questions about this Privacy Policy, please contact us:</p>
                            <ul>
                                <li>Email: pcsacademyschool@gmail.com</li>
                                <li>Phone: +91 9977365777, +91 8269950030</li>
                                <li>Address: PCS Academy School, Ambah, Madhya Pradesh, India</li>
                            </ul>
                        </section>
                    </div>
                </div>
            </div>
        </div>

        <!-- Terms of Service Screen -->
        <div id="terms-screen" class="screen">
            <div class="page-container">
                <div class="page-header">
                    <button onclick="showScreen('home-screen')" class="back-button">← Back to Home</button>
                    <h1>Terms of Service</h1>
                </div>
                <div class="page-content">
                    <div class="policy-content">
                        <p><strong>Last Updated:</strong> October 11, 2025</p>
                        
                        <section>
                            <h2>Acceptance of Terms</h2>
                            <p>By accessing and using the PCS Academy Quiz Application, you accept and agree to be bound by the terms and provision of this agreement.</p>
                        </section>
                        
                        <section>
                            <h2>Educational Use</h2>
                            <p>This platform is designed for educational purposes. Users agree to use the quiz application solely for learning and academic improvement.</p>
                        </section>
                        
                        <section>
                            <h2>User Responsibilities</h2>
                            <ul>
                                <li>Provide accurate information when registering</li>
                                <li>Use the platform responsibly and ethically</li>
                                <li>Respect intellectual property rights</li>
                                <li>Not attempt to hack or manipulate the system</li>
                                <li>Not share inappropriate content</li>
                            </ul>
                        </section>
                        
                        <section>
                            <h2>Intellectual Property</h2>
                            <p>All content, including questions, explanations, and educational materials, is the property of PCS Academy School and is protected by copyright laws.</p>
                        </section>
                        
                        <section>
                            <h2>Limitation of Liability</h2>
                            <p>PCS Academy School shall not be liable for any indirect, incidental, special, consequential, or punitive damages resulting from your use of the platform.</p>
                        </section>
                        
                        <section>
                            <h2>Modifications</h2>
                            <p>We reserve the right to modify these terms at any time. Continued use of the platform constitutes acceptance of modified terms.</p>
                        </section>
                        
                        <section>
                            <h2>Governing Law</h2>
                            <p>These terms are governed by the laws of Madhya Pradesh, India.</p>
                        </section>
                        
                        <section>
                            <h2>Contact Information</h2>
                            <p>For questions regarding these terms, contact us at pcsacademyschool@gmail.com or +91 9977365777.</p>
                        </section>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- JavaScript -->
    <script src="app.js"></script>
</body>
</html>'''

with open(f"{project_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created comprehensive index.html")