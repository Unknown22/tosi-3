#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import sys
from bbs import BlumBlumShub


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def process_vernam_cypher(text, key=None):
    if key:
        p = 0
        answer = ""
        for ch in text:
            answer += str(int(ch) ^ int(key[p]))
            p += 1
        n = 10
        answer = [answer[i:i + n] for i in range(0, len(answer), n)]

        answer = [chr(int(el, 2)) for el in answer]
        answer = "".join([el for el in answer])
        key_bits = None
    else:
        bin_text = ''.join('{0:010b}'.format(ord(x), 'b') for x in text)
        bbs_instance = BlumBlumShub()
        key_bits = bbs_instance.run_bbs(bits=512, len_of_message=len(bin_text))
        answer = ""
        p = 0
        for ch in bin_text:
            answer += str(int(ch) ^ int(key_bits[p]))
            p += 1

    return answer, key_bits


def main():
    with open("test.txt", "r", encoding='utf8') as file, open("test_2.txt", "w", encoding='utf8') as w_file:
        message = file.read()

        answer, key = process_vernam_cypher(text=message, key=None)
        message, key = process_vernam_cypher(text=answer, key=key)
        w_file.write(message)
    # print(encoded_message)
    # print(process_vernam_cypher(text=encoded_message, key=test_key))


if __name__ == "__main__":
    main()
