movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def krutoifilm(dict):
    return True if dict['imdb']>5.5 else False
print(krutoifilm(movies[0]))
#2
def sublist(lst):
    ans = [x['name'] for x in lst if x['imdb']>5.5]
    return ans
print(sublist(movies))
#3
def chetan(movies, category):
    names = []
    for dict in movies:
        if dict["category"] == category:
            names.append(dict['name'])
    return names
print(chetan(movies,"Thriller"))
#4
def avg(movies):
    num = 0
    for dic in movies:
        num+=dic['imdb']
    return num/len(movies)
print(avg(movies))
#5
def cat_avg(movies, cat):
    num = 0
    caunt = 0
    for dic in movies:
        if dic['category'] == cat:
            num+=dic['imdb']
            caunt+=1
    return num/caunt