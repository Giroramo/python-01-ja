def encode(message):
    if not message:
        return "Empty input"
    
    encoded_message = []
    for char in message:
        encoded_message.append(str(ord(char)))
    
    return ' '.join(encoded_message)

def decode(encoded_message):
    if not encoded_message:
        return "Empty input"
    
    decoded_message = []
    unicode_list = encoded_message.split()
    for code in unicode_list:
        decoded_message.append(chr(int(code)))
    
    return ''.join(decoded_message)

# テスト
message = "Hello World"
encoded = encode(message)
print(encoded)  # 出力: 72 101 108 108 111 32 87 111 114 108 100
decoded = decode(encoded)
print(decoded)  # 出力: Hello World
