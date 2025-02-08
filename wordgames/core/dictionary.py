# wordgames/core/dictionary.py
class Dictionary:
    def __init__(self, file_path='data/dictionary.txt'):
        self.words = self._load_dictionary(file_path)
    
    def _load_dictionary(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return {word.strip().lower() for word in file}
        except FileNotFoundError:
            raise FileNotFoundError(f"Dictionary file not found: {file_path}")
