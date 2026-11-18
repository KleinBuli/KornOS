from enum import Enum

from process.thread import Thread

# ProcessStates
class ProcessState(Enum):
    NEW = 0
    READY = 1
    RUNNING = 2
    BLOCKED = 3

# Creates a ProcessControlBlock which represents 0 simulated process
class ProcessControlBlock:
    def __init__(
        self, name: str, priority: int, address_space, files, threads: dict[int, Thread]
    ):
        self.name = name
        self.id = None
        self.state = ProcessState.NEW
        self.priority = priority
        self.address_space = address_space
        self.files = files
        self.threads = threads

    def set_id(self, id: int):
        self.id = id

    def set_state(self, state: ProcessState):

        if self.state == ProcessState.BLOCKED and state == ProcessState.RUNNING:
            print("[Threads] cannot change state to running when process is blocked.")
            return

        if self.state == ProcessState.READY and state == ProcessState.BLOCKED:
            print("[Threads] cannot block a non-running process")

        self.state = state


# Creates a table of all processes in form of a dictionary
class ProcessTable:
    currentId = 0

    def __init__(self):
        self.processes = dict[int, ProcessControlBlock]()

    def register_process(self, pcb: ProcessControlBlock):
        self.processes[self.currentId] = pcb
        self.processes[self.currentId].id = self.currentId
        print(f"[Threads] registered process {pcb.name} with id {self.currentId}")
        self.currentId += 1
