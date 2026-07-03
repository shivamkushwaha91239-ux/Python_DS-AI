class DietPlan:

    def get_breakfast(self):
        pass

    #child class 1
class KetoDiet(DietPlan):

    def get_breakfast(self):
        return "Keto breakfast: Eggs ,with avocado and bacon"

    #child class 2
class VeganDiet(DietPlan):

    def get_breakfast(self):
        return "Vegan breakfast: Oatmeal with fruits and nuts"
#child class 3
class HighProteinDiet(DietPlan):

    def get_breakfast(self):
        return "High Protein breakfast: Greek yogurt with berries and almonds"

    #polymorphic function that takes a DietPlan object as an argument and calls the get_breakfast() method
    # this method can accept any object of the DietPlan class or its subclasses, demonstrating polymorphism
def print_morning_routine(diet_plan):
    print(f"Today's breakfast: {diet_plan.get_breakfast()}")

#create instances of the child classes
keto_diet = KetoDiet()
vegan_diet = VeganDiet()
high_protein_diet = HighProteinDiet()

#pass the different diet plan objects to the print_morning_routine() function
print_morning_routine(keto_diet) # prints the breakfast for the keto diet
print_morning_routine(vegan_diet) # prints the breakfast for the vegan diet
print_morning_routine(high_protein_diet) # prints the breakfast for the high-protein diet