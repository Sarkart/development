#cell 0
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

#cell 1
data = pd.read_csv('movie_bd_v5.csv')
data.head()

#cell 2
data.describe()

#cell 3
# Предобработка

#cell 4
answers = {} # создадим словарь для ответов

# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...

data['release_date'] = pd.to_datetime(data['release_date'])

#add profit column to dataframe

data['profit'] = data.revenue - data.budget

#counter fucntion for calculation in columns, where we have '|' as splitter

def counter(df, x): 
    joined = df[x].str.cat(sep='|')
    splited = pd.Series(joined.split('|'))
    counted = splited.value_counts(ascending=False)
    return counted

#add release_month column

data['release_month'] = pd.to_datetime(data.release_date).apply(lambda x: x.month)

#add title_length column

data['length'] = data.original_title.map(lambda x: len(x) - x.count(' '))

#add overview_words_length column

data['overview_words_length'] = data.overview.map(lambda x: len(x.split(' ')))

#cell 5
# 1. У какого фильма из списка самый большой бюджет?

#cell 6
Использовать варианты ответов в коде решения запрещено.    
Вы думаете и в жизни у вас будут варианты ответов?)

#cell 7
# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
#answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = 'Pirates of the Caribbean: On Stranger Tides (tt1298650)'
# если ответили верно, можете добавить комментарий со значком "+"
#+

#cell 8
# тут пишем ваш код для решения данного вопроса:
max_budget = data[data['budget'] == data['budget'].max()]
print('%s (%s)' % (max_budget['original_title'].iloc[0], max_budget['imdb_id'].iloc[0]))


#cell 9
# 2. Какой из фильмов самый длительный (в минутах)?

#cell 10
# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = 'Gods and Generals (tt0279111)'
#+

#cell 11
max_runtime = data[data['runtime'] == data['runtime'].max()]
print('%s (%s)' % (max_runtime['original_title'].iloc[0], max_runtime['imdb_id'].iloc[0]))


#cell 12
# 3. Какой из фильмов самый короткий (в минутах)?





#cell 13
answers['3'] = 'Winnie the Pooh (tt1449283)'
#+

#cell 14
min_runtime = data[data['runtime'] == data['runtime'].min()]
print('%s (%s)' % (min_runtime['original_title'].iloc[0], min_runtime['imdb_id'].iloc[0]))

#cell 15
# 4. Какова средняя длительность фильмов?


#cell 16
answers['4'] = '110'
#+

#cell 17
round(data['runtime'].mean(), 0)

#cell 18
# 5. Каково медианное значение длительности фильмов? 

#cell 19
answers['5'] = '107'
#+

#cell 20
round(data['runtime'].median(), 0)

#cell 21
# 6. Какой самый прибыльный фильм?
#### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

#cell 22
# лучше код получения столбца profit вынести в Предобработку что в начале
answers['6'] = 'Avatar (tt0499549)'
#+

#cell 23
max_profit = data[data['profit'] == data['profit'].max()]
print('%s (%s)' % (max_profit['original_title'].iloc[0], max_profit['imdb_id'].iloc[0]))

#cell 24
# 7. Какой фильм самый убыточный? 

#cell 25
answers['7'] = 'The Lone Ranger (tt1210819)'
#+

#cell 26
min_profit = data[data['profit'] == data['profit'].min()]
print('%s (%s)' % (min_profit['original_title'].iloc[0], min_profit['imdb_id'].iloc[0]))

#cell 27
# 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

#cell 28
answers['8'] = '1478'

#cell 29
profitable_films = data[data['profit'] > 0].count()
print('%s' % (profitable_films[0]))

#cell 30
# 9. Какой фильм оказался самым кассовым в 2008 году?

#cell 31
answers['9'] = 'The Dark Knight (tt0468569)'

#cell 32
most_rev_2008 = data[(data['release_year'] == 2008)].revenue.idxmax()
print('%s (%s)' % (data['original_title'].iloc[most_rev_2008], data['imdb_id'].iloc[most_rev_2008]))

#cell 33
# 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?


#cell 34
answers['10'] = 'The Lone Ranger (tt1210819)'

#cell 35
least_rev_2012_2014 = data[(data['release_year'] <= 2014) & (data['release_year'] >= 2012)].profit.idxmin()
print('%s (%s)' % (data['original_title'].iloc[least_rev_2012_2014], data['imdb_id'].iloc[least_rev_2012_2014]))

#cell 36
# 11. Какого жанра фильмов больше всего?

#cell 37
# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале
answers['11'] = 'Drama'
#+

#cell 38
counter(data, 'genres')

#cell 39
genres = data['genres'].str.split('|').explode().value_counts()
genres  

#cell 40
ВАРИАНТ 2

#cell 41
genres_1 = data['genres'].str.split('|', expand = True)
genres_1 = genres_1.stack().tolist()
pd.Series(genres_1).value_counts()

#cell 42
# 12. Фильмы какого жанра чаще всего становятся прибыльными? 

#cell 43
answers['12'] = 'Drama'
#+

#cell 44
display(counter(data[data['profit'] > 0], 'genres'))

#cell 45
genre_most_profit = data[data.profit > 0]
genre_most_profit['genres'].str.split('|').explode().value_counts()

#cell 46
# 13. У какого режиссера самые большие суммарные кассовые сбооры?

#cell 47
answers['13'] = 'Peter Jackson'
#+

#cell 48
def director_revenue(df):
    summ = Counter()
    for i in range(len(df)):
        for j in df.iloc[i].director.split('|'):
            summ[j] += df.iloc[i].revenue
    return pd.DataFrame.from_dict(summ, orient='index', columns = ['Summ'])

display(director_revenue(data[data.revenue > 0]).sort_values(by=['Summ'], ascending = False))


#cell 49
# 14. Какой режисер снял больше всего фильмов в стиле Action?

#cell 50
answers['14'] = 'Robert Rodriguez'
#+

#cell 51
def director_action(df):
    summ = Counter()
    for i in range(len(df)):
        for j in df.iloc[i].director.split('|'):
            if 'Action' in df.iloc[i].genres.split('|'):
                summ[j] += 1
    return pd.DataFrame.from_dict(summ, orient='index', columns = ['Summ'])
display(director_action(data[data.revenue > 0]).sort_values(by=['Summ'], ascending = False))

#cell 52
# 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

#cell 53
answers['15'] = 'Chris Hemsworth'
#+

#cell 54
data_2012 = data[data['release_year'] == 2012]
def actor_revenue(df):
    summ = Counter()
    for i in range(len(df)):
        for j in df.iloc[i].cast.split('|'):
            summ[j] += df.iloc[i].revenue
    return pd.DataFrame.from_dict(summ, orient='index', columns = ['Summ'])
display(actor_revenue(data_2012[data_2012.revenue > 0]).sort_values(by=['Summ'], ascending = False))

#cell 55
# 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

#cell 56
answers['16'] = 'Matt Damon'

#cell 57
counter(data[data['budget'] > data['budget'].mean()], 'cast')

#cell 58
# 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

#cell 59
answers['17'] = 'Action'
#+

#cell 60
def cage_films(df):
    summ = Counter()
    for i in range(len(df)):
        for j in df.iloc[i].genres.split('|'):
            if 'Nicolas Cage' in df.iloc[i].cast.split('|'):
                summ[j] += 1
    return pd.DataFrame.from_dict(summ, orient='index', columns = ['Summ'])
display(cage_films(data).sort_values(by=['Summ'], ascending = False))

#cell 61
count_genres = Counter()
for x in data.loc[data['cast'].map(lambda x: True if 'Nicolas Cage' in x else False)]['genres'].str.split('|'):
    count_genres+=Counter(x)
display(count_genres.most_common())

#cell 62
# 18. Самый убыточный фильм от Paramount Pictures

#cell 63
answers['18'] = 'K-19: The Widowmaker (tt0267626)'
#+

#cell 64
data_paramount = data[data.production_companies.str.contains('Paramount Pictures')]
data_paramount = data_paramount[data_paramount.profit == data_paramount.profit.min()]
print('%s (%s)' % (data_paramount['original_title'].iloc[0], data_paramount['imdb_id'].iloc[0]))

#cell 65
# 19. Какой год стал самым успешным по суммарным кассовым сборам?

#cell 66
answers['19'] = '2015'
#+

#cell 67
year_revenue = data.groupby(['release_year']).sum().sort_values('revenue',ascending=False)
display(year_revenue)

#cell 68
# 20. Какой самый прибыльный год для студии Warner Bros?

#cell 69
answers['20'] = '2014'
#+

#cell 70
data_wb = data[data.production_companies.str.contains('Warner Bros')]
data_wb.groupby(['release_year']).sum().sort_values('profit',ascending=False)

#cell 71
# 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

#cell 72
answers['21'] = 'Сентябрь'
#+

#cell 73

data.groupby('release_month').count().sort_values('imdb_id', ascending=False)

#cell 74
# 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

#cell 75
answers['22'] = '450'
#+

#cell 76
summer = data[data.release_month.isin([6, 7, 8])]
summer.groupby('release_month').count().sum().sort_values()

#cell 77
# 23. Для какого режиссера зима – самое продуктивное время года? 

#cell 78
answers['23'] = 'Peter Jackson'
#+

#cell 79
winter = data[data.release_month.isin([12, 1, 2])]
def director_winter(df):
    summ = Counter()
    for i in range(len(df)):
        for j in df.iloc[i].director.split('|'):
            summ[j] += 1
    return pd.DataFrame.from_dict(summ, orient='index', columns = ['Summ'])
display(director_winter(winter).sort_values(by=['Summ'], ascending = False))

#cell 80
# 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

#cell 81
answers['24'] = 'Four By Two Productions'
#+

#cell 82

sum_length=counter(data,'production_companies')
for length in sum_length.index:
    sum_length[length] = data['length'][data['production_companies'].map(lambda x: True if length in x else False)].mean()
sum_length = pd.DataFrame(sum_length).sort_values(0, ascending=False)
sum_length

#cell 83
# 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

#cell 84
answers['25'] = 'Midnight Picture Show'
#+

#cell 85

sum_gen=counter(data,'production_companies')
for gen in sum_gen.index:
    sum_gen[gen] = data['overview_words_length'][data['production_companies'].map(lambda x: True if gen in x else False)].mean()
sum_gen = pd.DataFrame(sum_gen).sort_values(0, ascending=False)
sum_gen

#cell 86
# 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
по vote_average

#cell 87
answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave'

#cell 88
data[data['vote_average']>data.quantile(0.99, numeric_only=True)['vote_average']]

#cell 89
# 27. Какие актеры чаще всего снимаются в одном фильме вместе?


#cell 90
answers['27'] = 'Daniel Radcliffe Rupert Grint'
#+

#cell 91
from itertools import combinations
actor_list = data.cast.str.split('|').tolist()
combo_list=[]
for i in actor_list:
    for j in combinations(i, 2):
        combo_list.append(' '.join(sorted(j)))
combo_list = pd.DataFrame(combo_list)
combo_list.columns = ['actor_combinations']
combo_list.actor_combinations.value_counts().head(10)

#cell 92
ВАРИАНТ 2

#cell 93


#cell 94
# Submission

#cell 95
# в конце можно посмотреть свои ответы к каждому вопросу
answers

#cell 96
# и убедиться что ни чего не пропустил)
len(answers)

#cell 97
data

#cell 98


