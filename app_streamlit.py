import streamlit as st


st.title("Streamlit examples!")
st.header("Step 1")
#st.subheader("import",<span style='color:blue'> streamlit</span> ,"as st")

#st.text(\Users\rudrashah\Aaryan\Diseases_Pred_System\Streamlit command.txt)

if st.button("Hello World",key="id1"):
    st.header("Who's there??")

if st.checkbox("Click Me!"):
    st.write("Iamcheckboxmaster")

selected_item = st.radio("check me!",["Red","Yellow","Blue","Green"])
