import streamlit as st
import pandas as pd
import numpy as np

uploaded_excel_file_all = st.file_uploader("上传云窗Panic日志", type=["xlsx", "txt"])

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

if uploaded_excel_file_all is None:
    st.stop()

dataframe = pd.read_excel(uploaded_excel_file_all)
st.write(dataframe)

# remove panic_string_column null values
panic_string_column = dataframe["original_data"]
id_column = dataframe["id"]
for i in range(len(id_column)):
  id_string = str(id_column.iloc[i])
  if "is_alive_func returned unhealthy" in id_string:
    # modify the panic_string_column in i-1 location
    panic_string_column.iloc[i-1] = panic_string_column.iloc[i-1] + " " + id_string

# get panic_string_columns number
panic_string_column = panic_string_column.dropna()
panic_string_column_number = len(panic_string_column)
st.write("### Panic日志数量: " + str(panic_string_column_number))
st.write(panic_string_column)

panic_string_arr = []
for i in range(panic_string_column_number):
    panic_string = panic_string_column.iloc[i]
    # panic_string has more than 1 : , split it, and get the rest of the string after the first :
    panic_string = panic_string.split(":", 1)[1].strip()
    panic_string_arr.append(panic_string)

# unique panic_string
panic_string_arr = list(set(panic_string_arr))

# convert panic_string_arr to dataframe
st.write("### Panic日志去重后数量: " + str(len(panic_string_arr)))
panic_string_df = pd.DataFrame(panic_string_arr, columns=["panic_string"])
st.write(panic_string_df)

merged_csv = convert_df(panic_string_df)

st.download_button(
    label="Download data as CSV",
    data=merged_csv,
    file_name='panic_string.csv',
    mime='text/csv',
)