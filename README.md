# failing-tests

## Zweck
Testfall für Pipeline Doctor: **Build schlägt in der Test-Stage fehl.**

## Erwarteter Fehler
```
FAILED test_main.py::test_add_intentionally_wrong - AssertionError: assert 2 == 3
FAILED test_main.py::test_multiply_intentionally_wrong - AssertionError: assert 10 == 99
2 failed, 2 passed in ...
```

## Fehler-Typ
`pytest` — absichtlich falsche Assertions in `test_main.py`

## Stage die fehlschlägt
`Test` — Install läuft erfolgreich durch, Test schlägt fehl.
