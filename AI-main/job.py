# n = 3  # number of jobs
# #  job-id , time , profit
# # TC->O(n)
# # SC->O(n)
jobs = [['Job1', '2', '100'], ['Job2', '5', '450'], ['Job3', '3', '325']]
# extract profit from jobs
def sorter(job): return int(job[2])


# sort the jobs based on profit in descending order
jobs = sorted(jobs, key=sorter, reverse=True)
# empty array for storing scheduled jobs
scheduled = []
# time is zero initially
time = 0

# Iterate through the sorted jobs and check if they can be scheduled within their deadlines
for i in jobs:
    deadline = int(i[1])
    jobId = i[0]
    if time <= deadline:
        scheduled.append(jobId)
        time += 1

print("Jobs are scheduled as:")
print(scheduled)

max_profit = 0

for job in jobs:
    if job[0] in scheduled:
        max_profit += int(job[2])

print("Maximum Profit:", max_profit)
