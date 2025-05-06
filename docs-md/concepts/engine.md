## Types
### **engine** `$tType` { #engine data-toc-label='engine' }
Does work within a **CoreSense** [agent](agent.md) to produce [modelets](modelet.md).

- Takes multiple [modelets](modelet.md) as an input [modelet_set](modelet.md#modelet_set)
- Uses semantic information to identify valid input modelet [formalisms](formalism.md)
    - semantics could be external (part of the type definition) or internal
      (modeled within the [modelet](modelet.md) itself)
- Produces one output [modelet](modelet.md)
	- May or may not impart semantic meaning to the output [modelet](modelet.md)
    - May (re)define the output modelet [origin](origin.md), [concept](concept.md),
      or characteristics
- Has [exertion](exertion.md) characteristics
	- e.g. time delay, resource usage, power consumption

!!! example
    - DroneStateEngine (see tff/tests/test-wind-estimation.tff)
        - Input Model:
            - Modelet
                - formalism: IMU.msg
                - modelled concept: inertia
            - Modelet
                - formalism: NavSatFix.msg
                - modelled concept: geolocation
        - Output Modelet:
            - modelet
                - formalism: DroneState.msg
                - modelled concept: drone\_state
###### Source: `engines-and-modelets.tff`

## Relations
### **interface_of** `(`[**`engine`**](#engine)` > `[**`template_set`**](template.md#template_set)`)` { #interface_of data-toc-label='interface_of' }
An [engine](#engine) requires a set of input [modelets](modelet.md) which
matches the [template_set](template.md#template_set).
###### Source: `engines-and-modelets.tff`

### **output_modelet_formalism** `(`[**`engine`**](#engine)` > `[**`formalism`**](formalism.md)`)` { #output_modelet_formalism data-toc-label='output_modelet_formalism' }
The [formalism](formalism.md) of an [engine](#engine) output [modelet](modelet.md).
###### Source: `engines-and-modelets.tff`

### **is_output_modelet_concept** `(`[**`engine`**](#engine)` > `[**`phenomenon`**](phenomenon.md)`)` { #is_output_modelet_concept data-toc-label='is_output_modelet_concept' }
The [concept](concept.md) of an [engine](#engine) output [modelet](modelet.md).
###### Source: `engines-and-modelets.tff`

### **output_property_of_engine** `(`[**`engine`**](#engine)` > `[**`property`**](property.md)`)` { #output_property_of_e data-toc-label='output_property_of_e' }
The [property](property.md) an [engine](#engine) imparts on its output [modelet](modelet.md).
###### Source: `properties.tff`


### **engine_imparts_representation_class** `(`[**`engine`**](#engine)` > `[**`representation_class`**](representation_class.md)`)` { #engine_imparts_representation_class data-toc-label='engine_imparts_representation_class' }
The [representation_class](representation_class.md) an [engine](#engine) imparts on its output [modelet](modelet.md).
###### Source: `engines-and-modelets.tff`
