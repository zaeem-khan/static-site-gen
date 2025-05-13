import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        html_node = HTMLNode('p', 'hello', props=props)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(html_node.props_to_html(), expected)

    def test_no_props_to_html(self):
        html_node = HTMLNode('p', 'hello')
        expected = ""
        self.assertEqual(html_node.props_to_html(), expected)
    
    def test_empty_dict_props_to_html(self):
        html_node = HTMLNode('p', 'hello', props={})
        expected = ""
        self.assertEqual(html_node.props_to_html(), expected)


if __name__ == "__main__":
    unittest.main()