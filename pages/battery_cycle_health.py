import streamlit as st
import pandas as pd
import numpy as np
from qccheck import qckey
from io import StringIO
from streamlit_echarts import st_echarts
import json

uploaded_excel_file_all = st.file_uploader("上传电池循环次数 - 健康度", type=["txt"])
my_bar = st.progress(0)

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

if uploaded_excel_file_all is None:
    st.stop()


# To read file as bytes:
bytes_data = uploaded_excel_file_all.getvalue()

# To convert to a string based IO:
stringio = StringIO(uploaded_excel_file_all.getvalue().decode("utf-8"))
string_data = stringio.read()
battery_info_list = string_data.split("\n")[1:]
if battery_info_list[-1] == "":
   battery_info_list = battery_info_list[0:-2]
st.write(battery_info_list)
battery_infos_count = len(battery_info_list)

index = 0
for battery in battery_info_list:
  index += 1
  json_str = battery.split("\t")[1]
  json_obj = json.loads(json_str)
  device_name = json_obj["ios_type"]["origin"]
  cycle_count = json_obj["cdcs"]["read"]
  health = json_obj["dcxl"]["read"]

  st.write(f"{device_name}----{cycle_count}----{health}")

  my_bar.progress(index / battery_infos_count)
  if index >= battery_infos_count:
     st.success('处理数据完毕', icon="✅")
     break
  
