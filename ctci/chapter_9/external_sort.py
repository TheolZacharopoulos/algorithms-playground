"""
Imagine you have a 20 GB file with one string per line. Explain how you would sort the file.

SOLUTION:
When an interviewer gives a size limit of 20 gigabytes, it should tell you something. In this case, it suggests
that they don't want you to bring all the data into memory.
So what do we do? We only bring part of the data into memory.
We'll divide the file into chunks, which are x megabytes each,
where x is the amount of memory we have available.
Each chunk is sorted separately and then saved back to the file system.
Once all the chunks are sorted, we merge the chunks, one by one.
At the end, we have a fully sorted file. This algorithm is known as external sort.

https://www.youtube.com/watch?v=ATK74YSzwxg
"""

# pages available for a run (typically = available main memory)
M = 2

FAN_IN = M - 1


def run_generate(r, m):
    pass


def merge_runs(inputs):
    pass


def external_sort(pages):
    # heap of runs to consider
    runs = []

    # Pass 0
    while pages:
        # read M pages of input from pages and sort
        run = run_generate(pages, M)

        # add reference of run in heap
        runs.append(run)

    # Passes 1 and following
    while len(runs) > 1:
        # list of inputs to merge (in a single merge)
        inputs = []

        # remove next Fan_in inputs from the heap
        inputs = runs.popK(FAN_IN)

        # merge runs into one output run
        run = merge_runs(inputs)

        # add reference of run in heap
        runs.append(run)
