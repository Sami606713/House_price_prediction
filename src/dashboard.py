import streamlit as st
from utils import read_data,load_image,load_model,load_tailwind
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import plotly.figure_factory as ff
import seaborn as sns

# Streamlit app page config
# st.set_page_config(page_title="Dashboard", page_icon=":house:", layout="wide")

def dashboard():
    load_tailwind()
    df=read_data("src/Notebook/clean_data.csv")
    st.markdown(
        """
        <h1 class='text-center text-darkblue font-bold font-serif text-4xl'>US House Dashboard</h1>
       """,
        unsafe_allow_html=True
        )

    # with st.container():
        # st.dataframe(df.head(5))

    with st.container(border=True,height=None):
        col1,col2,col3,col4=st.columns(4)
        with col1:
            logo,title=st.columns(2)
            with logo:
                img=load_image()
                st.image(img, output_format="JPEG", width=80)
            with title:
                st.markdown(
                """
                <h1 class='bg-blue text-center text-black font-bold font-serif text-xl'>US House title</h1>

                """,
                unsafe_allow_html=True
                )
        with col2:
            st.title("val1")
        with col3:
            st.title("val2")
        with col4:
            st.title("val3")
    
    with st.container(border=True,height=None):
    
        col1,col2=st.columns(2)
        with col1:
            select_col,graph=st.columns(2)
            with select_col:
                select_col=st.selectbox("",df[["price","sqft_total"]].columns)
            with graph:
                graph=st.selectbox("",["Histogram","Density Plot","BoxPlot"])
            
            with st.container():
                if select_col and graph=="Histogram":
                    fig, ax = plt.subplots()
                    sns.histplot(df[select_col], bins=20,palette="deep",color="skyblue", edgecolor="black")
                    plt.title(select_col)

                    st.pyplot(fig) 
                elif select_col and graph=="Density Plot":
                    fig, ax = plt.subplots()
                    sns.kdeplot(df[select_col],palette="deep")
                    plt.title(select_col)
                    st.pyplot(fig) 

                elif select_col and graph=="BoxPlot":
                    fig, ax = plt.subplots()
                    sns.boxplot(df[select_col],palette="deep")
                    plt.title(select_col)
                    st.pyplot(fig)       
        with col2:
            select_col,graph=st.columns(2)
            with select_col:
                select_col=st.selectbox("",df[["bedrooms","bathrooms","floors","view","waterfront"]].columns)
            with graph:
                graph=st.selectbox("",["Barplot","Pie Chart"])
            
            with st.container():
                if select_col and graph == "Barplot":
                    # Create a bar plot using Seaborn
                    fig, ax = plt.subplots()
                    sns.countplot(x=df[select_col], palette="pastel", edgecolor="black")
                    plt.title(select_col)

                    st.pyplot(fig)
                elif select_col and graph == "Pie Chart":
                    # Create a bar plot using Seaborn
                    fig, ax = plt.subplots()
                    plt.pie(df[select_col].value_counts(),labels=df[select_col].value_counts().index,autopct="%.2f")
                    # plt.title(select_col)

                    st.pyplot(fig)


    # with st.container(border=True,height=None):
        
    #     fig,axis=plt.subplots()
    #     fig.set_size_inches(20, 5)
    #     plt.title("Relation b/w Price and Area")
    #     sns.lineplot(x="sqft_total",y="price",data=df,color="red") 
    #     st.pyplot(fig) 