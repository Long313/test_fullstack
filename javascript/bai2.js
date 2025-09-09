// Bài 2
// Hàm để tìm ra k phần tử xuất hiện nhiều nhất trong mảng nums
function topKcountMapuent(nums, k) {
    const countMap = new Map();    // Tạo Map để lưu số lần xuất hiện
    for (let num of nums) {
        countMap.set(num, (countMap.get(num) || 0) + 1);
    }

    // Tạo bucket với index là số lần xuất hiện
    const bucket = Array(nums.length + 1).fill().map(() => []);
    for (let [num, count] of countMap.entries()) {
        bucket[count].push(num);
    }

    const res = [];
    // Duyệt từ bucket lớn nhất tới nhỏ nhất
    for (let i = bucket.length - 1; i >= 0 && res.length < k; i--) {
        if (bucket[i].length > 0) {
            res.push(...bucket[i]);
        }
    }
    return res.slice(0, k);
}

console.log("--- Bài 2 ---")
console.log(topKcountMapuent([1, 1, 1, 2, 2, 3], 2));         //  Kết quả: [1, 2]
console.log(topKcountMapuent([4, 4, 4, 4, 5, 5, 6], 1));      //  Kết quả: [4]
console.log(topKcountMapuent([4, 4, 4, 6, 5, 5, 6, 7], 3));   //  Kết quả: [4,6,5]