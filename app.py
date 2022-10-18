import streamlit as st

#st.title("Welcome to Streamlit for DS")

# st.text("It is text")
#
# st.markdown("""<b>This is bold</b>""", True)
#
# st.write(sum)
# st.write("This is write")
#
# stud_dict = {'sno':[100, 200, 300],
#              'sname':['abcd', 'anxf', 'dsfdsf']
#              }
#
# st.write(stud_dict)

st.title("House Price Prediction")

area = st.text_input("Area", 0)

if area:
    st.write("Area is : ", area)

gen = st.radio('Gender',["Male", "Female"], index=0)
cnt = st.selectbox('Country', ["Ind", "Pak", "Aus"], index=0)

if gen:
    st.write("Seleced : ", gen)

if cnt:
    st.write("Selected : ", cnt)