
from bakingstep import BakingStep
#     def __intit__(title, duration, waitDuration)

def main():
    step1 = BakingStep("Mix ingredients",10,40)
    step2 = BakingStep("Add salt & water",10,30)
    #step3 should be repeated 4 times
    step3 = BakingStep("Fold",5,30)
    #Not quite sure how many times I want to repeat this yet.
    step4 = BakingStep("Shape",5,20)
    step5 = BakingStep("Prep proofing baskets",5,0)
    step6 = BakingStep("Final shape and prepp for proof",15,0)
    # Not yet sure if it is best to have proofing as an event or waiting time.
    step7a = BakingStep("Warm Proofing",240,0)
    step7b = BakingStep("Cold Proofing",720,0)
    step8 = BakingStep("Room temp",2,30)
    step9 = BakingStep("Bake", 10, 40)




main()
