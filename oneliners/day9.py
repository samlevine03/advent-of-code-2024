digits = [int(c) for c in open('../inputs/day9.txt').read().strip()]
disk = sum([[-1 if idx % 2 else idx // 2] * n for idx, n in enumerate(digits)], [])
fill = [x for x in disk[::-1] if x >= 0]
print(sum(i * v if v >= 0 else i * fill.pop(0) for i, v in enumerate(disk[:len(fill)])))

files, free, pos, id = [], [], 0, 0
[files.append((id, pos, digits[i])) or (id := id + 1, pos := pos + digits[i])[0] if digits[i] > 0 else None for i in range(0, len(digits), 2)]
[free.append((pos, digits[i + 1])) or (pos := pos + digits[i + 1]) if i + 1 < len(digits) and digits[i + 1] > 0 else None for i in range(0, len(digits), 2)]
files.sort(reverse=True)
free = [(spos + flen, slen - flen) if (flen := files[idx][2]) <= slen and spos < files[idx][1] else (spos, slen) for idx, (fid, fpos, _) in enumerate(files) for j, (spos, slen) in enumerate(free) if spos < fpos and slen >= flen]
print(sum((fpos + i) * fid for fid, fpos, flen in files for i in range(flen)))

# what an abomination this file is.