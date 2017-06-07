"""Tests for our main byof CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from byof import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['byof', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['byof', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['byof', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
