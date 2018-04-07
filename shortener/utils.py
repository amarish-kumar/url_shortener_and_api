import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    code = ""
    for _ in range(size):
        code += random.choice(chars)
    return code


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    qs = Klass.objects.filter(shortcode__iexact=new_code)
    if qs.exists():
        return create_shortcode(size=size)
    return new_code
