# Creates a ProcessControlBlock which represents 1 simulated process
class ProcessControlBlock:
    def __init__(self, name: str, priority, address_space, files, threads):
        self.name = name
        self.priority = priority
        self.address_space = address_space
        self.files = files
        self.threads = threads


# Creates a table of all processes in form of a dictionary
class ProcessTable:
    currentId = 0

    def __init__(self):
        self.processes = dict[int, ProcessControlBlock]()

    def register_process(self, pcb: ProcessControlBlock):
        self.processes[self.currentId] = pcb
        print(f"[Threads] registered process {pcb}")
        self.currentId += 1
