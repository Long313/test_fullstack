import keyword
import re

# Bài 1
# Hàm kiểm tra xem chuỗi có phải là tên biến hợp lệ
def is_valid_identifier(s: str):
    if not isinstance(s, str): # kiểm tra có phải là chuỗi hay không
        return False
    if not s:         # kiểm tra chuỗi rỗng hay không
        return False
    if keyword.iskeyword(s): # kiểm tra chuỗi có trùng với keywords trong Py không
        return False
    if s[0].isdigit(): # kiểm tra chuỗi có bắt đầu với số hay không
        return False
    if re.match(r'^[A-Za-z0-9_]+$', s): # kiểm tra chuỗi hợp lệ bằng regex
        return True
    else:
        return False
    


# Bài 2
# Hàm nhóm các từ trong danh sách thành các các nhóm từ đảo chữ
def group_anagrams(words):
    if not isinstance(words, (list, tuple)): # kiểm tra có phải là một danh sách hay không, nếu không trả về chính nó
        return words
    elif len(words) == 0:                    # kiểm tra xem độ dài của danh sách, nếu độ dài danh sách == 0 thì trả về chính nó
        return words
    else:
        groups = {}  # Tạo một dict rỗng để lưu nhóm anagram
        for word in words: 
            key = ''.join(sorted(word))  # Sắp xếp các chữ trong 1 từ thành key       
            if key not in groups:  # Nếu key chưa tồn tại trong dict, tạo một list rỗng để chứa các từ cùng nhóm
                groups[key] = []         
            groups[key].append(word)  # Thêm từ hiện tại vào nhóm
    return [list(dict.fromkeys(group)) for group in groups.values()] # Trả về danh sách đã gom nhóm, nếu có trùng gặp thì gom lại một nhóm        

print("---Kết quả test---")

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

print("\n---Bài 2---")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))                               # Kết quả: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams(["listen", "silent", "cat", "enlist", "google", "tac", "act", "gogole"]))  # Kết quả: [['listen', 'silent', 'enlist'], ['cat', 'tac', 'act'], ['google', 'gogole']]
print(group_anagrams(["cat", "tea", "", "ate", "logn","act", "long"]))                          # Kết quả: [['cat', 'act'], ['tea', 'ate'], [''], ['logn', 'long']]
print(group_anagrams([]))                                                                       # Kết quả: [];
print(group_anagrams(['', '']))                                                                 # Kết quả: [['']];
print(group_anagrams(['cat', '', 'act']))                                                       # Kết quả: [['cat', 'act'], ['']];
print(group_anagrams(2))                                                                        # Kết quả: 2