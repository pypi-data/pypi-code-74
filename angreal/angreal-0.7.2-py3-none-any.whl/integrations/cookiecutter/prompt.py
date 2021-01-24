# -*- coding: utf-8 -*-

"""
    angreal.integrations.cookiecutter.prompt
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Functions for prompting the user for project info.

    Over rides cookiecutter.prompt to ensure some cookie cutter specific syntaxes aren't enforced
"""

from collections import OrderedDict
import json

import click
from past.builtins import basestring

from future.utils import iteritems

from jinja2.exceptions import UndefinedError

from cookiecutter.exceptions import UndefinedVariableInTemplate
from cookiecutter.environment import StrictEnvironment


def read_user_variable(var_name, default_value):# pragma: no cover
    """Prompt the user for the given variable and return the entered value
    or the given default.

    :param str var_name: Variable of the context to query the user
    :param default_value: Value that will be returned if no input happens
    """
    # Please see http://click.pocoo.org/4/api/#click.prompt
    return click.prompt(var_name, default=default_value)


def read_user_yes_no(question, default_value):# pragma: no cover
    """Prompt the user to reply with 'yes' or 'no' (or equivalent values).

    Note:
      Possible choices are 'true', '1', 'yes', 'y' or 'false', '0', 'no', 'n'

    :param str question: Question to the user
    :param default_value: Value that will be returned if no input happens
    """
    # Please see http://click.pocoo.org/4/api/#click.prompt
    return click.prompt(
        question,
        default=default_value,
        type=click.BOOL
    )


def read_repo_password(question):# pragma: no cover
    """Prompt the user to enter a password

    :param str question: Question to the user
    """
    # Please see http://click.pocoo.org/4/api/#click.prompt
    return click.prompt(question, hide_input=True)


def read_user_choice(var_name, options):# pragma: no cover
    """Prompt the user to choose from several options for the given variable.

    The first item will be returned if no input happens.

    :param str var_name: Variable as specified in the context
    :param list options: Sequence of options that are available to select from
    :return: Exactly one item of ``options`` that has been chosen by the user
    """
    # Please see http://click.pocoo.org/4/api/#click.prompt
    if not isinstance(options, list):
        raise TypeError

    if not options:
        raise ValueError

    choice_map = OrderedDict(
        (u'{}'.format(i), value) for i, value in enumerate(options, 1)
    )
    choices = choice_map.keys()
    default = u'1'

    choice_lines = [u'{} - {}'.format(*c) for c in choice_map.items()]
    prompt = u'\n'.join((
        u'Select {}:'.format(var_name),
        u'\n'.join(choice_lines),
        u'Choose from {}'.format(u', '.join(choices))
    ))

    user_choice = click.prompt(
        prompt, type=click.Choice(choices), default=default
    )
    return choice_map[user_choice]


def process_json(user_value):# pragma: no cover
    try:
        user_dict = json.loads(
            user_value,
            object_pairs_hook=OrderedDict,
        )
    except Exception:
        # Leave it up to click to ask the user again
        raise click.UsageError('Unable to decode to JSON.')

    if not isinstance(user_dict, dict):
        # Leave it up to click to ask the user again
        raise click.UsageError('Requires JSON dict.')

    return user_dict


def read_user_dict(var_name, default_value):# pragma: no cover
    """Prompt the user to provide a dictionary of data.

    :param str var_name: Variable as specified in the context
    :param default_value: Value that will be returned if no input is provided
    :return: A Python dictionary to use in the context.
    """
    # Please see http://click.pocoo.org/4/api/#click.prompt
    if not isinstance(default_value, dict):
        raise TypeError

    default_display = 'default'

    user_value = click.prompt(
        var_name,
        default=default_display,
        type=click.STRING,
        value_proc=process_json,
    )

    if user_value == default_display:
        # Return the given default w/o any processing
        return default_value
    return user_value


def render_variable(env, raw, cookiecutter_dict):# pragma: no cover
    """Inside the prompting taken from the cookiecutter.json file, this renders
    the next variable. For example, if a project_name is "Peanut Butter
    Cookie", the repo_name could be be rendered with:

        `{{ cookiecutter.project_name.replace(" ", "_") }}`.

    This is then presented to the user as the default.

    :param Environment env: A Jinja2 Environment object.
    :param str raw: The next value to be prompted for by the user.
    :param dict cookiecutter_dict: The current context as it's gradually
        being populated with variables.
    :return: The rendered value for the default variable.
    """
    if raw is None:
        return None
    elif isinstance(raw, dict):
        return {
            render_variable(env, k, cookiecutter_dict):
                render_variable(env, v, cookiecutter_dict)
            for k, v in raw.items()
        }
    elif isinstance(raw, list):
        return [
            render_variable(env, v, cookiecutter_dict)
            for v in raw
        ]
    elif not isinstance(raw, basestring):
        raw = str(raw)

    template = env.from_string(raw)

    rendered_template = template.render(angreal=cookiecutter_dict)
    return rendered_template


def prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input):# pragma: no cover
    """Prompt the user which option to choose from the given. Each of the
    possible choices is rendered beforehand.
    """
    rendered_options = [
        render_variable(env, raw, cookiecutter_dict) for raw in options
    ]

    if no_input:
        return rendered_options[0]
    return read_user_choice(key, rendered_options)


def prompt_for_config(context, no_input=False):# pragma: no cover
    """
    Prompts the user to enter new config, using context as a source for the
    field names and sample values.

    :param no_input: Prompt the user at command line for manual configuration?
    """
    cookiecutter_dict = OrderedDict([])
    env = StrictEnvironment(context=context)

    # First pass: Handle simple and raw variables, plus choices.
    # These must be done first because the dictionaries keys and
    # values might refer to them.
    for key, raw in iteritems(context[u'angreal']):
        if key.startswith(u'_'):
            # If a variable starts with an underscore , it is simply rendered without requesting input
            val = render_variable(env, raw, cookiecutter_dict)
            cookiecutter_dict[key] = val

            continue

        try:
            if isinstance(raw, list):
                # We are dealing with a choice variable
                val = prompt_choice_for_config(
                    cookiecutter_dict, env, key, raw, no_input
                )
                cookiecutter_dict[key] = val
            elif not isinstance(raw, dict):
                # We are dealing with a regular variable
                val = render_variable(env, raw, cookiecutter_dict)

                if not no_input:
                    val = read_user_variable(key, val)

                cookiecutter_dict[key] = val
        except UndefinedError as err:
            msg = "Unable to render variable '{}'".format(key)
            raise UndefinedVariableInTemplate(msg, err, context)

    # Second pass; handle the dictionaries.
    for key, raw in iteritems(context[u'angreal']):

        try:
            if isinstance(raw, dict):
                # We are dealing with a dict variable
                val = render_variable(env, raw, cookiecutter_dict)

                if not no_input:
                    val = read_user_dict(key, val)

                cookiecutter_dict[key] = val
        except UndefinedError as err:
            msg = "Unable to render variable '{}'".format(key)
            raise UndefinedVariableInTemplate(msg, err, context)

    return cookiecutter_dict