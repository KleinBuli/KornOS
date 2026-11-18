from process.pcb import ProcessControlBlock, ProcessTable

def main():
    print("KornOS v0.1")
    print("Kornel initalized.")

    process_table = ProcessTable()
    process = ProcessControlBlock(
        name="Process1", priority=1, address_space=0, files=[], threads={}
    )

    process_table.register_process(process)

main()
