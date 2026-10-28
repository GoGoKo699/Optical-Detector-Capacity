#!/usr/bin/env python3
"""Check the shared learning route and its local navigation, not hosted rendering."""
from __future__ import annotations

import json
import posixpath
import re
from pathlib import Path
from typing import Mapping
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = (
    'README.md', 'llms.txt', 'learning/README.md',
    'learning/MILESTONES.md', 'learning/PRESKILL_BRIDGE.md',
)
ANCHOR = 'https://arxiv.org/abs/1604.07450v5'
FIELDS = ('Phase', 'Central question', 'Understanding target', 'Dependencies',
          'Story role', 'Conceptual connection', 'Sources')


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def explicit_anchors(text: str) -> set[str]:
    values = re.findall(r'<a id="([^"]+)"></a>', text)
    require(len(values) == len(set(values)), 'Duplicate explicit anchor')
    return set(values)


def validate_documents(texts: Mapping[str, str], available_paths: set[str]) -> dict:
    """Validate supplied text and a file inventory of the same source tree.

    Separating the inventory from text makes link checks and failure tests explicit.
    The CLI obtains both from its actual checkout; it has no network dependency.
    """
    require(set(DOCUMENTS).issubset(texts), 'Missing learning or entrance document')
    require(set(DOCUMENTS).issubset(available_paths), 'Missing entrance path')
    for path in ('learning/README.md', 'learning/PRESKILL_BRIDGE.md'):
        require(ANCHOR in texts[path], f'Unpinned educational anchor: {path}')
    for path in DOCUMENTS:
        require('1604.07450v5' in texts[path], f'Missing selected source version: {path}')
    for path in ('README.md', 'llms.txt', 'learning/README.md'):
        require('MILESTONES.md' in texts[path] and 'PRESKILL_BRIDGE.md' in texts[path],
                f'Missing learning navigation: {path}')

    milestone_text = texts['learning/MILESTONES.md']
    heads = list(re.finditer(r'^### M(\d{2}) — (.+)$', milestone_text, re.M))
    require([int(h[1]) for h in heads] == list(range(1, 31)),
            'Expected exactly M01 through M30 in order')
    phases = {'Background/preliminaries': 0, 'Narrative/innovation': 0}
    dependency_edges = 0
    for i, head in enumerate(heads, 1):
        end = heads[i].start() if i < len(heads) else len(milestone_text)
        block = milestone_text[head.end():end]
        fields = {}
        for field in FIELDS:
            matches = re.findall(r'^\*\*' + re.escape(field) + r':\*\* (.+)$', block, re.M)
            require(len(matches) == 1 and len(matches[0].strip()) > 0,
                    f'M{i:02d}: missing, empty, or repeated {field}')
            fields[field] = matches[0]
        phase = 'Background/preliminaries' if i <= 14 else 'Narrative/innovation'
        require(fields['Phase'] == phase + '.', f'M{i:02d}: incorrect phase')
        phases[phase] += 1
        dependencies = [int(x) for x in re.findall(r'\[M(\d{2})\]', fields['Dependencies'])]
        require(len(dependencies) == len(set(dependencies)), f'M{i:02d}: repeated dependency')
        require(all(1 <= j < i for j in dependencies), f'M{i:02d}: non-earlier dependency')
        require(bool(dependencies) or fields['Dependencies'] == 'None.',
                f'M{i:02d}: malformed dependencies')
        require('Preskill' in fields['Sources'] and '../science/' in fields['Sources'],
                f'M{i:02d}: incomplete source pointers')
        dependency_edges += len(dependencies)
    anchors = {path: explicit_anchors(text) for path, text in texts.items() if path.endswith('.md')}
    require({f'm{i:02d}' for i in range(1, 31)}.issubset(anchors['learning/MILESTONES.md']),
            'Missing milestone anchor')

    local_links = 0
    math_blocks = 0
    for path in DOCUMENTS:
        text = texts[path]
        require(text.count('$`') == text.count('`$'), f'Unpaired inline math: {path}')
        if not path.endswith('.md'):
            continue
        # This route deliberately uses explicit IDs for its cross-file fragments.
        for link in re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)', text):
            split = urlsplit(link)
            if split.scheme or split.netloc:
                require(split.scheme in {'https', 'http', 'mailto'}, f'Unexpected URL: {link}')
                continue
            require(not split.path.startswith('/'), f'Absolute local link: {link}')
            target = path if not split.path else posixpath.normpath(
                posixpath.join(posixpath.dirname(path), unquote(split.path)))
            require(target in available_paths, f'Broken local link in {path}: {link}')
            if split.fragment:
                require(target in texts, f'Cannot check anchor without text: {target}')
                require(unquote(split.fragment) in anchors.get(target, set()),
                        f'Broken anchor in {path}: {link}')
            local_links += 1
        fence = None
        math = []
        for line in text.splitlines():
            if line.startswith('```'):
                if fence is None:
                    fence = line[3:].strip()
                    math = []
                else:
                    require(line == '```', f'Malformed closing fence: {path}')
                    if fence == 'math':
                        equation = '\n'.join(math)
                        require(equation.strip() != '', f'Empty math fence: {path}')
                        starts = re.findall(r'\\begin\{([^}]+)\}', equation)
                        ends = re.findall(r'\\end\{([^}]+)\}', equation)
                        require(sorted(starts) == sorted(ends), f'Unpaired math environment: {path}')
                        math_blocks += 1
                    fence = None
            elif fence == 'math':
                math.append(line)
        require(fence is None, f'Unclosed code/math fence: {path}')
        if path.startswith('learning/'):
            for marker in ('COACHING.md', 'Revise → Learn → Test', 'answer_history', 'challenge_attempt'):
                require(marker not in text, f'Personal coaching marker in shared learning: {path}')

    return {'milestones': 30, 'phases': phases, 'dependency_edges': dependency_edges,
            'local_links': local_links, 'math_blocks': math_blocks,
            'anchor': ANCHOR, 'scope': 'Learning structure and source navigation; not hosted rendering.'}


def main() -> None:
    texts = {path: (ROOT / path).read_text(encoding='utf-8') for path in DOCUMENTS}
    available = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
                 and '.git' not in p.relative_to(ROOT).parts}
    print(json.dumps(validate_documents(texts, available), indent=2))


if __name__ == '__main__':
    main()
