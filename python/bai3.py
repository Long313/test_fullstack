# Bài 3
# Thiết kế class TaskScheduler mô phỏng việc sắp xếp và chạy các tác vụ
class TaskScheduler:
    # Hàm khởi tạo
    def __init__(self):
        self.tasks: dict[str, callable] = {}   # Dùng để lưu function
        self.results: dict[str, object] = {}   # Dùng để lưu result

    # Hàm thêm tác vụ
    def add_task(self, name: str, func: callable):
        if name in self.tasks:         # Kiểm tra tác vụ có tồn tại chưa, nếu tồn tại rồi thì raise error, chưa có thì thêm vào
            raise ValueError(f"Tác vụ '{name}' tồn tại rồi")
        self.tasks[name] = func          

    # Hàm xóa tác vụ
    def remove_task(self, name: str):
        if name not in self.tasks:     # Kiểm tra tên tác vụ có không, không có thì raise error, còn nếu có thì xóa
            raise KeyError(f"Tác vụ '{name}' không tồn tại")
        del self.tasks[name]

    # Hàm chạy tất cả các tác vụ theo thứ tự được thêm vào
    def run_all(self):
        self.results.clear()
        for name, func in self.tasks.items(): 
            try:
                self.results[name] = func()
            except Exception as e:
                self.results[name] = f"{type(e).__name__}: {e}"

    # Hàm trả về dict
    def get_results(self) -> dict[str, object]:
        return self.results

def f1(): return 1
def f2(): return "hello"
def f3(): raise RuntimeError("fail")
s = TaskScheduler()
s.add_task("t1", f1)
s.add_task("t2", f2)
s.add_task("t3", f3)
s.run_all()
print("\n---Bài 3---")
print(s.get_results())    
# Kết quả: {"t1": 1, "t2": "hello", "t3": "RuntimeError: fail"}