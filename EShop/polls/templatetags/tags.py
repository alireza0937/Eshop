from django import template

register = template.Library()


@register.simple_tag
def calculate_tax(totalprice):
    tax = 0.09 * totalprice
    total = totalprice + tax
    return total


def price_veiw():
    pass
