import copy

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    disk_map = [(int(v), int(y)) for v, y in zip(lines[0].strip()[::2], lines[0].strip()[1::2])]
    if len(lines[0].strip()) % 2 :
        disk_map.append((int(lines[0].strip()[-1]), 0))
    return disk_map

def expand_disk(disk_map):
    disk = []
    for file_id, (file_size, void_size) in enumerate(disk_map):
        for _ in range(file_size):
            disk.append(file_id)
        for _ in range(void_size):
            disk.append('.')
    return disk

def defragment(disk):
    voids = []
    used = []

    for i, element in enumerate(disk):
        if element == '.':
            voids.append(i)
        else:
            used.append((element, i))

    used = iter(reversed(used))
    for void in voids:
        # Grab an element
        element, i = next(used)
        if i <= void:
            break
        disk[void] = element
        disk[i] = '.'
        # print_disk(disk)

    return disk

def defragment_files(disk, disk_map):
    voids = []
    files = []

    location = 0
    for file_id, (file_size, void_size) in enumerate(disk_map):
        if file_size:
            files.append((file_size, location, file_id))
        if void_size:
            voids.append((void_size, location + file_size))
        location += file_size + void_size

    files = iter(reversed(files))
    for file_size, file_location, file_id in files:
        for i, (void_size, void_location) in enumerate(voids):
            if file_size <= void_size:
                for offset, _ in enumerate(disk[void_location:void_location + file_size]):
                    disk[void_location + offset] = file_id
                for offset, _ in enumerate(disk[file_location:file_location + file_size]):
                    disk[file_location + offset] = '.'
                if void_size == file_size:
                    del voids[i]
                else:
                    voids[i] = (void_size - file_size, void_location + file_size)
                break

        # print_disk(disk)
    return disk


def calculate_checksum(disk):
    sum = 0
    for i, id in enumerate(disk):
        if id == '.':
            continue
        sum += i * id
    return sum

def print_disk(disk):
    print(''.join(str(element) for element in disk))

def main():
    disk_map = read_input("day09/input/input.txt")
    disk = expand_disk(disk_map)
    disk_copy = copy.deepcopy(disk)
    # print_disk(disk)
    disk = defragment(disk)
    checksum = calculate_checksum(disk)
    print(f"Part 1: {checksum}")

    disk = defragment_files(disk_copy, disk_map)
    # print_disk(disk)
    checksum = calculate_checksum(disk)
    try:
        assert(checksum < 8355781418715)
    except AssertionError:
        print(f"Part 2: {checksum} is to high!")
        exit()

    print(f"Part 2: {checksum}")

if __name__ == '__main__':
    main()
