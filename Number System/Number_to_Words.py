class Solution:
    def number_to_words(self, n):
        if n == 0:
            return "Zero"
        
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]
        
        result = ""
        
        # Thousands
        if n >= 1000:
            result += ones[n // 1000] + " Thousand "
            n %= 1000
        
        # Hundreds
        if n >= 100:
            result += ones[n // 100] + " Hundred "
            n %= 100
        
        # Tens & Ones
        if n >= 20:
            result += tens[n // 10] + " "
            n %= 10
        
        if 10 <= n < 20:
            result += teens[n - 10] + " "
        elif n > 0:
            result += ones[n] + " "
        
        return result.strip()

n = 1234
obj = Solution()
print(obj.number_to_words(n))