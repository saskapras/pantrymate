# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: PantryMate
import ast
import textwrap

def merge_imports(source, new_imports):
    """Append new_imports to source, merging any that are already present (exact
    and from-style) to keep the file compact."""
    tree = ast.parse(source)
    imports = [(n, a) for n, a in ast.iter_child_nodes(tree) if isinstance(n, ast.Import)]
    existing = {
        (node.lineno, node.col_offset) for node in imports
    }
    for node in new_imports:
        if isinstance(node, ast.Import):
            if (node.lineno, node.col_offset) in existing:
                continue
            imports.append(node)
        elif isinstance(node, ast.ImportFrom):
            if any(
                isinstance(n, ast.ImportFrom)
                and (n.module, n.names) == (node.module, node.names)
                for n in imports
            ):
                continue
            imports.append(node)
    source = ast.unparse(tree)
    if imports:
        source += "\n" + "\n".join(textwrap.dedent(ast.unparse(node) for node in imports))
    return source
