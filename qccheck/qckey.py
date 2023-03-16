total = "质检设备总量"
total_ios = "质检设备总量-ios"
total_andr = "质检设备总量-android"

total_fault = "所有故障"
total_fault_ios = "所有故障-ios"
total_fault_andr = "所有故障-android"

screen_stripes_blurry_splash_total = "条纹/花屏/闪屏"
screen_stripes_blurry_splash_ios = "条纹/花屏/闪屏(ios)"
screen_stripes_blurry_splash_andr = "条纹/花屏/闪屏(android)"

touch_exception_total = "触摸异常"
touch_exception_ios = "触摸异常(ios)"
touch_exception_andr = "触摸异常(android)"

boot_exception_total = "不开机"
boot_exception_ios = "不开机(ios)"
boot_exception_andr = "不开机(android)"

boot_repeat_total = "反复重启"
boot_repeat_ios = "反复重启(ios)"
boot_repeat_andr = "反复重启(android)"

auto_shutdown_restart_total = "自动关机/重启"
auto_shutdown_restart_ios = "自动关机/重启(ios)"
auto_shutdown_restart_andr = "自动关机/重启(android)"

cannot_into_sys_total = "无法进入系统"
cannot_into_sys_ios = "无法进入系统(ios)"
cannot_into_sys_andr = "无法进入系统(android)"

fast_power_consumption_total = "耗电快"
fast_power_consumption_ios = "耗电快(ios)"
fast_power_consumption_andr = "耗电快(android)"

motherboard_failure_total = "主板故障"
motherboard_failure_ios = "主板故障(ios)"
motherboard_failure_andr = "主板故障(android)"

screen_display_exception_total = "屏幕无法正常显示"
screen_display_exception_ios = "屏幕无法正常显示(ios)"
screen_display_exception_andr = "屏幕无法正常显示(android)"

date = "日期"

merge_suffix_perf = "-perf"
merge_suffix_noperf = "-noperf"
merge_suffix_all = "-all"
def proportion(key):
    return key + "-占比"


def no_perf(key):
    return key + "-noperf"

def perf(key):
    return key + "-perf"

def all(key):
    return key + "-all"