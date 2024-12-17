class Calculator: 

    def __init__(self,math_Exercise):
        self.math_Exercise = math_Exercise

    def print_mathExercise(self):
        print(self.math_Exercise)
    
    def checking_results(self):
        error="division by zero"
        try:
            print(eval(self.math_Exercise))
        except Exception as e:
            print("Error ",e)