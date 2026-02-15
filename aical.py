import random

responses = ["Let me cook...", "Easy peasy!", "Calculating at light speed...", "Beep boop, got it:"]

print("------- AI CALCULATOR IN TERMINAL -------")
print("""Tips:

1.Make Sure To use Proper Detail for Example- Typeing 2(2*2)+4 will give you error instead Try 2*(2*2)+4

2.When Doing Sq-root put '**' for ex- 2**2

3.When Doing Mod use % for ex-2%6

""") 

while True:
    expression = input("\nEnter Expression: ").strip()
    
    if expression.lower() == "exit":
        print("AI: Goodbye! Thanks for using me.")
        break
    
    try:
        
        result = eval(expression)
        
        pun= random.choice(responses)
        print(f"AI: {pun} The result is: {result}")
        
    except Exception as e:
        print(f"AI: OOPS! That doesn't look like a valid expression. (The Error was: {e})")