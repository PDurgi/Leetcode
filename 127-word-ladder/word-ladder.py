class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words=set()
        for word in wordList:
            words.add(word)
        queue=collections.deque([(beginWord,1)])
        chars=[0]*26
        while queue:
            new_word,distance=queue.popleft()
            if new_word==endWord:
                return distance
            for i in range(len(new_word)):
                for char in range(len(chars)):
                    replacement_char=chr(char+ord('a'))
                    new_string = new_word[:i] + replacement_char +new_word[i+1:] 
                    if new_string in words:
                        queue.append((new_string,distance+1))
                        words.remove(new_string)
        return 0