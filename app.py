import streamlit as st
import pandas as pd
import pickle
import requests
st.title('Movie Recomended sysytem')
import streamlit as st

def fetch_poster(movie_id):

        response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8164db24f71fec1c94f99d2254d845c1'.format(movie_id))
        data=response.json()
        return "https://image.tmdb.org/t/p/w500"+data['poster_path']

def recommend(selected_movie_name):
    movie_index=movies[movies['title']==selected_movie_name].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recomended_movies=[]
    recomended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster
        recomended_movies.append(movies.iloc[i[0]].title)
        recomended_movies_posters.append(fetch_poster(movie_id))
    return recomended_movies,recomended_movies_posters



movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)


if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])



