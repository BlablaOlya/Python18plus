def apply_discount(product, discount):
    price = int(product['цена']) * (1.0 - discount)
    try:
        assert 0 <= price <= product['цена']
    except AssertionError:
        return "Произошла ошибка расчетов"
    else:
        return product['имя'], price


name_of_product = "data.txt"
name_of_discount = "discount.txt"

with open(name_of_product, 'r', encoding='utf-8') as product:
    content_p = product.readlines()

with open(name_of_discount, 'r', encoding='utf-8') as discount:
    content_d = discount.readlines()

data = []
for i in content_p:
    p = {}
    x = i.rstrip().split(',')
    p['имя'] = x[0]
    p['цена'] = int(x[1])
    data.append(p)

disc = []
for i in content_d:
    disc.append(float(i.rstrip()))

result = []
y = 0
for i in data:
    q = apply_discount(i, disc[y])
    y += 1
    result.append(q)

print(result)



