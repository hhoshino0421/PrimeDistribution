import sys
import math
#import numpy as np
import array

# 最大処理可能値定義
MAX_LIMIT_INDEX = 10000000
# 分割処理閾値
DIVIDE_LIMIT = 10000


# 使い方表示
def usage():
    print("使い方")
    print(" python PrimeMain.py start end")
    print("")
    print("")


# 引数チェック処理
def argv_check(args):

    if len(args) < 3:
        # 引数不足
        print("argv is not enough.")
        usage()
        return None, None, False

    start_index = 0
    end_index = 0

    if args[1].isdecimal():
        start_index = int(args[1])
    else:
        # 第一引数が数値でない
        print("first argv is not numeric")
        usage()
        return None, None, False

    if args[2].isdecimal():
        end_index = int(args[2])
    else:
        # 第二引数が数値でない
        print("second argv is not numeric")
        usage()
        return None, None, False

    if start_index < 0 or end_index < 0:
        # 自然数でない
        print("argv is not minus value.")
        usage()
        return None, None, False

    if start_index >= end_index:
        # 大小関係が異常
        print("argv is not logical error.")
        usage()
        return None, None, False

    if end_index > MAX_LIMIT_INDEX:
        # 限界値オーバー
        print("argv is too large error.")
        usage()
        return None, None, False

    return start_index, end_index, True


# 素数検索処理
def prime_number_search(start_pos, end_pos):

    # 素数候補リスト
    candidate_list = []
    # 素数リスト
    prime_number_list = []

    # 素数候補リスト初期化
    for i in range(start_pos, end_pos, 1):
        candidate_list.append(i)

    # ループ終端index算出
    check_max_pos = int(math.sqrt(end_pos))

    # ループ始端index
    loop_start_pos = 2
    # ループ終端index
    loop_end_pos = check_max_pos

    # 1は素数扱いにならないので補正
    if start_pos == 1:
        candidate_list.remove(1)

    # 素数検出ループ
    for i in range(loop_start_pos, loop_end_pos, 1):

        if i >= start_pos:

            if candidate_list.count(i) <= 0:
                continue

            prime_number_list.append(i)

        for j in range(1, end_pos, 1):

            pos = i * j

            if pos >= end_pos:
                break
            elif pos < start_pos:
                continue

            if candidate_list.count(pos) <= 0:
                continue

            candidate_list.remove(pos)

    prime_number_list.extend(candidate_list)

    return prime_number_list


# 素数リスト作成処理
def prime_number_make_list(strat_pos, end_pos):

    search_cnt = end_pos - strat_pos
    prime_number_list = []

    if search_cnt > DIVIDE_LIMIT:
        # 分割実行処理
        loop_cnt = int(end_pos / DIVIDE_LIMIT) + 1

        for i in range(0, loop_cnt, 1):

            hosei_start_pos = strat_pos + DIVIDE_LIMIT * i
            hosei_end_pos = DIVIDE_LIMIT * i + DIVIDE_LIMIT

            if hosei_start_pos > end_pos:
                break

            if hosei_end_pos > end_pos:
                hosei_end_pos = end_pos

            prime_number_list.extend(prime_number_search(hosei_start_pos, hosei_end_pos))


    else:
        # 単一実行処理
        # 素数計算処理
        prime_number_list.extend(prime_number_search(strat_pos, end_pos))

    return prime_number_list


# メイン処理
def main(strat_pos, end_pos):

    prime_number_list = []

    # 素数リスト作成
    prime_number_list.extend(prime_number_make_list(strat_pos, end_pos))

    # デバッグ用
    #print(prime_number_list)

    array_len = int((end_pos - strat_pos) /100) + 1

    distribution_arrar =[0] * array_len

    for i in range(0,array_len,1):
        distribution_arrar[i] = 0

    for prime_num in prime_number_list:

        # 簡易版
        array_index = int(prime_num / 100)
        distribution_arrar[array_index] += 1

    print(distribution_arrar)


# プログラムのエントリポイント
if __name__ == "__main__":

    # 引数確認
    args = sys.argv

    # 引数チェック
    strat_pos, end_pos, result = argv_check(args)

    if not result:
        usage()
        sys.exit(-1)

    # メイン処理実行
    main(strat_pos, end_pos)


