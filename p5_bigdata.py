import pandas as pd
import os
from datetime import datetime


def howmany_user():
    path1 = os.path.join(root_dir, 'tags.csv')
    path2 = os.path.join(root_dir, 'ratings.csv')
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)
    user1 = list(df1['userId'].unique())
    user2 = list(df2['userId'].unique())
    user = user1+user2
    user_set = set(user)
    nums_user = len(user_set)
    return nums_user


def howmany_movie():
    path = os.path.join(root_dir, 'movies.csv')
    df = pd.read_csv(path)
    nums_movie = df['movieId'].count()
    return nums_movie


def howmany_type_movie():
    path = os.path.join(root_dir, 'movies.csv')
    df = pd.read_csv(path)
    genres_movie = df['genres'].str.split('|')
    nums_type = []
    for v in genres_movie:
        if '(' in v[0]:
            continue
        nums_type += v
    type_set = set(nums_type)
    return len(type_set)


def howmany_nolink():
    path = os.path.join(root_dir, 'links.csv')
    df = pd.read_csv(path)
    t0 = df['imdbId'].count()
    t1 = df['tmdbId'].count()
    return t0-t1


def howmany_rate_user():
    path = os.path.join(root_dir, 'ratings.csv')
    df = pd.read_csv(path)
    df['year'] = pd.to_datetime(df['timestamp'], unit='s').dt.year
    df_2018 = df[df['year']==2018]
    # print(df_2018)
    num = df_2018['year'].count()
    return num


if __name__ == '__main__':
    root_dir = r'E:\work\ZYBank\Study\prestudy\data\ml-25m'
    files = os.listdir(root_dir)
    # print(files)
    nums_user = howmany_user()
    nums_movie = howmany_movie()
    nums_movie_type = howmany_type_movie()
    nums_nolink = howmany_nolink()
    nums_2018 = howmany_rate_user()
    print("一共有{}不同的用户".format(nums_user))
    print("一共有{}不同的电影".format(nums_movie))
    print("一共有{}不同的电影种类".format(nums_movie_type))
    print("一共有{}电影没有外部链接".format(nums_nolink))
    print("2018年一共有{}人进行过电影评分".format(nums_2018))
