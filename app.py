import pickle
import streamlit as st

with open('./resourses/model.pkl','rb+') as f:
    clf = pickle.load(f)

with open('./resourses/cv.pkl','rb+') as f:
    cv = pickle.load(f)


type(cv)
st.title("Hate Speech Detection")
user = st.text_area("Enter any Tweet: ")
if len(user) < 1:
    st.write("  ")
else:
    sample = user
    data = cv.transform([sample])
    a = clf.predict(data)
    st.title(a[0])
