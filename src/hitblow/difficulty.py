"""難易度の表示と選択を担当するモジュール。"""


DIFFICULTIES = {
    "1": {
        "name": "低",
        "digits": 3,
        "allow_duplicates": False,
        "description": "3桁・数字の重複なし",
    },
    "2": {
        "name": "中",
        "digits": 3,
        "allow_duplicates": True,
        "description": "3桁・数字の重複あり",
    },
    "3": {
        "name": "高",
        "digits": 5,
        "allow_duplicates": False,
        "description": "5桁・数字の重複なし",
    },
    "4": {
        "name": "最高",
        "digits": 5,
        "allow_duplicates": True,
        "description": "5桁・数字の重複あり",
    },
}


def select_difficulty():
    """難易度一覧を表示し、選択された設定を返す。"""

    print("難易度を選択してください")
    print("1：低　　3桁・数字の重複なし")
    print("2：中　　3桁・数字の重複あり")
    print("3：高　　5桁・数字の重複なし")
    print("4：最高　5桁・数字の重複あり")

    while True:
        choice = input("難易度 > ").strip()

        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]

        print("1～4の数字で選択してください")