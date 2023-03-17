import streamlit as st
import pandas as pd
import numpy as np
from qccheck import qckey
from streamlit_echarts import st_echarts

uploaded_excel_file = st.file_uploader("上传故障检出 Excel 文件", type=["xlsx"])

if uploaded_excel_file is None:
    st.stop()

dataframe = pd.read_excel(uploaded_excel_file)

date_colume = dataframe["日期"]
date_arr = np.array(date_colume)
last_row = dataframe.iloc[-1]

# ------------------------------

dataframe[qckey.proportion(qckey.screen_stripes_blurry_splash_ios)] = dataframe[qckey.screen_stripes_blurry_splash_ios]  / dataframe[qckey.total_ios]
dataframe[qckey.proportion(qckey.touch_exception_ios)] = dataframe[qckey.touch_exception_ios]  / dataframe[qckey.total_ios]
dataframe[qckey.proportion(qckey.boot_exception_ios)] = dataframe[qckey.boot_exception_ios]  / dataframe[qckey.total_ios]
dataframe[qckey.proportion(qckey.boot_repeat_ios)] = dataframe[qckey.boot_repeat_ios]  / dataframe[qckey.total_ios]
dataframe[qckey.proportion(qckey.auto_shutdown_restart_ios)] = dataframe[qckey.auto_shutdown_restart_ios]  / dataframe[qckey.total_ios]
dataframe[qckey.proportion(qckey.cannot_into_sys_ios)] = dataframe[qckey.cannot_into_sys_ios]  / dataframe[qckey.total_ios]
dataframe[qckey.proportion(qckey.fast_power_consumption_ios)] = dataframe[qckey.fast_power_consumption_ios]  / dataframe[qckey.total_ios]
dataframe[qckey.proportion(qckey.motherboard_failure_ios)] = dataframe[qckey.motherboard_failure_ios]  / dataframe[qckey.total_ios]
dataframe[qckey.proportion(qckey.screen_display_exception_ios)] = dataframe[qckey.screen_display_exception_ios]  / dataframe[qckey.total_ios]

dataframe[qckey.proportion(qckey.total_fault_ios)] = (dataframe[qckey.screen_stripes_blurry_splash_ios] 
                               + dataframe[qckey.touch_exception_ios]
                               + dataframe[qckey.boot_exception_ios] 
                               + dataframe[qckey.boot_repeat_ios]
                               + dataframe[qckey.auto_shutdown_restart_ios] 
                               + dataframe[qckey.cannot_into_sys_ios] 
                               + dataframe[qckey.fast_power_consumption_ios]  
                               + dataframe[qckey.motherboard_failure_ios]  
                               + dataframe[qckey.screen_display_exception_ios]) / dataframe[qckey.total_ios]

# ------------------------------

dataframe[qckey.proportion(qckey.screen_stripes_blurry_splash_andr)] = dataframe[qckey.screen_stripes_blurry_splash_andr]  / dataframe[qckey.total_andr]
dataframe[qckey.proportion(qckey.touch_exception_andr)] = dataframe[qckey.touch_exception_andr]  / dataframe[qckey.total_andr]
dataframe[qckey.proportion(qckey.boot_exception_andr)] = dataframe[qckey.boot_exception_andr]  / dataframe[qckey.total_andr]
dataframe[qckey.proportion(qckey.boot_repeat_andr)] = dataframe[qckey.boot_repeat_andr]  / dataframe[qckey.total_andr]
dataframe[qckey.proportion(qckey.auto_shutdown_restart_andr)] = dataframe[qckey.auto_shutdown_restart_andr]  / dataframe[qckey.total_andr]
dataframe[qckey.proportion(qckey.cannot_into_sys_andr)] = dataframe[qckey.cannot_into_sys_andr]  / dataframe[qckey.total_andr]
dataframe[qckey.proportion(qckey.fast_power_consumption_andr)] = dataframe[qckey.fast_power_consumption_andr]  / dataframe[qckey.total_andr]
dataframe[qckey.proportion(qckey.motherboard_failure_andr)] = dataframe[qckey.motherboard_failure_andr]  / dataframe[qckey.total_andr]
dataframe[qckey.proportion(qckey.screen_display_exception_andr)] = dataframe[qckey.screen_display_exception_andr]  / dataframe[qckey.total_andr]

dataframe[qckey.proportion(qckey.total_fault_andr)] = (dataframe[qckey.screen_stripes_blurry_splash_andr] 
                               + dataframe[qckey.touch_exception_andr]
                               + dataframe[qckey.boot_exception_andr] 
                               + dataframe[qckey.boot_repeat_andr]
                               + dataframe[qckey.auto_shutdown_restart_andr] 
                               + dataframe[qckey.cannot_into_sys_andr] 
                               + dataframe[qckey.fast_power_consumption_andr]  
                               + dataframe[qckey.motherboard_failure_andr]  
                               + dataframe[qckey.screen_display_exception_andr]) / dataframe[qckey.total_andr]


# ------------------------------
dataframe[qckey.proportion(qckey.screen_stripes_blurry_splash_total)] = dataframe[qckey.screen_stripes_blurry_splash_total]  / dataframe[qckey.total]
dataframe[qckey.proportion(qckey.touch_exception_total)] = dataframe[qckey.touch_exception_total]  / dataframe[qckey.total]
dataframe[qckey.proportion(qckey.boot_exception_total)] = dataframe[qckey.boot_exception_total]  / dataframe[qckey.total]
dataframe[qckey.proportion(qckey.boot_repeat_total)] = dataframe[qckey.boot_repeat_total]  / dataframe[qckey.total]
dataframe[qckey.proportion(qckey.auto_shutdown_restart_total)] = dataframe[qckey.auto_shutdown_restart_total]  / dataframe[qckey.total]
dataframe[qckey.proportion(qckey.cannot_into_sys_total)] = dataframe[qckey.cannot_into_sys_total]  / dataframe[qckey.total]
dataframe[qckey.proportion(qckey.fast_power_consumption_total)] = dataframe[qckey.fast_power_consumption_total]  / dataframe[qckey.total]
dataframe[qckey.proportion(qckey.motherboard_failure_total)] = dataframe[qckey.motherboard_failure_total]  / dataframe[qckey.total]
dataframe[qckey.proportion(qckey.screen_display_exception_total)] = dataframe[qckey.screen_display_exception_total]  / dataframe[qckey.total]

dataframe[qckey.proportion(qckey.total_fault)] = (dataframe[qckey.screen_stripes_blurry_splash_total] 
                               + dataframe[qckey.touch_exception_total]
                               + dataframe[qckey.boot_exception_total] 
                               + dataframe[qckey.boot_repeat_total]
                               + dataframe[qckey.auto_shutdown_restart_total] 
                               + dataframe[qckey.cannot_into_sys_total] 
                               + dataframe[qckey.fast_power_consumption_total]  
                               + dataframe[qckey.motherboard_failure_total]  
                               + dataframe[qckey.screen_display_exception_total]) / dataframe[qckey.total]

dataframe.fillna(0, inplace=True)
st.write(dataframe)

dataframe.set_index('日期', inplace=True)
st.markdown("### 整体故障检出率")
st.line_chart(dataframe[[qckey.proportion(qckey.total_fault),
                         qckey.proportion(qckey.screen_stripes_blurry_splash_total),
                         qckey.proportion(qckey.touch_exception_total),
                         qckey.proportion(qckey.boot_exception_total),
                         qckey.proportion(qckey.boot_repeat_total),
                         qckey.proportion(qckey.auto_shutdown_restart_total),
                         qckey.proportion(qckey.cannot_into_sys_total),
                         qckey.proportion(qckey.fast_power_consumption_total),
                         qckey.proportion(qckey.motherboard_failure_total),
                         qckey.proportion(qckey.screen_display_exception_total),
                         ]], use_container_width=True)

total_check_rate_option_xAxis_data = date_arr.astype(str).tolist()
total_check_rate_option_legend_data = [
    qckey.proportion(qckey.total_fault),
    qckey.proportion(qckey.screen_stripes_blurry_splash_total),
    qckey.proportion(qckey.touch_exception_total),
    qckey.proportion(qckey.boot_exception_total),
    qckey.proportion(qckey.boot_repeat_total),
    qckey.proportion(qckey.auto_shutdown_restart_total),
    qckey.proportion(qckey.cannot_into_sys_total),
    qckey.proportion(qckey.fast_power_consumption_total),
    qckey.proportion(qckey.motherboard_failure_total),
    qckey.proportion(qckey.screen_display_exception_total)
]
total_check_rate_option_series = []
data = np.array(dataframe[qckey.proportion(qckey.total_fault)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.total_fault), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.screen_stripes_blurry_splash_total)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.screen_stripes_blurry_splash_total), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.touch_exception_total)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.touch_exception_total), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.boot_exception_total)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.boot_exception_total), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.boot_repeat_total)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.boot_repeat_total), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.auto_shutdown_restart_total)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.auto_shutdown_restart_total), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.cannot_into_sys_total)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.cannot_into_sys_total), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.fast_power_consumption_total)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.fast_power_consumption_total), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.motherboard_failure_total)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.motherboard_failure_total), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.screen_display_exception_total)]).astype(float).tolist()
total_check_rate_option_series.append({ "name": qckey.proportion(qckey.screen_display_exception_total), "type": "line", "data": data })
total_check_rate_option = {
  "title": {
    "text": ''
  },
  "dataZoom": [
    {
      "xAxisIndex": 0
    },
    {
      "yAxisIndex": 0
    }    
  ],
  "tooltip": {
    "trigger": 'axis'
  },
  "legend": {
    "data": total_check_rate_option_legend_data
  },
  "grid": {
    "left": '3%',
    "right": '4%',
    "bottom": '3%',
    "height": "100%",
    "containLabel": "true"
  },
  "toolbox": {
    "feature": {
      "saveAsImage": {}
    }
  },
  "xAxis": {
    "type": 'category',
    "boundaryGap": "false",
    "data": total_check_rate_option_xAxis_data,
  },
  "yAxis": {
    "type": 'value'
  },
  "series": total_check_rate_option_series
};
st_echarts(options=total_check_rate_option)

# ------------------------------


st.markdown("### iOS 故障检出率")

st.line_chart(dataframe[[qckey.proportion(qckey.total_fault_ios),
                         qckey.proportion(qckey.screen_stripes_blurry_splash_ios),
                         qckey.proportion(qckey.touch_exception_ios),
                         qckey.proportion(qckey.boot_exception_ios),
                         qckey.proportion(qckey.boot_repeat_ios),
                         qckey.proportion(qckey.auto_shutdown_restart_ios),
                         qckey.proportion(qckey.cannot_into_sys_ios),
                         qckey.proportion(qckey.fast_power_consumption_ios),
                         qckey.proportion(qckey.motherboard_failure_ios),
                         qckey.proportion(qckey.screen_display_exception_ios),
                         ]], use_container_width=True)

ios_check_rate_option_xAxis_data = date_arr.astype(str).tolist()
ios_check_rate_option_legend_data = [
    qckey.proportion(qckey.total_fault_ios),
    qckey.proportion(qckey.screen_stripes_blurry_splash_ios),
    qckey.proportion(qckey.touch_exception_ios),
    qckey.proportion(qckey.boot_exception_ios),
    qckey.proportion(qckey.boot_repeat_ios),
    qckey.proportion(qckey.auto_shutdown_restart_ios),
    qckey.proportion(qckey.cannot_into_sys_ios),
    qckey.proportion(qckey.fast_power_consumption_ios),
    qckey.proportion(qckey.motherboard_failure_ios),
    qckey.proportion(qckey.screen_display_exception_ios)
]
ios_check_rate_option_series = []
data = np.array(dataframe[qckey.proportion(qckey.total_fault_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.total_fault_ios), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.screen_stripes_blurry_splash_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.screen_stripes_blurry_splash_ios), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.touch_exception_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.touch_exception_ios), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.boot_exception_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.boot_exception_ios), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.boot_repeat_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.boot_repeat_ios), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.auto_shutdown_restart_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.auto_shutdown_restart_ios), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.cannot_into_sys_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.cannot_into_sys_ios), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.fast_power_consumption_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.fast_power_consumption_ios), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.motherboard_failure_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.motherboard_failure_ios), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.screen_display_exception_ios)]).astype(float).tolist()
ios_check_rate_option_series.append({ "name": qckey.proportion(qckey.screen_display_exception_ios), "type": "line", "data": data })
ios_check_rate_option = {
  "title": {
    "text": ''
  },
  "dataZoom": [
    {
      "xAxisIndex": 0
    },
    {
      "yAxisIndex": 0
    }    
  ],  
  "tooltip": {
    "trigger": 'axis'
  },
  "legend": {
    "data": ios_check_rate_option_legend_data
  },
  "grid": {
    "left": '3%',
    "right": '4%',
    "bottom": '3%',
    "height": "100%",
    "containLabel": "true"
  },
  "toolbox": {
    "feature": {
      "saveAsImage": {}
    }
  },
  "xAxis": {
    "type": 'category',
    "boundaryGap": "false",
    "data": ios_check_rate_option_xAxis_data,
  },
  "yAxis": {
    "type": 'value'
  },
  "series": ios_check_rate_option_series
};
st_echarts(options=ios_check_rate_option)




st.markdown("### Android 故障检出率")

st.line_chart(dataframe[[qckey.proportion(qckey.total_fault_andr),
                         qckey.proportion(qckey.screen_stripes_blurry_splash_andr),
                         qckey.proportion(qckey.touch_exception_andr),
                         qckey.proportion(qckey.boot_exception_andr),
                         qckey.proportion(qckey.boot_repeat_andr),
                         qckey.proportion(qckey.auto_shutdown_restart_andr),
                         qckey.proportion(qckey.cannot_into_sys_andr),
                         qckey.proportion(qckey.fast_power_consumption_andr),
                         qckey.proportion(qckey.motherboard_failure_andr),
                         qckey.proportion(qckey.screen_display_exception_andr),
                         ]], use_container_width=True)

andr_check_rate_option_xAxis_data = date_arr.astype(str).tolist()
andr_check_rate_option_legend_data = [
    qckey.proportion(qckey.total_fault_andr),
    qckey.proportion(qckey.screen_stripes_blurry_splash_andr),
    qckey.proportion(qckey.touch_exception_andr),
    qckey.proportion(qckey.boot_exception_andr),
    qckey.proportion(qckey.boot_repeat_andr),
    qckey.proportion(qckey.auto_shutdown_restart_andr),
    qckey.proportion(qckey.cannot_into_sys_andr),
    qckey.proportion(qckey.fast_power_consumption_andr),
    qckey.proportion(qckey.motherboard_failure_andr),
    qckey.proportion(qckey.screen_display_exception_andr)
]
andr_check_rate_option_series = []
data = np.array(dataframe[qckey.proportion(qckey.total_fault_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.total_fault_andr), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.screen_stripes_blurry_splash_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.screen_stripes_blurry_splash_andr), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.touch_exception_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.touch_exception_andr), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.boot_exception_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.boot_exception_andr), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.boot_repeat_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.boot_repeat_andr), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.auto_shutdown_restart_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.auto_shutdown_restart_andr), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.cannot_into_sys_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.cannot_into_sys_andr), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.fast_power_consumption_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.fast_power_consumption_andr), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.motherboard_failure_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.motherboard_failure_andr), "type": "line", "data": data })
data = np.array(dataframe[qckey.proportion(qckey.screen_display_exception_andr)]).astype(float).tolist()
andr_check_rate_option_series.append({ "name": qckey.proportion(qckey.screen_display_exception_andr), "type": "line", "data": data })
andr_check_rate_option = {
  "title": {
    "text": ''
  },
  "dataZoom": [
    {
      "xAxisIndex": 0
    },
    {
      "yAxisIndex": 0
    }    
  ],  
  "tooltip": {
    "trigger": 'axis'
  },
  "legend": {
    "data": andr_check_rate_option_legend_data
  },
  "grid": {
    "left": '3%',
    "right": '4%',
    "bottom": '3%',
    "height": "100%",
    "containLabel": "true"
  },
  "toolbox": {
    "feature": {
      "saveAsImage": {}
    }
  },
  "xAxis": {
    "type": 'category',
    "boundaryGap": "false",
    "data": andr_check_rate_option_xAxis_data,
  },
  "yAxis": {
    "type": 'value'
  },
  "series": andr_check_rate_option_series
};
st_echarts(options=andr_check_rate_option)

# -------------------------------------------------------------


last_date = date_arr[-1]
st.markdown(f"### {last_date} 整体故障占比 Pie 图")
total_option_data = []
total_option_data.append({ "value": int(last_row[qckey.screen_stripes_blurry_splash_total]), "name": qckey.screen_stripes_blurry_splash_total })
total_option_data.append({ "value": int(last_row[qckey.touch_exception_total]), "name": qckey.touch_exception_total })
total_option_data.append({ "value": int(last_row[qckey.boot_exception_total]), "name": qckey.boot_exception_total })
total_option_data.append({ "value": int(last_row[qckey.boot_repeat_total]), "name": qckey.boot_repeat_total })
total_option_data.append({ "value": int(last_row[qckey.auto_shutdown_restart_total]), "name": qckey.auto_shutdown_restart_total })
total_option_data.append({ "value": int(last_row[qckey.cannot_into_sys_total]), "name": qckey.cannot_into_sys_total })
total_option_data.append({ "value": int(last_row[qckey.fast_power_consumption_total]), "name": qckey.fast_power_consumption_total })
total_option_data.append({ "value": int(last_row[qckey.motherboard_failure_total]), "name": qckey.motherboard_failure_total })
total_option_data.append({ "value": int(last_row[qckey.screen_display_exception_total]), "name": qckey.screen_display_exception_total })

total_option = {
  "tooltip": {
    "trigger": 'item'
  },
  "legend": {
    "top": '5%',
    "left": 'center'
  },
  "series": [
    {
      "name": '隐性故障',
      "type": 'pie',
      "radius": ['40%', '70%'],
      "avoidLabelOverlap": "true",
      "itemStyle": {
        "borderRadius": 10,
        "borderColor": '#fff',
        "borderWidth": 2
      },
      "label": {
        "show": "false",
        "position": 'center'
      },
      "emphasis": {
        "label": {
          "show": "true",
          "fontSize": 40,
          "fontWeight": 'bold'
        }
      },
      "labelLine": {
        "show": "false"
      },
      "data": total_option_data
    }
  ]
};
st_echarts(options=total_option)


st.markdown(f"### {last_date} iOS故障占比 Pie 图")
ios_option_data = []
ios_option_data.append({ "value": int(last_row[qckey.screen_stripes_blurry_splash_ios]), "name": qckey.screen_stripes_blurry_splash_ios })
ios_option_data.append({ "value": int(last_row[qckey.touch_exception_ios]), "name": qckey.touch_exception_ios })
ios_option_data.append({ "value": int(last_row[qckey.boot_exception_ios]), "name": qckey.boot_exception_ios })
ios_option_data.append({ "value": int(last_row[qckey.boot_repeat_ios]), "name": qckey.boot_repeat_ios })
ios_option_data.append({ "value": int(last_row[qckey.auto_shutdown_restart_ios]), "name": qckey.auto_shutdown_restart_ios })
ios_option_data.append({ "value": int(last_row[qckey.cannot_into_sys_ios]), "name": qckey.cannot_into_sys_ios })
ios_option_data.append({ "value": int(last_row[qckey.fast_power_consumption_ios]), "name": qckey.fast_power_consumption_ios })
ios_option_data.append({ "value": int(last_row[qckey.motherboard_failure_ios]), "name": qckey.motherboard_failure_ios })
ios_option_data.append({ "value": int(last_row[qckey.screen_display_exception_ios]), "name": qckey.screen_display_exception_ios })

ios_option = {
  "tooltip": {
    "trigger": 'item'
  },
  "legend": {
    "top": '5%',
    "left": 'center'
  },
  "series": [
    {
      "name": '隐性故障',
      "type": 'pie',
      "radius": ['40%', '70%'],
      "avoidLabelOverlap": "true",
      "itemStyle": {
        "borderRadius": 10,
        "borderColor": '#fff',
        "borderWidth": 2
      },
      "label": {
        "show": "false",
        "position": 'center'
      },
      "emphasis": {
        "label": {
          "show": "true",
          "fontSize": 40,
          "fontWeight": 'bold'
        }
      },
      "labelLine": {
        "show": "false"
      },
      "data": ios_option_data
    }
  ]
};
st_echarts(options=ios_option)


st.markdown(f"### {last_date} Android故障占比 Pie 图")

andr_option_data = []
andr_option_data.append({ "value": int(last_row[qckey.screen_stripes_blurry_splash_andr]), "name": qckey.screen_stripes_blurry_splash_andr })
andr_option_data.append({ "value": int(last_row[qckey.touch_exception_andr]), "name": qckey.touch_exception_andr })
andr_option_data.append({ "value": int(last_row[qckey.boot_exception_andr]), "name": qckey.boot_exception_andr })
andr_option_data.append({ "value": int(last_row[qckey.boot_repeat_andr]), "name": qckey.boot_repeat_andr })
andr_option_data.append({ "value": int(last_row[qckey.auto_shutdown_restart_andr]), "name": qckey.auto_shutdown_restart_andr })
andr_option_data.append({ "value": int(last_row[qckey.cannot_into_sys_andr]), "name": qckey.cannot_into_sys_andr })
andr_option_data.append({ "value": int(last_row[qckey.fast_power_consumption_andr]), "name": qckey.fast_power_consumption_andr })
andr_option_data.append({ "value": int(last_row[qckey.motherboard_failure_andr]), "name": qckey.motherboard_failure_andr })
andr_option_data.append({ "value": int(last_row[qckey.screen_display_exception_andr]), "name": qckey.screen_display_exception_andr })

andr_option = {
  "tooltip": {
    "trigger": 'item'
  },
  "legend": {
    "top": '5%',
    "left": 'center'
  },
  "series": [
    {
      "name": '隐性故障',
      "type": 'pie',
      "radius": ['40%', '70%'],
      "avoidLabelOverlap": "true",
      "itemStyle": {
        "borderRadius": 10,
        "borderColor": '#fff',
        "borderWidth": 2
      },
      "label": {
        "show": "false",
        "position": 'center'
      },
      "emphasis": {
        "label": {
          "show": "true",
          "fontSize": 40,
          "fontWeight": 'bold'
        }
      },
      "labelLine": {
        "show": "false"
      },
      "data": andr_option_data
    }
  ]
};
st_echarts(options=andr_option)
