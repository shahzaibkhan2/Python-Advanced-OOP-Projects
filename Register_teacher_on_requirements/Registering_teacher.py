# INSTRUCTOR 

class Instructor:
    def __init__(self, name, techno, exp, fedbck):
        self.name = name
        self.techno = techno
        self.exp = exp
        self.fedbck = fedbck
        
        
    def check_eligible(self):
        if self.exp > 3 and self.fedbck > 4.5:
            return True
        elif self.exp >= 3 and self.fedbck >= 4:
            return True
        else:
            return False
        
    def allocate_course(self, tech):
        is_elig = self.check_eligible()
        
        if is_elig:
            if tech in self.techno:
                return "Technology matched"
            else:
                return "Sorry ! technology did not match"
            
        else:
            return "Sorry ! not eligible for teaching"
        
obj = Instructor("Shahzaib", ["Data Science", "Python Development"], 5,4.5)
obj.allocate_course("Python Development")