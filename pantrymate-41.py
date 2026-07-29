# === Stage 41: Add plain text import for a simple line-based format ===
# Project: PantryMate
def parse_line(text):
    """Parse a single line into a dictionary of key-value pairs."""
    result = {}
    for token in text.split(','):
        if ':' in token:
            key, value = token.split(':', 1)
            result[key.strip()] = value.strip()
    return result

def format_line(data):
    """Format a dictionary into a single line string."""
    parts = [f"{k}:{v}" for k, v in data.items()]
    return ', '.join(parts)

def read_lines(filename):
    """Read lines from file and parse each one into a dict."""
    records = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                records.append(parse_line(line))
    return records

def write_lines(filename, records):
    """Write records to file as comma-separated key:value lines."""
    with open(filename, 'w') as f:
        for record in records:
            f.write(format_line(record) + '\n')
