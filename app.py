import streamlit as st

st.title(":red[Innomatics] Data App")
st.header("Welcome to your Dashboard")
st.snow()


# Ask the user for their name
name = st.text_input('Enter your name')

# Display a greeting using the user's name
if name:
    st.subheader(f'Hello, {name}!. Welcome to :red[Innomatics]')

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :smile:")
    st.balloons()