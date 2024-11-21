def lzw_compress(data):
    """
    Function to compress a string using the LZW algorithm.
    Outputs both the code and its corresponding sequence.
    """
    # Initialize the dictionary with single-character ASCII mappings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256  # Code for the next new sequence
    w = ""  # Current sequence
    compressed = []  # Resulting compressed data

    print("Compression Steps:")
    print(f"{'Sequence':<10}{'Output Code':<15}")

    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc  # Sequence exists, continue building
        else:
            # Add the current sequence code to the result
            compressed.append(dictionary[w])
            print(f"{w:<10}{dictionary[w]:<15}")  # Print sequence and its code

            # Add new sequence to the dictionary
            dictionary[wc] = next_code
            next_code += 1
            w = c  # Start a new sequence

    # Add the last sequence
    if w:
        compressed.append(dictionary[w])
        print(f"{w:<10}{dictionary[w]:<15}")  # Print sequence and its code

    return compressed


def lzw_decompress(compressed):
    """
    Function to decompress a list of LZW codes back to the original string.
    """
    # Initialize the dictionary with single-character ASCII mappings
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256  # Code for the next new sequence

    # Start with the first code
    w = chr(compressed.pop(0))
    decompressed = [w]  # Resulting decompressed data

    for code in compressed:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = w + w[0]  # Special case: handle sequence not in the dictionary
        else:
            raise ValueError("Invalid code detected during decompression")

        decompressed.append(entry)

        # Add the new sequence to the dictionary
        dictionary[next_code] = w + entry[0]
        next_code += 1
        w = entry

    return "".join(decompressed)


if __name__ == "__main__":
    # Input data
    data = "ABABABA"

    print("Original Data:", data)
    print()

    # Compress the data
    compressed = lzw_compress(data)
    print("\nCompressed Data (Codes):", compressed)

    # Decompress the data
    decompressed = lzw_decompress(compressed)
    print("\nDecompressed Data:", decompressed)

    # Validate the result
    if data == decompressed:
        print("\nSuccess: Decompressed data matches the original!")
    else:
        print("\nError: Decompressed data does not match the original.")
