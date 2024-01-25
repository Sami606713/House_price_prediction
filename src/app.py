import streamlit as st
from utils import read_data,load_image

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
            st.title("Image")
            img=load_image("src/Notebook/2pie.jpeg")
            st.image(img)

        
        # Right col
        with right_col:
            # Make a form
            with st.form("House Form"):
                st.title("load")
                
                # Add a text input field
                area=st.number_input("Enter Area", format="%d",min_value=0)
                
                df=read_data("src/Notebook/clean_data.csv")
                """
                add rauio btn heres
                
                """
                
                bed,bath,flor=st.columns(3)
                with bed:
                    # Bedrooms
                    st.selectbox("Bedrooms", sorted(df[df["bedrooms"]>0]["bedrooms"].unique()))
               
                # Bath
                with bath:
                    st.selectbox("bath", sorted(df[df["bathrooms"]>0]["bathrooms"].unique()))
                
                with flor:
                    st.selectbox("floor", sorted(df[df["floors"]>0]["floors"].unique()))
                # Use st.selectbox to create a dropdown
                selected_city = st.selectbox("location", df["city"])

                # form submit button
                st.form_submit_button("predict")

if __name__=="__main__":
    main()