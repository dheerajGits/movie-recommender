import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index= movies[movies['title'] == movie].index[0]
    distances= similarity_array[movie_index] 
    movies_list= sorted(list(enumerate(distances)),reverse=True,key= lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
        

movies_list= pickle.load(open('model/movies_dict.pkl','rb'))
similarity_array= pickle.load(open('model/similarity.pkl','rb'))
movies= pd.DataFrame(movies_list)
st.title('Movie Recommender System')

selected_movie= st.selectbox("Select the movie to be get recommendations",movies['title'].values)

if st.button('Recommend'):
    recommendations= recommend(selected_movie )
    for i in recommendations: 
        st.write(i)