import json
import sys
import pprint

device_health_cycle_map = {}
health_cycle_map = {}

def preprocess(file_path):
  global device_health_cycle_map
  global health_cycle_map
  index = 1
  with open(file_path) as f:
    line = f.readline()
    while line:
      json_str = line.split("\t")[1]
      if json_str != '原始数据':
        json_obj = json.loads(json_str)
        device_name = json_obj["ios_type"]["origin"]
        cycle_count = json_obj["cdcs"]["read"]
        health = json_obj["dcxl"]["read"]
        print(f"line {index} -- {device_name}----{cycle_count}----{health}")
        if device_name in device_health_cycle_map.keys():
            device_health_cycle_map[device_name].add(f"{health}_{cycle_count}")
        else:
            device_health_cycle_map[device_name] = set()

        if health in health_cycle_map.keys():
            health_cycle_map[health].add(cycle_count)
        else:
           health_cycle_map[health] = set()

        index += 1


      line = f.readline()


  
if __name__ == "__main__":
  preprocess(sys.argv[1])

  # change device_health_cycle_map all set value to list
  for key in device_health_cycle_map.keys():
    device_health_cycle_map[key] = list(device_health_cycle_map[key])

  # change health_cycle_map all set value to list
  for key in health_cycle_map.keys():
    health_cycle_map[key] = list(health_cycle_map[key])

  with open("device_health_cycle_map.json", "w") as f:
    f.write(pprint.pformat(device_health_cycle_map))

  with open("health_cycle_map.json", "w") as f:
    f.write(pprint.pformat(health_cycle_map))