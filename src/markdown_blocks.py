from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED = 'unordered_list'
    ORDERED = 'ordered_list'

def block_to_block_type(block):
    if not block.strip():
        return BlockType.PARAGRAPH
    
    lines = block.split("\n")
    
    if _is_heading(block):
        return BlockType.HEADING
    if _is_code_block(lines):
        return BlockType.CODE
    if _is_quote(block, lines):
        return BlockType.QUOTE
    if _is_unordered_list(block, lines):
        return BlockType.UNORDERED
    if _is_ordered_list(block, lines):
        return BlockType.ORDERED
    
    return BlockType.PARAGRAPH

def _is_heading(block):
    return block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### "))

def _is_code_block(lines):
    return (len(lines) > 1 and 
            lines[0].startswith("```") and 
            lines[-1].startswith("```"))

def _is_quote(block, lines):
    if not block.startswith(">"):
        return False
    return all(line.startswith(">") for line in lines)

def _is_unordered_list(block, lines):
    if not block.startswith("- "):
        return False
    return all(line.startswith("- ") for line in lines)

def _is_ordered_list(block, lines):
    if not block.startswith("1. "):
        return False
    for i, line in enumerate(lines, 1):
        if not line.startswith(f"{i}. "):
            return False
    return True

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(str.strip, blocks))
    blocks = list(filter(None, blocks))
    return blocks