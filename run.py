import re

SOURCES = {
    "seo": (
        "SEO stands for search engine optimization. It is the practice of improving a website "
        "so that it appears higher in search engine results. Good SEO focuses on useful "
        "content, relevant keywords and fast page loading. Search engines reward pages that "
        "answer what people are looking for."
    ),
    "email marketing": (
        "Email marketing means sending messages to people who have agreed to receive them. "
        "A subscriber list is the group of people who signed up to get emails from a business. "
        "Open rate is the percentage of recipients who open an email. Click-through rate is "
        "the percentage of recipients who click a link inside the email."
    ),
    "social media": (
        "Social media marketing uses platforms like Instagram, YouTube and Facebook to reach "
        "customers. Engagement measures how much people like, comment on or share a post. "
        "Reach is the number of unique people who see a post. Impressions count how many times "
        "a post is shown, including repeat views by the same person."
    ),
    "paid ads": (
        "Pay per click advertising charges a business only when someone clicks its ad. Cost per "
        "click is the amount paid for each click on an ad. Conversion rate is the percentage of "
        "visitors who complete a goal, such as buying a product or filling a form. Return on ad "
        "spend shows how much revenue an ad campaign earns for every unit of money spent."
    ),
    "ecommerce": (
        "E-commerce means buying and selling products or services over the internet. A product "
        "page shows a description, price and photos so customers can decide to buy. A shopping "
        "cart holds the items a customer plans to purchase. Cart abandonment happens when a "
        "customer adds items to the cart but leaves without paying."
    ),
}

QUESTIONS = [
    ("What does SEO stand for?", "seo"),
    ("What is open rate?", "email marketing"),
    ("What is a subscriber list?", "email marketing"),
    ("What is engagement?", "social media"),
    ("What is cost per click?", "paid ads"),
    ("What is conversion rate?", "paid ads"),
    ("What is cart abandonment?", "ecommerce"),
    ("What is a shopping cart?", "ecommerce"),
    ("What does impressions mean?", "social media"),
    ("What does the term SEO refer to?", "seo"),
    ("What is the capital of France?", None),
    ("Who won the cricket world cup?", None),
    ("How do I bake a cake?", None),
    ("What is the price of gold?", None),
    ("What is machine learning?", None),
    ("How many people use Instagram?", None),
    ("What is the price of a Facebook ad?", None),
    ("Who invented email?", None),
    ("What is the best time to post on YouTube?", None),
    ("What is blockchain?", None),
    ("What is meant by SEO?", "seo"),
    ("What is a subscriber list in email marketing?", "email marketing"),
    ("Why is social media a distracting platform?", None),
    ("What are the fundamentals of good SEO?", "seo"),
    ("What is email marketing?", "email marketing"),
    ("What is an LLM?", None),
    ("What is ML?", None),
    ("What is data analytics?", None),
    ("Write 5 core elements of email marketing.", None),
]

CURRENT_THRESHOLD = 0.6

STOPWORDS = set(
    (
        "a an and are as at be by can did do does for how i in is it its mean means me my of "
        "on or tell that the this to was were what when where which who whom whose why with "
        "you your"
    ).split()
)


def key_terms(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    terms = set()
    for word in words:
        if len(word) < 2 or word in STOPWORDS:
            continue
        if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
            word = word[:-1]
        terms.add(word)
    return terms


def build_passages():
    passages = []
    for name, text in SOURCES.items():
        sentences = re.split(r"(?<=[.!?])\s+", text)
        for start in range(0, len(sentences), 2):
            passages.append((name, " ".join(sentences[start:start + 2])))
    return passages


def best_match(question, passages):
    question_terms = key_terms(question)
    best_score = 0.0
    best_name = None
    if question_terms:
        for name, text in passages:
            score = len(question_terms & key_terms(text)) / len(question_terms)
            if score > best_score:
                best_score = score
                best_name = name
    return best_name, best_score


def evaluate(matches, threshold):
    counts = {
        "correct answers": 0,
        "wrong answers": 0,
        "correct refusals": 0,
        "wrong refusals": 0,
    }
    mistakes = []
    for question, expected, name, score in matches:
        answered = name is not None and score >= threshold
        if answered and name == expected:
            counts["correct answers"] += 1
        elif answered:
            counts["wrong answers"] += 1
            mistakes.append(f"WRONG ANSWER: {question} -> got {name} ({score:.2f})")
        elif expected is None:
            counts["correct refusals"] += 1
        else:
            counts["wrong refusals"] += 1
            mistakes.append(f"WRONG REFUSAL: {question} ({score:.2f})")
    return counts, mistakes


def main():
    passages = build_passages()
    matches = []
    for question, expected in QUESTIONS:
        name, score = best_match(question, passages)
        matches.append((question, expected, name, score))
    total = len(matches)

    print(f"Questions tested: {total}")
    print()
    print("Thr   Acc   WrongAns  WrongRef")
    for threshold in (0.4, 0.5, 0.6, 0.7, 0.8, 1.0):
        counts, _ = evaluate(matches, threshold)
        correct = counts["correct answers"] + counts["correct refusals"]
        print(
            f"{threshold:.1f}  {correct / total:>4.0%}  "
            f"{counts['wrong answers']:>7}  {counts['wrong refusals']:>8}"
        )

    counts, mistakes = evaluate(matches, CURRENT_THRESHOLD)
    print()
    print(f"Details at threshold {CURRENT_THRESHOLD}")
    for label, count in counts.items():
        print(f"{label}: {count}")
    print()
    print("Mistakes:")
    if not mistakes:
        print("none")
    for mistake in mistakes:
        print(mistake)


main()
