<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-yesman

_✨ 你的发言，值得被肯定 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-yesman.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-yesman">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-yesman.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

这里是插件的详细介绍部分

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-yesman

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-yesman
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-yesman
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-yesman
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-yesman
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_example"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| yesman_threshold | 是 | 0.5 | 设置概率触发的阈值，例如0.5表示50%的概率 |
|yesman_allowed_user_ids | 是 | 无 | 包含允许的 user_id 的数组 |

## 🎉 使用

想要回复被肯定时，发言时以`.`或`。`结尾即可。（也可以自定义为自己喜欢的）


