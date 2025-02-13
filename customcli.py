"""
this is customcli.py and made by givemetocode
github: givemetocode-net-hk/customOSopensource

"""
from rich.prompt import Prompt
from datetime import datetime
import json
import yaml
from datetime import datetime
import pytz
def create_utc_offset_map():
    utc_offset_map = {}
    for tz in pytz.all_timezones:
        timezone = pytz.timezone(tz)
        offset = timezone.utcoffset(datetime.now()).total_seconds() / 3600
        utc_offset_map[f"UTC{int(offset):+d}"] = tz
    return utc_offset_map

def gettime() :
	utc_offset_map = create_utc_offset_map()
	# Load the configuration from config.yaml
	with open('config.yaml', 'r') as file:
		config = yaml.safe_load(file)
	timezone_str = config['settings']['timezone'] if config['settings']['timezone'] else 'UTC+8'
	timezone_name = utc_offset_map.get(timezone_str, 'Asia/Singapore')  #set timezone to Asia/Singapore
	timezone = pytz.timezone(timezone_name)
	now = datetime.now(timezone)
	date_time = now.strftime("%m/%d/%Y_%H:%M:%S")
