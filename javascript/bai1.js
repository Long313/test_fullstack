// Bài 1
// Hàm để kiểm tra xem một chuỗi dấu ngoặc ()[]{} có hợp lệ hay không
function isValidBracketString(s) {
    const stack = [];
    const map = {
        ")": "(",
        "]": "[",
        "}": "{"
    };

    for (let char of s) {
        if (char === "(" || char === "[" || char === "{") {
            stack.push(char);   // Kiểm tra nếu là dấu mở thì đưa vào stack
        } else {
            if (stack.length === 0 || stack.pop() !== map[char]) {
                return false;   // Kiểm tra nếu không khớp thì chuỗi sai
            }
        }
    }

    return stack.length === 0; // nếu stack rỗng thì hợp lệ
}
console.log("--- Bài 1 ---")
console.log(isValidBracketString("()[]{}"));  // Kết quả: true
console.log(isValidBracketString("({[]})"));  // Kết quả: true
console.log(isValidBracketString("(]"));      // Kết quả: false
console.log(isValidBracketString("([)]"));    // Kết quả: false