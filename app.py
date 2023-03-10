import os
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode, GridOptionsBuilder
import requests

from google.oauth2 import service_account
from google.cloud import storage

credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
client = storage.Client(credentials=credentials)

bucket_name = "cagri-ozmemis-streamlit"
file_name = "answers.csv"

bucket = client.bucket(bucket_name)
blob = bucket.blob(file_name)


st.title("HORIZON GRANT CALLS")

st.write ("This is an online survey through which you can indicate your interest in specific HORIZON grant calls. There are six clusters in total. Please choose the calls that draw your attention at each cluster. You can choose more than one.")

st.write ("")

st.write ("Please provide your name, last name, and faculty")

name = st.text_input("Your name", key="name")

last_name = st.text_input("Your last name", key="last_name")

faculty = st.selectbox("Your faculty", {"Architecture and Design", "Aviation and Aeronautical Sciences", "Business", "Engineering", "Law", "Social Sciences"})

st.write ("")
###########################

cluster1_url = "https://github.com/cagriozmemis/survey/raw/main/cluster1.xlsx"
cluster1 = pd.read_excel(cluster1_url)

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

cluster2_url = "https://github.com/cagriozmemis/survey/raw/main/cluster2.xlsx"
cluster2 = pd.read_excel(cluster2_url)

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

cluster3_url = "https://github.com/cagriozmemis/survey/raw/main/cluster3.xlsx"
cluster3 = pd.read_excel(cluster3_url)

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

cluster4_url = "https://github.com/cagriozmemis/survey/raw/main/cluster4.xlsx"
cluster4 = pd.read_excel(cluster4_url)

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

cluster5_url = "https://github.com/cagriozmemis/survey/raw/main/cluster5.xlsx"
cluster5 = pd.read_excel(cluster5_url)

st.write("Cluster5: Climate Energy and Mobility")

gd5 = GridOptionsBuilder.from_dataframe(cluster5)

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

cluster6_url = "https://github.com/cagriozmemis/survey/raw/main/cluster6.xlsx"
cluster6 = pd.read_excel(cluster6_url)
cluster6 = cluster6.iloc[: , :-3]

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
########################


if st.button('Submit my response'):
    
    main_list = []
    
    main_list.append(name)
    main_list.append(last_name)
    main_list.append(faculty)
    
    chosen = list(df["#"])
    string_chosen = ",".join(str(e) for e in chosen)
    main_list.append(string_chosen)
    
    chosen = list(df2["#"])
    string_chosen = ",".join(str(e) for e in chosen)
    main_list.append(string_chosen)
    
    chosen = list(df3["#"])
    string_chosen = ",".join(str(e) for e in chosen)
    main_list.append(string_chosen)
    
    chosen = list(df4["#"])
    string_chosen = ",".join(str(e) for e in chosen)
    main_list.append(string_chosen)
    
    chosen = list(df5["#"])
    string_chosen = ",".join(str(e) for e in chosen)
    main_list.append(string_chosen)
    
    chosen = list(df6["#"])
    string_chosen = ",".join(str(e) for e in chosen)
    main_list.append(string_chosen)
    
    #main_data = pd.DataFrame([main_list],columns=["Name", "Last name", "Faculty", "Chosen from Cluster1", "Chosen from Cluster2", "Chosen from Cluster3", "Chosen from Cluster4", "Chosen from Cluster5", "Chosen from Cluster6"])
    #st.write(main_data)
    
    write_to_cloud = " | ".join(main_list)
    
    blob.upload_from_string(write_to_cloud, content_type="text/csv")
    
    blob.upload_from_string("\n", content_type="text/csv")
    
    st.write("Thank you for your response! You can close this page now.")
    
    
    

       
     
     











