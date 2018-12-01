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
        print("Bin_text", answer)
        answer = [answer[i:i + n] for i in range(0, len(answer), n)]
        print("Answer:", answer)

        answer = [bytes(el, encoding='utf-8').decode() for el in answer]
        print("Answer 2:", answer)
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
        print("Bin_text",bin_text)
        print("Key bits:",key_bits)
        print("Answer ciphered:",answer)

    return answer, key_bits
    # bin_text = [bin(ord(x))[2:] for x in text]
    # bin_text = "".join(el for el in bin_text)
    # bbs_instance = BlumBlumShub()
    # if key:
    #     key_bits = [bin(ord(x))[2:] for x in key]
    #     key_bits = "".join(el for el in key_bits)
    # else:
    #     key_bits = bbs_instance.run_bbs(bits=512, len_of_message=len(bin_text))
    #
    # print(bin_text)
    # print(key_bits)
    # answer = ""
    # p = 0
    # for ch in bin_text:
    #     answer += str(int(ch) ^ int(key_bits[p]))
    #     p += 1
    # # answer = int(bin_text) ^ int(key_bits)
    # n = 6
    # ciphered_msg = [answer[i:i + n] for i in range(0, len(answer), n)]
    # ciphered_msg = "".join(el for el in [chr(int(x)) for x in ciphered_msg])
    # key = [str(key_bits)[i:i + n] for i in range(0, len(str(key_bits)), n)]
    # key = "".join(el for el in [chr(int(x)) for x in key])
    # return ciphered_msg, key
    # # return text_from_bits(), text_from_bits(key_bits)
    # return text_from_bits(int(answer))


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