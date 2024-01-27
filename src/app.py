import streamlit as st
from utils import read_data,load_image,load_model,load_tailwind
from dashboard import dashboard
from prediction import prediction
from streamlit_option_menu import option_menu
# import plotly.figure_factory as ff

# Streamlit app page config
st.set_page_config(page_title="House Price Prediction", page_icon=":house:", layout="wide")

def main():
    # add the menu
    selected = option_menu(
        menu_title=None,
        options=["Home", 'Dashboard'], 
        icons=['house', 'camera',"data","book"], 
        menu_icon="cast", 
        default_index=0,
        orientation="horizontal"
        )
        
    # Display the selected page
    if selected == "Home":
        # dashboard()
        prediction()
    elif selected == "Dashboard":
        # prediction()
        dashboard()
    # elif selected=="Data-Set":
        with st.container():
            st.markdown(
                """
                <h1 class='text-center text-darkblue font-bold font-serif text-4xl'>US House Data-Set</h1>
                """,
                unsafe_allow_html=True
            )
            df=read_data("src/Notebook/clean_data.csv")
            st.dataframe(df)
    

if __name__=="__main__":
    main()