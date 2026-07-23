"""スコア履歴の保存と表示を担当するモジュール。"""

import json
from pathlib import Path


HISTORY_FILE = Path("score_history.json")
MAX_RECORDS = 5


def load_history():
    """保存済みの履歴を読み込む。"""

    if not HISTORY_FILE.exists():
        return []

    try:
        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_history(history):
    """履歴をJSONファイルに保存する。"""

    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=2)


def update_history(score, difficulty, tries, hint_count):
    """新しい記録を追加し、上位5件だけ保存する。

    戻り値：
        updated: 上位5件に入ったか
        history: 更新後の履歴
        rank: 今回の記録順位。入らなければNone
    """

    history = load_history()

    new_record = {
        "score": score,
        "difficulty": difficulty,
        "tries": tries,
        "hint_count": hint_count,
    }

    history.append(new_record)
    history.sort(key=lambda record: record["score"], reverse=True)

    rank = history.index(new_record) + 1
    updated = rank <= MAX_RECORDS

    history = history[:MAX_RECORDS]
    save_history(history)

    if not updated:
        rank = None

    return updated, history, rank