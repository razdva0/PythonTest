from icecream import ic  # pip install icecream


def human_years_cat_years_dog_years(human_years):
    cat = [15, 9, 4]
    dog = [15, 9, 5]
    return [human_years,
            sum(cat[x] if x < 3 else cat[-1] for x in range(human_years)),
            sum(dog[x] if x < 3 else dog[-1] for x in range(human_years))]


if human_years_cat_years_dog_years(1) == [1, 15, 15]:
    print('OK')
else:
    ic(human_years_cat_years_dog_years(1))
if human_years_cat_years_dog_years(2) == [2, 24, 24]:
    print('OK')
else:
    ic(human_years_cat_years_dog_years(2))
if human_years_cat_years_dog_years(10) == [10, 56, 64]:
    print('OK')
else:
    ic(human_years_cat_years_dog_years(10))
