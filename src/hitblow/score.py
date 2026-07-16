"""スコア計算を担当するモジュール。"""

START_SCORE = 1000
MISS_PENALTY = 50
HINT_PENALTY = 75


def calc_score(tries, hint_count=0):
    """試行回数とヒント使用回数からスコアを計算する。"""

    score = START_SCORE

    # 2回目以降は1回につき50点減点
    score -= (tries - 1) * MISS_PENALTY

    # ヒント1回につき75点減点
    score -= hint_count * HINT_PENALTY

    return max(score, 0)


def get_rank(score):
    """スコアからランクを返す。"""

    if score >= 800:
        return "S"
    elif score >= 600:
        return "A"
    elif score >= 400:
        return "B"
    else:
        return "C"