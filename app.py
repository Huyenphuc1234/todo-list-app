# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm công việc (dạng dictionary)."""
    task = {'name': task_name, 'completed': False} 
    tasks.append(task)
    print(f'Đã thêm công việc:"{task_name}"')
def list_tasks():
    """Liệt kê công việc kèm trạng thái."""
    if not tasks:
        print("Chưa có công việc nào.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")
def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("Số thứ tự không hợp lệ!")
    # --- Điểm bắt đầu của chương trình ---
    if __name__ == "__main__":
        print("Chào mừng đến với ứng dụng To-Do List!")
        add_task("Học bài Git và Github")
        add_task("Làm bài tập thực hành ở nhà")
        complete_task(0)
        list_tasks()