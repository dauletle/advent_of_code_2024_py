import os
from collections import deque

DEBUG = True

def get_data():
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    data = []
    with open(input_filename, "r") as f:
        # Read data
        data = f.readline().strip()
    return data

class DiskMap:
    def __init__(self, disk_map_input):
        self.disk_map_input = disk_map_input
        self.file_space_queue = deque([])
        self.free_space_queue = deque([])
        self.file_id = 0
        self.full_disk_map = []
        self.pos = 0

    def decrypt_disk_map(self):
        for c_idx, char in enumerate(self.disk_map_input):
            if c_idx % 2 == 0:
                for i in range(int(char)):
                    self.full_disk_map.append(self.file_id)
                    self.file_space_queue.append((self.pos, 1, self.file_id))
                    self.pos += 1
                self.file_id += 1
            else:
                self.free_space_queue.append((self.pos, int(char)))
                for i in range(int(char)):
                    self.full_disk_map.append(None)
                    self.pos += 1
        
    def compact_disk_map(self):
        for (pos, size, file_id) in reversed(self.file_space_queue):
            for space_i,(space_pos, space_size) in enumerate(self.free_space_queue):
                if space_pos < pos and size <= space_size:
                    for i in range(size):
                        assert self.full_disk_map[pos+i] == file_id, f'{self.full_disk_map[pos+i]=}'
                        self.full_disk_map[pos+i] = None
                        self.full_disk_map[space_pos+i] = file_id
                    self.free_space_queue[space_i] = (space_pos + size, space_size-size)
                    break
    
    def get_checksum(self, full_disk_map):
        ans = 0
        for c_idx, char in enumerate(full_disk_map):
            if char is not None:
                ans += c_idx*char
        return ans


def __main__():
    disk_map_input = get_data()
    if DEBUG:
        print("Disk Map Input:", disk_map_input)
        print()
    dm = DiskMap(disk_map_input)
    dm.decrypt_disk_map()
    if DEBUG:
        print("Expanded Disk Map:", dm.file_space_queue)
        print("Free Space Queue:", dm.free_space_queue)
        print("Full Disk Map:", dm.full_disk_map)
        print()
    dm.compact_disk_map()
    if DEBUG:
        print("Compact Disk Map:", dm.full_disk_map)
    print("Checksum:", dm.get_checksum(dm.full_disk_map))
    
    

if __name__ == "__main__":
    __main__()