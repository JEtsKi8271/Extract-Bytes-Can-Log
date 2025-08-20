import re
import os

# change this to your log file name
filename = "note pad name" #put yout txt log name
base_name = os.path.splitext(os.path.basename(filename))[0]
output_file = base_name + "_ExactBytes.txt"

# use a set to avoid duplicates
unique_frames = set()

with open(filename, "r", errors="ignore") as f:
    for line in f:
        # Match CAN ID + up to 8 data bytes (hex)
        match = re.match(r"(0x[0-9A-Fa-f]+)\s+((?:[0-9A-Fa-f]{2}\s+){0,7}[0-9A-Fa-f]{2})", line)
        if match:
            can_id = match.group(1)
            data_bytes = match.group(2).split()
            # pad with zeros if fewer than 8 bytes
            while len(data_bytes) < 8:
                data_bytes.append("00")
            # only take first 8 if more
            data_bytes = data_bytes[:8]
            # add 0x prefix to each byte
            data_bytes = tuple(f"0x{b.upper()}" for b in data_bytes)
            # store unique (CAN ID + data) combinations
            unique_frames.add((can_id, data_bytes))

# write unique frames to file
with open(output_file, "w") as f:
    for can_id, data in sorted(unique_frames, key=lambda x: int(x[0], 16)):
        byte_str = ", ".join(data)
        f.write(f"CanSend({can_id}, {byte_str});\n")

print(f"Exported {len(unique_frames)} unique frames to {output_file}")
