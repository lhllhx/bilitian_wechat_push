# BiliBiliHelper Python Version
# Copy right (c) 2019 TheWanderingCoel
# 直接在git的项目改的,测试要要清理配置文件很烦。
# 干脆写一个小脚本,快速删除重要信息

import os
from configobj import ConfigObj

config = ConfigObj(os.getcwd()+"/BiliBiliHelper.conf")

config['SCKEY']['SCKEY'] = ""
config["Account"]["BILIBILI_USER"] = ""
config["Account"]["BILIBILI_PASSWORD"] = ""
config["Token"]["ACCESS_TOKEN"] = ""
config["Token"]["REFRESH_TOKEN"] = ""
config["Token"]["CSRF"] = ""
config["Token"]["UID"] = ""
config["Token"]["COOKIE"] = ""
config["pcheaders"]["cookie"] = ""
config.write()