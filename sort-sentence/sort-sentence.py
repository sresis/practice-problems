class Solution:
    def sortSentence(self, s: str) -> str:
        # last char is the number
        sent = s.split(' ')
        new_sentence = ['']*len(sent)
        for i in range(len(sent)):
            val = int(sent[i][-1])-1
            new_sentence[val] = sent[i][:-1]
            i += 1
        return (' ').join(new_sentence)

