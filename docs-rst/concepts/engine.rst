Types
=====

.. _engine:

**engine** ``$tType``
---------------------

Does work within a **CoreSense** `agent <agent.rst>`__ to produce
`modelets <modelet.rst>`__.

-  Takes multiple `modelets <modelet.rst>`__ as an input
   `modelet_set <modelet.rst#modelet_set>`__
-  Uses semantic information to identify valid input modelet
   `formalisms <formalism.rst>`__

   -  semantics could be external (part of the type definition) or
      internal (modeled within the `modelet <modelet.rst>`__ itself)

-  Produces one output `modelet <modelet.rst>`__

   -  May or may not impart semantic meaning to the output
      `modelet <modelet.rst>`__
   -  May (re)define the output modelet `origin <origin.rst>`__,
      `concept <concept.rst>`__, or characteristics

-  Has `exertion <exertion.rst>`__ characteristics

   -  e.g. time delay, resource usage, power consumption

!!! example - DroneStateEngine (see tff/tests/test-wind-estimation.tff)
- Input Model: - Modelet - formalism: IMU.msg - modelled concept:
inertia - Modelet - formalism: NavSatFix.msg - modelled concept:
geolocation - Output Modelet: - modelet - formalism: DroneState.msg -
modelled concept: drone_state ###### Source:
``engines-and-modelets.tff``

Relations
=========

.. _interface_of:

**interface_of** ``(``\ ```engine`` <#engine>`__\ ``>``\ ```template_set`` <template.rst#template_set>`__\ ``)``
---------------------------------------------------------------------------------------------------------------

An `engine <#engine>`__ requires a set of input
`modelets <modelet.rst>`__ which matches the
`template_set <template.rst#template_set>`__. ###### Source:
``engines-and-modelets.tff``

.. _output_modelet_formalism:

**output_modelet_formalism** ``(``\ ```engine`` <#engine>`__\ ``>``\ ```formalism`` <formalism.rst>`__\ ``)``
------------------------------------------------------------------------------------------------------------

The `formalism <formalism.rst>`__ of an `engine <#engine>`__ output
`modelet <modelet.rst>`__. ###### Source: ``engines-and-modelets.tff``

.. _is_output_modelet_concept:

**is_output_modelet_concept** ``(``\ ```engine`` <#engine>`__\ ``>``\ ```phenomenon`` <phenomenon.rst>`__\ ``)``
---------------------------------------------------------------------------------------------------------------

The `concept <concept.rst>`__ of an `engine <#engine>`__ output
`modelet <modelet.rst>`__. ###### Source: ``engines-and-modelets.tff``

.. _output_property_of_e:

**output_property_of_engine** ``(``\ ```engine`` <#engine>`__\ ``>``\ ```property`` <property.rst>`__\ ``)``
-----------------------------------------------------------------------------------------------------------

The `property <property.rst>`__ an `engine <#engine>`__ imparts on its
output `modelet <modelet.rst>`__. ###### Source: ``properties.tff``

.. _engine_imparts_representation_class:

**engine_imparts_representation_class** ``(``\ ```engine`` <#engine>`__\ ``>``\ ```representation_class`` <representation_class.rst>`__\ ``)``
---------------------------------------------------------------------------------------------------------------------------------------------

The `representation_class <representation_class.rst>`__ an
`engine <#engine>`__ imparts on its output `modelet <modelet.rst>`__.
###### Source: ``engines-and-modelets.tff``
