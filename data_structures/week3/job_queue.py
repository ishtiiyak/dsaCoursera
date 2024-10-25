from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs(n_workers, jobs):
    result = []
    
    # Initialize the priority queue with each worker's availability (0 at start)
    # Each entry is a tuple: (next_free_time, worker_id)
    priority_queue = [(0, worker_id) for worker_id in range(n_workers)]
    heapq.heapify(priority_queue)

    for job in jobs:
        # Extract the worker with the earliest available time
        next_free_time, worker_id = heapq.heappop(priority_queue)
        
        # Assign job to the selected worker
        result.append(AssignedJob(worker_id, next_free_time))
        
        # Update worker's next free time and push back to priority queue
        heapq.heappush(priority_queue, (next_free_time + job, worker_id))

    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)

if __name__ == "__main__":
    main()
