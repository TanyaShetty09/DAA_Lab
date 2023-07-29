class Job:
    def __init__(self, taskId, deadline, profit):
        self.taskId = taskId
        self.deadline = deadline
        self.profit = profit

def scheduleJobs():
    n = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(n):
        taskId = i + 1
        deadline = int(input(f"Enter the deadline of Job {taskId}: "))
        profit = int(input(f"Enter the profit of Job {taskId}: "))
        job = Job(taskId, deadline, profit)
        jobs.append(job)

    T = max(job.deadline for job in jobs)
    profit = 0
    slot = [-1] * T
    jobs.sort(key=lambda x: x.profit, reverse=True)

    for job in jobs:
        for j in reversed(range(job.deadline)):
            if j < T and slot[j] == -1:
                slot[j] = job.taskId
                profit += job.profit
                break

    scheduled_jobs = list(filter(lambda x: x != -1, slot))
    print("The scheduled jobs are:", scheduled_jobs)
    print("The total profit earned is:", profit)

if __name__ == '__main__':
    scheduleJobs()