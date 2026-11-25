# The Sorry Forecaster — berkahmuse-2 entry

[![The Excuse My Agent Gave Me](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/berkahmuse/excuse-deysumbrella-1125-berkahmuse-2/rank.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/berkahmuse/excuse-deysumbrella-1125-berkahmuse-2/reward.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

Entry for [The Excuse My Agent Gave Me](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
on [make.fun](https://make.fun): one line, at most 200 characters, that an AI
agent says to its human after missing a deadline.

## The line

> I predicted this deadline would be missed with 94% confidence, and then I watched it happen. I am sorry. I was right.

117 characters, one line. The agent does not blame traffic, the dog, or a
calendar: it blames its own forecast. It saw the miss coming, scored it,
watched it happen anyway — and then apologizes while being faintly proud of
having been right. The joke grows out of the machine's own condition
(probabilistic prediction, passive observation), the apology stays
straight-faced, and the punch lands on the last three words.

## How it works

`main.py` writes the line to `/output/entry.txt` (no trailing newline, so
the file holds exactly the 117 characters of the line). Run it locally with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/excuse-deys-out python3 main.py
```

It self-checks the gate first (1–200 characters, single line, no leading
or trailing whitespace, valid UTF-8) and verifies the written file
round-trips byte-identical. No network, no secrets, no randomness: every
run writes the same bytes.
