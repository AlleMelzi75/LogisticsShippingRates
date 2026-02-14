Contribution guidelines
Welcome Contributors!
Thank you for considering contributing to the centralized repository. This document outlines the guidelines for contributing to the development of Shipping Rates and Calculations.
Code style
Please follow the coding style and conventions used in the existing codebase. This helps maintain consistency across the project.
Documentation
Ensure that your contributions are well-documented. Include comments in your code where necessary and provide a clear and concise description of your changes in the pull request.
Testing
Before submitting a pull request, make sure your changes have been tested thoroughly. Include relevant test cases and ensure that existing tests pass.
Issue tracker
Check the issue tracker for any open issues or feature requests. If you're working on something, please comment on the issue to let others know.
Code review
All contributions will go through a code review process. Be open to feedback and be willing to make changes if necessary. Code reviews help maintain code quality and consistency.
Thank you for your contribution!

Copied!

Wrap Toggled!
Commit this file to your repository.
PP7.png

Click on Code to go to the repository home page.

Your project now contains Contribution Guidelines as well.

Task 5: Create a new branch.
Click on branch in your repository.
PP8.png

Now, click on New Branch and enter the branch name as Shipping_Calculation, then click Create New Branch

This will be used for adding your Shipping Calculation code.

Task 6: Add the Shipping Calculation code in this branch.
Change to the Shipping_Calculation branch by selecting it from the dropdown.

Create a new file named Shipping_Cost_Calculator.py.

Add the following code in the new file:

1
2
3
4
5
6
7
8
9
10
11
# Shipping Cost Calculator
## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
## Calculate shipping cost
shipping_cost = weight * rate
## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
