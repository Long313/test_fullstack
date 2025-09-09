// Bài 3
// Lớp LRUCache mô phỏng bộ nhớ cache LRU (Least Recently Used)
class LRUCache {
    // Khởi tạo capacity
    constructor(capacity) {
        this.capacity = capacity;
        this.cache = new Map();
    }

    // Hàm trả về giá trị
    get(key) {
        if (!this.cache.has(key)) {  // Kiểm tra nếu không có key thì trả về -1
            return -1;
        }
        const value = this.cache.get(key);
        // Đưa key ra cuối rồi mới set key và return giá trị 
        this.cache.delete(key);
        this.cache.set(key, value);
        return value;
    }

    // Hàm thêm hoặc cập nhật giá trị 
    put(key, value) {
        if (this.cache.has(key)) {
            // Nếu key đã có thì xóa key để cập nhật vị trí mới
            this.cache.delete(key);
        } else if (this.cache.size >= this.capacity) {
            // Nếu cache đầy thì xóa phần tử ít dùng nhất
            const firstKey = this.cache.keys().next().value;
            this.cache.delete(firstKey);
        }
        this.cache.set(key, value);
    }
}

// Tạo đối tượng cache
const cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);

console.log("--- Bài 3 ---")

console.log(cache.get(1)); // Kết quả: 1
cache.put(3, 3);           // loại bỏ key=2
console.log(cache.get(2)); // Kết quả: -1
cache.put(4, 4);           // loại bỏ key=1
console.log(cache.get(1)); // Kết quả: -1
console.log(cache.get(3)); // Kết quả: 3
console.log(cache.get(4)); // Kết quả: 4