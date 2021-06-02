class Process:
    def __init__(self, id, alive) -> None:
        self.id = id
        self.alive = alive
        self.coordinator = False
        self.crashNotice = False

    def know_all_processes(self):
        all_processes = System().get_all_processess()
        return all_processes

    def get_message(self, reqid):
        if reqid < self.id and self.alive:
            return "OK"
        else:
            return "Nil"


class System:
    all_processes = []

    def create_process(self, id, alive):
        process = Process(id, alive)
        self.all_processes.append(process)

    def get_all_processes(self):
        return self.all_processes

    def processes_count(self):
        return len(self.all_processes)

    def get_higher_ids(self, id):
        processes = []
        for process in self.all_processes:
            if process.id > id:
                processes.append(process.id)
        return processes

    def get_process(self, id):
        for process in self.all_processes:
            if process.id == id:
                return process


def main():
    s = System()
    for i in range(1, 11):
        s.create_process(i, True)
    p = s.get_process(5)
    p.crashNotice = True

    processes = s.get_all_processes()
    global intiator

    for process in processes:
        if process.alive == False:
            print(f"Process {process.id} is crashed")

        if process.crashNotice:
            intiator = process
            print(f"Process {process.id} noticed the crash")

    print(f"Process {intiator.id} is initiating the election")

    def conduct_election(id):
        next_available = []
        for i in s.get_higher_ids(id):
            if s.get_process(id).alive:
                message = s.get_process(i).get_message(id)
                print(f"Message from process {i} to {id} is {message}")
                if message == "OK":
                    next_available.append(i)

                if (
                    len(s.get_higher_ids(id) == 2)
                    and s.get_process(s.get_higher_ids[id][1]).alive == False
                ):
                    print(f"Process {i} is the new coordinator")

                s.get_process(i).coordinator = True
                quit()

        if len(next_available) == 0:
            print(f"Process {i} is the new coordiantor")
            s.get_process(id).coordinator = True
            quit()

        smaller = next_available[0]
        conduct_election(smaller)

    conduct_election(intiator.id)


if __name__ == "__main__":
    main()
