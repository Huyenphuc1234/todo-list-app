# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    
    task = {'name': task_name, 'completed': False} 
    tasks.append(task)
    print(f'Đã thêm công việc:"{task_name}"')
def list_tasks():
    if not tasks:
        print("Chưa có công việc nào.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("Số thứ tự không hợp lệ!")
def delete_task(task_index):
    """Xóa một công việc khỏi danh sách."""
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Đã xóa công việc: {removed['name']}")
    else:
        print("Số thứ tự không hợp lệ!")
    # --- Điểm bắt đầu của chương trình ---
    if __name__ == "__main__":
        print("Chào mừng đến với ứng dụng To-Do List!")
        add_task("Học bài Git và Github")
        add_task("Làm bài tập thực hành ở nhà")
        complete_task(0)
        delete_task(1)
        list_tasks()