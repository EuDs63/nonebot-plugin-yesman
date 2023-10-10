import random
from collections.abc import Callable
from pathlib import Path

from nonebot import on_message,get_driver
from nonebot.adapters.onebot.v11 import Message, MessageEvent, MessageSegment
from nonebot.params import EventPlainText
from nonebot.plugin import PluginMetadata
from nonebot.typing import T_State

import random
from pathlib import Path
from .config import Config

agree_path = Path(__file__).parent / "agree.txt"
agree_text = agree_path.read_text('utf-8').splitlines()

__plugin_meta__ = PluginMetadata(
    name="肯定机",
    description="你的发言，值得被肯定",
    usage="想要回复被肯定时，发言时以`.`或`。`结尾即可。（也可以自定义为自己喜欢的）",
    type="application",
    homepage="https://github.com/EuDs63/nonebot-plugin-yesman",
    config = Config,
    supported_adapters={"~onebot.v11"}, # 仅测试了onebot
)

global_config = get_driver().config
config = Config.parse_obj(global_config)


# 事件处理器
def endswith(msg: str) -> Callable[[str], bool]:
    def rule(message: str = EventPlainText()) -> bool:
        return message.endswith(".") or message.endswith("。") 

    return rule

generate_agree = on_message(rule=endswith("."))

@generate_agree.handle()
async def agree(event:MessageEvent) -> None:
    print(event.user_id)
    if event.user_id in config.allowed_user_ids:
        # 生成一个介于0到1之间的随机浮点数
        random_probability = random.random()

        if random_probability < config.threshold:
            # 如果生成的随机浮点数小于阈值，发送一条肯定的消息
            await generate_agree.finish(
                MessageSegment.text(random.choice(agree_text))
            )
        else:
            # 否则，不做任何事
            await generate_agree.finish()
