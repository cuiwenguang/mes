# 工序模块

import enum


class DataState(enum.Enum):
    delete = -1  # 删除
    draft = 0  # 草稿 暂存
    normal = 1  # 有效数据
    archive = 2  # 归档，以结算


class FlowState(enum.Enum):
    htsg = 1  # 活体收购
    tzqcz = 2  # 屠宰前称重
    ttcz = 3  # 酮体称重
    pscz = 4  # 排酸称重