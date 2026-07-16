"""ヒント機能を担当するモジュール。"""

import random


def hint(secret, shown_positions):
    """まだ表示していない位置から、数字を1つ返す。

    戻り値は (位置, 数字)。
    すべて表示済みなら None を返す。
    """

    candidates = [
        i for i in range(len(secret))
        if i not in shown_positions
    ]

    if not candidates:
        return None

    position = random.choice(candidates)
    return position, secret[position]