# Importing Libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Loading datasets
books = pd.read_csv("./dataset/books.csv", sep=";", error_bad_lines=False, encoding="latin-1")
ratings = pd.read_csv("./dataset/ratings.csv", sep=";", error_bad_lines=False, encoding="latin-1")
users = pd.read_csv("./dataset/users.csv", sep=";", error_bad_lines=False, encoding="latin-1")

books.columns = ['ISBN', 'Title', 'Author', 'Year', 'Publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
users.columns = ['userID', 'Location', 'Age']
ratings.columns = ['userID', 'ISBN', 'Rating']


# Cleaning and merging datasets
books.columns = ['ISBN', 'Title', 'Author', 'Year', 'Publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
books['Title'] = books['Title'].apply(str.title)
books.dropna(inplace=True)
books.drop(['imageUrlS', 'imageUrlM', 'imageUrlL'],axis=1,inplace=True)
book_df = ratings.merge(books, on='ISBN')


''' Collaborative Book Recommender System '''

# selecting users who have rated more than 100 books
rating_users = book_df.groupby('userID').count()['Rating'] > 100
rating_users = rating_users[rating_users].index
filtered_rating = book_df[book_df['userID'].isin(rating_users)]

# selecting books with more than 50 ratings
famous_books = filtered_rating.groupby('Title').count()['Rating'] >= 100
famous_books = famous_books[famous_books].index
final_rating = filtered_rating[filtered_rating['Title'].isin(famous_books)]

# Drop duplicates
final_rating.drop_duplicates()

# Applying Pivot Table
matrix = final_rating.pivot_table(index='Title', columns='userID', values='Rating').fillna(0)

# to calculte the same type of books
similarity_score = cosine_similarity(matrix)


def recomendations(book_name):
    # getting the index of the book_name
    index_of_book = np.where(matrix.index == book_name)[0][0]
    
    # getting the indexes of the books that are similar to book_name
    similar_books_index = sorted(list(enumerate(similarity_score[index_of_book])), key= lambda x:x[1], reverse = True)[1:11]
    
    # printing the names of the similar books
    print('\nRecommended books : ')
    for item in similar_books_index:
        book_index = item[0]
        same_type_book = matrix.index[book_index]
        print(f'{same_type_book}')

# recommend_me_books('A Painted House')

# Taking user input for movie name
book_name = input("Enter book name: ")

# Converting movie name to uppercase
x = book_name.title()

# Calling the recommendation function
recomendations(x)