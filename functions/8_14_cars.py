def make_car(manufacturer, model, **other_info):
    """Store information about a car."""

    other_info['manufacturer_name'] = manufacturer
    other_info['model_name'] = model
    return other_info

    print("\nInformation about your new car:")
    for value in make_car:
        print(f"- {value}")

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)