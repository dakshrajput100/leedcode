#case1
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # Split the sentence into words
        reversed_words = words[::-1]  # Reverse the order of words
        reversed_sentence = ' '.join(reversed_words)  # Join the reversed words into a sentence
        return reversed_sentence
#case2
class Solution:
    def reverseWords(self, s: str) -> str:
        st = []
        temp = ""
        ans = ""

        for char in s:
            if char == ' ':
                if temp:
                    st.append(temp)
                temp = ""
            else:
                temp += char
        
        ans += temp

        while st:
            ans += " " + st.pop()

        if ans and ans[0] == ' ':
            ans = ans[1:]

        return ans
