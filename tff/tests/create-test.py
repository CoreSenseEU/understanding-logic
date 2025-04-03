#!/usr/bin/env python3

import sys
import argparse
import random



NUM_PHENOMENA=250
NUM_FORMALISMS=50
NUM_DATATYPES=30
NUM_TEMPLATES=50 # has to be smaller than real of modelets
NUM_MODELETS=200 # has to be bigger than real of templates
NUM_PROPERTIES=80 # equals the number of requirements
NUM_ENGINES=50
NUM_ROLES=300
NUM_TEMPLATE_SETS=50

MAX_PROPERTIES = 20 # cannot be greater than NUM_PROPERTIES
MAX_TEMPLATES = 5 # cannot be greater than NUM_TEMPLATES
MAX_REALS = 10
MAX_UINTS = 10

REALS = ["0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"]


USE_ROS_DATATYPES = True
UINTS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


def create_phenomena(n):
    output = "%%%  phenomena  %%%\n"
    for index in range(1, n+1):
        output += f"tff(phenomenon_{index}_decl, type, phenomenon_{index} : phenomenon_class).\n"
    output += f"\ntff(distinct_phenomena, axiom,\n  $distinct({",".join([f"phenomenon_{index}" for index in range(1, n+1)])})\n).\n\n"
    return output

def create_roles(n):
    output = "%%%  roles  %%%\n"
    for index in range(1, n+1):
        output += f"tff(role_{index}_decl, type, role_{index} : role).\n"
    output += f"\ntff(distinct_roles, axiom,\n  $distinct({",".join([f"role_{index}" for index in range(1, n+1)])})\n).\n\n"
    return output


def create_datatypes(n):
    output = "%%%  datatypes  %%%\n"
    for index in range(1, n+1):
        output += f"tff(datatype_{index}_decl, type, datatype_{index} : datatype).\n"
    output += f"\ntff(distinct_datatypes, axiom,\n  $distinct({",".join([f"datatype_{index}" for index in range(1, n+1)])})\n).\n\n"
    return output



def create_formalisms(n):
    output = "%%%  formalisms  %%%\n"
    for index in range(1, n+1):
        output += f"tff(formalism_{index}_decl, type, formalism_{index} : formalism).\n"
    output += f"\ntff(distinct_formalisms, axiom,\n  $distinct({",".join([f"formalism_{index}" for index in range(1, n+1)])})\n).\n\n"
    return output



def create_reals():
    output = "%%%  reals  %%%\n"
    for n in range(MAX_REALS):
        real = REALS[n]
        output += f"tff({real}_decl, type, {real} : $real).\n"
    return output + "\n"



def create_uints():
    output = "%%%  uints  %%%\n"
    for n in range(MAX_UINTS):
        size = UINTS[n]
        output += f"tff({size}_decl, type, {size} : $int).\n"
    return output + "\n"



def create_properties_and_requirements(n):
    output = "%%%  properties and requirements  %%%\n"
    for index in range(1, n+1):
        datatype = _get_random_datatype()
        v = random.randint(0, MAX_REALS-1)
        output += f"tff(property_{index}_decl, type, prop_{index} : property).\n"
        output += f"tff(property_{index}_has_datatype_decl, axiom,\n  datatype_of_property(prop_{index}) = {datatype}\n).\n"
        output += f"tff(property_{index}_has_value_{v}, axiom,\n  has_value(prop_{index}) = {REALS[v]}\n).\n\n"

        output += f"tff(requirement_{index}_decl, type, req_{index} : requirement).\n"
        output += f"tff(requirement_{index}_has_datatype_decl, axiom,\n  datatype_of_requirement(req_{index}) = {datatype}\n).\n"
        output += f"tff(requirement_{index}_has_permissible_value_{v}, axiom,\n  is_permissible(req_{index}, {REALS[v]})\n).\n\n"
    output += f"tff(distinct_props, axiom,\n  $distinct({",".join([f"prop_{index}" for index in range(1, n+1)])})\n).\n"
    output += f"tff(distinct_reqs, axiom,\n  $distinct({",".join([f"req_{index}" for index in range(1, n+1)])})\n).\n\n"
    return output


def _get_random_datatype():
    if not USE_ROS_DATATYPES:
        return f"datatype_{random.randint(1, NUM_DATATYPES)}"

    assert(MAX_UINTS > 0)

    builtins = [
                'Bool',
                'Byte',
                'Char',
                'Float32',
                'Float64',
                'Int8',
                'Uint8',
                'Int16',
                'Uint16',
                'Int32',
                'Uint32',
                'Int64',
                'Uint64',
                'String',
                'Wstring']
    arrays = [
              'BoundedString',
              'UnboundedDynamicArray',
              'BoundedDynamicArray',
              'StaticArray']
    namespace = 'ROS2.msg.'

    i = random.randint(0, len(builtins) + len(arrays) - 1)
    # i = random.randint(0, len(builtins) - 1) # only include the builtins
    if i >= len(builtins): # arrays
        a = i - len(builtins)
        b = random.randint(0, len(builtins) - 1)

        if a == 1: # UnboundedDynamicArray
            return f"'{namespace}{arrays[a]}'('{namespace}{builtins[b]}')"

        s = random.randint(0, MAX_UINTS - 1)
        if a == 0: # BoundedString
            return f"'{namespace}{arrays[a]}'({UINTS[s]})"

        return f"'{namespace}{arrays[a]}'('{namespace}{builtins[b]}', {UINTS[s]})"

    return f"'{namespace}{builtins[i]}'"



def create_templates_and_modelets(num_templates, num_modelets, max_properties, property_count):
    output = "%%%  templates and modelets  %%%\n"

    for index in range(1, num_templates+1):
        template = ""
        modelet = ""
        phenomenon = random.randint(1, NUM_PHENOMENA)
        formalism = random.randint(1, NUM_FORMALISMS)
        role = random.randint(1, NUM_ROLES)
        modelet += f"tff(modelet_{index}_decl, type, modelet_{index} : modelet).\n"
        template += f"tff(template_{index}_decl, type, template_{index} : template).\n"
        properties = random.sample(range(1, property_count+1), random.randint(1, max_properties))
        for m in properties:
            modelet += f"tff(modelet_{index}_has_property_{m}, axiom,\n  is_property_of_modelet(prop_{m}, modelet_{index})\n).\n"
            template += f"tff(template_{index}_has_requirement_{m}, axiom,\n  is_part_of(req_{m}, template_{index})\n).\n"
        modelet += f"tff(modelet_{index}_of_phenomenon_{phenomenon}, axiom,\n  topic_of_modelet(modelet_{index}) = phenomenon_{phenomenon}\n).\n"
        modelet += f"tff(formalism_of_modelet_{index}, axiom,\n  formalism_of_modelet(modelet_{index}) = formalism_{formalism}\n).\n\n"
        modelet += f"tff(role_of_modelet_{index}, axiom,\n  role_of_modelet(modelet_{index}) = role_{role}\n).\n\n"
        #for m in random.sample(range(1, property_count+1), random.randint(1, max_requirements)):
        template += f"tff(template_{index}_of_phenomenon_{phenomenon}, axiom,\n  topic_of_template(template_{index}) = phenomenon_{phenomenon}\n).\n"
        template += f"tff(role_of_template_{index}, axiom,\n  role_of_template(template_{index}) = role_{role}\n).\n"
        template += f"tff(formalism_of_template_{index}, axiom,\n  formalism_of_template(template_{index}) = formalism_{formalism}\n).\n"
        template += f"tff(template_{index}_requirements, axiom,\n  ![R : requirement]:\n  (\n"
        template += f"    is_part_of(R, template_{index})\n    =>\n    (\n      "
        template += "\n      |\n      ".join([f"R = req_{m}" for m in properties])
        template += "\n    )\n  )\n).\n\n"
        output += modelet
        output += template
    for index in range(num_templates+1, num_modelets+1):
        phenomenon = random.randint(1, NUM_PHENOMENA)
        formalism = random.randint(1, NUM_FORMALISMS)
        output += f"tff(modelet_{index}_decl, type, modelet_{index} : modelet).\n"
        for m in random.sample(range(1, property_count+1), random.randint(1, max_properties)):
            output += f"tff(modelet_{index}_has_property_{m}, axiom,\n  is_property_of_modelet(prop_{m}, modelet_{index})\n).\n"
        output += f"tff(modelet_{index}_has_phenomenon_{phenomenon}, axiom,\n  topic_of_modelet(modelet_{index}) = phenomenon_{phenomenon}\n).\n"
        output += f"tff(formalism_of_modelet_{index}, axiom,\n  formalism_of_modelet(modelet_{index}) = formalism_{formalism}\n).\n\n"
    output += f"tff(distinct_modelets, axiom,\n  $distinct({",".join([f" modelet_{index}" for index in range(1, num_modelets+1)])})\n).\n"
    output += f"tff(distinct_templates, axiom,\n  $distinct({",".join([f"template_{index}" for index in range(1, num_templates+1)])})\n).\n\n"
    return output


    
def create_template_sets(n, max_templates, template_count):
    output = "%%%  template sets  %%%\n"
    for index in range(1, n+1):
        output += f"tff(template_set_{index}_decl, type, template_set_{index} : template_set).\n"
        
        templates = random.sample(range(1, template_count+1), random.randint(1, max_templates))
        for m in templates:
            output += f"tff(template_{m}_in_template_set_{index}, axiom,\n  is_in_template_set(template_{m}, template_set_{index})\n).\n\n"
        output += f"tff(template_set_{index}_templates, axiom,\n  ![T : template]:\n  (\n"
        output += f"    is_in_template_set(T, template_set_{index})\n    =>\n    (\n      "
        output += "\n      |\n      ".join([f"T = template_{t}" for t in templates])
        output += "\n    )\n  )\n).\n\n"
    output += f"tff(distinct_template_sets, axiom,\n  $distinct({",".join([f"template_set_{index}" for index in range(1, n+1)])})\n).\n\n"
    return output



def create_engines(n, template_set_count, max_properties, property_count):
    output = "%%%  engines  %%%\n"
    for index in range(1, n+1):
        output += f"tff(engine_{index}_decl, type, engine_{index} : engine).\n"

        for m in random.sample(range(1, property_count+1), random.randint(1, max_properties)):
            output += f"tff(engine_{index}_has_property_{m}_decl, axiom,\n  is_property_of_engine(prop_{m}, engine_{index})\n).\n"

        m = random.randint(1,template_set_count)
        output += f"tff(engine_{index}_uses_template_set_{m}_decl, axiom,\n  interface_of(engine_{index}) = template_set_{m}\n).\n\n"
    output += f"tff(distinct_engines, axiom,\n  $distinct({",".join([f"engine_{index}" for index in range(1, n+1)])})\n)\n\n."
    return output



def create_modelet_sets(n):
    output = "%%%  modelet sets  %%%\n"
    for index in range(1, n+1):
        modelets = []
        for index2 in range(1, index+1):
            modelets.append(f"M{index2}")
        output += f"tff(modelet_sets_of_size_{index}_exist, axiom,\n  !["
        output += ", ".join([f"{modelet}: modelet" for modelet in modelets])
        output += "]:\n    ?[MS: modelet_set]:\n    (\n      "
        output += "\n      &\n      ".join([f"is_in_modelet_set({modelet}, MS)" for modelet in modelets])
        output += "\n    )  \n).\n\n"
    output += "\n%%%  conjectures   %%%"
    return output



def main() -> int:
    output = "include('understanding-logic/tff/model/properties.tff').\n\n"
    if USE_ROS_DATATYPES:
        output += "include('understanding-logic/tff/model/datatypes.tff').\n\n"
        #output += create_uints()
    #output += create_reals()
    output += create_phenomena(NUM_PHENOMENA)
    output += create_roles(NUM_ROLES)
    if not USE_ROS_DATATYPES:
        output += create_datatypes(NUM_DATATYPES)
    output += create_formalisms(NUM_FORMALISMS)
    output += create_properties_and_requirements(NUM_PROPERTIES)
    output += create_templates_and_modelets(NUM_TEMPLATES, NUM_MODELETS, MAX_PROPERTIES, NUM_PROPERTIES)
    output += create_template_sets(NUM_TEMPLATE_SETS, MAX_TEMPLATES, NUM_TEMPLATES)
    #output += create_modelets(NUM_MODELETS, MAX_PROPERTIES, NUM_PROPERTIES)
    output += create_engines(NUM_ENGINES, NUM_TEMPLATE_SETS, MAX_PROPERTIES, NUM_PROPERTIES)
    output += create_modelet_sets(MAX_TEMPLATES)

    print(output)
    return 0


if  __name__ == "__main__":
    sys.exit(main())
