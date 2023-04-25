import os
from gpt_index.storage.index_store.keyval_index_store import KeyValIndexStore
from gpt_index.storage.keyval_store.simple import SimpleKeyValStore


DEFAULT_PERSIST_DIR = "./storage"
DEFAULT_PERSIST_FNAME = "index_store.json"


class SimpleIndexStore(KeyValIndexStore):
    def __init__(self, simple_keyval_store: SimpleKeyValStore):
        super().__init__(simple_keyval_store)

    @classmethod
    def from_persist_dir(cls, persist_dir: str = DEFAULT_PERSIST_DIR):
        persist_path = os.path.join(persist_dir, DEFAULT_PERSIST_FNAME)
        simple_keyval_store = SimpleKeyValStore(persist_path)
        return cls(simple_keyval_store)
