# Integration tests

This project includes a set of fast integration tests (marked `integration`) and
some heavy tests (marked `slow`). The heavy tests are intended to run less
frequently (nightly or on-demand) since they generate full projects and may
exercise DB setup.

## Run tests locally

- Fast integration tests (integration but not slow):

```bash
pytest -q -m "integration and not slow"
```

- All integration tests (including slow):

```bash
pytest -q -m integration
```

- Only slow tests:

```bash
pytest -q -m slow
```

## Why slow tests are separate

Some tests generate complete projects and simulate DB backends. They are
valuable but may be slower and sometimes rely on filesystem timing. We run
them nightly or on-demand in CI to keep PR feedback fast while still catching
regressions.

## CI

We added a workflow `Integration Tests (nightly)` that runs all integration
tests on a schedule and can be triggered manually. There's also a separate
workflow that runs `slow` tests only.
