import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("invalid markdown")
        for i, part in enumerate(parts):
            if part == "":
                continue
            elif i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
        
    return new_nodes


def split_nodes_image(old_nodes):
    return split_nodes_markdown(
        old_nodes,
        extract_markdown_images,
        TextType.IMAGE,
        "![{alt}]({url})"
    )

def split_nodes_link(old_nodes):
    return split_nodes_markdown(
        old_nodes,
        extract_markdown_links,
        TextType.LINK,
        "[{text}]({url})"
    )


def split_nodes_markdown(old_nodes, extract_func, text_type, md_format):
    new_nodes = []
    for node in old_nodes:
        matches = extract_func(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        text = node.text
        for match in matches:
            main_text, url = match
            markdown = md_format.format(text=main_text, alt=main_text, url=url)
            parts = text.split(markdown, 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(main_text, text_type, url))
            text = parts[1] if len(parts) > 1 else ""
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    regex_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern, text)
    return matches

def extract_markdown_links(text):
    regex_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern, text)
    return matches

