"""
This question is asked by Amazon. Given two strings representing sentences,
return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). 
You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]

"""
import unittest

class Solution:
    def getUncommonWords(self, sentence1, sentence2):
        if len(sentence1) == 0: return list(set(sentence2.split(" ")))
        if len(sentence2) == 0: return list(set(sentence1.split(" ")))

        words1, words2 = sentence1.split(" "), sentence2.split(" ")
        words1, words2 = set(words1), set(words2)

        for word in words1:
          if word in words2:
            words2.remove(word)
          else:
            words2.add(word)
        
        return sorted(list(words2))

class Tests(unittest.TestCase):
    def test_sentences_have_not_intersection(self):
        self.assertEqual(Solution().getUncommonWords("the quick", "brown fox"), ["brown","fox","quick","the"])
    
    def test_sentences_have_some_intersection(self):
        self.assertEqual(Solution().getUncommonWords("the tortoise beat the haire", "the tortoise lost to the haire"), ["beat", "lost", "to", ])
    
    def test_equal_sentences(self):
        self.assertEqual(Solution().getUncommonWords("the tortoise beat the haire", "the tortoise beat the haire"), [])

    def test_one_sentence_is_empty(self):
        self.assertEqual(sorted(Solution().getUncommonWords("", "beat the haire")), ["beat","haire","the"])

if __name__ == '__main__':
    unittest.main()


