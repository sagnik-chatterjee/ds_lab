class Process:
    def __init__(self, id, alive) -> None:
        self.id = id
        self.alive = alive
        self.coordiantor = False
        self.crash_notice = False


class System:
    all_processes = []

    def create_process(self, id, alive):
        process = Process(id, alive)
        self.all_processes.append(process)

    def get_all_process(self):
        return self.all_processes

    def processes_count(self):
        return len(self.all_processes)

    def get_next_process(self, id):
        return self.get_process(id + 1)

    def get_next_process(self, id):
        return self.get_process(id + 1)

    def get_process(self, id):
        for process in self.all_processes:
            if process.id == id:
                return process


def main():
    s = System()
    for i in range(1, 9):
        s.create_process(i, True)

    p = s.get_process(5)
    p.crash_notice = True

    processes = s.get_all_process()

    global initiator

    for process in processes:
        if process.alive == False:
            print(f"Process {process.id} is crashed")

        if process.crash_notice:
            initiator = process
            print(f"Process {process.id} noticed the crash")

    print(f"Process {initiator.id} is initating the election ")

    election_message = []

    def conduct_election(id):
        process = s.get_process(id)
        if process != None:
            if process.alive:
                election_message.append(process.id)
            if s.get_next_process(id) == None:
                return None

        conduct_election(s.get_next_process(id).id)

    conduct_election(initiator.id)
    print(f"Election message is : {election_message}")
    s.get_process(election_message[-1]).coordinator = True
    print(f"Process {election_message[-1]} is the new coordiantor")


if __name__ == "__main__":
    main()
