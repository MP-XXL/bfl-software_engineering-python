"""
TEST SCORER SOURCE CODE - KEEP PRIVATE
Compile this to .pyc before distributing to students
"""

import sys
import os

class MCQScorer:
    def __init__(self):
        self.score = 0
        self.total_questions = 15
        self.student_answers = {}
        self.correct_answers = {
            'Q1_ANSWER': 'D',
            'Q2_ANSWER': 'B', 
            'Q3_ANSWER': 'C',
            'Q4_ANSWER': 'D',
            'Q5_ANSWER': 'B',
            'Q6_ANSWER': 'C',
            'Q7_ANSWER': 'A',
            'Q8_ANSWER': 'B',
            'Q9_ANSWER': 'B',
            'Q10_ANSWER': 'B',
            'Q11_ANSWER': 'B',
            'Q12_ANSWER': 'B',
            'Q13_ANSWER': 'B',
            'Q14_ANSWER': 'A',
            'Q15_ANSWER': 'A'
        }
        
    def load_student_answers(self):
        """Load student answers from their test file"""
        try:
            # Import the student's test file
            import mcq as st
            
            # Collect all answers
            for q_num in range(1, 16):
                var_name = f'Q{q_num}_ANSWER'
                if hasattr(st, var_name):
                    self.student_answers[var_name] = getattr(st, var_name)
                else:
                    self.student_answers[var_name] = None
                    
            return True
            
        except ImportError:
            print("❌ ERROR: Could not find 'mcq.py'")
            print("Make sure it's in the same directory as this scorer.")
            return False
        except Exception as e:
            print(f"❌ ERROR loading test: {e}")
            return False
    
    def score_questions(self):
        """Score each question and provide feedback"""
        print("🔍 Scoring your MCQ test...")
        print("=" * 50)
        
        for q_num in range(1, 16):
            var_name = f'Q{q_num}_ANSWER'
            student_answer = self.student_answers.get(var_name)
            correct_answer = self.correct_answers[var_name]
            
            if student_answer is None:
                print(f"❌ Q{q_num}: Not answered (0 points)")
            elif student_answer.upper() == correct_answer.upper():
                self.score += 1
                print(f"✅ Q{q_num}: Correct (+1 point)")
            else:
                print(f"❌ Q{q_num}: Incorrect. Your answer: {student_answer}, Correct: {correct_answer}")
    
    def calculate_results(self):
        """Calculate and display final results"""
        percentage = (self.score / self.total_questions) * 100
        
        print("\n" + "=" * 50)
        print("📊 FINAL RESULTS")
        print("=" * 50)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage >= 70:
            print("🎉 STATUS: PASS - Congratulations! You may proceed.")
        else:
            print("💡 STATUS: FAIL - Review Python fundamentals and try again.")
        
        print("=" * 50)
        
        return percentage >= 70
    
    def show_answer_key(self):
        """Show correct answers for learning purposes"""
        print("\n" + "=" * 50)
        print("📚 ANSWER KEY (For Learning)")
        print("=" * 50)
        
        explanations = {
            'Q1': "D - NameError: name 'greetings' is not defined, greetings was commented out",
            'Q2': "B - Default mutable argument retains state between calls",
            'Q3': "C - *args collects positional args, **kwargs collects keyword args",
            'Q4': "D - Lists are mutable and cannot be dictionary keys",
            'Q5': "B - nums[1:4] is [20,30,40], [::-1] reverses it",
            'Q6': "C - Tuples are immutable, lists are mutable",
            'Q7': "A - text[:4]='Prog', text[-4:]='ming' → 'Progming'",
            'Q8': "B - 17 & 1 checks if number is odd (1 means odd)",
            'Q9': "B - Division with float operand returns float",
            'Q10': "B - global x modifies the global variable",
            'Q11': "B - Duplicate keys overwrite previous values",
            'Q12': "B - 3! = 3 × 2 × 1 = 6",
            'Q13': "D - ZeroDivisionError is caught first, prints Zero",
            'Q14': "A - finally always executes, crucial for resource cleanup",
            'Q15': "A - Missing base case causes infinite recursion"
        }
        
        for q_num in range(1, 16):
            var_name = f'Q{q_num}_ANSWER'
            print(f"Q{q_num}: {self.correct_answers[var_name]} - {explanations[f'Q{q_num}']}")

def main():
    """Main scoring function"""
    print("FOUNDATIONS - MCQ TEST SCORER")
    print("Loading your answers...")
    
    scorer = MCQScorer()
    
    if not scorer.load_student_answers():
        sys.exit(1)
    
    scorer.score_questions()
    passed = scorer.calculate_results()
    
    if not passed:
        scorer.show_answer_key()
    
    print("\n💡 Tip: Master these fundamentals before moving to FastAPI!")

if __name__ == "__main__":
    main()