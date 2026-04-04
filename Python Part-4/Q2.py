class Book:
    def __init__(self, title, author, review_list):
        self.title = title
        self.author =author
        self.review_list = review_list

    def addNewReview(self, newReview):
        self.review_list.append(newReview)

    def countReview(self):
        print(f"No. of Review: {len(self.review_list)}")

    def displayAllReviews(self):
        print("List of Reviews :")
        for i in self.review_list:
            print(f"{i}")


oxford = Book("DSA", "Reema Thareja", ["It's a nice book"])
oxford.addNewReview("It's well representated")
oxford.countReview()
oxford.displayAllReviews()