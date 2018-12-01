#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import os
from bbs import BlumBlumShub


def process_vernam_cypher(text, key=None):
    bin_text = ''.join('{0:010b}'.format(ord(x), 'b') for x in text)
    if key:
        key = ''.join('{0:010b}'.format(ord(x), 'b') for x in key)
        p = 0
        answer = ""
        for ch in bin_text:
            answer += str(int(ch) ^ int(key[p]))
            p += 1
        n = 10
        answer = [answer[i:i + n] for i in range(0, len(answer), n)]

        answer = [chr(int(el, 2)) for el in answer]
        answer = "".join([el for el in answer])
        key_to_return = None
    else:
        bbs_instance = BlumBlumShub()
        key_bits = bbs_instance.run_bbs(bits=512, len_of_message=len(bin_text))
        answer = ""
        p = 0
        for ch in bin_text:
            answer += str(int(ch) ^ int(key_bits[p]))
            p += 1

        n = 10
        tmp = [answer[i:i + n] for i in range(0, len(answer), n)]
        tmp = [chr(int(el, 2)) for el in tmp]
        tmp = "".join([el for el in tmp])
        answer = tmp

        tmpk = [key_bits[i:i + n] for i in range(0, len(key_bits), n)]
        tmpk = [chr(int(el, 2)) for el in tmpk]
        tmpk = "".join([el for el in tmpk])
        key_to_return = tmpk

    return answer, key_to_return


def main():
    with open("test.txt", "r", encoding='utf8') as file, open("test_2.txt", "w", encoding='utf8') as w_file:
        message = file.read()

        print("To cipher:", message)
        w_file.write(message)
        w_file.write("\n")
        answer, key = process_vernam_cypher(text=message, key=None)
        print("Ciphered message:", answer)
        print("Key:", key)
        w_file.write(answer)
        w_file.write("\n")
        w_file.write(key)
        w_file.write("\n")
        message, key = process_vernam_cypher(text=answer, key=key)
        print("Deciphered message:", message)
        w_file.write(message)
        w_file.write("\n")
    # print(encoded_message)
    # print(process_vernam_cypher(text=encoded_message, key=test_key))


if __name__ == "__main__":
    main()
