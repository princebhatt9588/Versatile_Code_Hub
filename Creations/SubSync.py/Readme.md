# SRT Subtitle Timestamp Synchronization Script

This script is designed to synchronize the timestamps in an SRT (SubRip) subtitle file by applying a user-specified time shift. SRT files are commonly used to provide subtitles for videos, and each subtitle entry is associated with a start and end timestamp indicating when the subtitle should be displayed.

## How It Works

The script consists of three main functions: `convertToMilliseconds`, `synchronize`, and `convertToTime`, as well as a `main` function that orchestrates the process. Here's how each function works:

### `convertToMilliseconds(time)`

This function takes a timestamp in the format "hh:mm:ss,mmm" and converts it into milliseconds. It does so by extracting the hours, minutes, and milliseconds components from the timestamp and then calculating the equivalent time in milliseconds.

### `synchronize(time, shift)`

This function takes a timestamp in milliseconds and applies a time shift to it. The shift value is provided by the user. The function subtracts the shift from the input timestamp to effectively move the time forward or backward.

### `convertToTime(milliseconds)`

This function converts milliseconds back into the "hh:mm:ss,mmm" timestamp format. It extracts the hours, minutes, seconds, and milliseconds components from the milliseconds value and formats them into the desired timestamp format.

### `main()`

The `main` function is the entry point of the script. It prompts the user to input the desired time shift in milliseconds. It then reads an input SRT file named "input.srt", processes each line, and applies the time shift to the timestamp lines. The updated lines are written to an output file named "output.srt". Lines that are not timestamps are copied as they are to the output file.

## Running the Script

1. Make sure you have Python installed on your system.
2. Place the script in the same directory as your "input.srt" file.
3. Run the script. It will prompt you to enter the time shift in milliseconds.
4. The script will create an "output.srt" file with synchronized timestamps.

## Example Output

Assuming the input SRT file contains the following content:

```
1
00:00:10,000 --> 00:00:15,000
Subtitle line 1

2
00:00:20,000 --> 00:00:25,000
Subtitle line 2
```

If you input a shift of 5000 milliseconds, the output "output.srt" file will contain:

```
1
00:00:15,000 --> 00:00:20,000
Subtitle line 1

2
00:00:25,000 --> 00:00:30,000
Subtitle line 2
```

## Note

- Make sure the input SRT file follows the standard format with subtitles represented by sequential numbers, timestamp lines, and content lines.
- The script assumes the input SRT file is named "input.srt" and will create the output in "output.srt".
- The script processes timestamps using milliseconds precision.
- Always make backups of your files before running scripts that modify them.

This README provides an overview of the script's functionality, usage, and example output. Make sure to read and understand the code thoroughly before using it on important files.