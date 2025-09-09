// Bài 2
// Hàm để tìm ra k phần tử xuất hiện nhiều nhất trong mảng nums
function topKFrequent(nums, k) {
    const freq = new Map();
    for (let num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Tạo bucket: index = số lần xuất hiện, value = mảng số có count = index
    const bucket = Array(nums.length + 1).fill().map(() => []);
    for (let [num, count] of freq.entries()) {
        bucket[count].push(num);
    }

    const res = [];
    // Duyệt từ bucket lớn nhất xuống nhỏ nhất
    for (let i = bucket.length - 1; i >= 0 && res.length < k; i--) {
        if (bucket[i].length > 0) {
            res.push(...bucket[i]);
        }
    }
    return res.slice(0, k);
}

console.log("--- Bài 2 ---")
console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));         //  Kết quả: [1, 2]
console.log(topKFrequent([4, 4, 4, 4, 5, 5, 6], 1));      //  Kết quả: [4]
console.log(topKFrequent([4, 4, 4, 6, 5, 5, 6, 7], 3));   //  Kết quả: [4,6,5]