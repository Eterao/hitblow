"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は自分の担当の場所に書く（1機能=1ファイル）。
下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
importも自分の場所の近くに書く。
"""

from .core import judge, make_secret


def play():
    # ===== ① 開始時に足す（難易度・あいさつなど） =====
    from .difficulty import select_difficulty

    difficulty = select_difficulty()

    digits = difficulty["digits"]
    allow_duplicates = difficulty["allow_duplicates"]
    secret = make_secret(digits, allow_duplicates)

    print()
    print("========== Hit & Blow ==========")
    print(f"難易度：{difficulty['name']}")
    print(f"ルール：{difficulty['description']}")
    print(f"{digits}桁の数字を予想してください")
    print("ヒントを使う：h")
    print("ゲームを終了：q")
    print("================================")

    tries = 0
    hint_count = 0
    shown_positions = []

    while True:
        guess = input("予想 > ").strip().lower()

        # ゲーム終了
        if guess == "q":
            print()
            print("ゲームを終了します")
            print(f"答えは「{secret}」でした")
            break

        # ===== ② 入力コマンドに足す（ヒントなど） =====
        from .hint import hint

        if guess == "h":
            result = hint(secret, shown_positions)

            if result is None:
                print("これ以上ヒントはありません")
            else:
                position, digit = result
                shown_positions.append(position)
                hint_count += 1

                print(f"ヒント：答えには「{digit}」が含まれています")
                print(f"ヒント使用回数：{hint_count}回")

            continue

        # 入力チェック
        if len(guess) != digits or not guess.isdigit():
            print(f"{digits}桁の数字で入力してください")
            print("ヒントは「h」、終了は「q」です")
            continue

        tries += 1

        hit, blow = judge(secret, guess)

        print(f"結果：Hit={hit}  Blow={blow}")
        print(f"挑戦回数：{tries}回")

        if hit == digits:
            # ===== ③ 勝利時に足す（スコア・履歴など） =====
            from .score import calc_score, get_rank
            from .history import update_history

            score = calc_score(tries, hint_count)
            rank = get_rank(score)

            updated, history, history_rank = update_history(
                score,
                difficulty["name"],
                tries,
                hint_count,
            )

            print()
            print("========== 結果 ==========")
            print(f"正解！ 答えは「{secret}」です")
            print(f"挑戦回数：{tries}回")
            print(f"ヒント使用回数：{hint_count}回")
            print(f"スコア：{score}点")
            print(f"ランク：{rank}")

            if updated:
                print(f"記録更新！ スコア履歴の第{history_rank}位に入りました")
            else:
                print("上位5件の記録更新はありませんでした")

            print()
            print("===== スコア履歴 上位5件 =====")

            for index, record in enumerate(history, start=1):
                print(
                    f"{index}位：{record['score']}点 "
                    f"難易度={record['difficulty']} "
                    f"挑戦={record['tries']}回 "
                    f"ヒント={record['hint_count']}回"
                )

            print("==============================")
            break
