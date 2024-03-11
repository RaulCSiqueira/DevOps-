from dataclasses import dataclass

@dataclass
class Book:
    author: str
    topics: list[str]
    rating: int

def book_db(selector: callable):
    books = [
        Book('A K', 'python development'.split(), 4),
        Book('E L', 'lambda development'.split(), 5),
        Book('E L', 'callables development'.split(), 3),
        Book('P A', 'cracks sidewalks'.split(), 2),
        Book('G G', 'grates sidewalks sewers'.split(), 5),
        Book('B R', 'plants oxygen'.split(), 5),
        Book('U F', 'trucks cars vehicles'.split(), 3),
    ]
    
    for book in books:
        if selector(book):
            yield book

def good_development_books():
    return book_db(lambda b: 'development' in b.topics and b.rating > 3)


if __name__ == "__main__":    
    print(list(good_development_books()))