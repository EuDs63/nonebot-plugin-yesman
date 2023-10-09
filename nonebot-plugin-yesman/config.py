from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""
    # 设置概率触发的阈值，例如0.5表示50%的概率
    yesman_threshold = 0.5

    # 包含允许的user_id的数组
    yesman_allowed_user_ids = [123456, 654321]