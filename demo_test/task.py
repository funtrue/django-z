from django_q.tasks import Task
 
def demo_task(number: int):
    return number + 10086

def task_finish(task: Task):
    print(f'任务 {task.name}（ID：{task.id}）完成！')
