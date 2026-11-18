# Creates a ProcessControlBlock which represents 1 simulated process
from process.thread import Thread


class ProcessControlBlock:
    def __init__(
        self, name: str, priority: int, address_space, files, threads: dict[int, Thread]
    ):
        self.name = name
        self.id = None
        self.priority = priority
        self.address_space = address_space
        self.files = files
        self.threads = threads

    def set_id(self, id: int):
        self.id = 0


# Creates a table of all processes in form of a dictionary
class ProcessTable:
    currentId = 0

    def __init__(self):
        self.processes = dict[int, ProcessControlBlock]()

    def register_process(self, pcb: ProcessControlBlock):
        self.processes[self.currentId] = pcb
        print(f"[Threads] registered process {pcb.name} with id {self.currentId}")
        self.currentId += 1
