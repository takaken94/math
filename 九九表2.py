import io
import sys

# 1 から n までの九九表を作成する
def print_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
            # print("{:4d}".format(i * j), end="")
        print()

# print_multiplication_table(20)
# テストコード
def test_print_multiplication_table():
    # キャプチャ出力
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_multiplication_table(3)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    expected_output = "   1   2   3\n   2   4   6\n   3   6   9\n"
    assert output == expected_output, f"Expected:\n{expected_output}\nBut got:\n{output}"
    print("テストが成功しました")

test_print_multiplication_table()