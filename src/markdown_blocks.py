def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(str.strip, blocks))
    blocks = list(filter(None, blocks))
    return blocks