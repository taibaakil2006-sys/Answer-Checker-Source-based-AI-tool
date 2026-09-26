import random

QUESTIONS = [
    {"q": "What does ICAI stand for?", "options": ["A) Institute of Certified Accountancy in India", "B) Institute of Chartered Accountants of India", "C) International Chartered Accounting Institute", "D) Indian Certified Accounting Institution"], "correct": "B", "topic": "CA Basics"},
    {"q": "Which body regulates Chartered Accountancy in India?", "options": ["A) Ministry of Finance", "B) ICAI", "C) RBI", "D) SEBI"], "correct": "B", "topic": "CA Basics"},
    {"q": "What is a balance sheet?", "options": ["A) Statement of cash flows", "B) Financial statement showing assets, liabilities, and equity", "C) Record of daily transactions", "D) List of expenses"], "correct": "B", "topic": "CA Basics"},
    {"q": "An income statement shows:", "options": ["A) Cash positions only", "B) Revenues, expenses, gains, and losses", "C) Balance of accounts", "D) Inventory status"], "correct": "B", "topic": "CA Basics"},
    {"q": "What does a cash flow statement track?", "options": ["A) Customer purchases", "B) Employee salaries", "C) Cash movements in and out", "D) Product inventory"], "correct": "C", "topic": "CA Basics"},
    {"q": "The primary role of a CA is:", "options": ["A) Marketing products", "B) Accounting, auditing, taxation, and financial advisory", "C) Manufacturing goods", "D) Sales management"], "correct": "B", "topic": "CA Basics"},
    {"q": "Which financial statement balances?", "options": ["A) Income statement", "B) Cash flow", "C) Balance sheet (Assets = Liabilities + Equity)", "D) Trial balance"], "correct": "C", "topic": "CA Basics"},
    {"q": "Accrual accounting records transactions:", "options": ["A) Only when cash is received", "B) At time of transaction (not cash)", "C) End of year only", "D) Never"], "correct": "B", "topic": "CA Basics"},
    {"q": "What is entrepreneurship?", "options": ["A) Working for a company", "B) Creating economic value and new ventures", "C) Studying business", "D) Managing finances"], "correct": "B", "topic": "Business Fundamentals"},
    {"q": "A business plan typically includes:", "options": ["A) Only profit goals", "B) Goals, methods, and financial projections", "C) Just market research", "D) Only expense data"], "correct": "B", "topic": "Business Fundamentals"},
    {"q": "Customer Acquisition Cost (CAC) means:", "options": ["A) Total revenue", "B) Cost to acquire one customer", "C) Price of products", "D) Marketing budget"], "correct": "B", "topic": "Business Fundamentals"},
    {"q": "What is the main function of accounting?", "options": ["A) Marketing", "B) Recording and analyzing financial data", "C) HR management", "D) Production"], "correct": "B", "topic": "Business Fundamentals"},
    {"q": "Assets in a balance sheet include:", "options": ["A) Only cash", "B) Land, equipment, cash, receivables", "C) Only liabilities", "D) Revenue only"], "correct": "B", "topic": "Financial Statements"},
    {"q": "Liabilities represent:", "options": ["A) What company owns", "B) What company owes (debts)", "C) Profit margins", "D) Customer data"], "correct": "B", "topic": "Financial Statements"},
    {"q": "Equity in a balance sheet is:", "options": ["A) Cash amount", "B) Assets minus Liabilities", "C) Revenue", "D) Expense"], "correct": "B", "topic": "Financial Statements"},
    {"q": "The income statement shows profit by:", "options": ["A) Assets and liabilities", "B) Revenues minus expenses", "C) Cash positions", "D) Inventory counts"], "correct": "B", "topic": "Financial Statements"},
    {"q": "What is a cash flow statement's purpose?", "options": ["A) Show profit", "B) Track cash movement (operating, investing, financing)", "C) Record expenses", "D) List customers"], "correct": "B", "topic": "Financial Statements"},
    {"q": "Depreciation is:", "options": ["A) Loss of customers", "B) Allocation of asset cost over time", "C) Reduction in revenue", "D) Employee turnover"], "correct": "B", "topic": "Financial Statements"},
    {"q": "Machine Learning is:", "options": ["A) Just AI", "B) Systems learning from data without explicit programming", "C) Computer vision only", "D) Only for robots"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Supervised learning requires:", "options": ["A) No data", "B) Labeled data with correct answers", "C) Only text data", "D) Video only"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Unsupervised learning works with:", "options": ["A) Only labeled data", "B) Unlabeled data to discover patterns", "C) Structured data only", "D) Customer feedback"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Neural networks are inspired by:", "options": ["A) Computers", "B) Biological neurons and how they work", "C) Mathematics only", "D) Statistics"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Deep learning uses:", "options": ["A) Few layers", "B) Many layers of neural networks", "C) Only one neuron", "D) No algorithms"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Natural Language Processing (NLP) focuses on:", "options": ["A) Images", "B) Computers understanding and generating human language", "C) Numbers", "D) Graphics"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Computer vision enables machines to:", "options": ["A) Hear sounds", "B) Interpret visual information from images/videos", "C) Read text only", "D) Process audio"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Overfitting occurs when:", "options": ["A) Model underfits", "B) Model learns training data too well including noise", "C) Model is too simple", "D) Model has no layers"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Transfer learning means:", "options": ["A) Moving data", "B) Taking a trained model for one task and adapting for another", "C) Transferring servers", "D) Loading files"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Word embeddings are:", "options": ["A) Documents only", "B) Vector representations capturing word meaning", "C) Grammar rules", "D) Dictionaries"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "Cosine similarity measures:", "options": ["A) Angle between vectors (how similar)", "B) Distance only", "C) Text length", "D) File size"], "correct": "A", "topic": "AI/ML Advanced"},
    {"q": "Transformers in AI use:", "options": ["A) Only basic math", "B) Attention mechanisms for language understanding", "C) Fixed weights", "D) No learning"], "correct": "B", "topic": "AI/ML Advanced"},
    {"q": "What is an MVP?", "options": ["A) Maximum Viable Product", "B) Minimum Viable Product with core features", "C) Marketing Value Proposition", "D) Management Video Plan"], "correct": "B", "topic": "Entrepreneurship"},
    {"q": "Product-market fit means:", "options": ["A) Product is beautiful", "B) Market strongly demands the product actively", "C) High price", "D) Many competitors"], "correct": "B", "topic": "Entrepreneurship"},
    {"q": "An angel investor provides:", "options": ["A) Loans only", "B) Capital to startups for equity/convertible debt", "C) Services", "D) Advice only"], "correct": "B", "topic": "Entrepreneurship"},
    {"q": "Venture capital firms invest in:", "options": ["A) Established companies only", "B) Early-stage companies with high growth potential", "C) Only technology", "D) Nonprofits"], "correct": "B", "topic": "Entrepreneurship"},
    {"q": "A pitch deck includes:", "options": ["A) Only numbers", "B) Problem, solution, market, team, financials", "C) Just slides", "D) Company history"], "correct": "B", "topic": "Entrepreneurship"},
    {"q": "The startup ecosystem includes:", "options": ["A) Only startups", "B) Startups, VCs, angels, mentors, accelerators", "C) Only investors", "D) Government only"], "correct": "B", "topic": "Entrepreneurship"},
    {"q": "Series A funding occurs:", "options": ["A) Before any validation", "B) After product-market fit and readiness to scale", "C) At company end", "D) Never"], "correct": "B", "topic": "Entrepreneurship"},
    {"q": "Burn rate is:", "options": ["A) Revenue", "B) Monthly cash spent beyond revenue", "C) Profit", "D) Salary"], "correct": "B", "topic": "Startup Finance"},
    {"q": "Runway measures:", "options": ["A) Track length", "B) How long startup survives (cash / monthly burn)", "C) Distance", "D) Time to profit"], "correct": "B", "topic": "Startup Finance"},
    {"q": "Series B funding is for:", "options": ["A) Initial idea testing", "B) Scaling after Series A success", "C) Closing business", "D) Small experiments"], "correct": "B", "topic": "Startup Finance"},
    {"q": "Seed funding typically comes from:", "options": ["A) Banks only", "B) Angels, founders, early investors", "C) VCs exclusively", "D) Governments"], "correct": "B", "topic": "Startup Finance"},
    {"q": "Startup valuation considers:", "options": ["A) Only revenue", "B) Growth potential, market size, team", "C) Opinions only", "D) Nothing"], "correct": "B", "topic": "Startup Finance"},
    {"q": "Operating costs for startups include:", "options": ["A) Only salaries", "B) Salaries, rent, software, equipment", "C) Nothing", "D) Only rent"], "correct": "B", "topic": "Startup Finance"},
    {"q": "What does CAC payback period mean?", "options": ["A) Time to make back CAC investment", "B) Customer lifetime", "C) Revenue timing", "D) Profit margin"], "correct": "A", "topic": "Startup Finance"},
    {"q": "Dilution in startups refers to:", "options": ["A) Business shrinking", "B) Founder ownership reduction through funding rounds", "C) Customer loss", "D) Revenue drop"], "correct": "B", "topic": "Startup Finance"},
    {"q": "What is a financial projection?", "options": ["A) Past performance", "B) Forecasted future revenues and expenses", "C) Current balance", "D) Historical data"], "correct": "B", "topic": "Startup Finance"},
]

class QuizMega50:
    def __init__(self):
        self.results = []
        self.score = 0
        self.total = 0
        self.topic_scores = {}
    
    def display_header(self):
        print("\n" + "="*70)
        print("QUIZ v0.5 MEGA - 50 QUESTIONS")
        print("6 Topics: CA, Business, Financial, AI/ML, Entrepreneurship, Startup Finance")
        print("="*70 + "\n")
    
    def run_quiz(self, num_questions):
        self.display_header()
        
        questions = random.sample(QUESTIONS, min(num_questions, len(QUESTIONS)))
        
        print(f"Running {len(questions)} Questions\n")
        
        for i, q in enumerate(questions, 1):
            print(f"Q{i}: {q['q']}")
            for opt in q['options']:
                print(f"  {opt}")
            
            while True:
                answer = input("Your answer (A/B/C/D): ").upper().strip()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                print("Invalid. Enter A, B, C, or D")
            
            is_correct = (answer == q['correct'])
            
            if is_correct:
                self.score += 1
                print("✓ CORRECT!\n")
            else:
                print(f"✗ WRONG! Correct answer: {q['correct']}\n")
            
            self.total += 1
            
            topic = q['topic']
            if topic not in self.topic_scores:
                self.topic_scores[topic] = {'correct': 0, 'total': 0}
            self.topic_scores[topic]['total'] += 1
            if is_correct:
                self.topic_scores[topic]['correct'] += 1
        
        self.display_results()
    
    def display_results(self):
        print("="*70)
        print("QUIZ RESULTS")
        print("="*70)
        
        accuracy = (self.score / self.total * 100) if self.total > 0 else 0
        print(f"\nFinal Score: {self.score}/{self.total}")
        print(f"Accuracy: {accuracy:.1f}%\n")
        
        print("Topic Breakdown:")
        for topic in sorted(self.topic_scores.keys()):
            scores = self.topic_scores[topic]
            topic_acc = (scores['correct'] / scores['total'] * 100) if scores['total'] > 0 else 0
            print(f"  {topic}: {scores['correct']}/{scores['total']} ({topic_acc:.0f}%)")
        
        if accuracy >= 80:
            print(f"\nExcellent! You scored {accuracy:.0f}%! Keep it up!")
        elif accuracy >= 60:
            print(f"\nGood effort! {accuracy:.0f}% - Review weak topics.")
        else:
            print(f"\nMore practice needed. Focus on harder topics.")

def main():
    quiz = QuizMega50()
    
    print("QUIZ MEGA 50 - SELECT MODE")
    print("1) 10 Random Questions")
    print("2) 20 Random Questions")
    print("3) 30 Random Questions")
    print("4) All 50 Questions")
    
    mode = input("\nSelect mode (1-4): ").strip()
    
    mode_map = {'1': 10, '2': 20, '3': 30, '4': 50}
    num_q = mode_map.get(mode, 10)
    
    quiz.run_quiz(num_q)

if __name__ == '__main__':
    main()
