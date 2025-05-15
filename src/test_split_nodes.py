import unittest
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_two_word_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(result, expected_result)

    def test_two_word_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(result, expected_result)

    def test_two_word_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        result = split_nodes_delimiter(
            [node], "_", TextType.ITALIC
        )

        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(result, expected_result)

    def test_bold_italic_mix_error(self):
        node = TextNode("This is text with a **italic error block_ word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.ITALIC)

    def test_italic_bold_mix_no_error(self):
        node = TextNode("This is text with a **italic error block_ word", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_single_word(self):
        node = TextNode("**bold**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_result = [
            TextNode("bold", TextType.BOLD),
        ]

        self.assertListEqual(result, expected_result)

    def test_double_delims(self):
        node = TextNode(
            "This is text with one **bold word** and another **bold word**.",
            TextType.TEXT,
        )
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_result = [
            TextNode("This is text with one ", TextType.TEXT),
            TextNode("bold word", TextType.BOLD),
            TextNode(" and another ", TextType.TEXT),
            TextNode("bold word", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]

        self.assertListEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()