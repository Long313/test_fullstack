import keyword
import re

# Bài 1
# Hàm kiểm tra xem chuỗi có phải là tên biến hợp lệ
def is_valid_identifier(s: str):
    if not isinstance(s, str): # kiểm tra có phải là chuỗi hay không
        return False
    if not s:                  # kiểm tra chuỗi rỗng hay không
        return False
    if keyword.iskeyword(s):   # kiểm tra chuỗi có trùng với keywords trong Py không
        return False
    if s[0].isdigit():         # kiểm tra chuỗi có bắt đầu với số hay không
        return False
    if re.match(r'^[A-Za-z0-9_]+$', s): # kiểm tra chuỗi hợp lệ bằng regex
        return True
    else:
        return False
    
print("\n--- Bài 1---")
print(is_valid_identifier("abc"))     # Kết quả: True
print(is_valid_identifier("123var"))  # Kết quả: False
print(is_valid_identifier("for"))     # Kết quả: False
print(is_valid_identifier(1))         # Kết quả: False
print(is_valid_identifier(""))        # Kết quả: False
print(is_valid_identifier("a*bc"))    # Kết quả: False
print(is_valid_identifier("a_bc"))    # Kết quả: True
print(is_valid_identifier("_abc"))    # Kết quả: True
print(is_valid_identifier("a123_"))   # Kết quả: True
