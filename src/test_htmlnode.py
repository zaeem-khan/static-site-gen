import unittest

from htmlnode import HTMLNode, LeafNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)
    
    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")



if __name__ == "__main__":
    unittest.main()