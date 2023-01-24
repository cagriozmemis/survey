import os
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode, GridOptionsBuilder


cwd = "https://github.com/cagriozmemis/survey/blob/main/"


st.title("HORIZON GRANT CALLS")

st.write ("This is an online survey through which you can indicate your interest in specific HORIZON grant calls. There are six clusters in total. Please choose the calls that draw your attention at each cluster. You can choose more than one.")

st.write ("")

st.write ("Please provide your name and last name")

name = st.text_input("Your name", key="name")

last_name = st.text_input("Your last name", key="last_name")

st.write ("")

faculty = st.selectbox("Your faculty", {"Applied Sciences", "Architecture", "Business", "Engineering", "Law", "Social Sciences"})
###########################

file_path = cwd + "cluster1.xlsx"
cluster1 = pd.read_excel(file_path)

st.write("Cluster1: Health")

gd = GridOptionsBuilder.from_dataframe(cluster1)

gd.configure_selection(selection_mode='multiple', use_checkbox=True)

gridoptions = gd.build()

grid_table = AgGrid(cluster1, height=350, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)


st.write ("You selected:")
selected = grid_table['selected_rows']
df = pd.DataFrame(selected)
st.write(df)
st.write ("")
###########################

file_path = cwd + "cluster2.xlsx"
cluster2 = pd.read_excel(file_path)

st.write("Cluster2: Culture, Creativity and Inclusive Society")

gd2 = GridOptionsBuilder.from_dataframe(cluster2)

gd2.configure_selection(selection_mode='multiple', use_checkbox=True)

gridoptions2 = gd2.build()

grid_table2 = AgGrid(cluster2, height=350, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

st.write ("You selected:")
selected2 = grid_table2['selected_rows']
df2 = pd.DataFrame(selected2)
st.write(df2)
st.write ("")

###########################

file_path = cwd + "cluster3.xlsx"
cluster3 = pd.read_excel(file_path)

st.write("Cluster3: Civil Security for Society")

gd3 = GridOptionsBuilder.from_dataframe(cluster3)

gd3.configure_selection(selection_mode='multiple', use_checkbox=True)

gridoptions3 = gd3.build()

grid_table3 = AgGrid(cluster3, height=350, gridOptions=gridoptions3,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

st.write ("You selected:")
selected3 = grid_table3['selected_rows']
df3 = pd.DataFrame(selected3)
st.write(df3)
st.write ("")
###########################

file_path = cwd + "cluster4.xlsx"
cluster4 = pd.read_excel(file_path)

st.write("Cluster4: Digital Industry and Space")

gd4 = GridOptionsBuilder.from_dataframe(cluster4)

gd4.configure_selection(selection_mode='multiple', use_checkbox=True)

gridoptions4 = gd4.build()

grid_table4 = AgGrid(cluster4, height=350, gridOptions=gridoptions4,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

st.write ("You selected:")
selected4 = grid_table4['selected_rows']
df4 = pd.DataFrame(selected4)
st.write(df4)
st.write ("")
###########################

file_path = cwd + "cluster5.xlsx"
cluster5 = pd.read_excel(file_path)

st.write("Cluster5: Climate Energy and Mobility")

gd5 = GridOptionsBuilder.from_dataframe(cluster1)

gd5.configure_selection(selection_mode='multiple', use_checkbox=True)

gridoptions5 = gd5.build()

grid_table5 = AgGrid(cluster5, height=350, gridOptions=gridoptions5,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

st.write ("You selected:")
selected5 = grid_table5['selected_rows']
df5 = pd.DataFrame(selected5)
st.write(df5)
st.write ("")
###########################

file_path = cwd + "cluster6.xlsx"
cluster6 = pd.read_excel(file_path)

st.write("Cluster6: Food, Bioeceonomy, Natural Resources, Agriculture and Environment")

gd6 = GridOptionsBuilder.from_dataframe(cluster6)

gd6.configure_selection(selection_mode='multiple', use_checkbox=True)

gridoptions6 = gd6.build()

grid_table6 = AgGrid(cluster6, height=350, gridOptions=gridoptions6,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)



st.write ("You selected:")
selected6 = grid_table6['selected_rows']
df6 = pd.DataFrame(selected6)
st.write(df6)
st.write ("")

if st.button('Submit my response'):
    st.write("Thank you for your response! You can close this page now.")


# st.selectbox("Please choose the calls that draw your attention",cluster1["Name"])







