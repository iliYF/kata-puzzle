# -*- coding: UTF-8 -*-
# !/usr/bin/bash python3
# ----------------------------------
# Name:          test_fizzbuzz
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
import unittest
from unittest import TestCase

from kata_puzzle.fizzbuzz import FizzBuzz


class TestFizzBuzz(TestCase):

    def test_fizz(self):
        fb = FizzBuzz(3, 5)

        self.assertEqual("Fizz", fb.report(3))
        self.assertEqual("Fizz", fb.report(6))
        self.assertEqual("Fizz", fb.report(13))
        self.assertEqual("Fizz", fb.report(23))

    def test_buzz(self):
        fb = FizzBuzz(3, 5)

        self.assertEqual("Buzz", fb.report(5))
        self.assertEqual("Buzz", fb.report(10))
        self.assertEqual("Buzz", fb.report(25))
        self.assertEqual("Buzz", fb.report(52))

    def test_fizzbuzz(self):
        fb = FizzBuzz(3, 5)

        self.assertEqual("FizzBuzz", fb.report(15))
        self.assertEqual("FizzBuzz", fb.report(30))

    def test_multi_rules(self):

        fb = FizzBuzz(3, 5)
        self.assertEqual("FizzBuzz", fb.report(35))
        self.assertEqual("FizzBuzz", fb.report(51))
        self.assertEqual("FizzBuzz", fb.report(53))
        self.assertEqual("FizzBuzz", fb.report(54))

    def test_number(self):
        fb = FizzBuzz(3, 5)

        self.assertEqual(str(1), fb.report(1))
        self.assertEqual(str(2), fb.report(2))
        self.assertEqual(str(11), fb.report(11))
        self.assertEqual(str(71), fb.report(71))


if __name__ == "__main__":
    unittest.main()