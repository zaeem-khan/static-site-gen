from textnode import TextNode, TextType
from htmlnode import HTMLNode

text_node = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')

props = {
    "href": "https://www.google.com",
    "target": "_blank",
}

html_node = HTMLNode('p', 'hello', props=props)
# print(text_node)
print(html_node)
print(html_node.props_to_html())