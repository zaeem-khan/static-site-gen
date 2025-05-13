class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props:
            props_dict = self.props
            formatted_dict = ' '.join(f'{key}="{value}"' for key, value in props_dict.items())
            return ' ' + formatted_dict
        
        return ""
            