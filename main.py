from echange import echange


def main():

    values = [
        (123, "RUB", "CZK"),
        (123, "CAD", "EUR"),
        (123, "GBP", "HUF"),
        (123, "ISK", "INR")
    ]

    for (amount, source, target) in values:
        print(80*"-")
        print("Convert {} {} to {}".format(amount, source, target))
        x = echange(amount, source, target)

        print("Result: {}".format(x))
        print(80*"-")


if __name__ == "__main__":
    main()
