Types
=====

.. _template:

**template** ``$tType``
-----------------------

Describes the features that a single `modelet <modelet.rst>`__ should
have for an `engine <engine.rst>`__ to accept it as input.

-  a semantic function signature
-  `properties <property.rst>`__ and `requirements <requirement.rst>`__ of
   `modelets <modelet.rst>`__ ###### Source: ``engines-and-modelets.tff``

.. _template_set:

**template_set** ``$tType``
---------------------------

Some particular set of `templates <#template>`__ which describe the
inputs to an `engine <engine.rst>`__. !!! example - {t1, t2, t3} - {t2} -
{} ###### Source: ``engines-and-modelets.tff``

Relations
=========

.. _template_has_concept_requirement:

**template_has_concept_requirement** ``(``\ ```template`` <#template>`__\ ``>``\ ```concept`` <concept.rst>`__\ ``)``
--------------------------------------------------------------------------------------------------------------------

The `concept <concept.rst>`__ symbolizing the *phenomenon class* of a
`template <template.rst>`__. ###### Source: ``engines-and-modelets.tff``

.. _template_formalism_requirement:

**template_formalism_requirement** ``(``\ ```template`` <#template>`__\ ``>``\ ```formalism`` <formalism.rst>`__\ ``)``
----------------------------------------------------------------------------------------------------------------------

The `formalism <formalism.rst>`__ this `template <#template>`__ expects
the *phenomenon* to be described by. ###### Source:
``engines-and-templates.tff``

.. _template_has_location_requirement:

**template_has_location_requirement** ``(``\ ```template`` <#template>`__\ ``>``\ ```spacetime_point`` <spacetime_point.rst>`__\ ``)``
-------------------------------------------------------------------------------------------------------------------------------------

The time and spatial location a `template <#template>`__ refers to. A
`template <template.rst>`__ may have a specific temporal scope or expect
an observation at a specific
```spacetime_point`` <spacetime_point.rst>`__. ###### Source:
``engines-and-modelets.tff``

.. _template_has_extent_requirement:

**template_has_extent_requirement** ``(``\ ```template`` <#template>`__\ ``>``\ ```extent`` <extent.rst>`__\ ``)``
-----------------------------------------------------------------------------------------------------------------

The time and spatial `extent <extent.rst>`__ a `template <#template>`__
covers. A `template <#template>`__ may expect an area/volume/duration of
reference. ###### Source: ``engines-and-modelets.tff``

.. _template_has_creator_requirement:

**template_has_creator_requirement** ``(``\ ```template`` <#template>`__\ ``>``\ ```engine`` <engine.rst>`__\ ``)``
------------------------------------------------------------------------------------------------------------------

The `engine <engine.rst>`__ a `template <#template>`__ requires a
`modelet <modelet.rst>`__ to have been created by. ###### Source:
``engines-and-modelets.tff``

.. _is_in_template_set:

**is_in_template_set** ``((``\ ```template`` <#template>`__\ ``*``\ ```template_set`` <#template_set>`__\ ``) >``\ **``$o``**\ ``)``
------------------------------------------------------------------------------------------------------------------------------------

Check if a `template <#template>`__ is a member of a
`template_set <#template_set>`__. ###### Source:
``engines-and-modelets.tff``
