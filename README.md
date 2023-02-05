# Collaborative Filtering Based Book Recommender System

## Introduction
This is a collaborative book recommender system that suggests similar books based on user's reading history and other users' preferences.

## Requirements
To run this recommendation system, you will need the following:

Python 3.9.12
<br />
Pandas
<br />
Numpy
<br />
Scikit-learn 

## Dataset
The system uses 3 datasets: books, users and ratings. The datasets can be downloaded from the given link: https://www.kaggle.com/datasets/saurabhbagchi/books-dataset

## Implementation

The recommendation system is implemented in the brs.py file. The code performs the following steps:

1. Cleaning dataset

2. Selecting users and books with more than 100 books.

3. Applying Pivot Table.

4. Calculate the cosine similarity.

5. Make recoomendations of similar books to the users based on their reading history

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/jhasiddhant/book-recommender-system.git
```
Install the required packages:
```bash
pip install -r requirements.txt
```
Run the brs.py file:
```bash
python brs.py
```
When prompted, enter the name of a book to receive recommendations for book based on users history who have read that book.

## Example:
Enter book name: a painted house

Recommended books :
<br />
The Brethren
<br />
We Were The Mulvaneys
<br />
The Firm
<br />
The Pelican Brief
<br />
Cradle And All
<br />
The Chamber
<br />
The Testament
<br />
The Lovely Bones: A Novel
<br />
The King Of Torts
<br />
Fall On Your Knees
