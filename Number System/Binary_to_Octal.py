def bin_to_oct_fast(binary: str) -> str:
    binary = binary.replace(' ', '').removeprefix('0b')
    if not binary:
        return '0'
        
    # Pad left with zeros so length is multiple of 3
    r = len(binary) % 3
    if r:
        binary = '0' * (3 - r) + binary
    
    # 4-bit → 1 octal digit lookup (very fast)
    lookup = {
        '000': '0', '001': '1', '010': '2', '011': '3',
        '100': '4', '101': '5', '110': '6', '111': '7'
    }
    
    result = []
    for i in range(0, len(binary), 3):  
        result.append(lookup[binary[i:i+3]])
    
    # Remove leading zeros (but keep at least one digit)
    return ''.join(result).lstrip('0') or '0'  
binary = '010101'
print(bin_to_oct_fast(binary))