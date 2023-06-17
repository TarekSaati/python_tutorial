class Book:
    def __init__(self, name: str, numPages: int, origin: str):
        self.name = name
        self.numPages = numPages
        self.origin = origin
        self.currentPage = 0

    # each object similar to a book has its own way for navigation
    def navigate(self):
        raise NotImplementedError()

# Magazines share many properties with books => It can inherit from 'Book' class
class Magazine(Book):
    def __init__(self, name: str, numPages: int, author: str, topics: list):
        super().__init__(name, numPages, author)
        self.topics = topics
        self.currentTopic = 'news'

    def navigate(self, pageNum: int, topic: str):
        # make sure that topic is valid using assertion
        assert self.topics.__contains__(topic), 'No such topic'
        self.currentTopic = topic
        self.currentPage = pageNum

book1 = Book('maths', 200, 'Omran')
book2 = Book('History', 150, 'Tarek')
print('name of 1st book is: ', book1.name, ' and currentPage is = ', book1.currentPage)

mag = Magazine('The Guardian', 25, 'USA', ['news', 'sports', 'fashion'])
mag.navigate(5, topic='sports')
print('page: ', mag.currentPage, mag.currentTopic)