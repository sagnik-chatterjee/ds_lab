class Process:
    def __init__(self, id, alive):
        self.id = id
        self.alive = alive
        self.cordinator = False
        self.crashNoticer = False

    def knowAllProcesses(self):
        allProcesses = System().getAllProcessess()
        return allProcesses

    def getMessage(self, reqId):
        if reqId < self.id and self.alive:
            return "OK"
        else:
            return "NOT OK"


class System:
    allProcesses = []

    def createProcess(self, id, alive):
        process = Process(id, alive)
        self.allProcesses.append(process)

    def getAllProcessess(self):
        return self.allProcesses

    def processessCount(self):
        return len(self.allProcesses)

    def getHigherIds(self, id):
        processes = []
        for process in self.allProcesses:
            if process.id > id:
                processes.append(process.id)
        return processes

    def getProcess(self, id):
        for process in self.allProcesses:
            if process.id == id:
                return process


s = System()
"""
s.createProcess(1, True)
s.createProcess(2, True)
s.createProcess(3, True)
s.createProcess(4, True)
s.createProcess(5, True)
s.createProcess(6, True)
s.createProcess(7, True)
s.createProcess(8, True)
s.createProcess(9, False)
s.createProcess(10, True)
"""
for i in range(1, 11):
    s.createProcess(i, True)


p = s.getProcess(5)
p.crashNoticer = True

processes = s.getAllProcessess()
global initiator

for process in processes:
    if process.alive == False:
        print(f" :|> Process {process.id} is crashed.")
    if process.crashNoticer:
        initiator = process
        print(f" :|> Process {process.id} noticed the crash.")

print(f" :|> Process {initiator.id} is initiating the election.")


def conductElection(id):
    nextAvailable = []
    for i in s.getHigherIds(id):
        if s.getProcess(id).alive:
            message = s.getProcess(i).getMessage(id)
            print(f" :|> Message from process {i} to {id} is {message}")
            if message == "OK":
                nextAvailable.append(i)
            if (
                len(s.getHigherIds(id)) == 2
                and s.getProcess(s.getHigherIds(id)[1]).alive == False
            ):
                print(f" :|> Process {i} is new coordinator.")
                s.getProcess(i).coordinator = True
                quit()
    print("\n")
    if len(nextAvailable) == 0:
        print(f" :|> Process {id} is new coordinator.")
        s.getProcess(id).coordinator = True
        quit()
    smaller = nextAvailable[0]
    conductElection(smaller)


conductElection(initiator.id)
