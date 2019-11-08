#!/usr/bin/env python3
import random


def meets_provided_requirements(event, context):
    """Randomly return Yes or No to drive state machine."""
    return random.choice([{"result": "Yes",
                           "requirements": ["Islay Single Malt", "California Zinfandel", "Texas BBQ"]},
                          {"result": "No",
                           "requirements": ["Budmilobe Ultra Lite", "McFood"]}])



if __name__ == "__main__":
    print(meets_provided_requirements(None, None))
