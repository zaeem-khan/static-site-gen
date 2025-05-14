import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_multiple_leaf_children(self):
        child1 = LeafNode("span", "A")
        child2 = LeafNode("b", "B")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>A</span><b>B</b></div>"
        )

    def test_empty_children_list(self):
        parent_node = ParentNode("p", [])
        self.assertEqual(
            parent_node.to_html(),
            "<p></p>"
        )

    def test_leaf_and_parent_mixed_children(self):
        child = LeafNode("em", "emphasized")
        sub_parent = ParentNode("span", [child])
        parent_node = ParentNode("div", [sub_parent, LeafNode(None, "plain")])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><em>emphasized</em></span>plain</div>"
        )

    def test_missing_tag_raises_value_error(self):
        parent_node = ParentNode(None, [LeafNode("b", "bold")])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_missing_children_raises_value_error(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_props_rendering(self):
        child = LeafNode("span", "with class")
        parent_node = ParentNode("div", [child], props={"class": "styled"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="styled"><span>with class</span></div>'
        )
    




if __name__ == "__main__":
    unittest.main()