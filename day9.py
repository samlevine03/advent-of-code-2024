with open("inputs/day9.txt") as f:
    input = f.read().strip()

# input = "2333133121414131402"

blocks = []
is_free_space = False
id = 0
free_spaces = []
blocks_stack = []
for c in input:
    for i in range(int(c)):
        if is_free_space:
            free_spaces.append(len(blocks))
            blocks.append(-1)
        else:
            blocks.append(id)
            blocks_stack.append(id)
    if not is_free_space:
        id += 1
    is_free_space = not is_free_space

num_blocks = len(blocks_stack)

# print(blocks)
# print(free_spaces)

for idx in free_spaces:
    blocks[idx] = blocks_stack.pop()

# print(blocks[0:num_blocks])

res = 0
for i, n in enumerate(blocks[0:num_blocks]):
    res += i*n

print(res)

### PART 2:

# BLOCKS = []
# block_id = 0
# free_id = -1
# is_free_space = False
# stack = []
# free_id_to_size = {}
# for c in input:
#     for i in range(int(c)):
#         if is_free_space:
#             free_spaces.append(len(BLOCKS))
#             BLOCKS.append(free_id)
#             if free_id not in free_id_to_size:
#                 free_id_to_size[free_id] = int(c)
#         else:
#             BLOCKS.append(block_id)
#             if not stack or stack[-1] != (block_id, int(c)):
#                 stack.append((block_id, int(c)))
#     if not is_free_space:
#         block_id += 1
#     else:
#         free_id -= 1
#     is_free_space = not is_free_space

# print(BLOCKS)
# # print(stack)
# print(free_id_to_size)
# back_ptr = len(BLOCKS) - 1

# while stack:
#     id, size = stack.pop()
#     i = 0
#     while i < len(BLOCKS):
#         while BLOCKS[back_ptr] != id:
#             back_ptr -= 1
#         while i < len(BLOCKS) and free_id_to_size.get(BLOCKS[i], 0) < size:
#             i += 1
#         if i == len(BLOCKS): break
#         free_id = BLOCKS[i]
#         for _ in range(size):
#             BLOCKS[i] = id
#             i += 1
#             BLOCKS[back_ptr] = 0
#             back_ptr -= 1
#         if free_id in free_id_to_size:
#             free_id_to_size[free_id] -= size
#         break

# # print(BLOCKS)

# for n in BLOCKS:
#     if n <= 0:
#         n = 0

# print(BLOCKS)

# res = 0
# for i, n in enumerate(BLOCKS):
#     if n > 0:
#         res += i*n

# print(res)
# idk why this doesnt work so just giving up and doing a new approach

files = []
free = []
pos = 0
id = 0
digits = list(map(int, input))
for i in range(0, len(digits), 2):
    file_len = digits[i]
    if i + 1 < len(digits):
        free_len = digits[i + 1]
    else:
        free_len = 0

    if file_len > 0:
        files.append((id, pos, file_len))
        id += 1
        pos += file_len
    if free_len > 0:
        free.append((pos, free_len))
        pos += free_len

files.sort(key=lambda x: x[0], reverse=True)

for idx, (fid, fpos, flen) in enumerate(files):
    for j, (spos, slen) in enumerate(free):
        if spos < fpos and slen >= flen:
            # move the file
            files[idx] = (fid, spos, flen)
            # update free space
            new_free_start = spos + flen
            new_free_len = slen - flen
            # replace this free block with the new (possibly smaller) one
            free[j] = (new_free_start, new_free_len) if new_free_len > 0 else (new_free_start, 0)
            break

checksum = 0
for (fid, fpos, flen) in files:
    for i in range(flen):
        pos = fpos + i
        checksum += pos * fid

print(checksum)