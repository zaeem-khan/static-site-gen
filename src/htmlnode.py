from textnode import TextType

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT.value:
            return LeafNode(None, text_node.text)
        case TextType.BOLD.value:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC.value:
            return LeafNode("i", text_node.text)
        case TextType.CODE.value:
            return LeafNode("code", text_node.text)
        case TextType.LINK.value:
            props = {"href": text_node.url}
            return LeafNode("a", text_node.text, props)
        case TextType.IMAGE.value:
            props = {"src": text_node.url, "alt": text_node.text}
            return LeafNode("img", "", props)
        case _:
            raise Exception("Invalid Text type")

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props:
            props_dict = self.props
            formatted_dict = ' '.join(f'{key}="{value}"' for key, value in props_dict.items())
            return ' ' + formatted_dict
        
        return ""

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is missing")
        if self.children is None:
            raise ValueError("Children values are missing")
        
        return f"<{self.tag}{self.props_to_html()}>{"".join(map(lambda child: child.to_html(), self.children))}</{self.tag}>"