# Django application

---
![Main workflow](https://github.com/hillel-i-python-pro-i-2022-05-19/shared__django_example/actions/workflows/main-workflow.yml/badge.svg)

## ð  Homework

Homework related actions.

### â¶ï¸ Run

Make all actions needed for run homework from zero.

```shell
make d-homework-i-run
```

### ð® Purge

Make all actions needed for run homework from zero.

```shell
make d-homework-i-purge
```

---

## ð ï¸ Dev

### Initialize dev

Install dependencies and register pre-commit.

```shell
make init-dev
```

---

## ðï¸ Preparation

Make some initialization steps. For example, copy configs. For full-docker and for local dev.

```shell
make init-configs-i-dev
```

---

## ð³ Docker

Use services in dockers.

### â¶ï¸ Run

Just run

```shell
make d-run
```

### â¯ï¸ Run extended

Shutdown previous, run in detached mode, follow logs

```shell
make d-run-i-extended
```

### â¹ï¸Stop

Stop services

```shell
make d-stop
```

### ð® Purge

Purge all data related with services

```shell
make d-purge
```

---

### Add 2 humans via docker

```shell
make d-i-django-i-create-humans-i-2
```