import streamlit as st
import pickle

movies_list= pickle.load(open('model/movies.pkl','rb'))
st.title('Movie Recommender System')

option= st.selectbox("Select the movie to be get recommendations",('Email','Phone','Home Phone'))
