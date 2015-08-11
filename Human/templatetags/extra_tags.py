from django import template
import datetime, re


register = template.Library()


@register.filter(name="replace_word")
def my_replace_word(value, arg):
    return value.replace(arg, '~')


@register.tag(name="current_time")
def get_current_time(parse, token):
    try:
        tag_name, format_string = token.split_contents()
    except:
        raise template.TemplateSyntaxError("syntax")

    return CurrentNode(format_string[1:-1])


class CurrentNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)


# method 2
class CurrentTimeNode2(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        context['current_time_sec'] = now.strftime(self.format_string)
        return ''


@register.tag
def fetch_current_time(parse, token):
    try:
        tag_name, format_string = token.split_contents()
    except:
        raise template.TemplateSyntaxError("syntax")

    return CurrentTimeNode2(format_string[1:-1])


# method 3
class CurrentTimeNode3(template.Node):
    def __init__(self, format_string, var_name):
        self.format_string = str(format_string)
        self.var_name = var_name

    def render(self, context):
        now = datetime.datetime.now()
        context[self.var_name] = now.strftime(self.format_string)
        return ''


@register.tag
def do_current_time(parser, token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        msg = '%r tag requires arguments' % token.contents[0]
        raise template.TemplateSyntaxError(msg)

    m = re.search(r'(.*?) as (\w+)', arg)
    if m:
        fmt, var_name = m.groups()
    else:
        msg = '%r tag had invalid arguments' % tag_name
        raise template.TemplateSyntaxError(msg)

    if not (fmt[0] == fmt[-1] and fmt[0] in ('"', "'")):
        msg = "%r tag's argument should be in quotes" % tag_name
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode3(fmt[1:-1], var_name)

