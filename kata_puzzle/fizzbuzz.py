# -*- coding: UTF-8 -*-
# !/usr/bin/bash python3
# ----------------------------------
# Name:          fizzbuzz
# Purpose:

# Author:        ronniefeng
# Copyright:     (C) AIDC, Tencent 2019
# Licence: 
#
# Created:       2019-05-23
# Modified:
# Contributors:
#
# ----------------------------------

import sys
import fire


class FizzBuzz(object):
    """
    class comment
    """

    def __init__(self, fizz, buzz):
        self.fizz = fizz
        self.buzz = buzz

    def is_fizz(self, number):
        if number % self.fizz == 0 or str(self.fizz) in str(number):
            return True

        return False

    def is_buzz(self, number):
        if number % self.buzz == 0 or str(self.buzz) in str(number):
            return True

        return False

    # def is_fizz_buzz(self, number):
    #     if self.is_fizz(number) and self.is_buzz(number):
    #         return True
    #
    #     return False

    def report(self, number):
        # if self.is_fizz_buzz(number):
        #     return "FizzBuzz"
        #
        # if self.is_fizz(number):
        #     return "Fizz"
        #
        # if self.is_buzz(number):
        #     return "Buzz"

        s = ''
        if self.is_fizz(number):
            s += "Fizz"
        if self.is_buzz(number):
            s += "Buzz"

        if not s:
            s = str(number)

        return s


def count_off(count, fizz, buzz):
    fb = FizzBuzz(fizz, buzz)

    for n in range(1, count + 1):
        s = fb.report(n)
        print("%i -> %s" % (n, s))


def main():

    fire.Fire()

if __name__ == '__main__':
    sys.exit(main())
