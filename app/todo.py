from ast import List
class Todo:
  def __init__(self) -> None:
    """2d array of [tasks, state], state being True or False
    True -> task completed
    False -> task incomplete
    """
    self.tasks = []

  def add_task(self, task) -> None:
    """
    adds a task to the list whose default state is incomplete i.e False
    """
    self.tasks.append([task, False])
  
  def remove_task(self, pos) -> None:
    """
    removes a task at the given position
    """
    if 0 <= pos < len(self.tasks):
      self.tasks.pop(pos)
    else:
      print("Task already removed or doesn't exist")
  
  def update_task(self, pos,updated_task=None, updated_state = None)->List:
    """
    task can be updated in two ways, either by updating the text or updating the task's state
    """
    if updated_task: 
      self.tasks[pos][0] = updated_task
    elif updated_state:
      self.tasks[pos][1] = updated_state
    return self.tasks
  
  def show_tasks(self)->List:
    """
    shows current state of tasks board
    """
    return self.tasks

todo_list = Todo()
todo_list.add_task("Finish coding")
todo_list.add_task("wash bottle")
print(todo_list.show_tasks())
todo_list.update_task(1,None, True)
print(todo_list.show_tasks())
todo_list.remove_task(1)
print(todo_list.show_tasks())