import streamlit as st
from utils import read_data,load_image,load_model
import numpy as np
import pandas as pd
# df=read_data("src/Notebook/data.csv")
# st.dataframe(df)
def main():
    # set the title
    st.title("US House Price Prediction")

    # make a main cntainer inside the main container make two left and right columns
    with st.container():
        # make two columns
        left_col,right_col=st.columns(2)

        # left col
        with left_col:
            # st.title("Image")
            img=load_image("src/Notebook/house.jpg")
            st.image(img)

        
        # Right col
        with right_col:
            # Make a form
            with st.form("House Predict Form"):
                # st.title("load")
                
                # Add a text input field
                area=st.number_input("Enter Area", format="%d",min_value=0)
                
                # Load the dataset
                df=read_data("src/Notebook/clean_data.csv")
                
                bed,bath,floor=st.columns(3)
                with bed:
                    # Bedrooms
                    bedroom=st.selectbox("Bedrooms", sorted(df[df["bedrooms"]>0]["bedrooms"].unique()))
               
                # Bath
                with bath:
                    bathroom=st.selectbox("bath", sorted(df[df["bathrooms"]>0]["bathrooms"].unique()))
                
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
                    data=np.array([[bedroom,bathroom,floors,water_front,views,selected_city,country,area]])
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
                    
                    
                    st.dataframe(df)
                    pred=model.predict(df)
                    st.success(f"House preice is {pred[0].round()}")
                    

if __name__=="__main__":
    main()