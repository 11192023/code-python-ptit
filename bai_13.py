def encode_and_reverse(K, S):
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    encoded_string = ""
    for char in S:
        print(P.index(char))
        encoded_char_index = (P.index(char) + K) % 28
        encoded_string += P[encoded_char_index]
    return encoded_string[::-1]

while True:
    K, S = input().split()
    K = int(K)
    if K == 0:
        break
    encoded_result = encode_and_reverse(K, S)
    print(encoded_result)
