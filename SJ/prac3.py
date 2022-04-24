class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 처음엔 letters = logs = list()로 했어서 같은 빈 리스트를 참조해
        # 둘 다 ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']라는 값을 가지게 되는 오류를 범함.
        letters = list()
        digits = list()
        
        for log in logs:
            if log.split()[1].isalpha():
                letters.append(log)
            elif log.split()[1].isdigit():
                digits.append(log)
        
        
        letters.sort(key = lambda x:(x.split()[1:], x.split()[0]))
        
        return letters + digits