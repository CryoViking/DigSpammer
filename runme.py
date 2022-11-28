# Author: Cryosis
# Date: 2022-11-22

import time
import subprocess

class DNS_Server:
    def __init__(self) -> None:
        self.servers = [
            "8.8.8.8",
            "76.76.2.0",
            "9.9.9.9",
            "208.67.222.222",
            "1.1.1.1",
            "185.228.168.9",
            "76.76.19.19",
            "94.140.14.14"
        ]
        self.index = 0
        self.count = len(self.servers)
    
    def _inc_counter(self):
        self.index += 1
        if self.index >= len(self.servers):
            self.index = 0

    def next(self):
        server_to_return = self.servers[self.index]
        self._inc_counter()
        return server_to_return


# The main method
def __main__():
    filename = "domains.txt"
    attempts = 0
    DNSServer = DNS_Server()
    with open(filename, "r") as handle:
        # Get first line
        line = handle.readline().strip()

        # Iterate while line is not None
        while line is not None:
            print(f"Digging line: {line}")
            subprocess.run(["dig", line, f"@{DNSServer.next()}"])
            # Get next line
            line = handle.readline().strip()
            if attempts % DNSServer.count:
                time.sleep(1)

            attempts += 1

if __name__ == "__main__":
    __main__()