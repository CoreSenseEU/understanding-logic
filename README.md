# Understanding Logic WiP coded in TPTP THF and TFF

## Setup
To run the tests, you need to set your TPTP HOME to the path of this directory like so (i.e. without trailing slash):
```
export TPTP=/path/to/repo
```
This results in `include()` paths being read relative to this directory.

## Development Notes
Because Higher Order Logic (HOL) is not currently well supported in Vampire,
any `.thf` files need to obey a few rules to avoid problems with their `TPTP`
parser.
- Do not use builtin predicates or functiors (`$distinct`, `$let`, `$ite`).
- Do not use builtin theory axioms (`$less`, `$greatereq`, `$floor`, etc.).
- Do not use cannonical `tff` or `fol` formulas. You can convert them all to
  `thf` by rewriting functions and predicates with the `@` operator between
  arguments.
  For example:
  ```prolog
  tff(my_formula, axiom, my_function(v1, v2, v3) = v4).

  % -->
  thf(my_formula, axiom, ((my_function @ v1 @ v2 @ v3) = v4)).
  ```
