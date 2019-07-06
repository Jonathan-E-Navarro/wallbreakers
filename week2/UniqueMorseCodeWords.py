class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:        
        morse_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        
        transformations = set()
        
        for word in words:
            translation = ""
            for char in word:
                translation+=morse_alphabet[(ord(char.upper())-ord('A'))]
            transformations.add(translation)
        
        return(len(transformations))

