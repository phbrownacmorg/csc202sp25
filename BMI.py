# Average American woman age >= 20: 63.5", 170.8 lbs.
# https://www.healthline.com/health/womens-health/average-weight-for-women

# Average American man age >= 20: 69.1", 197.9 lbs.
# https://www.healthline.com/health/mens-health/average-weight-for-men

# Shaq: 7'1" = 85", 325 lbs. (https://en.wikipedia.org/wiki/Shaquille_O%27Neal)
# Kevin Hart: 5'2" = 62", 140 lbs. (https://www.sociosite.net/age-height-weight-of-celebrities/kevin-hart)
# Big Show: 7' = 84", 383 lbs. (https://en.wikipedia.org/wiki/Big_Show)
# Kate Moss: 5'7" = 67", 121 lbs.(https://www.sociosite.net/age-height-weight-of-celebrities/kate-moss)

def calc_bmi(height: float, weight: float) -> float:
    return 703 * weight / height**2

def classify_bmi(bmi: float) -> str:
    result = 'normal'
    if bmi < 18.5:
        result = 'underweight'
    elif bmi >= 30:
        result = 'obese'
    elif bmi >= 25: # If we're here, we already know BMI < 30
        result = 'overweight'
    return result

def main(args: list[str]) -> int:
    height: float = float(input("Please enter a person's height in inches: "))
    weight: float = float(input("Please enter the person's weight in pounds: "))
    bmi: float = calc_bmi(height, weight)
    print('A person {0:.1f}" tall, weighing {1:.1f} lbs., '.format(height, weight),
          end='')
    print('has a BMI of {:.1f}.'.format(bmi))
    print('This person is classed as {}.'.format(classify_bmi(bmi)))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))