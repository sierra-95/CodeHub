#!/usr/bin/env python3
"""Opening a binary file for writing"""

with open('binary_data.bin', 'wb') as file:
    data = b'\x48\x65\x6c\x6c\x6f'  # Binary data (Hello in ASCII)
    file.write(data)