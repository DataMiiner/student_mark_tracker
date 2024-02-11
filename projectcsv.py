import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Marks Tracker",
    page_icon="📝"
)

# Define st.session_state
if "data" not in st.session_state:
    st.session_state["data"] = {'Roll No': [], 'Name': [], 'Marks': []}
if "student_count" not in st.session_state:
    st.session_state["student_count"] = 1
if "student_index" not in st.session_state:
    st.session_state["student_index"] = 0

# Main code
st.title("ENTER STUDENT MARKS RECORDS 📒")
school = st.text_input("Enter school Name:")
st.session_state["student_count"] = st.number_input("Enter no of students:", step=1, value=1)

if st.button("Enter"):
    st.session_state["ok"] = True

st.write("-----------------------------------------")

if st.session_state.get("ok", False):
    rollno = st.text_input(f"Enter Rollno for Student {st.session_state['student_index'] + 1}:")
    name = st.text_input(f"Enter student Name for Student {st.session_state['student_index'] + 1}:")
    marks = st.text_input(f"Enter student Mark for Student {st.session_state['student_index'] + 1}:")

    if st.button(f"ADD Student {st.session_state['student_index'] + 1}"):
        st.session_state["data"]['Roll No'].append(rollno)
        st.session_state["data"]['Name'].append(name)
        st.session_state["data"]['Marks'].append(marks)
    
        st.success(f"Enter student {st.session_state['student_index'] + 1} data in excel")

        # Move to the next student index
        st.session_state["student_index"] += 1
        
    if st.session_state["student_index"] == st.session_state["student_count"]:
        # Convert data to DataFrame
        df = pd.DataFrame(st.session_state["data"])

        # Download CSV button
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv.encode(),
            file_name=f"{school}.csv",
            mime="text/csv"
        )
    else:
       st.button("Next Student")   
