
import streamlit as st 

st.title("Hello")

st.header("This is a header")

st.subheader("This is a subheader")

if st.checkbox("Show/Hide"):
	st.text("Showing the widget")
else:
	st.text("Click to move to the next page")
	
status = st.radio("Select Gender: ", ('Male', 'Female'))

if status == 'Male':
	st.text('You are a man')
else:
	st.text('You are a Woman')

hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports'])

hobbies = st.multiselect("Hobbies: ", ['Dancing', 'Reading', 'Sports'])

st.button("Predict")

if(st.button("About")):

	st.text("Welcome!!!")
	
first_name = st.text_input("Enter Your name")