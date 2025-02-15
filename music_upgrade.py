import os
import re

music_dir = "/Users/arneshpal/Music/NewPipe"
output_dir = "/Users/arneshpal/Downloads/mm"

# Function to clean filename and extract words
def extract_words(filename):
    filename = filename.lower()
    filename = re.sub(r"[^\w\s]", "", filename)  # Remove special characters
    words = filename.split()
    return set(words)  # Convert to set for easy comparison

# Get file names without extensions
music_files = {os.path.splitext(f)[0] for f in os.listdir(music_dir) if os.path.isfile(os.path.join(music_dir, f))}
output_files = {os.path.splitext(f)[0] for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))}

# Extract words from filenames
music_words = {f: extract_words(f) for f in music_files}
output_words = {f: extract_words(f) for f in output_files}

# Find matches where at least 1 word overlaps
missing_files = []

for music_file, music_word_set in music_words.items():
    found = False
    for output_word_set in output_words.values():
        if music_word_set & output_word_set:  # At least 1 common word
            found = True
            break
    if not found:
        missing_files.append(music_file)

# Save results
report_file = os.path.join(output_dir, "final_missing_files.txt")
with open(report_file, "w") as f:
    f.write(f"Total files in NewPipe: {len(music_files)}\n")
    f.write(f"Total downloaded files: {len(output_files)}\n")
    f.write(f"Completely missing files: {len(missing_files)}\n\n")

    f.write("Completely Missing Files ❌:\n")
    for file in missing_files:
        f.write(f"{file}\n")

print(f"Final missing file report saved to {report_file}")
