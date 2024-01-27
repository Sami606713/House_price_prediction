import streamlit as st
from utils import read_data,load_image,load_model,load_tailwind
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
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

    with st.container(border=True,height=None):
        col1,col2,col3,col4=st.columns(4)
        with col1:
            logo,title=st.columns(2)
            with logo:
                img=load_image()
                st.image(img, output_format="JPEG", width=100)
            with title:
                st.markdown(
                """
                <h1 class='bg-blue text-center text-black font-bold font-serif text-xl'>US House title</h1>

                """,
                unsafe_allow_html=True
                )
        with col2:
            with st.container(border=True):
                st.markdown(
                        f"""
                        <h2 class='bg-blue text-center text-black font-bold font-serif text-xl'>Total Record</h2>

                        <h3 class='bg-blue text-center text-red-500 font-bold font-serif text-xl'>{df.shape[0]}</h3>

                        """,
                        unsafe_allow_html=True
                    )
        with col3:
            with st.container(border=True):
                st.markdown(
                        f"""
                        <h2 class='bg-blue text-center text-black font-bold font-serif text-xl'>Total Cities</h2>

                        <h3 class='bg-blue text-center text-green-500 font-bold font-serif text-xl'>{df["city"].nunique()}</h3>

                        """,
                        unsafe_allow_html=True
                    )
        with col4:
            with st.container(border=True):
                st.markdown(
                        f"""
                        <h2 class='bg-blue text-center text-black font-bold font-serif text-xl'>Country</h2>

                        <h3 class='bg-blue text-center text-yellow-500 font-bold font-serif text-xl'>{df["country"].unique()[0]}</h3>

                        """,
                        unsafe_allow_html=True
                    )
    
    with st.container(border=True,height=None):
        # filter_data=st.columns(1)
        with st.container():
            # st.title("Add Filter")
            select_filter=st.selectbox("",["All"]+sorted(df["city"].unique().tolist()))
            
            if(select_filter=="All"):
                filter_data=df
            else:
                filter_data=df[df["city"]==select_filter]
            
        col1,col2=st.columns(2)
        with col1:
            select_col,graph=st.columns(2)
            with select_col:
                select_col=st.selectbox("",filter_data[["price","sqft_total"]].columns)
            with graph:
                graph=st.selectbox("",["Histogram","Density Plot","BoxPlot"])
            
            with st.container():
                if select_col and graph=="Histogram":
                    fig, ax = plt.subplots()
                    fig = px.histogram(filter_data, x=select_col, nbins=50, title="Histogram")
                    st.plotly_chart(fig)
            
                elif select_col and graph=="Density Plot":
                    fig, ax = plt.subplots()
                    sns.kdeplot(filter_data[select_col],palette="deep")
                    plt.title(select_col)
                    st.pyplot(fig) 

                elif select_col and graph=="BoxPlot":
                    fig, ax = plt.subplots()
                    sns.boxplot(df[select_col],palette="deep")
                    fig = px.box(filter_data, y=select_col, title="Histogram")
                    st.plotly_chart(fig)
                    # plt.title(select_col)     
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
                    sns.countplot(data=filter_data,x=select_col)
                    st.pyplot(fig) 
                elif select_col and graph == "Pie Chart":
                    # Create a bar plot using Seaborn
                    fig, ax = plt.subplots()
                    # plt.pie(filter_data[select_col].value_counts(),labels=filter_data[select_col].value_counts().index,autopct="%.2f")
                    fig = px.pie(filter_data, names=select_col, title="Pie Chart")
                    st.plotly_chart(fig)


    with st.container(border=True,height=None):
        fig,axis=plt.subplots()
        fig.set_size_inches(20, 5)
        plt.title("Relation b/w Price and Area")
        sns.lineplot(x="sqft_total",y="price",data=filter_data,color="red") 
        st.pyplot(fig)