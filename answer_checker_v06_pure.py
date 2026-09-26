SOURCES = {
    'ai_ml.txt': (
        'Machine Learning is a subset of Artificial Intelligence where systems learn from data without being explicitly programmed. '
        'Artificial Intelligence is a broad field that aims to create machines capable of performing tasks that typically require human intelligence. '
        'Supervised learning requires labeled data where each example has a correct answer provided during training. '
        'Unsupervised learning works with unlabeled data and aims to discover hidden patterns or structure within it. '
        'A neural network is inspired by how biological neurons work and consists of interconnected layers of artificial neurons. '
        'Deep learning uses neural networks with many layers to learn hierarchical representations of data. '
        'Natural Language Processing is the field focused on enabling computers to understand, interpret, and generate human language. '
        'Computer vision is the discipline that enables machines to interpret and understand visual information from images and videos. '
        'Training a machine learning model involves feeding it labeled data and adjusting its internal parameters to minimize prediction errors. '
        'Overfitting occurs when a model learns the training data too well including its noise, causing poor performance on new data. '
        'A Large Language Model is trained on vast amounts of text data and learns to predict the next word in a sequence. '
        'Transformers are a neural network architecture using attention mechanisms that has become the foundation for modern language models. '
        'Word embeddings are vector representations of words that capture semantic meaning and relationships. '
        'Cosine similarity measures the angle between two vectors to determine how similar they are. '
        'Transfer learning involves taking a model trained on one task and adapting it for a different but related task. '
    ),
    'ca_business.txt': (
        'Chartered Accountancy is a prestigious profession dedicated to accounting, auditing, taxation, and financial planning regulated by ICAI. '
        'The Institute of Chartered Accountants of India (ICAI) is the national professional accounting body responsible for regulating CA profession. '
        'CAs handle accounting and auditing financial records, offer taxation advice, provide financial advisory services, and ensure compliance. '
        'A balance sheet is a financial statement that presents a company\'s financial position by listing assets, liabilities, and equity. '
        'The income statement is a financial report showing revenues, expenses, gains, and losses during a specific period. '
        'The cash flow statement shows how cash moves in and out during an accounting period, tracking operating and investing activities. '
        'Entrepreneurship is the creation of economic value and the process of identifying business opportunities and creating new ventures. '
        'A business plan is a formal written document containing business goals, methods for attaining goals, and financial projections. '
        'An angel investor is an individual who provides capital to startups usually in exchange for convertible debt or ownership equity. '
        'Venture capital is private equity financing provided by VC firms to early-stage companies in exchange for an ownership stake. '
        'Burn rate is the monthly rate at which a startup spends cash reserves beyond its revenue. '
        'Runway is calculated as cash on hand divided by monthly net burn rate and shows how long a startup can survive. '
        'Series A funding is provided by venture capitalists to companies after they demonstrate product-market fit and are ready to scale. '
        'Product-market fit occurs when a startup\'s product satisfies strong market demand and customers actively want and use it. '
        'An MVP is the Minimum Viable Product with just enough features to satisfy early adopters and validate the core business idea. '
    ),
    'marketing.txt': (
        'Email marketing is a direct communication channel allowing businesses to send targeted messages to opted-in subscribers. '
        'A subscriber list is a database of email addresses from people who have opted in to receive communications. '
        'Segmentation divides an email list into groups based on demographics, behavior, or interests for targeted campaigns. '
        'Social media marketing leverages platforms like Facebook, Instagram, Twitter to reach audiences and build communities. '
        'Organic reach refers to free visibility from posting content while paid reach requires advertising spend. '
        'Engagement metrics include likes, comments, shares, and follows showing audience interest and interaction. '
        'Search Engine Optimization (SEO) is the process of improving a website to increase its visibility in search results. '
        'SEO involves optimizing web content, structure, and metadata to rank higher for relevant keywords. '
        'Content quality is critical for SEO performance as search engines prioritize helpful, original, and comprehensive content. '
        'Paid advertising includes Google Ads, Facebook Ads, and programmatic display advertising across the internet. '
        'Pay-per-click (PPC) advertising charges advertisers only when someone clicks their ad. '
        'Cost-per-thousand-impressions (CPM) advertising charges based on ad views regardless of clicks or conversions. '
        'Landing page optimization increases conversion rates by removing friction and clearly stating value propositions. '
        'Retargeting ads follow users across the web after they visit your site reminding them of products or services. '
        'A/B testing compares two versions to determine which elements perform better with audiences. '
    ),
}

class SimpleEmbedding:
    def __init__(self):
        self.word_freq = {}
        self.vocab = {}
        self._build_vocabulary()
    
    def _build_vocabulary(self):
        all_text = ' '.join([text for text in SOURCES.values()])
        words = all_text.lower().split()
        
        for word in words:
            clean_word = ''.join(c for c in word if c.isalpha())
            if clean_word:
                self.word_freq[clean_word] = self.word_freq.get(clean_word, 0) + 1
        
        for i, word in enumerate(sorted(self.word_freq.keys())):
            self.vocab[word] = i
    
    def encode(self, text):
        text_lower = text.lower()
        words = text_lower.split()
        
        vector = [0.0] * len(self.vocab)
        count = 0
        
        for word in words:
            clean_word = ''.join(c for c in word if c.isalpha())
            if clean_word in self.vocab:
                vector[self.vocab[clean_word]] += 1.0
                count += 1
        
        if count > 0:
            vector = [v / count for v in vector]
        
        mag = sum(v * v for v in vector) ** 0.5
        if mag > 0:
            vector = [v / mag for v in vector]
        
        return vector

embedding_model = SimpleEmbedding()

def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    return dot_product

def get_answer_semantic(question, threshold=0.45):
    question_embedding = embedding_model.encode(question)
    
    best_score = 0
    best_passage = None
    best_source = None
    
    for source_name, source_text in SOURCES.items():
        sentences = [s.strip() for s in source_text.split('.') if s.strip()]
        
        for i in range(0, len(sentences), 2):
            if i + 1 < len(sentences):
                passage = sentences[i] + '. ' + sentences[i + 1] + '.'
            else:
                passage = sentences[i] + '.'
            
            passage_embedding = embedding_model.encode(passage)
            similarity = cosine_similarity(question_embedding, passage_embedding)
            
            if similarity > best_score:
                best_score = similarity
                best_passage = passage
                best_source = source_name
    
    if best_score >= threshold:
        return f"✓ {best_passage}\n[Source: {best_source}]\n[Confidence: {best_score:.2f}]"
    else:
        return f"✗ I don't know. The sources don't cover this.\n[Max confidence found: {best_score:.2f}]"

class AnswerCheckerV06:
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def display_header(self):
        print("\n" + "="*70)
        print("ANSWER-CHECKER v0.6 - SEMANTIC SEARCH (PURE PYTHON)")
        print("Embeddings + Cosine Similarity - NO EXTERNAL DEPENDENCIES")
        print("="*70 + "\n")
    
    def run_interactive(self):
        self.display_header()
        threshold = 0.45
        
        print("Mode: Interactive Q&A\n")
        
        while True:
            print("Ask a question (or 'quit' to exit, 'threshold N' to change):")
            user_input = input("> ").strip()
            
            if user_input.lower() == 'quit':
                print("\nGoodbye!")
                break
            
            if user_input.lower().startswith('threshold'):
                parts = user_input.split()
                if len(parts) == 2:
                    try:
                        threshold = float(parts[1])
                        print(f"Threshold set to {threshold}\n")
                    except:
                        print("Invalid. Use: threshold 0.45\n")
                continue
            
            if not user_input:
                continue
            
            answer = get_answer_semantic(user_input, threshold)
            print(f"\n{answer}\n")

    def run_evaluation(self):
        self.display_header()
        
        test_cases = [
            ("What is machine learning?", True, "ai_ml.txt"),
            ("Explain supervised learning", True, "ai_ml.txt"),
            ("What is a neural network?", True, "ai_ml.txt"),
            ("Why is social media distracting?", False, None),
            ("What is email marketing?", True, "marketing.txt"),
            ("Explain SEO", True, "marketing.txt"),
            ("What does a CA do?", True, "ca_business.txt"),
            ("What is a balance sheet?", True, "ca_business.txt"),
            ("What is venture capital?", True, "ca_business.txt"),
            ("How many people use Instagram?", False, None),
        ]
        
        print("Running 10 Evaluation Questions...\n")
        
        for i, (question, should_answer, expected_source) in enumerate(test_cases, 1):
            answer = get_answer_semantic(question, threshold=0.45)
            
            has_answer = answer.startswith("✓")
            is_correct = has_answer == should_answer
            
            if is_correct:
                self.score += 1
            self.total += 1
            
            status = "✓" if is_correct else "✗"
            print(f"{status} Q{i}: {question}")
            print(f"   Expected: {'Answer' if should_answer else 'Refuse'}")
            print(f"   Got: {'Answer' if has_answer else 'Refuse'}")
            print(f"   Result: {answer[:60]}...\n")
        
        print("="*70)
        print("EVALUATION SUMMARY")
        print("="*70)
        accuracy = (self.score / self.total * 100) if self.total > 0 else 0
        print(f"Score: {self.score}/{self.total}")
        print(f"Accuracy: {accuracy:.1f}%")
        print("\nv0.6 Pure Python Features:")
        print("✓ Semantic understanding (word frequency embeddings)")
        print("✓ Cosine similarity matching")
        print("✓ NO numpy/sklearn needed")
        print("✓ Works in Pydroid 3!")
        print("✓ Trustworthy AI complete!")

def main():
    checker = AnswerCheckerV06()
    
    print("ANSWER-CHECKER v0.6 (PURE PYTHON)")
    print("1) Interactive Q&A")
    print("2) Evaluation (10 questions)")
    mode = input("\nSelect: ").strip()
    
    if mode == '2':
        checker.run_evaluation()
    else:
        checker.run_interactive()

if __name__ == '__main__':
    main()
