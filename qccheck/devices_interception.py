import json
from datetime import datetime
from pprint import pprint
from operator import itemgetter

total_imeis = set()
# 统计日志规则命中的imei数
rules = [
  # done
   'AOP PANIC',
   'Missing sensor(s)',
   'AppleSocHot',
   'AOP data abort',
   'Kernel data abort',
   'SEP Panic',
   'AppleSEPManager panic for AppleSEPKeyStore: sks request timeout',

  # to do
   'WDT timeout',
   'userspace watchdog timeout: no successful checkins from SpringBoard',
   'Unexpected fault in kernel static region',
   'Sleep/Wake hang detected',
   'Halt/Restart Timed Out',
   'memorystatus_jetsam_thread: no victim',
   'mbuf_watchdog',
   'AppleCS35L26Amp::setPowerState',
   'AppleHydra: could not find system ID: bad IPC message ID',
   'ANS2 Recoverable Panic',
   'DCP PANIC',
   'SMC PANIC',
   'AOP NMI FIQ',
   'AMCC PLANE3 PIO request with RO flag set error',
   'i2c2::_checkBusStatus Bus is still in a bad state',
   'i2c2::_runInterruptMode Timed out waiting for interrupt',
   'i2c3::_checkBusStatus SCL is stuck low',
   'LLC Bus error from cpu',
   'AppleCS46L0xDevice::setPowerState',
   'AppleBCMWLANBusInterfacePCIe::reset()',
   'ANS NMI: ep ANSEndpoint1 - unknown reason',
   'vnode_rele_ext',
   
]

rule_count_map = {}

with open('panic_athena_log.txt', 'r') as f:
    for line in f.readlines():
        try:
          content_list = line.split('\t')
          origin_content = content_list[5]
          imei = content_list[1]
          if origin_content == 'origin_content':
            continue
          content_list = json.loads(origin_content)
        except Exception as e:
          continue

        total_imeis.add(imei)
        for content in content_list:
            date = content['date']
            panic = content['panicString']
            for rule in rules:
              if rule in panic:
                rule_count_map[rule] = rule_count_map.get(rule, []) + [imei]

rule_count_map = {k: len(set(v)) for k, v in rule_count_map.items()}

print('总imei数：', len(total_imeis))
sorted_rule_count_map = dict(sorted(rule_count_map.items(), key=itemgetter(1), reverse=True))
for k, v in sorted_rule_count_map.items():
  print(f"{k}: {v} ({v/len(total_imeis)*100:.2f}%)")

print("============================dot csv format ============================")
print("规则,命中数")
for k, v in sorted_rule_count_map.items():
  print(f"{k},{v}")

print('总命中数：', sum(sorted_rule_count_map.values()))



# /* 被拦截明细，但不一定已经提交报告 */
# SELECT 
# 	dt AS `日期`,
# 	datapool['romos'] as `系统`,
# 	datapool['qccode'] as `质检码`,
# 	datapool['imei'] as `imei`,
# 	concat_ws("," , collect_list(cast(datapool['value'] as string))) `命中崩溃日志值`
# from hdp_zhuanzhuan_dw_global.dw_log_server_action_1d
# where dt = ${hiveconf:target_date} AND region='q' and action='qc_crash'
# group by dt, datapool['qccode'], datapool['imei'],datapool['romos']
# ORDER by `系统` ASC
# LIMIT 1000;