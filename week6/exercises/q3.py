import os
import random


class Process:
    def __init__(self, id, alive) -> None:
        self.id = id
        self.alive = alive
        self.coordinator = False
        self.crashNoticer = False

    def know_all_processes(self):
        all_processes = System().get_all_processess()
        return all_processes

    def get_message(self, reqid):
        if reqid < self.id and self.alive:
            return "Alive"
        else:
            return "Not Alive"


class System:
    all_processes = []

    def create_process(self, id, alive):
        process = Process(id, alive)
        self.all_processes.append(process)

    def get_all_processes():
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
