class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }
        
        
        d = date.split(' ')
        yyyy = (d[-1])
        mm = months[d[1]]
        
        day = "0" + d[0][:1] if len(d[0])==3 else d[0][:2]
        
        ans = yyyy + "-" + mm + "-"+day
        return ans
        