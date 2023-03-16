import streamlit as st
import pandas as pd
import numpy as np
from qccheck import qckey
from streamlit_echarts import st_echarts

uploaded_excel_file_all = st.file_uploader("上传【30天内故障检出量统计(所有站点)】 Excel 文件", type=["xlsx"])
uploaded_excel_file_perf = st.file_uploader("上传【30天内运行过性能检测的设备的故障检出数据(所有站点)】 Excel 文件", type=["xlsx"])

if uploaded_excel_file_all is None:
    st.stop()

if uploaded_excel_file_perf is None:
    st.stop() 

dataframe = pd.read_excel(uploaded_excel_file_all)
dataframe_perf = pd.read_excel(uploaded_excel_file_perf)

# 将a和b按照日期进行外连接
merged = pd.merge(dataframe, dataframe_perf, on=qckey.date, how='outer', suffixes=(qckey.merge_suffix_all, qckey.merge_suffix_perf))

# 将缺失值填充为0
merged = merged.fillna(0)

merged[qckey.no_perf(qckey.screen_stripes_blurry_splash_total)] = merged[qckey.all(qckey.screen_stripes_blurry_splash_total)] - merged[qckey.perf(qckey.screen_stripes_blurry_splash_total)]
merged[qckey.no_perf(qckey.touch_exception_total)] = merged[qckey.all(qckey.touch_exception_total)] - merged[qckey.perf(qckey.touch_exception_total)]
merged[qckey.no_perf(qckey.boot_exception_total)] = merged[qckey.all(qckey.boot_exception_total)] - merged[qckey.perf(qckey.boot_exception_total)]
merged[qckey.no_perf(qckey.boot_repeat_total)] = merged[qckey.all(qckey.boot_repeat_total)] - merged[qckey.perf(qckey.boot_repeat_total)]
merged[qckey.no_perf(qckey.auto_shutdown_restart_total)] = merged[qckey.all(qckey.auto_shutdown_restart_total)] - merged[qckey.perf(qckey.auto_shutdown_restart_total)]
merged[qckey.no_perf(qckey.cannot_into_sys_total)] = merged[qckey.all(qckey.cannot_into_sys_total)] - merged[qckey.perf(qckey.cannot_into_sys_total)]
merged[qckey.no_perf(qckey.fast_power_consumption_total)] = merged[qckey.all(qckey.fast_power_consumption_total)] - merged[qckey.perf(qckey.fast_power_consumption_total)]
merged[qckey.no_perf(qckey.motherboard_failure_total)] = merged[qckey.all(qckey.motherboard_failure_total)] - merged[qckey.perf(qckey.motherboard_failure_total)]
merged[qckey.no_perf(qckey.screen_display_exception_total)] = merged[qckey.all(qckey.screen_display_exception_total)] - merged[qckey.perf(qckey.screen_display_exception_total)]

merged[qckey.no_perf(qckey.screen_stripes_blurry_splash_ios)] = merged[qckey.all(qckey.screen_stripes_blurry_splash_ios)] - merged[qckey.perf(qckey.screen_stripes_blurry_splash_ios)]
merged[qckey.no_perf(qckey.touch_exception_ios)] = merged[qckey.all(qckey.touch_exception_ios)] - merged[qckey.perf(qckey.touch_exception_ios)]
merged[qckey.no_perf(qckey.boot_exception_ios)] = merged[qckey.all(qckey.boot_exception_ios)] - merged[qckey.perf(qckey.boot_exception_ios)]
merged[qckey.no_perf(qckey.boot_repeat_ios)] = merged[qckey.all(qckey.boot_repeat_ios)] - merged[qckey.perf(qckey.boot_repeat_ios)]
merged[qckey.no_perf(qckey.auto_shutdown_restart_ios)] = merged[qckey.all(qckey.auto_shutdown_restart_ios)] - merged[qckey.perf(qckey.auto_shutdown_restart_ios)]
merged[qckey.no_perf(qckey.cannot_into_sys_ios)] = merged[qckey.all(qckey.cannot_into_sys_ios)] - merged[qckey.perf(qckey.cannot_into_sys_ios)]
merged[qckey.no_perf(qckey.fast_power_consumption_ios)] = merged[qckey.all(qckey.fast_power_consumption_ios)] - merged[qckey.perf(qckey.fast_power_consumption_ios)]
merged[qckey.no_perf(qckey.motherboard_failure_ios)] = merged[qckey.all(qckey.motherboard_failure_ios)] - merged[qckey.perf(qckey.motherboard_failure_ios)]
merged[qckey.no_perf(qckey.screen_display_exception_ios)] = merged[qckey.all(qckey.screen_display_exception_ios)] - merged[qckey.perf(qckey.screen_display_exception_ios)]

merged[qckey.no_perf(qckey.screen_stripes_blurry_splash_andr)] = merged[qckey.all(qckey.screen_stripes_blurry_splash_andr)] - merged[qckey.perf(qckey.screen_stripes_blurry_splash_andr)]
merged[qckey.no_perf(qckey.touch_exception_andr)] = merged[qckey.all(qckey.touch_exception_andr)] - merged[qckey.perf(qckey.touch_exception_andr)]
merged[qckey.no_perf(qckey.boot_exception_andr)] = merged[qckey.all(qckey.boot_exception_andr)] - merged[qckey.perf(qckey.boot_exception_andr)]
merged[qckey.no_perf(qckey.boot_repeat_andr)] = merged[qckey.all(qckey.boot_repeat_andr)] - merged[qckey.perf(qckey.boot_repeat_andr)]
merged[qckey.no_perf(qckey.auto_shutdown_restart_andr)] = merged[qckey.all(qckey.auto_shutdown_restart_andr)] - merged[qckey.perf(qckey.auto_shutdown_restart_andr)]
merged[qckey.no_perf(qckey.cannot_into_sys_andr)] = merged[qckey.all(qckey.cannot_into_sys_andr)] - merged[qckey.perf(qckey.cannot_into_sys_andr)]
merged[qckey.no_perf(qckey.fast_power_consumption_andr)] = merged[qckey.all(qckey.fast_power_consumption_andr)] - merged[qckey.perf(qckey.fast_power_consumption_andr)]
merged[qckey.no_perf(qckey.motherboard_failure_andr)] = merged[qckey.all(qckey.motherboard_failure_andr)] - merged[qckey.perf(qckey.motherboard_failure_andr)]
merged[qckey.no_perf(qckey.screen_display_exception_andr)] = merged[qckey.all(qckey.screen_display_exception_andr)] - merged[qckey.perf(qckey.screen_display_exception_andr)]

merged[qckey.no_perf(qckey.total)] = merged[qckey.all(qckey.total)] - merged[qckey.perf(qckey.total)]
merged[qckey.no_perf(qckey.total_ios)] = merged[qckey.all(qckey.total_ios)] - merged[qckey.perf(qckey.total_ios)]
merged[qckey.no_perf(qckey.total_andr)] = merged[qckey.all(qckey.total_andr)] - merged[qckey.perf(qckey.total_andr)]

# dataframe all --------------------------------
merged[qckey.proportion(qckey.all(qckey.screen_stripes_blurry_splash_ios))] = merged[qckey.all(qckey.screen_stripes_blurry_splash_ios)]  / merged[qckey.all(qckey.total_ios)]
merged[qckey.proportion(qckey.all(qckey.touch_exception_ios))] = merged[qckey.all(qckey.touch_exception_ios)]  / merged[qckey.all(qckey.total_ios)]
merged[qckey.proportion(qckey.all(qckey.boot_exception_ios))] = merged[qckey.all(qckey.boot_exception_ios)]  / merged[qckey.all(qckey.total_ios)]
merged[qckey.proportion(qckey.all(qckey.boot_repeat_ios))] = merged[qckey.all(qckey.boot_repeat_ios)]  / merged[qckey.all(qckey.total_ios)]
merged[qckey.proportion(qckey.all(qckey.auto_shutdown_restart_ios))] = merged[qckey.all(qckey.auto_shutdown_restart_ios)]  / merged[qckey.all(qckey.total_ios)]
merged[qckey.proportion(qckey.all(qckey.cannot_into_sys_ios))] = merged[qckey.all(qckey.cannot_into_sys_ios)]  / merged[qckey.all(qckey.total_ios)]
merged[qckey.proportion(qckey.all(qckey.fast_power_consumption_ios))] = merged[qckey.all(qckey.fast_power_consumption_ios)]  / merged[qckey.all(qckey.total_ios)]
merged[qckey.proportion(qckey.all(qckey.motherboard_failure_ios))] = merged[qckey.all(qckey.motherboard_failure_ios)]  / merged[qckey.all(qckey.total_ios)]
merged[qckey.proportion(qckey.all(qckey.screen_display_exception_ios))] = merged[qckey.all(qckey.screen_display_exception_ios)]  / merged[qckey.all(qckey.total_ios)]

merged[qckey.proportion(qckey.all(qckey.total_fault_ios))] = (merged[qckey.all(qckey.screen_stripes_blurry_splash_ios)] 
                               + merged[qckey.all(qckey.touch_exception_ios)]
                               + merged[qckey.all(qckey.boot_exception_ios)] 
                               + merged[qckey.all(qckey.boot_repeat_ios)]
                               + merged[qckey.all(qckey.auto_shutdown_restart_ios)] 
                               + merged[qckey.all(qckey.cannot_into_sys_ios)] 
                               + merged[qckey.all(qckey.fast_power_consumption_ios)]  
                               + merged[qckey.all(qckey.motherboard_failure_ios)]  
                               + merged[qckey.all(qckey.screen_display_exception_ios)]) / merged[qckey.all(qckey.total_ios)]

# ------------------------------

merged[qckey.proportion(qckey.all(qckey.screen_stripes_blurry_splash_andr))] = merged[qckey.all(qckey.screen_stripes_blurry_splash_andr)]  / merged[qckey.all(qckey.total_andr)]
merged[qckey.proportion(qckey.all(qckey.touch_exception_andr))] = merged[qckey.all(qckey.touch_exception_andr)]  / merged[qckey.all(qckey.total_andr)]
merged[qckey.proportion(qckey.all(qckey.boot_exception_andr))] = merged[qckey.all(qckey.boot_exception_andr)]  / merged[qckey.all(qckey.total_andr)]
merged[qckey.proportion(qckey.all(qckey.boot_repeat_andr))] = merged[qckey.all(qckey.boot_repeat_andr)]  / merged[qckey.all(qckey.total_andr)]
merged[qckey.proportion(qckey.all(qckey.auto_shutdown_restart_andr))] = merged[qckey.all(qckey.auto_shutdown_restart_andr)]  / merged[qckey.all(qckey.total_andr)]
merged[qckey.proportion(qckey.all(qckey.cannot_into_sys_andr))] = merged[qckey.all(qckey.cannot_into_sys_andr)]  / merged[qckey.all(qckey.total_andr)]
merged[qckey.proportion(qckey.all(qckey.fast_power_consumption_andr))] = merged[qckey.all(qckey.fast_power_consumption_andr)]  / merged[qckey.all(qckey.total_andr)]
merged[qckey.proportion(qckey.all(qckey.motherboard_failure_andr))] = merged[qckey.all(qckey.motherboard_failure_andr)]  / merged[qckey.all(qckey.total_andr)]
merged[qckey.proportion(qckey.all(qckey.screen_display_exception_andr))] = merged[qckey.all(qckey.screen_display_exception_andr)]  / merged[qckey.all(qckey.total_andr)]

merged[qckey.proportion(qckey.all(qckey.total_fault_andr))] = (merged[qckey.all(qckey.screen_stripes_blurry_splash_andr)] 
                               + merged[qckey.all(qckey.touch_exception_andr)]
                               + merged[qckey.all(qckey.boot_exception_andr)] 
                               + merged[qckey.all(qckey.boot_repeat_andr)]
                               + merged[qckey.all(qckey.auto_shutdown_restart_andr)] 
                               + merged[qckey.all(qckey.cannot_into_sys_andr)] 
                               + merged[qckey.all(qckey.fast_power_consumption_andr)]  
                               + merged[qckey.all(qckey.motherboard_failure_andr)]  
                               + merged[qckey.all(qckey.screen_display_exception_andr)]) / merged[qckey.all(qckey.total_andr)]


# ------------------------------
merged[qckey.proportion(qckey.all(qckey.screen_stripes_blurry_splash_total))] = merged[qckey.all(qckey.screen_stripes_blurry_splash_total)]  / merged[qckey.all(qckey.total)]
merged[qckey.proportion(qckey.all(qckey.touch_exception_total))] = merged[qckey.all(qckey.touch_exception_total)]  / merged[qckey.all(qckey.total)]
merged[qckey.proportion(qckey.all(qckey.boot_exception_total))] = merged[qckey.all(qckey.boot_exception_total)]  / merged[qckey.all(qckey.total)]
merged[qckey.proportion(qckey.all(qckey.boot_repeat_total))] = merged[qckey.all(qckey.boot_repeat_total)]  / merged[qckey.all(qckey.total)]
merged[qckey.proportion(qckey.all(qckey.auto_shutdown_restart_total))] = merged[qckey.all(qckey.auto_shutdown_restart_total)]  / merged[qckey.all(qckey.total)]
merged[qckey.proportion(qckey.all(qckey.cannot_into_sys_total))] = merged[qckey.all(qckey.cannot_into_sys_total)]  / merged[qckey.all(qckey.total)]
merged[qckey.proportion(qckey.all(qckey.fast_power_consumption_total))] = merged[qckey.all(qckey.fast_power_consumption_total)]  / merged[qckey.all(qckey.total)]
merged[qckey.proportion(qckey.all(qckey.motherboard_failure_total))] = merged[qckey.all(qckey.motherboard_failure_total)]  / merged[qckey.all(qckey.total)]
merged[qckey.proportion(qckey.all(qckey.screen_display_exception_total))] = merged[qckey.all(qckey.screen_display_exception_total)]  / merged[qckey.all(qckey.total)]

merged[qckey.proportion(qckey.all(qckey.total_fault))] = (merged[qckey.all(qckey.screen_stripes_blurry_splash_total)] 
                               + merged[qckey.all(qckey.touch_exception_total)]
                               + merged[qckey.all(qckey.boot_exception_total)] 
                               + merged[qckey.all(qckey.boot_repeat_total)]
                               + merged[qckey.all(qckey.auto_shutdown_restart_total)] 
                               + merged[qckey.all(qckey.cannot_into_sys_total)] 
                               + merged[qckey.all(qckey.fast_power_consumption_total)]  
                               + merged[qckey.all(qckey.motherboard_failure_total)]  
                               + merged[qckey.all(qckey.screen_display_exception_total)]) / merged[qckey.all(qckey.total)]



# dataframe_perf -----------------------------------------------------
merged[qckey.proportion(qckey.perf(qckey.screen_stripes_blurry_splash_ios))] = merged[qckey.perf(qckey.screen_stripes_blurry_splash_ios)]  / merged[qckey.perf(qckey.total_ios)]
merged[qckey.proportion(qckey.perf(qckey.touch_exception_ios))] = merged[qckey.perf(qckey.touch_exception_ios)]  / merged[qckey.perf(qckey.total_ios)]
merged[qckey.proportion(qckey.perf(qckey.boot_exception_ios))] = merged[qckey.perf(qckey.boot_exception_ios)]  / merged[qckey.perf(qckey.total_ios)]
merged[qckey.proportion(qckey.perf(qckey.boot_repeat_ios))] = merged[qckey.perf(qckey.boot_repeat_ios)]  / merged[qckey.perf(qckey.total_ios)]
merged[qckey.proportion(qckey.perf(qckey.auto_shutdown_restart_ios))] = merged[qckey.perf(qckey.auto_shutdown_restart_ios)]  / merged[qckey.perf(qckey.total_ios)]
merged[qckey.proportion(qckey.perf(qckey.cannot_into_sys_ios))] = merged[qckey.perf(qckey.cannot_into_sys_ios)]  / merged[qckey.perf(qckey.total_ios)]
merged[qckey.proportion(qckey.perf(qckey.fast_power_consumption_ios))] = merged[qckey.perf(qckey.fast_power_consumption_ios)]  / merged[qckey.perf(qckey.total_ios)]
merged[qckey.proportion(qckey.perf(qckey.motherboard_failure_ios))] = merged[qckey.perf(qckey.motherboard_failure_ios)]  / merged[qckey.perf(qckey.total_ios)]
merged[qckey.proportion(qckey.perf(qckey.screen_display_exception_ios))] = merged[qckey.perf(qckey.screen_display_exception_ios)]  / merged[qckey.perf(qckey.total_ios)]

merged[qckey.proportion(qckey.perf(qckey.total_fault_ios))] = (merged[qckey.perf(qckey.screen_stripes_blurry_splash_ios)] 
                               + merged[qckey.perf(qckey.touch_exception_ios)]
                               + merged[qckey.perf(qckey.boot_exception_ios)] 
                               + merged[qckey.perf(qckey.boot_repeat_ios)]
                               + merged[qckey.perf(qckey.auto_shutdown_restart_ios)] 
                               + merged[qckey.perf(qckey.cannot_into_sys_ios)] 
                               + merged[qckey.perf(qckey.fast_power_consumption_ios)]  
                               + merged[qckey.perf(qckey.motherboard_failure_ios)]  
                               + merged[qckey.perf(qckey.screen_display_exception_ios)]) / merged[qckey.perf(qckey.total_ios)]

# ------------------------------

merged[qckey.proportion(qckey.perf(qckey.screen_stripes_blurry_splash_andr))] = merged[qckey.perf(qckey.screen_stripes_blurry_splash_andr)]  / merged[qckey.perf(qckey.total_andr)]
merged[qckey.proportion(qckey.perf(qckey.touch_exception_andr))] = merged[qckey.perf(qckey.touch_exception_andr)]  / merged[qckey.perf(qckey.total_andr)]
merged[qckey.proportion(qckey.perf(qckey.boot_exception_andr))] = merged[qckey.perf(qckey.boot_exception_andr)]  / merged[qckey.perf(qckey.total_andr)]
merged[qckey.proportion(qckey.perf(qckey.boot_repeat_andr))] = merged[qckey.perf(qckey.boot_repeat_andr)]  / merged[qckey.perf(qckey.total_andr)]
merged[qckey.proportion(qckey.perf(qckey.auto_shutdown_restart_andr))] = merged[qckey.perf(qckey.auto_shutdown_restart_andr)]  / merged[qckey.perf(qckey.total_andr)]
merged[qckey.proportion(qckey.perf(qckey.cannot_into_sys_andr))] = merged[qckey.perf(qckey.cannot_into_sys_andr)]  / merged[qckey.perf(qckey.total_andr)]
merged[qckey.proportion(qckey.perf(qckey.fast_power_consumption_andr))] = merged[qckey.perf(qckey.fast_power_consumption_andr)]  / merged[qckey.perf(qckey.total_andr)]
merged[qckey.proportion(qckey.perf(qckey.motherboard_failure_andr))] = merged[qckey.perf(qckey.motherboard_failure_andr)]  / merged[qckey.perf(qckey.total_andr)]
merged[qckey.proportion(qckey.perf(qckey.screen_display_exception_andr))] = merged[qckey.perf(qckey.screen_display_exception_andr)]  / merged[qckey.perf(qckey.total_andr)]

merged[qckey.proportion(qckey.perf(qckey.total_fault_andr))] = (merged[qckey.perf(qckey.screen_stripes_blurry_splash_andr)] 
                               + merged[qckey.perf(qckey.touch_exception_andr)]
                               + merged[qckey.perf(qckey.boot_exception_andr)] 
                               + merged[qckey.perf(qckey.boot_repeat_andr)]
                               + merged[qckey.perf(qckey.auto_shutdown_restart_andr)] 
                               + merged[qckey.perf(qckey.cannot_into_sys_andr)] 
                               + merged[qckey.perf(qckey.fast_power_consumption_andr)]  
                               + merged[qckey.perf(qckey.motherboard_failure_andr)]  
                               + merged[qckey.perf(qckey.screen_display_exception_andr)]) / merged[qckey.perf(qckey.total_andr)]


# ------------------------------
merged[qckey.proportion(qckey.perf(qckey.screen_stripes_blurry_splash_total))] = merged[qckey.perf(qckey.screen_stripes_blurry_splash_total)]  / merged[qckey.perf(qckey.total)]
merged[qckey.proportion(qckey.perf(qckey.touch_exception_total))] = merged[qckey.perf(qckey.touch_exception_total)]  / merged[qckey.perf(qckey.total)]
merged[qckey.proportion(qckey.perf(qckey.boot_exception_total))] = merged[qckey.perf(qckey.boot_exception_total)]  / merged[qckey.perf(qckey.total)]
merged[qckey.proportion(qckey.perf(qckey.boot_repeat_total))] = merged[qckey.perf(qckey.boot_repeat_total)]  / merged[qckey.perf(qckey.total)]
merged[qckey.proportion(qckey.perf(qckey.auto_shutdown_restart_total))] = merged[qckey.perf(qckey.auto_shutdown_restart_total)]  / merged[qckey.perf(qckey.total)]
merged[qckey.proportion(qckey.perf(qckey.cannot_into_sys_total))] = merged[qckey.perf(qckey.cannot_into_sys_total)]  / merged[qckey.perf(qckey.total)]
merged[qckey.proportion(qckey.perf(qckey.fast_power_consumption_total))] = merged[qckey.perf(qckey.fast_power_consumption_total)]  / merged[qckey.perf(qckey.total)]
merged[qckey.proportion(qckey.perf(qckey.motherboard_failure_total))] = merged[qckey.perf(qckey.motherboard_failure_total)]  / merged[qckey.perf(qckey.total)]
merged[qckey.proportion(qckey.perf(qckey.screen_display_exception_total))] = merged[qckey.perf(qckey.screen_display_exception_total)]  / merged[qckey.perf(qckey.total)]

merged[qckey.proportion(qckey.perf(qckey.total_fault))] = (merged[qckey.perf(qckey.screen_stripes_blurry_splash_total)] 
                               + merged[qckey.perf(qckey.touch_exception_total)]
                               + merged[qckey.perf(qckey.boot_exception_total)] 
                               + merged[qckey.perf(qckey.boot_repeat_total)]
                               + merged[qckey.perf(qckey.auto_shutdown_restart_total)] 
                               + merged[qckey.perf(qckey.cannot_into_sys_total)] 
                               + merged[qckey.perf(qckey.fast_power_consumption_total)]  
                               + merged[qckey.perf(qckey.motherboard_failure_total)]  
                               + merged[qckey.perf(qckey.screen_display_exception_total)]) / merged[qckey.perf(qckey.total)]

# dataframe_noperf -------------------
merged[qckey.proportion(qckey.no_perf(qckey.screen_stripes_blurry_splash_ios))] = merged[qckey.no_perf(qckey.screen_stripes_blurry_splash_ios)]  / merged[qckey.no_perf(qckey.total_ios)]
merged[qckey.proportion(qckey.no_perf(qckey.touch_exception_ios))] = merged[qckey.no_perf(qckey.touch_exception_ios)]  / merged[qckey.no_perf(qckey.total_ios)]
merged[qckey.proportion(qckey.no_perf(qckey.boot_exception_ios))] = merged[qckey.no_perf(qckey.boot_exception_ios)]  / merged[qckey.no_perf(qckey.total_ios)]
merged[qckey.proportion(qckey.no_perf(qckey.boot_repeat_ios))] = merged[qckey.no_perf(qckey.boot_repeat_ios)]  / merged[qckey.no_perf(qckey.total_ios)]
merged[qckey.proportion(qckey.no_perf(qckey.auto_shutdown_restart_ios))] = merged[qckey.no_perf(qckey.auto_shutdown_restart_ios)]  / merged[qckey.no_perf(qckey.total_ios)]
merged[qckey.proportion(qckey.no_perf(qckey.cannot_into_sys_ios))] = merged[qckey.no_perf(qckey.cannot_into_sys_ios)]  / merged[qckey.no_perf(qckey.total_ios)]
merged[qckey.proportion(qckey.no_perf(qckey.fast_power_consumption_ios))] = merged[qckey.no_perf(qckey.fast_power_consumption_ios)]  / merged[qckey.no_perf(qckey.total_ios)]
merged[qckey.proportion(qckey.no_perf(qckey.motherboard_failure_ios))] = merged[qckey.no_perf(qckey.motherboard_failure_ios)]  / merged[qckey.no_perf(qckey.total_ios)]
merged[qckey.proportion(qckey.no_perf(qckey.screen_display_exception_ios))] = merged[qckey.no_perf(qckey.screen_display_exception_ios)]  / merged[qckey.no_perf(qckey.total_ios)]

merged[qckey.proportion(qckey.no_perf(qckey.total_fault_ios))] = (merged[qckey.no_perf(qckey.screen_stripes_blurry_splash_ios)] 
                               + merged[qckey.no_perf(qckey.touch_exception_ios)]
                               + merged[qckey.no_perf(qckey.boot_exception_ios)] 
                               + merged[qckey.no_perf(qckey.boot_repeat_ios)]
                               + merged[qckey.no_perf(qckey.auto_shutdown_restart_ios)] 
                               + merged[qckey.no_perf(qckey.cannot_into_sys_ios)] 
                               + merged[qckey.no_perf(qckey.fast_power_consumption_ios)]  
                               + merged[qckey.no_perf(qckey.motherboard_failure_ios)]  
                               + merged[qckey.no_perf(qckey.screen_display_exception_ios)]) / merged[qckey.no_perf(qckey.total_ios)]

# ------------------------------

merged[qckey.proportion(qckey.no_perf(qckey.screen_stripes_blurry_splash_andr))] = merged[qckey.no_perf(qckey.screen_stripes_blurry_splash_andr)]  / merged[qckey.no_perf(qckey.total_andr)]
merged[qckey.proportion(qckey.no_perf(qckey.touch_exception_andr))] = merged[qckey.no_perf(qckey.touch_exception_andr)]  / merged[qckey.no_perf(qckey.total_andr)]
merged[qckey.proportion(qckey.no_perf(qckey.boot_exception_andr))] = merged[qckey.no_perf(qckey.boot_exception_andr)]  / merged[qckey.no_perf(qckey.total_andr)]
merged[qckey.proportion(qckey.no_perf(qckey.boot_repeat_andr))] = merged[qckey.no_perf(qckey.boot_repeat_andr)]  / merged[qckey.no_perf(qckey.total_andr)]
merged[qckey.proportion(qckey.no_perf(qckey.auto_shutdown_restart_andr))] = merged[qckey.no_perf(qckey.auto_shutdown_restart_andr)]  / merged[qckey.no_perf(qckey.total_andr)]
merged[qckey.proportion(qckey.no_perf(qckey.cannot_into_sys_andr))] = merged[qckey.no_perf(qckey.cannot_into_sys_andr)]  / merged[qckey.no_perf(qckey.total_andr)]
merged[qckey.proportion(qckey.no_perf(qckey.fast_power_consumption_andr))] = merged[qckey.no_perf(qckey.fast_power_consumption_andr)]  / merged[qckey.no_perf(qckey.total_andr)]
merged[qckey.proportion(qckey.no_perf(qckey.motherboard_failure_andr))] = merged[qckey.no_perf(qckey.motherboard_failure_andr)]  / merged[qckey.no_perf(qckey.total_andr)]
merged[qckey.proportion(qckey.no_perf(qckey.screen_display_exception_andr))] = merged[qckey.no_perf(qckey.screen_display_exception_andr)]  / merged[qckey.no_perf(qckey.total_andr)]

merged[qckey.proportion(qckey.no_perf(qckey.total_fault_andr))] = (merged[qckey.no_perf(qckey.screen_stripes_blurry_splash_andr)] 
                               + merged[qckey.no_perf(qckey.touch_exception_andr)]
                               + merged[qckey.no_perf(qckey.boot_exception_andr)] 
                               + merged[qckey.no_perf(qckey.boot_repeat_andr)]
                               + merged[qckey.no_perf(qckey.auto_shutdown_restart_andr)] 
                               + merged[qckey.no_perf(qckey.cannot_into_sys_andr)] 
                               + merged[qckey.no_perf(qckey.fast_power_consumption_andr)]  
                               + merged[qckey.no_perf(qckey.motherboard_failure_andr)]  
                               + merged[qckey.no_perf(qckey.screen_display_exception_andr)]) / merged[qckey.no_perf(qckey.total_andr)]


# ------------------------------
merged[qckey.proportion(qckey.no_perf(qckey.screen_stripes_blurry_splash_total))] = merged[qckey.no_perf(qckey.screen_stripes_blurry_splash_total)]  / merged[qckey.no_perf(qckey.total)]
merged[qckey.proportion(qckey.no_perf(qckey.touch_exception_total))] = merged[qckey.no_perf(qckey.touch_exception_total)]  / merged[qckey.no_perf(qckey.total)]
merged[qckey.proportion(qckey.no_perf(qckey.boot_exception_total))] = merged[qckey.no_perf(qckey.boot_exception_total)]  / merged[qckey.no_perf(qckey.total)]
merged[qckey.proportion(qckey.no_perf(qckey.boot_repeat_total))] = merged[qckey.no_perf(qckey.boot_repeat_total)]  / merged[qckey.no_perf(qckey.total)]
merged[qckey.proportion(qckey.no_perf(qckey.auto_shutdown_restart_total))] = merged[qckey.no_perf(qckey.auto_shutdown_restart_total)]  / merged[qckey.no_perf(qckey.total)]
merged[qckey.proportion(qckey.no_perf(qckey.cannot_into_sys_total))] = merged[qckey.no_perf(qckey.cannot_into_sys_total)]  / merged[qckey.no_perf(qckey.total)]
merged[qckey.proportion(qckey.no_perf(qckey.fast_power_consumption_total))] = merged[qckey.no_perf(qckey.fast_power_consumption_total)]  / merged[qckey.no_perf(qckey.total)]
merged[qckey.proportion(qckey.no_perf(qckey.motherboard_failure_total))] = merged[qckey.no_perf(qckey.motherboard_failure_total)]  / merged[qckey.no_perf(qckey.total)]
merged[qckey.proportion(qckey.no_perf(qckey.screen_display_exception_total))] = merged[qckey.no_perf(qckey.screen_display_exception_total)]  / merged[qckey.no_perf(qckey.total)]

merged[qckey.proportion(qckey.no_perf(qckey.total_fault))] = (merged[qckey.no_perf(qckey.screen_stripes_blurry_splash_total)] 
                               + merged[qckey.no_perf(qckey.touch_exception_total)]
                               + merged[qckey.no_perf(qckey.boot_exception_total)] 
                               + merged[qckey.no_perf(qckey.boot_repeat_total)]
                               + merged[qckey.no_perf(qckey.auto_shutdown_restart_total)] 
                               + merged[qckey.no_perf(qckey.cannot_into_sys_total)] 
                               + merged[qckey.no_perf(qckey.fast_power_consumption_total)]  
                               + merged[qckey.no_perf(qckey.motherboard_failure_total)]  
                               + merged[qckey.no_perf(qckey.screen_display_exception_total)]) / merged[qckey.no_perf(qckey.total)]

st.write(merged)


merged.set_index('日期', inplace=True)
st.markdown(f"### {qckey.total_fault}")
st.markdown(f"#### 整体")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.total_fault)),
                         qckey.proportion(qckey.perf(qckey.total_fault)),
                         qckey.proportion(qckey.no_perf(qckey.total_fault))
                         ]], use_container_width=True)
st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.total_fault_ios)),
                         qckey.proportion(qckey.perf(qckey.total_fault_ios)),
                         qckey.proportion(qckey.no_perf(qckey.total_fault_ios))
                         ]], use_container_width=True)
st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.total_fault_andr)),
                         qckey.proportion(qckey.perf(qckey.total_fault_andr)),
                         qckey.proportion(qckey.no_perf(qckey.total_fault_andr))
                         ]], use_container_width=True)


st.markdown(f"### {qckey.screen_stripes_blurry_splash_total}")
st.markdown(f"#### 整体")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.screen_stripes_blurry_splash_total)),
                         qckey.proportion(qckey.perf(qckey.screen_stripes_blurry_splash_total)),
                         qckey.proportion(qckey.no_perf(qckey.screen_stripes_blurry_splash_total))
                         ]], use_container_width=True)
st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.screen_stripes_blurry_splash_ios)),
                         qckey.proportion(qckey.perf(qckey.screen_stripes_blurry_splash_ios)),
                         qckey.proportion(qckey.no_perf(qckey.screen_stripes_blurry_splash_ios))
                         ]], use_container_width=True)

st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.screen_stripes_blurry_splash_andr)),
                         qckey.proportion(qckey.perf(qckey.screen_stripes_blurry_splash_andr)),
                         qckey.proportion(qckey.no_perf(qckey.screen_stripes_blurry_splash_andr))
                         ]], use_container_width=True)

st.markdown(f"### {qckey.touch_exception_total}")
st.markdown(f"#### 整体")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.touch_exception_total)),
                         qckey.proportion(qckey.perf(qckey.touch_exception_total)),
                         qckey.proportion(qckey.no_perf(qckey.touch_exception_total))
                         ]], use_container_width=True)

st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.touch_exception_ios)),
                         qckey.proportion(qckey.perf(qckey.touch_exception_ios)),
                         qckey.proportion(qckey.no_perf(qckey.touch_exception_ios)),
                         ]], use_container_width=True)

st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.touch_exception_andr)),
                         qckey.proportion(qckey.perf(qckey.touch_exception_andr)),
                         qckey.proportion(qckey.no_perf(qckey.touch_exception_andr))
                         ]], use_container_width=True)

st.markdown(f"### {qckey.boot_exception_total}")
st.markdown(f"#### 整体")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.boot_exception_total)),
                         qckey.proportion(qckey.perf(qckey.boot_exception_total)),
                         qckey.proportion(qckey.no_perf(qckey.boot_exception_total))
                         ]], use_container_width=True)

st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.boot_exception_ios)),
                         qckey.proportion(qckey.perf(qckey.boot_exception_ios)),
                         qckey.proportion(qckey.no_perf(qckey.boot_exception_ios))
                         ]], use_container_width=True)

st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.boot_exception_andr)),
                         qckey.proportion(qckey.perf(qckey.boot_exception_andr)),
                         qckey.proportion(qckey.no_perf(qckey.boot_exception_andr))
                         ]], use_container_width=True)

st.markdown(f"### {qckey.boot_repeat_total}")
st.markdown(f"#### 整体")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.boot_repeat_total)),
                         qckey.proportion(qckey.perf(qckey.boot_repeat_total)),
                         qckey.proportion(qckey.no_perf(qckey.boot_repeat_total))
                         ]], use_container_width=True)

st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.boot_repeat_ios)),
                         qckey.proportion(qckey.perf(qckey.boot_repeat_ios)),
                         qckey.proportion(qckey.no_perf(qckey.boot_repeat_ios))
                         ]], use_container_width=True)

st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.boot_repeat_andr)),
                         qckey.proportion(qckey.perf(qckey.boot_repeat_andr)),
                         qckey.proportion(qckey.no_perf(qckey.boot_repeat_andr))
                         ]], use_container_width=True)

st.markdown(f"### {qckey.auto_shutdown_restart_total}")
st.markdown(f"#### 整体")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.auto_shutdown_restart_total)),
                         qckey.proportion(qckey.perf(qckey.auto_shutdown_restart_total)),
                         qckey.proportion(qckey.no_perf(qckey.auto_shutdown_restart_total))
                         ]], use_container_width=True)
st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.auto_shutdown_restart_ios)),
                         qckey.proportion(qckey.perf(qckey.auto_shutdown_restart_ios)),
                         qckey.proportion(qckey.no_perf(qckey.auto_shutdown_restart_ios))
                         ]], use_container_width=True)

st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.auto_shutdown_restart_andr)),
                         qckey.proportion(qckey.perf(qckey.auto_shutdown_restart_andr)),
                         qckey.proportion(qckey.no_perf(qckey.auto_shutdown_restart_andr))
                         ]], use_container_width=True)

st.markdown(f"### {qckey.cannot_into_sys_total}")
st.markdown(f"#### 整体")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.cannot_into_sys_total)),
                         qckey.proportion(qckey.perf(qckey.cannot_into_sys_total)),
                         qckey.proportion(qckey.no_perf(qckey.cannot_into_sys_total))
                         ]], use_container_width=True)

st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.cannot_into_sys_ios)),
                         qckey.proportion(qckey.perf(qckey.cannot_into_sys_ios)),
                         qckey.proportion(qckey.no_perf(qckey.cannot_into_sys_ios))
                         ]], use_container_width=True)
st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.cannot_into_sys_andr)),
                         qckey.proportion(qckey.perf(qckey.cannot_into_sys_andr)),
                         qckey.proportion(qckey.no_perf(qckey.cannot_into_sys_andr))
                         ]], use_container_width=True)

st.markdown(f"### {qckey.fast_power_consumption_total}")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.total_fast_power_consumption_total)),
                         qckey.proportion(qckey.perf(qckey.fast_power_consumption_total)),
                         qckey.proportion(qckey.no_perf(qckey.fast_power_consumption_total))
                         ]], use_container_width=True)

st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.total_fast_power_consumption_ios)),
                         qckey.proportion(qckey.perf(qckey.total_fast_power_consumption_ios)),
                         qckey.proportion(qckey.no_perf(qckey.total_fast_power_consumption_ios))
                         ]], use_container_width=True)
st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.total_fast_power_consumption_andr)),
                         qckey.proportion(qckey.perf(qckey.fast_power_consumption_andr)),
                         qckey.proportion(qckey.no_perf(qckey.fast_power_consumption_andr))
                         ]], use_container_width=True)

st.markdown(f"### {qckey.motherboard_failure_total}")
st.markdown(f"#### 整体")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.motherboard_failure_total)),
                         qckey.proportion(qckey.perf(qckey.motherboard_failure_total)),
                         qckey.proportion(qckey.no_perf(qckey.motherboard_failure_total))
                         ]], use_container_width=True)

st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.motherboard_failure_ios)),
                         qckey.proportion(qckey.perf(qckey.motherboard_failure_ios)),
                         qckey.proportion(qckey.no_perf(qckey.motherboard_failure_ios))
                         ]], use_container_width=True)

st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.motherboard_failure_andr)),
                         qckey.proportion(qckey.perf(qckey.motherboard_failure_andr)),
                         qckey.proportion(qckey.no_perf(qckey.motherboard_failure_andr))
                         ]], use_container_width=True)

st.markdown(f"### {qckey.screen_display_exception_total}")
st.markdown(f"#### 整体")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.screen_display_exception_total)),
                         qckey.proportion(qckey.perf(qckey.screen_display_exception_total)),
                         qckey.proportion(qckey.no_perf(qckey.screen_display_exception_total))
                         ]], use_container_width=True)

st.markdown(f"#### iOS")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.screen_display_exception_ios)),
                         qckey.proportion(qckey.perf(qckey.screen_display_exception_ios)),
                         qckey.proportion(qckey.no_perf(qckey.screen_display_exception_ios))
                         ]], use_container_width=True)

st.markdown(f"#### Android")
st.line_chart(merged[[   qckey.proportion(qckey.all(qckey.screen_display_exception_andr)),
                         qckey.proportion(qckey.perf(qckey.screen_display_exception_andr)),
                         qckey.proportion(qckey.no_perf(qckey.screen_display_exception_andr))
                         ]], use_container_width=True)
