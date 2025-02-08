
# jinja2.select_autoescape(enabled_extensions=('html', 'htm', 'xml'), disabled_extensions=(), default_for_string=True, default=False)

# enables for all templates created from strings or for all templates with .html and .xml extensions
from jinja2 import Environment, select_autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
))

# exclude templates ending with .txt:
from jinja2 import Environment, select_autoescape
env = Environment(autoescape=select_autoescape(
    disabled_extensions=('txt',),
    default_for_string=True,
    default=True,
))



    The enabled_extensions is an iterable of all the extensions that autoescaping should be enabled for. Likewise disabled_extensions is a list of all templates it should be disabled for. If a template is loaded from a string then the default from default_for_string is used. If nothing matches then the initial value of autoescaping is set to the value of default.

    For security reasons this function operates case insensitive.
    Changelog

    Parameters:

            enabled_extensions (Collection[str])

            disabled_extensions (Collection[str])

            default_for_string (bool)

            default (bool)

    Return type:

        Callable[[str | None], bool]

Here a recommended setup that enables autoescaping for templates ending in '.html', '.htm' and '.xml' and disabling it by default for all other extensions. You can use the select_autoescape() function for this:

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(autoescape=select_autoescape(['html', 'htm', 'xml']),
                  loader=PackageLoader('mypackage'))

The select_autoescape() function returns a function that works roughly like this:

def autoescape(template_name):
    if template_name is None:
        return False
    if template_name.endswith(('.html', '.htm', '.xml'))

