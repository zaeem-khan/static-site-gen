from textnode import TextNode, TextType

text_node = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')

print(text_node)