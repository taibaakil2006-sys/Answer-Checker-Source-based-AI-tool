import re

SOURCES = {
    "seo": (
        "SEO stands for search engine optimization. It is the practice of improving "
        "a website so that it appears higher in search engine results. Good SEO "
        "focuses on useful content, relevant keywords and fast page loading."
    ),
    "email marketing": (
        "Email marketing means sending messages to people who have agreed to receive them. "
        "A subscriber list is the group of people who signed up to get emails from a business. "
        "Open rate is the percentage of recipients who open an email."
    ),
    "social media": (
        "Social media marketing uses platforms like Instagram, YouTube and Facebook to reach "
        "customers. Engagement measures how much people like, comment on or share a post."
    ),
}

THRESHOLD = 0.6

STOPWORDS = set(
    "a an and are as at be by can do does for how i in is it its of on or "
    "that the this to was were what when where which who why with you your".split()
)


def key_terms(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {
        word[:-1] if len(word) > 3 and word.endswith("s") else word
        for word in words
        if len(word) >= 2 and word not in STOPWORDS
    }


def find_answer(question):
    question_terms = key_terms(question)

    best_name = None
    best_score = 0

    for name, text in SOURCES.items():
        source_terms = key_terms(text)

        if question_terms:
            score = len(question_terms & source_terms) / len(question_terms)

            if score > best_score:
                best_score = score
                best_name = name

    if best_name
