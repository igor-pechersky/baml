# Impl: {{name}}
# Client: {{client}}
# An implementation of {{function_name}}.


__prompt_template = """\
{{{prompt}}}\
"""

__input_replacers = {
    {{#each inputs}}
    "{{BLOCK_OPEN}}{{{this}}}{{BLOCK_CLOSE}}"{{#unless @last}},{{/unless}}
    {{/each}}
}


# We ignore the type here because baml does some type magic to make this work
# for inline SpecialForms like Optional, Union, List.
__deserializer = Deserializer[{{function.return.0.type}}]({{function.return.0.type}})  # type: ignore
{{#each overrides}}
__deserializer.overload("{{{name}}}", {{BLOCK_OPEN}}{{#each aliases}}"{{{alias}}}": "{{value}}"{{#unless @last}}, {{/unless}}{{/each}}{{BLOCK_CLOSE}})
{{/each}}

@BAML{{function.name}}.register_impl("{{name}}")
{{> func_def func_name=name unnamed_args=function.unnamed_args args=function.args return=function.return}}
    updates = {k: k.format({{> arg_values unnamed_args=function.unnamed_args args=function.args}}) for k in __input_replacers}

    prompt = str(__prompt_template)
    for k, v in updates.items():
        prompt = prompt.replace(k, v)

    response = await {{client}}.run_prompt(prompt)
    return __deserializer.from_string(response.generated)
