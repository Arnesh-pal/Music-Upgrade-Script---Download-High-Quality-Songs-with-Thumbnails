# Music-Upgrade-Script---Download-High-Quality-Songs-with-Thumbnails

## Overview
This script automates upgrading your music collection by downloading higher-quality versions of existing songs with embedded metadata and thumbnails. It uses `yt-dlp` to fetch the best available audio quality from YouTube and ensures all songs are replaced with their highest-quality versions.

## Features
- Automatically identifies and upgrades songs in a specified directory.
- Downloads the highest-quality available audio.
- Embeds album artwork (thumbnail) and metadata.
- Ensures an organized and clean music library.

## Requirements
- Python 3.x installed
- `yt-dlp` installed (`pip install yt-dlp`)
- `ffmpeg` installed (for audio conversion)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/music-upgrade-script.git
   cd music-upgrade-script
   ```
2. Install dependencies:
   ```sh
   pip install yt-dlp
   ```
3. Ensure `ffmpeg` is installed. On Debian-based systems:
   ```sh
   sudo apt install ffmpeg
   ```
   On macOS (using Homebrew):
   ```sh
   brew install ffmpeg
   ```

## Usage
1. Update `music_dir` and `output_dir` in the script to match your local music collection.
2. Run the script:
   ```sh
   python music_upgrade.py
   ```
3. The script will:
   - Scan your music directory.
   - Search for higher-quality versions.
   - Download and replace the existing songs.
   - Embed metadata and album artwork.

## Code Explanation
1. **Setup Directories:**
   - The script defines `music_dir` (your existing music folder) and `output_dir` (where upgraded songs are saved).
   - It ensures the output directory exists.
2. **Process Each File:**
   - Extracts song titles from filenames.
   - Uses `yt-dlp` to search for and download the highest-quality version.
   - Saves the upgraded song with metadata and thumbnail embedded.
3. **Automation:**
   - Runs through all files in the directory, replacing them with better versions.
   - Prints status updates to keep track of progress.

## Example
Before:
```
/Users/arneshpal/Music/NewPipe/song1.mp3
```
After running the script:
```
/Users/arneshpal/Downloads/mm/song1.mp3  (Now higher quality with metadata and thumbnail)
```

## License
This project is open-source and available under the MIT License.

