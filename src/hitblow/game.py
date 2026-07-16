"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret
from .score import calc_score, get_rank
from .hint import hint
from .difficulty import select_difficulty

def play():
    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    difficulty = select_difficulty()

    digits = difficulty["digits"]
    allow_duplicates = difficulty["allow_duplicates"]

    secret = make_secret(digits, allow_duplicates)

    print()
    print(f"難易度：{difficulty['name']}")
    print(f"ルール：{difficulty['description']}")
    print("Hit & Blowを開始します")


    tries = 0
    hint_count = 0
    shown_positions = []
    
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue
        if guess == "h":
            result = hint(secret, shown_positions)

            if result is None:
                print("これ以上ヒントはありません")
            else:
                position, digit = result
                shown_positions.append(position)
                hint_count += 1
                print(f"ヒント：答えには「{digit}」が含まれています")

            continue

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")
        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            score = calc_score(tries, hint_count)
            rank = get_rank(score)

            print(f"スコア : {score} 点")
            print(f"ランク : {rank}")


            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break
