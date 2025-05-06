## Types
### **template** `$tType` { #template data-toc-label='template' }
Describes the features that a single [modelet](modelet.md) should have for an
[engine](engine.md) to accept it as input.

- a semantic function signature
- [properties](property.md) and [requirements](requirement.md) of [modelets](modelet.md)
###### Source: `engines-and-modelets.tff`

### **template_set** `$tType` { #template_set data-toc-label='template_set' }
Some particular set of [templates](#template) which describe the inputs to an [engine](engine.md).
!!! example
    - {t1, t2, t3}
    - {t2}
    - {}
###### Source: `engines-and-modelets.tff`


## Relations
### **template_has_concept_requirement** `(`[**`template`**](#template)` > `[**`concept`**](concept.md)`)` { #template_has_concept_requirement data-toc-label='template_has_concept_requirement' }
The [concept](concept.md) symbolizing the *phenomenon class* of a [template](template.md).
###### Source: `engines-and-modelets.tff`

### **template_formalism_requirement** `(`[**`template`**](#template)` > `[**`formalism`**](formalism.md)`)` { #template_formalism_requirement data-toc-label='template_formalism_requirement' }
The [formalism](formalism.md) this [template](#template) expects the *phenomenon*
to be described by.
###### Source: `engines-and-templates.tff`

### **template_has_location_requirement** `(`[**`template`**](#template)` > `[**`spacetime_point`**](spacetime_point.md)`)` { #template_has_location_requirement data-toc-label='template_has_location_requirement' }
The time and spatial location a [template](#template) refers to.
A [template](template.md) may have a specific temporal scope or expect an observation
at a specific [`spacetime_point`](spacetime_point.md).
###### Source: `engines-and-modelets.tff`

### **template_has_extent_requirement** `(`[**`template`**](#template)` > `[**`extent`**](extent.md)`)` { #template_has_extent_requirement data-toc-label='template_has_extent_requirement' }
The time and spatial [extent](extent.md) a [template](#template) covers.
A [template](#template) may expect an area/volume/duration of reference.
###### Source: `engines-and-modelets.tff`

### **template_has_creator_requirement** `(`[**`template`**](#template)` > `[**`engine`**](engine.md)`)` { #template_has_creator_requirement data-toc-label='template_has_creator_requirement' }
The [engine](engine.md) a [template](#template) requires a [modelet](modelet.md) to have been created by.
###### Source: `engines-and-modelets.tff`

### **is_in_template_set** `((`[**`template`**](#template)` * `[**`template_set`**](#template_set)`) > `**`$o`**`)` { #is_in_template_set data-toc-label='is_in_template_set' }
Check if a [template](#template) is a member of a [template_set](#template_set).
###### Source: `engines-and-modelets.tff`
