import re
import os

def restyle():
    # Load current script ergo current style
    with open("tree.py", "r") as tree_file:
        tree = tree_file.read()
        # new_text = re.sub(r'.*def __init__\(self\) -> None:', 'Start:', text, flags=re.DOTALL)
        # new_text = re.sub(r'def learning_vpython\(self\):.*', 'The End.', new_text, flags=re.DOTALL)
        tree_file.close()
    
    # Load new style
    with open("style.css", "r") as style_file:
        style_lines = style_file.readlines()
        style = ""
        for line in style_lines: style+= "\t\t\t" + line
        style = style.replace("{","{{")
        style = style.replace("}","}}")
        style = style.replace("->","{")
        style = style.replace("<-","}")
        style = style.replace("'","")
        style_file.close()
    
    # Replace old style with new one
    style = re.sub(r'<style>.*</style>', f'<style>\n{style}\n\t\t</style>', tree, flags=re.DOTALL)

    print("Fixed style, writting to tree file...")
    with open("tree.py", "w") as tree_file:
        tree_file.write(style)
        tree_file.close()

def run(new_style : bool):
    if __name__ == "__main__":
        if new_style:
            restyle()
        
        os.system("py tree.py")

run(True)