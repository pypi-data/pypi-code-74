# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['baidupcs_py',
 'baidupcs_py.app',
 'baidupcs_py.baidupcs',
 'baidupcs_py.commands',
 'baidupcs_py.common']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.1.0,<9.0.0',
 'aget>=0.1.17,<0.2.0',
 'chardet>=4.0.0,<5.0.0',
 'click>=7.1.2,<8.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.25.1,<3.0.0',
 'rich>=9.8.0,<10.0.0',
 'typing-extensions>=3.7.4,<4.0.0']

entry_points = \
{'console_scripts': ['BaiduPCS-Py = baidupcs_py.app:main']}

setup_kwargs = {
    'name': 'baidupcs-py',
    'version': '0.3.8',
    'description': 'Baidu Pcs App',
    'long_description': '# BaiduPCS-Py\n\n[![PyPI version](https://badge.fury.io/py/baidupcs-py.svg)](https://badge.fury.io/py/baidupcs-py)\n![Build](https://github.com/PeterDing/BaiduPCS-Py/workflows/BaiduPCS-Py%20Build%20&%20Test/badge.svg)\n\nA BaiduPCS API and An App\n\nBaiduPCS-Py 是百度网盘 pcs 的非官方 api 和一个命令行运用程序。\n\n> 也是 https://github.com/PeterDing/iScript/blob/master/pan.baidu.com.py 的重构版。\n\n- [安装](#安装)\n- [API](#API)\n- [用法](#用法)\n- [命令别名](#命令别名)\n- [添加用户](#添加用户)\n- [显示当前用户的信息](#显示当前用户的信息)\n- [更新用户信息](#更新用户信息)\n- [显示所有用户](#显示所有用户)\n- [切换当前用户](#切换当前用户)\n- [删除一个用户](#删除一个用户)\n- [文件操作](#文件操作)\n- [显示当前工作目录](#显示当前工作目录)\n- [切换当前工作目录](#切换当前工作目录)\n- [列出网盘路径下的文件](#列出网盘路径下的文件)\n- [搜索文件](#搜索文件)\n- [显示文件内容](#显示文件内容)\n- [创建目录](#创建目录)\n- [移动文件](#移动文件)\n- [文件重命名](#文件重命名)\n- [拷贝文件](#拷贝文件)\n- [删除文件](#删除文件)\n- [下载文件](#下载文件)\n- [播放媒体文件](#播放媒体文件)\n- [上传文件](#上传文件)\n- [同步本地目录到远端](#同步本地目录到远端)\n- [分享文件](#分享文件)\n- [列出分享链接](#列出分享链接)\n- [取消分享链接](#取消分享链接)\n- [保存其他用户分享的链接](#保存其他用户分享的链接)\n- [添加离线下载任务](#添加离线下载任务)\n- [列出离线下载任务](#列出离线下载任务)\n- [清除已经下载完和下载失败的任务](#清除已经下载完和下载失败的任务)\n- [取消下载任务](#取消下载任务)\n- [删除所有离线下载任务](#删除所有离线下载任务)\n\n## 安装\n\n需要 Python 版本大于或等于 3.6\n\n```\npip3 install BaiduPCS-Py\n```\n\n## API\n\nBaiduPCS-Py 的百度网盘 API 只依赖 requests，方便用户开发自己的运用。\n\n```python\nfrom baidupcs_py.baidupcs import BaiduPCSApi\n\napi = BaiduPCSApi(bduss=bduss, cookies=cookies)\n```\n\n## 用法\n\n```\nBaiduPCS-Py --help\n```\n\n## 命令别名\n\n可以用下面的命令别名代替原来的命令名。\n\n| 别名 | 原名         |\n| ---- | ------------ |\n| w    | who          |\n| uu   | updateuser   |\n| su   | su           |\n| ul   | userlist     |\n| ua   | useradd      |\n| ud   | userdel      |\n| l    | ls           |\n| f    | search       |\n| md   | mkdir        |\n| mv   | move         |\n| rn   | rename       |\n| cp   | copy         |\n| rm   | remove       |\n| d    | download     |\n| p    | play         |\n| u    | upload       |\n| sn   | sync         |\n| S    | share        |\n| sl   | shared       |\n| cs   | cancelshared |\n| s    | save         |\n| a    | add          |\n| t    | tasks        |\n| ct   | cleartasks   |\n| cct  | canceltasks  |\n\n## 添加用户\n\nBaiduPCS-Py 目前不支持用帐号登录。需要使用者在 pan.baidu.com 登录后获取 cookies 和其中的 bduss 值，并用命令 `useradd` 为 BaiduPCS-Py 添加一个用户。\n\n使用者可以用下面的方式获取用户的 cookies 和 bduss 值。\n\n1. 登录 pan.baidu.com\n2. 打开浏览器的开发者工具(如 Chrome DevTools)。\n3. 然后选择开发者工具的 Network 面板。\n4. 在登录后的页面中任意点开一个文件夹。\n5. 在 Network 面板中找到 `list?....` 一行，然后在右侧的 Headers 部分找到 `Cookie:` 所在行，复制 `Cookie:` 后的所有内容作为 cookies 值，其中的 `BDUSS=...;` 的 `...` (没有最后的字符;)作为 bduss 值。\n\n![cookies](./imgs/cookies.png)\n\n现在找到了 cookies 和 bduss 值，我们可以用下面的命令添加一个用户。\n\n交互添加：\n\n```\nBaiduPCS-Py useradd\n```\n\n或者直接添加：\n\n```\nBaiduPCS-Py useradd --cookies "cookies 值" --bduss "bduss 值"\n```\n\n你也可以只添加 `bduss`，省去 `cookies` (或 `cookies` 中没有 `STOKEN` 值)，但这会让你无发使用 `share` 和 `save` 命令来转存其他用法的分享文件。\n\nBaiduPCS-Py 支持多用户，你只需一直用 `useradd` 来添加用户即可。\n\n## 显示当前用户的信息\n\n```\nBaiduPCS-Py who\n```\n\n或者：\n\n```\nBaiduPCS-Py who user_id\n```\n\n指明显示用户 id 为 `user_id` 的用户信息。\n\n## 更新用户信息\n\n默认更新当前用户信息。\n\n```\nBaiduPCS-Py updateuser\n```\n\n也可指定多个 `user_id`\n\n```\nBaiduPCS-Py updateuser user_id\n```\n\n## 显示所有用户\n\n```\nBaiduPCS-Py userlist\n```\n\n## 切换当前用户\n\n```\nBaiduPCS-Py su\n```\n\n## 删除一个用户\n\n```\nBaiduPCS-Py userdel\n```\n\n## 文件操作\n\nBaiduPCS-Py 操作网盘中的文件可以使用文件的绝对路径或相对路径（相对与当前目录 pwd）。\n\n每一个用户都有自己的当前工作目录（pwd），默认为 `/` 根目录。\n\n使用者可以用 `cd` 命令来切换当前的工作目录（pwd）。\n\n下面所有涉及网盘路径的命令，其中如果网盘路径用的是相对路径，那么是相对于当前工作目录（pwd）的。\n如果是网盘路径用的是绝对路径，那么就是这个绝对路径。\n\n## 显示当前工作目录\n\n```\nBaiduPCS-Py pwd\n```\n\n## 切换当前工作目录\n\n切换到绝对路径：\n\n```\nBaiduPCS-Py cd /to/some/path\n```\n\n切换到相对路径：\n\n```\n# 切换到 (pwd)/../path\nBaiduPCS-Py cd ../path\n```\n\n## 列出网盘路径下的文件\n\n```\nBaiduPCS-Py ls [OPTIONS] [REMOTEPATHS]...\n\nBaiduPCS-Py ls /absolute/path\n\n# or\nBaiduPCS-Py ls relative/path\n```\n\n### 选项\n\n| Option                     | Description                          |\n| -------------------------- | ------------------------------------ |\n| -r, --desc                 | 逆序排列文件                         |\n| -n, --name                 | 依名字排序                           |\n| -t, --time                 | 依时间排序                           |\n| -s, --size                 | 依文件大小排序                       |\n| -R, --recursive            | 递归列出文件                         |\n| -I, --include TEXT         | 筛选包含这个字符串的文件             |\n| --include-regex, --IR TEXT | 筛选包含这个正则表达式的文件         |\n| -E, --exclude TEXT         | 筛选 **不** 包含这个字符串的文件     |\n| --exclude-regex, --ER TEXT | 筛选 **不** 包含这个正则表达式的文件 |\n| -f, --is-file              | 筛选 **非** 目录文件                 |\n| -d, --is-dir               | 筛选目录文件                         |\n| --no-highlight, --NH       | 取消匹配高亮                         |\n| -S, --show-size            | 显示文件大小                         |\n| -D, --show-date            | 显示文件创建时间                     |\n| -M, --show-md5             | 显示文件 md5                         |\n| -A, --show-absolute-path   | 显示文件绝对路径                     |\n\n## 搜索文件\n\n搜索包含 `keyword` 的文件\n\n```\nBaiduPCS-Py search [OPTIONS] KEYWORD [REMOTEDIR]\n\n# 在当前工作目录中搜索\nBaiduPCS-Py search keyword\n\n# or\nBaiduPCS-Py search keyword /absolute/path\n\n# or\nBaiduPCS-Py search keyword relative/path\n```\n\n### 选项\n\n| Option                     | Description                          |\n| -------------------------- | ------------------------------------ |\n| -R, --recursive            | 递归搜索文件                         |\n| -I, --include TEXT         | 筛选包含这个字符串的文件             |\n| --include-regex, --IR TEXT | 筛选包含这个正则表达式的文件         |\n| -E, --exclude TEXT         | 筛选 **不** 包含这个字符串的文件     |\n| --exclude-regex, --ER TEXT | 筛选 **不** 包含这个正则表达式的文件 |\n| -f, --is-file              | 筛选 **非** 目录文件                 |\n| -d, --is-dir               | 筛选目录文件                         |\n| --no-highlight, --NH       | 取消匹配高亮                         |\n| -S, --show-size            | 显示文件大小                         |\n| -D, --show-date            | 显示文件创建时间                     |\n| -M, --show-md5             | 显示文件 md5                         |\n\n## 显示文件内容\n\n```\nBaiduPCS-Py cat [OPTIONS] REMOTEPATH\n```\n\n### 选项\n\n| Option              | Description            |\n| ------------------- | ---------------------- |\n| -e, --encoding TEXT | 文件编码，默认自动解码 |\n\n## 创建目录\n\n```\nBaiduPCS-Py mkdir [OPTIONS] [REMOTEDIRS]...\n```\n\n### 选项\n\n| Option     | Description |\n| ---------- | ----------- |\n| -S, --show | 显示目录    |\n\n## 移动文件\n\n移动一些文件到一个目录中。\n\n```\nBaiduPCS-Py move [OPTIONS] [REMOTEPATHS]... REMOTEDIR\n```\n\n### 选项\n\n| Option     | Description |\n| ---------- | ----------- |\n| -S, --show | 显示结果    |\n\n## 文件重命名\n\n```\nBaiduPCS-Py rename [OPTIONS] SOURCE DEST\n```\n\n### 选项\n\n| Option     | Description |\n| ---------- | ----------- |\n| -S, --show | 显示结果    |\n\n## 拷贝文件\n\n拷贝一些文件到一个目录中。\n\n```\nBaiduPCS-Py move [OPTIONS] [REMOTEPATHS]... REMOTEDIR\n```\n\n### 选项\n\n| Option     | Description |\n| ---------- | ----------- |\n| -S, --show | 显示结果    |\n\n## 删除文件\n\n```\nBaiduPCS-Py remove [OPTIONS] [REMOTEPATHS]...\n```\n\n## 下载文件\n\n```\nBaiduPCS-Py download [OPTIONS] [REMOTEPATHS]...\n```\n\n### 选项\n\n| Option                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                      |\n| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| -o, --outdir TEXT                              | 指定下载本地目录，默认为当前目录                                                                                                                                                                                                                                                                                                                                                                                                                                 |\n| -R, --recursive                                | 递归下载                                                                                                                                                                                                                                                                                                                                                                                                                                                         |\n| -f, --from-index INTEGER                       | 从所有目录中的第几个文件开始下载，默认为 0（第一个）                                                                                                                                                                                                                                                                                                                                                                                                             |\n| -I, --include TEXT                             | 筛选包含这个字符串的文件                                                                                                                                                                                                                                                                                                                                                                                                                                         |\n| --include-regex, --IR TEXT                     | 筛选包含这个正则表达式的文件                                                                                                                                                                                                                                                                                                                                                                                                                                     |\n| -E, --exclude TEXT                             | 筛选 不 包含这个字符串的文件                                                                                                                                                                                                                                                                                                                                                                                                                                     |\n| --exclude-regex, --ER TEXT                     | 筛选 不 包含这个正则表达式的文件                                                                                                                                                                                                                                                                                                                                                                                                                                 |\n| -s, --concurrency INTEGER                      | 下载同步链接数，默认为 5。数子越大下载速度越快，但是容易被百度封锁                                                                                                                                                                                                                                                                                                                                                                                               |\n| -k, --chunk-size TEXT                          | 同步链接分块大小                                                                                                                                                                                                                                                                                                                                                                                                                                                 |\n| -q, --quiet                                    | 取消第三方下载应用输出                                                                                                                                                                                                                                                                                                                                                                                                                                           |\n| --out-cmd, --OC                                | 输出第三方下载应用命令                                                                                                                                                                                                                                                                                                                                                                                                                                           |\n| -d, --downloader [me\\|aget_py\\|aget_rs\\|aria2] | 指定下载应用<br> <br> 默认为 me (BaiduPCS-Py 自己的下载器，支持断续下载)<br> me 使用多文件并发下载。<br> <br> 除 me 外，其他下载器，不使用多文件并发下载，使用一个文件多链接下载。<br> 如果需要下载多个小文件推荐使用 me，如果需要下载少量大文件推荐使用其他下载器。<br> <br> aget_py (https://github.com/PeterDing/aget) 默认安装<br> aget_rs (下载 https://github.com/PeterDing/aget-rs/releases)<br> aria2 (下载 https://github.com/aria2/aria2/releases)<br> |\n\n## 播放媒体文件\n\n```\nBaiduPCS-Py play [OPTIONS] [REMOTEPATHS]...\n```\n\n### 选项\n\n| Option                     | Description                                          |\n| -------------------------- | ---------------------------------------------------- |\n| -R, --recursive            | 递归播放                                             |\n| -f, --from-index INTEGER   | 从所有目录中的第几个文件开始播放，默认为 0（第一个） |\n| -I, --include TEXT         | 筛选包含这个字符串的文件                             |\n| --include-regex, --IR TEXT | 筛选包含这个正则表达式的文件                         |\n| -E, --exclude TEXT         | 筛选 不 包含这个字符串的文件                         |\n| --exclude-regex, --ER TEXT | 筛选 不 包含这个正则表达式的文件                     |\n| --player-params, --PP TEXT | 第三方播放器参数                                     |\n| -m, --m3u8                 | 获取 m3u8 文件并播放                                 |\n| -q, --quiet                | 取消第三方播放器输出                                 |\n| --out-cmd, --OC            | 输出第三方播放器命令                                 |\n| -p, --player [mpv]         | 指定第三方播放器<br><br>默认为 mpv (https://mpv.io)  |\n\n## 上传文件\n\n上传一些本地文件或目录到网盘目录。\n\n```\nBaiduPCS-Py upload [OPTIONS] [LOCALPATHS]... REMOTEDIR\n```\n\n### 选项\n\n| Option                     | Description        |\n| -------------------------- | ------------------ |\n| -w, --max-workers INTEGER  | 同时上传文件数     |\n| --no-ignore-existing, --NI | 上传已经存在的文件 |\n| --no-show-progress, --NP   | 不显示上传进度     |\n\n## 同步本地目录到远端\n\n同步本地目录到远端。\n\n如果本地文件 md5 和远端不同则上传文件。对于本地不存在的文件但远端存在则删除远端文件。\n\n```\nBaiduPCS-Py sync [OPTIONS] LOCALDIR REMOTEDIR\n```\n\n### 选项\n\n| Option                    | Description    |\n| ------------------------- | -------------- |\n| -w, --max-workers INTEGER | 同时上传文件数 |\n| --no-show-progress, --NP  | 不显示上传进度 |\n\n## 分享文件\n\n**注意：使用这个命令需要 cookies 中含有 `STOKEN` 值。**\n\n```\nBaiduPCS-Py share [OPTIONS] [REMOTEPATHS]...\n```\n\n### 选项\n\n| Option              | Description                      |\n| ------------------- | -------------------------------- |\n| -p, --password TEXT | 设置秘密，4 个字符。默认没有秘密 |\n\n## 列出分享链接\n\n```\nBaiduPCS-Py shared\n```\n\n### 选项\n\n| Option         | Description                                  |\n| -------------- | -------------------------------------------- |\n| -S, --show-all | 显示所有分享的链接，默认只显示有效的分享链接 |\n\n## 取消分享链接\n\n```\nBaiduPCS-Py cancelshared [OPTIONS] [SHARE_IDS]...\n```\n\n## 保存其他用户分享的链接\n\n**注意：使用这个命令需要 cookies 中含有 `STOKEN` 值。**\n\n保存其他用户分享的链接到远端目录。\n\n```\nBaiduPCS-Py save [OPTIONS] SHARED_URL REMOTEDIR\n```\n\n### 选项\n\n| Option                | Description                        |\n| --------------------- | ---------------------------------- |\n| -p, --password TEXT   | 链接密码，如果没有不用设置         |\n| --no-show-vcode, --NV | 不显示验证码，如果需要验证码则报错 |\n\n## 添加离线下载任务\n\n```\nBaiduPCS-Py add [TASK_URLS]... REMOTEDIR\n```\n\n## 列出离线下载任务\n\n```\n# 列出所有离线下载任务\nBaiduPCS-Py tasks\n\n# 也可列出给定id的任务。\nBaiduPCS-Py tasks [TASK_IDS]...\n```\n\n## 清除已经下载完和下载失败的任务\n\n```\nBaiduPCS-Py cleartasks\n```\n\n## 取消下载任务\n\n```\nBaiduPCS-Py canceltasks [TASK_IDS]...\n```\n\n## 删除所有离线下载任务\n\n```\nBaiduPCS-Py purgetasks\n```\n\n### 选项\n\n| Option | Description  |\n| ------ | ------------ |\n| --yes  | 确定直接运行 |\n',
    'author': 'PeterDing',
    'author_email': 'dfhayst@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/PeterDing/BaiduPCS-Py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
