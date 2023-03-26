import unittest
from piscine import *

class TestReplaceHex(unittest.TestCase):
    def test_is_punctuation(self):
        self.assertTrue(is_punctuation('.'))
        self.assertTrue(is_punctuation('!'))
        self.assertTrue(is_punctuation(','))
        self.assertTrue(is_punctuation('!?'))
        self.assertTrue(is_punctuation(':'))
        self.assertTrue(is_punctuation(';'))
        self.assertFalse(is_punctuation('a'))
        self.assertFalse(is_punctuation('hello'))
        self.assertFalse(is_punctuation('2'))

    def test_should_replace_a_with_an(self):
        self.assertTrue(should_replace_a_with_an('a', 'apple'))
        self.assertTrue(should_replace_a_with_an('a', 'elephant'))
        self.assertTrue(should_replace_a_with_an('a', 'Ice cream'))
        self.assertFalse(should_replace_a_with_an('a', 'house'))
        self.assertFalse(should_replace_a_with_an('a', 'world'))
        self.assertFalse(should_replace_a_with_an('a', '123'))

    def test_match(self):
        self.assertTrue(match('(cap, 2)'))
        self.assertTrue(match('(low, 1)'))
        self.assertFalse(match('(bin, 4)'))
        self.assertTrue(match('(up, 3)'))
        self.assertFalse(match('cap, 2)'))
        self.assertFalse(match('(low, 1'))
        self.assertFalse(match('hello world'))

    def test_split_punctuation_and_word(self):
        self.assertEqual(split_punctuation_and_word('Hello,world!'), 'Hello, world!')
        self.assertEqual(split_punctuation_and_word('Good:morning'), 'Good: morning')

    def test_split_text(self):
        self.assertEqual(split_text('Hello , world !'), ['Hello', ',', 'world', '!'])
        self.assertEqual(split_text('Good : morning'), ['Good', ':', 'morning'])

    def test_replace(self):
        self.assertEqual(edit_text("1E (hex) files were added"), "30 files were added")
        self.assertEqual(edit_text("files were added 1E (hex)"), "files were added 30")
        self.assertEqual(edit_text("There is no greater agony than bearing a untold story inside you."), "There is no greater agony than bearing an untold story inside you.")
        self.assertEqual(edit_text("Punctuation tests are ... kinda boring ,don't you think !?"), "Punctuation tests are... kinda boring, don't you think!?")
        self.assertEqual(edit_text("As Elton John said: ' I am the most well-known homosexual in the world '"), "As Elton John said: 'I am the most well-known homosexual in the world'")
        self.assertEqual(edit_text("I was thinking ... You were right"), "I was thinking... You were right")
        self.assertEqual(edit_text("Simply add 42 (hex) and 10 (bin) and you will see the result is 68."), "Simply add 66 and 2 and you will see the result is 68.")
        self.assertEqual(edit_text("1E (hex) files were added It has been 10 (bin) years Ready, set, go (up) I SHOULD STOP SHOUTING (low, 3) Welcome to the Brooklyn bridge (cap)"), "30 files were added It has been 2 years Ready, set, GO I should stop shouting Welcome to the Brooklyn Bridge")
        self.assertEqual(edit_text("it (cap) was the best of times, it was the worst of times (up) , it was the age of wisdom, it was the age of foolishness (cap, 6) , it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of darkness, it was the spring of hope, IT WAS THE (low,3) winter of despair."), "It was the best of times, it was the worst of TIMES, it was the age of wisdom, It Was The Age Of Foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of darkness, it was the spring of hope, it was the winter of despair.")
        self.assertEqual(edit_text("There it was. A amazing rock!"), "There it was. An amazing rock!")


if __name__ == '__main__':
    unittest.main()