from flask import Flask


def print_routes(app: Flask):
    print('{:-^40}{:-^30}{:-^30}'.format('URL', 'METHODS', 'NAME'))
    for rule in app.url_map.iter_rules():
        methods = tuple(filter(lambda m: m != 'HEAD' and m != 'OPTIONS', rule.methods))
        print("| {:<40}{:<30}{:>26} |".format(str(rule), str(methods), str(rule.endpoint)))
    print('-' * 100)
