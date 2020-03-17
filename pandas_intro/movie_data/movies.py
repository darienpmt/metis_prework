import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pass in column names for each csv
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5), encoding='latin-1')

# create one merged DataFrame
movie_ratings = pd.merge(movies,ratings)
lens = pd.merge(movie_ratings, users)

# which movies have been rated the most? (print most_rated)
most_rated = lens.groupby('title').size().sort_values(ascending=False)
# or, more simply, print statement below
lens.title.value_counts()[:25]

# which movies are most highly rated?
movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean, 'median']}) # this tells us to apply the size, mean and median functions to the rating data of each group
# sort by rating average
movie_stats.sort_values([('rating','mean')], ascending=False).head() # we must pass a tuple in sorted_values because the columns are now multi-indexed (first rating, then size, mean or median)
# the movies returns in the df above have been reviewed so few times, lets only look at ones which have been reviewed at least 100 times

atleast_100 = movie_stats['rating']['size'] > 100 # using boolean indexing to filter the movie_stats df
movie_stats[atleast_100].sort_values([('rating', 'mean')], ascending=False)[:15]

# for the remainder, lets only at the 50 most rated movies
most_50 = lens.groupby('movie_id').size().sort_values(ascending=False)[:50]

# which movies are most controversial across different age groups? first, lets look at the distributions of ages
# users.age.plot.hist(bins=30)
# plt.title("Distribution of users' ages")
# plt.ylabel("count of users")
# plt.xlabel('age') 
# plt.show()

# binning together users by age group
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
lens['age_group'] = pd.cut(lens.age, range(0, 81, 10), right=False, labels=labels) # this adds a new 'age_group' column to the lens df
lens[['age', 'age_group']].drop_duplicates()[:10]

# now we can compare ratings across age groups
lens.groupby('age_group').agg({'rating': [np.size, np.mean]})
# the youngins' seem most critical. now let's look at how the top 50 most reviewed movies are viewed across agegroups
lens.set_index('movie_id', inplace=True) # sets the index as 'movie_id'
by_age = lens.loc[most_50.index].groupby(['title', 'age_group']) 
by_age.rating.mean().head(15)

# now we can view the series above as a table by using 'unstack'
by_age.rating.mean().unstack(level=-1).fillna(0)[:15] # groupby by default turns the grouped field into a multi-level index (if you use two fields to group)

# which movies do men and women disagree on?
lens.reset_index('movie_id', inplace=True) # resets the index to the default which is a range of numbers 0 to 10,000

pivoted = lens.pivot_table(index=['movie_id', 'title'], columns=['sex'], values='rating', fill_value=0)
pivoted['diff'] = pivoted.M - pivoted.F

# resetting the index for pivoted df because above we set it to be multi-index ('movie_id' then 'title') now the index is the default, which is 'title'
pivoted.reset_index('movie_id', inplace=True)

disagreements = pivoted[pivoted.movie_id.isin(most_50.index)]['diff'] # for the movies that are in the top 50 most reviewed, return the diff data from above
# disagreements2 = pivoted.loc[most_50.index]['diff'] This is equivalent to above but we need to keep the index as 'movie_id' as opposed to the deault 'title'
disagreements.sort_values().plot(kind='barh')
plt.title('Male vs. Female Avg. Ratings\n(Difference > 0 = Favored by Men)')
plt.ylabel('Title')
plt.xlabel('Average Rating Difference')
#plt.show()
























