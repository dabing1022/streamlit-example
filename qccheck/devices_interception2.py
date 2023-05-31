import json
from datetime import datetime

now_date = '2023-05-31'

# file_name = "1.txt"
# file_ready_name = "1_ready.txt"
# file_csv_name = "1.csv"
# rule = 'i2c2'

# file_name = "2.txt"
# file_ready_name = "2_ready.txt"
# file_csv_name = "2.csv"
# rule = 'multiple entries holding the registry busy, IOKit termination queue depth 0'


file_name = "3.txt"
file_ready_name = "3_ready.txt"
file_csv_name = "3.csv"
rule = 'i2c3'

date_imeis = {}

# 重新整理数据
line_index = 0
with open(file_name, 'r') as f:
    contents = f.readlines()
    final_contents = []
    for line in contents:
        if line_index == 0:
          final_contents.append(line)
        else:
          if line_index % 2 == 1:
            if line_index + 1 < len(contents):
                next_line = contents[line_index + 1]
                join_line = line.rstrip() + next_line
                final_contents.append(join_line)
        line_index += 1

    final_content_str = ''.join(final_contents)
    with open(file_ready_name, 'w') as f:
       f.write(final_content_str)


with open(file_ready_name, 'r') as f:
    for line in f.readlines():
        try:
          content_list = line.split('\t')
          origin_content = content_list[5]
          create_date = content_list[6][:10]
          imei = content_list[1]
          if origin_content == 'origin_content':
            continue
          panic_string_list = json.loads(origin_content)
        except:
          continue
        for content in panic_string_list:
            date = content['date']
            panic = content['panicString']
            # date is like "2023-05-08 01:44:44"
            # now is '2023-05-10'
            date = date[:10]
            d1 = datetime.strptime(now_date, '%Y-%m-%d')
            d2 = datetime.strptime(date, '%Y-%m-%d')
            delta = d1 - d2
            if (delta.days <= 180):
                if rule in panic:
                  date_imeis.setdefault(create_date, []).append(imei)  


date_imeis_count = {}
csv_contents = []
csv_contents.append('date,count')
for date, imeis in date_imeis.items():
    date_imeis_count[date] = len(set(imeis))
    csv_contents.append(date + ',' + str(len(set(imeis))))

with open(file_csv_name, 'w') as f:
    f.write('\n'.join(csv_contents))