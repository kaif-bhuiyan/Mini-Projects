import random
import re
responses = ["Let me cook...", "Easy peasy!", "Calculating at light speed...", "Cooking, Got it:"]

print("------- AI CALCULATOR IN TERMINAL -------")
print("""Tips:

1.Make Sure To use Proper Detail
2.When Doing Sq-root put '**' for ex- 2**2
3.When Doing Mod use % for ex-2%6

""") 

while True:
    expression = input("\nEnter Expression: ").strip()
    expression=re.sub(r"(\d)\(", r"\1*(", expression)
    
    if expression.lower() == "exit":
        print("AI: Goodbye! Thanks for using me.")
        break
    
    try:
        
        result = eval(expression)
        
        pun= random.choice(responses)
        print(f"AI: {pun} The result is: {result}")
        
    except Exception as e:
        print(f"AI: OOPS! That doesn't look like a valid expression. (The Error was: {e})")
