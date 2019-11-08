from .base import  example, Note, NoteDetailView, AuthorView, TagView, Index
from .part1 import get_json, bootstrap, bootstrap_table

__all__ = (
    'bootstrap', 'bootstrap_table', 'get_json', 'Note', 'Index', 'AuthorView',
    'TagView', 'NoteDetailView',
)