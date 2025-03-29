# Understanding Logic WiP coded in TPTP THF and TFF

## Setup
Create a `src` directory to use as your TPTP HOME and set the `TPTP` environment
variable with the absolute path:
```
mkdir src && cd src
export TPTP=$(pwd)
git clone git@github.com:alex-quin-gabriel/understanding-logic.git
```
This results in `include()` paths being read relative to the `src` directory.
Other TPTP files can be placed in the same `src` directory matching this tree
structure:
```
src
├── my_package
│   ├── example1.tff
│   ├── example2.thf
│   └── ...
└── understanding-logic
    ├── LICENSE
    ├── README.md
    ├── tff
    │   └── ...
    └── thf
        └── ...
```


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
