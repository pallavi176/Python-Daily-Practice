# 1148. Article Views I
# Table: Views
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | article_id    | int     |
# | author_id     | int     |
# | viewer_id     | int     |
# | view_date     | date    |
# +---------------+---------+
# There is no primary key (column with unique values) for this table, the table may have duplicate rows.
# Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
# Note that equal author_id and viewer_id indicate the same person.
# Write a solution to find all the authors that viewed at least one of their own articles.
# Return the result table sorted by id in ascending order.
# The result format is in the following example.
# Example 1:
# Input: 
# Views table:
# +------------+-----------+-----------+------------+
# | article_id | author_id | viewer_id | view_date  |
# +------------+-----------+-----------+------------+
# | 1          | 3         | 5         | 2019-08-01 |
# | 1          | 3         | 6         | 2019-08-02 |
# | 2          | 7         | 7         | 2019-08-01 |
# | 2          | 7         | 6         | 2019-08-02 |
# | 4          | 7         | 1         | 2019-07-22 |
# | 3          | 4         | 4         | 2019-07-21 |
# | 3          | 4         | 4         | 2019-07-21 |
# +------------+-----------+-----------+------------+
# Output: 
# +------+
# | id   |
# +------+
# | 4    |
# | 7    |
# +------+

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df = df[['author_id']].rename(columns={'author_id': 'id'})
    df_unique = df.drop_duplicates(subset='id', keep='first')
    return df_unique.sort_values(by='id', ascending=True)

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views['author_id'] == views['viewer_id']][['author_id']].drop_duplicates().rename(columns={'author_id': 'id'}).sort_values(by='id', ascending=True)

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author_id and viewer_id are the same (authors viewing their own articles)
    authors_viewed_own_articles = views[views['author_id'] == views['viewer_id']]
    
    # Get unique author_ids from the filtered data
    unique_authors = authors_viewed_own_articles['author_id'].unique()
    
    # Sort the unique author_ids in ascending order
    unique_authors = sorted(unique_authors)
    
    # Create a DataFrame with the sorted unique author_ids and rename the 'author_id' column to 'id'
    result_df = pd.DataFrame({'id': unique_authors})
    
    return result_df

