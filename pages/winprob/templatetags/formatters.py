from django import template

register = template.Library()

@register.filter
def format_predictedprob(value):
    if value > 0.5:
        return round(value * 100, 1)
    if value < 0.5:
        return round((1 - value) * 100, 1)
    if value == 0.5:
        return 50.0

@register.filter
def format_chgprob(value):
    if value > 0:
        return round(value * 100, 1)
    if value < 0:
        return round(abs(value) * 100, 1)
    if value == 0.5:
        return 0.0

@register.filter
def format_abschgprob(value):
    return f'+{round(value * 100, 1)}%'

@register.filter
def format_percent_one_decimal(value):
    return round(value * 100, 1)

@register.filter
def format_minutes(value):
    # if '90' in value:
    #     return value.replace('90', "90’")
    return value + "’"
