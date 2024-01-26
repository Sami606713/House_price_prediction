import streamlit as st
from utils import read_data,load_image,load_model,load_tailwind
import numpy as np
import pandas as pd
from dashboard import dashboard
# import plotly.figure_factory as ff

# Streamlit app page config
st.set_page_config(page_title="House Price Prediction", page_icon=":house:", layout="wide")

def prediction():
    # load the tailwind css for styling
    # make a navbar fun 
    load_tailwind()
    # set the title
    st.markdown(
        """
        <h1 class='text-center text-darkblue font-bold font-serif text-4xl'>US House Price Prediction</h1>
       """,
        unsafe_allow_html=True
        )
    st.markdown(
        """
        :red[House] :orange[Price] :green[Prediction]
        """
    )
    # make a main cntainer inside the main container make two left and right columns
    with st.container(border=True):
        # make two columns
        left_col,right_col=st.columns(2)

        # call the left container fun
        left_container(left_col)
        
        # call the right container
        right_container(right_col)

def left_container(left_col):
    with left_col:
        img=load_image()
        # set the image
        st.image(img, output_format="JPEG", width=None, caption="House Image")

def right_container(right_col):
    with right_col:
        try:
            # call the make form fun to make a form with different fields
            make_form()

        except:
            st.error("Some thing went wrong")

def make_form():
    # Make a form
    with st.form("House Predict Form"):      
        # Add a text input field
        area=st.number_input("Enter Area in foot", format="%d",min_value=100)
                    
        # Load the dataset
        df=read_data("src/Notebook/clean_data.csv")
                    
        bed,bath,floor=st.columns(3)
        with bed:
        # Bedrooms
            bedroom=st.selectbox("Bedrooms", sorted(df[df["bedrooms"]>0]["bedrooms"].unique()))
                
        # Bath
        with bath:
            bathroom=st.selectbox("bath", sorted(df[df["bathrooms"]>0]["bathrooms"].unique()))
        
        # Floor  
        with floor:
            floors=st.selectbox("floor", sorted(df[df["floors"]>0]["floors"].unique()))
                

        view,water=st.columns(2)
        with view:
            views=st.selectbox("view", sorted(df[df["view"]>0]["view"].unique()))
        
        with water:
            water_front=st.selectbox("waterfront", sorted(df["waterfront"].unique()))

                    # Use st.selectbox to create a dropdown
        count,city=st.columns(2)
        with count:
            country=st.selectbox("location", df["country"].unique())
        with city:
            selected_city = st.selectbox("location", df["city"])

                    # form submit button
        if(st.form_submit_button("Estimate Price")):
                        
                        # get the values and make a dataframe b/c columns transformer espect dataframe not a numpy array
            df = pd.DataFrame({
                        'bedrooms': [bedroom],
                        'bathrooms': [bathroom],
                        'floors': [floors],
                        'waterfront': [water_front],
                        'view': [views],
                        'city': [selected_city],
                        'country': [country],
                        'sqft_total': [area]
                        })
                        # load the model
            model=load_model("src/Model/house.pkl")
                        
                        # st.dataframe(df)
            pred=model.predict(df)
            success=st.success(f"House preice is {pred[0].round()}")

def main():
    navbar_classes = "bg-gray-500 text-white p-4 rounded border border-white-500"
    nav_item_classes = "mr-4 hover:text-white cursor-pointer"

    # Add a navigation menu in the navbar
    st.markdown(
    f"""
    <div class="{navbar_classes} text-center text-2xl">
        <span class="{nav_item_classes}  bg-white-500 text-black py-2 hover:text-white px-4 rounded hover:bg-green-500 border border-white-500 p-4" onclick="location.href='/prediction'">Prediction</span>
        <span class="{nav_item_classes} bg-white-500 text-black py-2 hover:text-white px-4 rounded hover:bg-blue-500 border border-white-500 p-4" onclick="location.href='/dashboard'">Dashboard</span>
    </div>
    """,
    unsafe_allow_html=True
    )

# Get the current page
    page = st.query_params.get("page", "dashboard")
    # Display the selected page
    if page != "dashboard":
        # dashboard()
        prediction()
    else:
        prediction()
        # dashboard()
        

if __name__=="__main__":
    main()