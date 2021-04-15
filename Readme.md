A todolist App takes an input task from a general form.
The task is stored in database and displayed on screen.
After a task is completed, it is marked done and the task is deleted. The concept of dynamic URLs comes into play now. The id of each task is appended to "delete/<str:id>" URL, from where the ID is fetched and the corresponding task is deleted then.