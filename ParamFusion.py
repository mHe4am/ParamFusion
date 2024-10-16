#!/usr/bin/env python3
"""
Takes a list of different endpoints, each with varying and repetitive parameters, and returns each endpoint along with its associated parameters.
"""

import urllib.parse
from collections import defaultdict
import sys


def parse_url(url):
    parsed = urllib.parse.urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}" if parsed.scheme else f"{parsed.netloc}{parsed.path}"
    params = urllib.parse.parse_qsl(parsed.query)
    return base, params


def consolidate_urls(urls, total_urls):
    consolidated = defaultdict(list)
    for i, url in enumerate(urls, 1):
        base, params = parse_url(url)
        consolidated[base].extend(params)
        if i % 10000 == 0 or i == total_urls:
            print(f"\rProcessing: {i:,}/{total_urls:,}", end="", flush=True)

    print()  # New line after progress tracking

    result = []
    for base, params in consolidated.items():
        seen = set()
        unique_params = []
        for param, value in params:
            if param not in seen:
                seen.add(param)
                unique_params.append((param, value))

        query = urllib.parse.urlencode(unique_params)
        result.append(f"{base}?{query}" if query else base)

    return result


def main():
    script_name = sys.argv[0]
    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        print(f"\n[*] Usage: python3 {script_name} <input_file> <output_file>")
        sys.exit(1)

    print("\n" + "=" * 50)
    print(f"{' ParamFusion ':=^50}")
    print("=" * 50)

    with open(input_file, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]

    total_urls = len(urls)
    print(f"\n[*] Imported {total_urls:,} URLs from {input_file}")

    print("\n[*] Processing URLs...")
    consolidated_urls = consolidate_urls(urls, total_urls)

    with open(output_file, 'w') as file:
        for url in consolidated_urls:
            file.write(f"{url}\n")

    print(f"\n[*] Consolidation complete!")
    print(f"[*] Input: {total_urls:,} URLs")
    print(f"[*] Output: {len(consolidated_urls):,} unique endpoints")
    print(f"[*] Results saved to: {output_file}")
    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()