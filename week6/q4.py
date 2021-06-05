import random


class Process:
    def __init__(self, id, alive):
        self.id = id
        self.alive = alive
        self.cordinator = False
        self.crashNoticer = False


class System:
    allProcesses = []

    def createProcess(self, id, alive):
        process = Process(id, alive)
        self.allProcesses.append(process)

    def getAllProcessess(self):
        return self.allProcesses

    def processessCount(self):
        return len(self.allProcesses)

    def getNextProcess(self, id):
        return self.getProcess(id + 1)

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
s.createProcess(6, False)
s.createProcess(7, False)
s.createProcess(8, False)
"""
for i in range(1, 9):
    s.createProcess(i, True)


p = s.getProcess(5)
p.crashNoticer = True

processes = s.getAllProcessess()
global initiator

for process in processes:
    if process.alive == False:
        print(f" :|> Process {process.id} is crashed\n")
    if process.crashNoticer:
        initiator = process
        print(f" :|> Process {process.id} noticed the crash")

print(f":|> Process {initiator.id} is initiating the election\n")


electionMessage = []


def conductElection(id):
    process = s.getProcess(id)
    if process != None:
        if process.alive:
            electionMessage.append(process.id)
        if s.getNextProcess(id) == None:
            return None
    conductElection(s.getNextProcess(id).id)


conductElection(initiator.id)

print(f" :|>  Election message is {electionMessage} \n")


s.getProcess(electionMessage[-1]).coordinator = True

print(f":|> Process {electionMessage[-1]} is the new coordinator\n")
