# Status and "alive": a few histories

> Rule: [FORMAT.md](../../FORMAT.en.md) §6 "Who writes the status".

## `失据` was added after actually running it

The rule originally only said "the alive set is empty → `待审`". Running it once revealed: that would crush "new entry" and "argument just knocked down"
into the same status — **the consequence of an attack was completely invisible in `status`**, and the attack is the repo's core mechanism.

A reader who sees a `失据` entry knows **it was once argued, and that argument no longer stands**.

## A mis-dispatched adversarial review (evidence truth vs logic)

The adversarial task was dispatched with:

> "You don't need to verify whether the quotation is true (that needs the network); **you may assume the quotation is true**;
> what you attack is 'even so, does the conclusion hold'."

**Result**: one adversarial review accurately pointed out that a piece of evidence had **insufficient resolution**, but **did not discover it was not a measurement at all** —
because **the task excluded truth verification**. (See the `ev-002` section in [`evidence/README.md`](../../evidence/README.en.md).)

**A logic attack and truth verification are not the same thing.** The former is cheap, but that is no reason to skip the latter.
So the dispatch template must now contain "**before attacking the logic, first question the evidence itself**".

## "Alive" spins on zero attacks

**"Alive" is defined as "all attackers knocked down". Marking "alive" when there are no attackers is a vacuous truth over an empty set.**

The repo measured this once: **76 arguments were marked "(alive)" with zero `攻击` edges.**
A reader seeing "alive" assumes it **survived something** — **nothing happened.**

## A deleted check

The "alive" check once had a third: **"`攻击` edge points to an argument already knocked down" — deleted.**
That check **gave wrong advice**: an attack edge pointing to the argument it knocked down **is exactly what an attack is supposed to do**.

It was **deleted** rather than lowered to a "hint", because **a check that gives wrong advice is worse than no check** — it trains people to ignore hints.

## The same class of problem, second time

This is the **second** time the repo has hit the same class of problem: the first was the proposition "the choice of analogy is stage-related", attacked
(n=2 cannot separate the variable that changes with the same). **Both times the lesson is the same: multiple observations from the same source are not multiple pieces of evidence.**
