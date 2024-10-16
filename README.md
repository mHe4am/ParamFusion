# ParamFusion

ParamFusion is a Python script that consolidates a list of URLs with varying and repetitive query parameters. It parses each URL, extracts the parameters, and returns unique endpoints with their associated parameters.

## Motivation / Why ParamFusion Exists?

As someone who is interested in penetration testing and bug hunting, I often find myself dealing with large sets of URLs during the reconnaissance phase of assessments. While analyzing these URLs, I noticed a common challenge: many URLs contained repetitive parameters that cluttered the results, making it difficult to identify unique endpoints effectively.

To tackle this problem, I decided to create **ParamFusion**. This script simplifies the process of consolidating URLs, allowing for a clearer overview of unique endpoints and their parameters. By doing so, it enhances efficiency during security assessments and helps streamline the workflow for professionals in the field.

## Features

- **URL Parsing**: Parses input URLs to separate the base URL from its query parameters.
- **Parameter Consolidation**: Combines multiple instances of the same parameter for each unique URL.
- **Progress Tracking**: Displays progress while processing large lists of URLs.
- **Output File**: Saves the consolidated URLs with unique parameters to a specified output file.

## Usage

To run the script, you need Python 3 installed on your system.

```bash
git clone https://github.com/mHe4am/ParamFusion.git
cd ParamFusion
python3 ParamFusion.py <input_file> <output_file>
```

### Example

Given an `input.txt` file with the following content:

```
http://example.com/page?param1=value1&param2=value2
http://example.com/page?param1=value3
http://example.com/page?param2=value4
http://example.com/page?param3=value5&param2=value6
```

You would run:

```bash
python3 paramfusion.py input.txt output.txt
```

The `output.txt` will contain:

```
http://example.com/page?param1=value1&param2=value2&param3=value5
```

## Why it Exists?

I've created this script to get 

## Requirements

- Python 3.x
- Standard library modules (urllib.parse, collections, sys)


## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.


