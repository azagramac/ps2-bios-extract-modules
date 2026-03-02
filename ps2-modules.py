#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib

# ---------------- MD5 UTILITY ----------------
def md5sum(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

# ---------------- ROM FUNCTIONS ----------------
def romOPEN(romfile):
    print(f"🔹 Processing {romfile} 🔹")
    print(f"🆔 Detected model: {romfile.split('.')[0]}")
    romsize = os.path.getsize(romfile)
    print(f"📦 Size of {romfile}: {romsize} bytes")
    rom = open(romfile, 'rb')
    return rom, romsize

def findROMDIRSIZE(file, romsize):
    file.seek(0)
    for i in range(romsize):
        a = file.read(1)
        if not a:
            break
        if a[0] == 0x52:  # 'R'
            b = list(file.read(4))
            if b == [0x45,0x53,0x45,0x54]:  # ESET
                h = file.tell() - 5
                f = parseSIZE(file, (h + 0x10 + 2 + 10))
                return h, f
    return None, None

def parseSIZE(file, offset):
    file.seek(offset)
    d = file.read(4)
    if len(d) < 4:
        return 0
    return int.from_bytes(d[::-1], byteorder='big')

# ---------------- ROMDIR PARSING ----------------
def parseROMDIR(file, romdir_location):
    if not romdir_location or romdir_location[0] is None:
        return []
    start, size = romdir_location
    file.seek(start)
    modules = []
    count = (size // 16) - 1
    offset_acc = 0
    for i in range(count):
        name_bytes = file.read(10)
        try:
            name = name_bytes.decode('ascii').rstrip('\x00')
        except:
            name = ''
        if not name:
            name = f"MOD_{i}"
        file.seek(file.tell()+2)
        mod_size = parseSIZE(file, file.tell())
        modules.append([name, offset_acc, mod_size])
        offset_acc += mod_size
    return modules

# ---------------- MODULE EXTRACTION ----------------
def extractModule(romfile, module, outdir, idx):
    name, offset, size = module
    filename = os.path.join(outdir, f"{idx}_{name}.bin")
    romfile.seek(offset)
    data = romfile.read(size)
    with open(filename, "wb") as f:
        f.write(data)
    md5 = md5sum(filename)
    print(f"📄 {idx}. {name} -> {filename} (MD5: {md5})")
    return [idx, name, size, size, outdir, md5]

# ---------------- PROCESS FILE ----------------
def process_file(filename):
    if filename.lower().endswith(('.mec', '.nvm')):
        print(f"⚠️ Skipping {filename} (raw binary file without modules)")
        return []

    romfile, size = romOPEN(filename)
    romdir_location = findROMDIRSIZE(romfile, size)
    modules_summary = []

    if romdir_location and romdir_location[0] is not None:
        outdir = f"modules-{filename}"
        os.makedirs(outdir, exist_ok=True)
        modules = parseROMDIR(romfile, romdir_location)
        print(f"📂 Extracting {len(modules)} modules into {outdir} ...")
        for i, mod in enumerate(modules):
            modules_summary.append(extractModule(romfile, mod, outdir, i))
        print(f"✅ Extraction completed for {filename}\n")
    else:
        print(f"⚠️ ROMDIR not found in {filename}, copying full file as raw")
        romfile.seek(0)
        data = romfile.read()
        raw_filename = f"{filename}"
        with open(raw_filename, "wb") as f:
            f.write(data)
        md5 = hashlib.md5(data).hexdigest()
        modules_summary.append(['RAW', raw_filename, size, size, '', md5])
        print(f"📄 {raw_filename} -> {raw_filename} (raw, MD5: {md5})")

    romfile.close()
    return modules_summary

# ---------------- MARKDOWN ----------------
def writeMarkdown(all_modules, input_files, mdfile="bios_modules.md"):
    with open(mdfile, "w") as f:
        f.write("# 📜 Extracted BIOS Modules\n\n")

        # Input files summary
        f.write("## 🗂 Input Files MD5\n\n")
        f.write("| File | Size (bytes) | MD5 |\n")
        f.write("|------|--------------|-----|\n")
        for file in input_files:
            size = os.path.getsize(file)
            md5 = md5sum(file)
            f.write(f"| {file} | {size} | `{md5}` |\n")
        f.write("\n")

        # Module table structured by input file
        for file in input_files:
            f.write(f"## 📂 Modules from {file}\n\n")
            f.write("| # | Module | Size (bytes) | MD5 |\n")
            f.write("|---|--------|--------------|-----|\n")
            for mod in all_modules:
                idx, name, size, _, folder, md5 = mod
                if folder.endswith(file):
                    f.write(f"| {idx} | {name} | {size} | `{md5}` |\n")
            f.write("\n")
    print(f"\n✅ Markdown generated: {mdfile}")

# ---------------- MAIN ----------------
def main():
    files = [f for f in os.listdir('.') if f.lower().endswith(('.mec','.nvm','.rom0','.rom1','.rom2'))]
    all_modules = []
    for f in files:
        all_modules.extend(process_file(f))

    writeMarkdown(all_modules, files)

if __name__ == "__main__":
    main()
