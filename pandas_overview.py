# Getting Pandas: virtual env + pip install pandas

import pandas as pd
import matplotlib.pyplot as plt

def hip_plot(vector, term):
    """Prints barplot in bash"""

    print '\nSummary statistics for {} frequencies: '.format(term)
    print vector.describe()
    print 'Set of values: '
    print list(vector)


def print_stats(df):
    """ Prints statistics for a given dataframe"""

    print df.dtypes # df.describe()

# downnload initial data set
lines = open('out.txt')

data = []

for line in lines:
    data.append([ln.strip() for ln in line.split('|')]);


print len(data), "lines loaded"

# creating pandas data frame for further manipulations
# link - http://www.jeannicholashould.com/tidy-data-in-python.html

# movie_id | title | released_at | release_year | imdb_url | rating_id |
# movie_id | user_id | score | user_id | email | password | age | zipcode

labels=[
            'movie_id_1', 'title', 'released_at',
            'release_year', 'imdb_url', 'rating_id',
            'movie_id_2', 'user_id_1', 'score',
            'user_id_2', 'email', 'password',
            'age', 'zipcode'
            ]

df = pd.DataFrame.from_records(data, columns=labels)

# check basic statistics of dataframe
# link - https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html

print "\ndataframe with the following columns created"
print_stats(df)

# little cleansing  
# link - https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe

df.drop('user_id_2', axis=1, inplace=True) # 0 for rows and 1 for columns
df.drop('movie_id_2', axis=1, inplace=True) # inplace allows to delete the column without having to reassign df

# and renaming

df = df.rename(columns={'movie_id_1': 'movie_id', 'user_id_1': 'user_id'})

# check e result
print "\ndataframe after cleansing"
print_stats(df)

# subsetting and extracting data

print "\nsubsetting and extracting data"
# The goal is to split dataset to 3 tables and save them 
# into file to be downloaded into database

# extract users table - 
#   user_id, age, zipcode, login, password
users_data = df[['user_id', 'age', 'zipcode', 'email', 'password']].drop_duplicates()
print '\nusers data: ', len(users_data)

# extract movies data - movie_id, title, released_at, release_year, imdb_url

movies_data = df[['movie_id', 'title', 'released_at', 'release_year', 'imdb_url']].drop_duplicates()
print '\nmovies data: ', len(movies_data)

# extract ratings - rating_id, movie_id, user_id, score

ratings_data = df[['rating_id', 'movie_id', 'user_id', 'score']].drop_duplicates()
print '\nratings data: ', len(ratings_data)

# basic statistics

df[['release_year','score', 'age']] = df[['release_year','score', 'age']].apply(pd.to_numeric)

print df["score"].describe()

print_stats(df)

# basic analysis for numeric columns
print df.describe().transpose()

hip_plot(users_data["age"].value_counts(), 'age')

plt.figure();
users_data = users_data[0:-1]

# users_data["age"].plot.bar(); plt.axhline(0, color='k')
plt.scatter(users_data['user_id'], users_data['age'])
plt.show()

# how to create learning vectors for users 

raw_data = pd.DataFrame(index=[user_id for user_id in users_data.user_id], 
                columns=[movie_id for movie_id in movies_data.movie_id])

print raw_data.shape
print raw_data['242']['936']
print "Access element - raw_data['242']['936']"


users_data["age_plus"] = users_data["age"] + " well yeah"

print users_data["age_plus"]

# for(line in df):

