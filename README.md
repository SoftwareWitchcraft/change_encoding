# change_encoding

**A Python package to automate text file encoding conversions**

The `change_encoding` package helps you handle and standardize text file encodings effortlessly. It’s specifically designed for batch processing files, like subtitles, that often come in non-UTF-8 encodings.

## Features

- Converts all `.srt` files in a specified folder from one encoding to another.
- Creates a separate folder for converted files, preserving the originals.
- Handles encoding errors gracefully to avoid disruptions.
- Defaults to converting from `windows-1250` to `utf-8` (configurable).

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/SoftwareWitchcraft/change_encoding.git
cd change_encoding
pip3 install .
```

## Usage

Once installed, use the `chenc` command directly from the terminal:

```bash
chenc /path/to/folder source_encoding target_encoding
```

### Parameters:

- `/path/to/folder`: Directory containing the text files to convert.
- `source_encoding`: (Optional) Current encoding of the files (default: `windows-1250`).
- `target_encoding`: (Optional) Encoding to convert the files to (default: `utf-8`).

### Example:

Convert files in `/subtitles` folder from `windows-1250` to `utf-8`:

```bash
chenc /subtitles windows-1250 utf-8
```

## How It Works

1. Scans the specified folder for `.srt` files.
2. Reads each file using the provided source encoding.
3. Writes the content to a new file with the target encoding.
4. Saves converted files in a subfolder named after the target encoding.

### Example Folder Structure

Before Conversion:

```markdown
subtitles/   
├── episode1.srt   
├── episode2.srt
```

After Conversion:

```markdown
subtitles/   
├── episode1.srt   
├── episode2.srt   
└── utf-8/       
    ├── episode1.srt       
    ├── episode2.srt
```

## Extending the Package

Ideas for future improvements:

- [ ] Auto-detection of source encodings using libraries like `chardet` or `charset-normalizer`
- [ ] Support for additional file types such as `.txt` and `.csv`
- [ ] Recursive folder scanning
- [ ] Make default settings editable 

## Contributing

Feel free to open issues or submit pull requests to enhance the functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

