# シーザー暗号
# アルファベットを一定の文字数だけずらすことで暗号化する。

def encrypt(plain_text, shift_num):
    # 暗号文
    cipher = ""

    for char in list(plain_text):
        # 暗号化
        cipher += chr(ord(char) + shift_num)
    
    return cipher

# 暗号化対象文字列
plain_text = "draemon"

# シフト数
shift_num = 3

print(encrypt(plain_text,shift_num))
