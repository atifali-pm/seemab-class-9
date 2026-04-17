# Deep Explanations — Chemistry Chapter 6: Stoichiometry

**The "why does this work?" companion.** Read this when a concept in [notes.md](notes.md) doesn't quite click. Take your time — these are meant to be read slowly, one topic at a time.

---

## Topic 1 — Empirical vs Molecular Formula: Two Ways to Describe a Compound

Imagine someone asks you: "How many students are in your school?"

You could answer two ways:
1. **"For every 1 teacher, there are about 25 students."** (a ratio)
2. **"We have 800 students."** (the actual number)

Both answers are correct — they just tell you different things. The first is a **ratio** (easy to compare to other schools). The second is the **actual count** (tells you exactly how big your school is).

Chemistry does the same trick with compounds. There are two ways to describe what's inside a molecule:

### The empirical formula — the "ratio answer"

The empirical formula tells you the **simplest whole-number ratio** of atoms in a compound. It's the most "stripped-down" version you can write.

Take glucose, the sugar in your blood. Its molecular formula is C₆H₁₂O₆. That means one molecule of glucose has 6 carbon, 12 hydrogen, and 6 oxygen atoms. But look at the ratio: 6 : 12 : 6. Divide everything by 6, and you get **1 : 2 : 1**. So the empirical formula of glucose is **CH₂O**.

CH₂O is the simplest way to say "for every 1 carbon, there are 2 hydrogens and 1 oxygen." It doesn't say how many total atoms there are — it just gives you the recipe proportions.

### The molecular formula — the "actual count answer"

The molecular formula gives you the **real number** of each type of atom in one molecule. For glucose, that's C₆H₁₂O₆. Not a ratio — the real thing.

### Why have both?

Because they answer different questions.

- If you're a chemist **analyzing** a new compound in a lab (you just measured the masses of each element), you'll probably find the empirical formula first. You see ratios before you see absolute counts.
- If you're **describing** a compound precisely (like in a textbook or reaction equation), you want the molecular formula — because it tells you exactly what's in one molecule.

### The cool case: when they're the same

Sometimes the molecular formula is already in its simplest form. Water is H₂O — the ratio of H to O is 2:1, and you can't reduce that any further (HCF of 2 and 1 is just 1). So for water, empirical = molecular.

Same goes for ammonia (NH₃), methane (CH₄), and carbon dioxide (CO₂). Their molecular formulas are already "reduced."

But compounds like glucose (C₆H₁₂O₆) and benzene (C₆H₆) have molecular formulas that can be simplified. Glucose reduces to CH₂O; benzene reduces to CH.

### How to find empirical from molecular — a 2-step recipe

1. Find the **highest common factor (HCF)** of all the subscripts.
2. Divide every subscript by that HCF.

That's it. Try it on:
- C₂H₄ → HCF(2,4) = 2 → divide → CH₂
- C₆H₆ → HCF(6,6) = 6 → divide → CH
- H₂O₂ → HCF(2,2) = 2 → divide → HO

---

## Topic 2 — Molecular Mass and Formula Mass: Weighing the Invisible

You can weigh an apple on a kitchen scale. You can weigh yourself on a bathroom scale. But how do you weigh a single molecule of water?

You can't — molecules are way too small. But you can calculate what one *should* weigh by adding up the masses of the atoms inside it. That's what **molecular mass** and **formula mass** are all about.

### Why "molecular mass" AND "formula mass" — two names?

Because compounds come in two flavours:

**Molecular compounds** (like water, carbon dioxide, sugar) are made of actual molecules — discrete groups of atoms stuck together. One water molecule is a real physical unit: 2 H atoms and 1 O atom bonded together.

**Ionic compounds** (like salt NaCl, or baking soda NaHCO₃) are NOT really molecules. They're vast arrays of positive and negative ions arranged in a crystal lattice. There's no such thing as "one molecule of salt" — salt is a sea of Na⁺ and Cl⁻ ions. The smallest repeating pattern is called a **formula unit** (one Na⁺ with one Cl⁻).

So chemists use:
- **Molecular mass** for real molecules (molecular compounds)
- **Formula mass** for formula units (ionic compounds)

But calculation-wise, they work **exactly the same way**. Add up the atomic masses of everything in the formula.

### Step-by-step calculation

Let's do H₂SO₄ (sulfuric acid) together.

1. Write the formula: H₂SO₄
2. Identify atoms: 2 H, 1 S, 4 O
3. Multiply each by its atomic mass:
   - 2 × 1 (H) = 2
   - 1 × 32 (S) = 32
   - 4 × 16 (O) = 64
4. Add them up: 2 + 32 + 64 = **98 amu**

So one molecule of H₂SO₄ weighs 98 atomic mass units.

### What's "amu"?

**amu** = atomic mass unit. It's a tiny unit of mass designed for weighing atoms. One amu is about 1.66 × 10⁻²⁴ grams — unimaginably small. But the magic is that atomic masses are written in amu as simple numbers like 1, 12, 16. So calculations stay easy.

This will pay off huge when we get to the mole. Trust me.

### Bracket trick for compounds like Mg(OH)₂

When you see brackets with a subscript, that subscript multiplies **everything inside the brackets**.

Mg(OH)₂ means:
- 1 Mg
- 2 × (OH) = 2 O and 2 H

So: Mg(OH)₂ mass = 24 (Mg) + 2(16) (O) + 2(1) (H) = 24 + 32 + 2 = **58 amu**

---

## Topic 3 — The Mole & Avogadro's Number: The Chemist's Counting Unit

This is THE most important topic in the whole chapter. If you understand this one idea deeply, everything else falls into place.

### The problem chemists had

Imagine you want to make water from hydrogen and oxygen. The reaction is:

`2H₂ + O₂ → 2H₂O`

This tells you: you need 2 molecules of H₂ for every 1 molecule of O₂. Great. But molecules are invisible. You can't reach into a bag of hydrogen and pull out exactly 2 molecules.

**So how do you measure them?**

You measure them the way we measure anything too big or too small to count one-by-one: by **grouping**.

### Groups you already know

We do this all the time in everyday life:
- **Pair** = 2 (socks, shoes)
- **Dozen** = 12 (eggs, donuts)
- **Score** = 20 (old English for counting sheep)
- **Gross** = 144 (used for pencils and old printing)
- **Ream** = 500 (sheets of paper)

Each of these is a **counting unit** — a convenient way to group items so we don't have to count one at a time.

### The chemist's counting unit: the mole

Atoms are so incredibly small that even a tiny speck of dust contains trillions of them. You can't count atoms in dozens or gross or reams — those groups are way, way too small.

So chemists invented a counting unit big enough to be useful for atoms: **the mole**.

**1 mole = 6.022 × 10²³ particles.**

That number — 6.022 × 10²³ — is called **Avogadro's number** (named after an Italian scientist you'll meet in [history.md](history.md)).

### Just how big is 6.022 × 10²³?

Let's try to grasp this. 6.022 × 10²³ is:

**602,200,000,000,000,000,000,000**

That's 602 sextillion. Some fun comparisons:
- If you had a mole of rice grains, they would cover the entire surface of the Earth to a depth of about 75 meters.
- If you counted at 1 item per second, it would take **19 quadrillion years** to count a mole. The universe is only 13.8 billion years old.
- A mole of basketballs would fill a sphere the size of the Earth.

So why such a ridiculous number? Because **atoms are that small**. You need a group that big to make a useful amount of material.

### What does "1 mole" actually feel like?

A mole of water weighs 18 grams. That's about 1 tablespoon.

A mole of sugar (glucose) weighs 180 grams. That's a little less than a cup.

A mole of iron weighs about 56 grams — a small handful of nails.

So even though 6.022 × 10²³ sounds insane, a mole of stuff is usually something you could hold in your hand. That's the whole point: the mole is defined to be a **useful, real-world amount**.

### Why 6.022 × 10²³ specifically?

Here's the really clever part. The number was chosen so that **1 mole of an element weighs exactly its atomic mass in grams**.

So:
- Carbon has atomic mass 12 amu → 1 mole of carbon weighs 12 grams.
- Oxygen has atomic mass 16 amu → 1 mole of oxygen atoms weighs 16 grams.
- Water has molecular mass 18 amu → 1 mole of water weighs 18 grams.

This is NOT a coincidence. It's how the mole was defined. That's what makes it useful — you can weigh things in grams (easy!) and instantly know how many moles you have.

---

## Topic 4 — Gram Atomic / Molecular / Formula Mass: Linking Grams to Moles

You already met this idea in Topic 3, but let's nail it down.

### The bridge between two worlds

There are two "worlds" in chemistry:

- **The world of individual atoms** — where you think about particles, molecules, ions. Things you can't see.
- **The world of grams** — where you put stuff on a balance and measure.

The mole is the **bridge** between these worlds. And the "gram atomic mass / gram molecular mass / gram formula mass" concept is how the bridge works.

### The rule, spelled out

> **If the atomic mass of carbon is 12 amu, then 1 mole of carbon atoms weighs exactly 12 grams.**

Same for compounds:

> **If the molecular mass of water is 18 amu, then 1 mole of water weighs exactly 18 grams.**

So to find the molar mass of any substance, you calculate its molecular or formula mass (in amu), then just **change the unit from amu to grams**. That's it.

### The three names

- Use **gram atomic mass** when talking about an element (like C or Na).
- Use **gram molecular mass** when talking about a molecular compound (like H₂O or CO₂).
- Use **gram formula mass** when talking about an ionic compound (like NaCl).

But honestly? In practice, chemists just call them all **molar mass** — the mass of one mole of that substance, measured in grams per mole (g/mol).

### The three golden equations (memorize these)

1. **Moles from mass:** `n = mass (in g) ÷ molar mass`
2. **Mass from moles:** `mass = moles × molar mass`
3. **Particles from moles:** `particles = moles × 6.022 × 10²³`

With these three, you can move between grams, moles, and particle counts in any direction. Every single calculation problem in this chapter is one of these three.

### A worked example — your first real problem

**Question:** How many moles are in 36 grams of water?

**Steps:**
1. Find molar mass of water: H₂O = 2(1) + 16 = 18 g/mol
2. Use `n = mass ÷ molar mass`
3. n = 36 ÷ 18 = **2 moles**

**Another one:** How many molecules are in 2 moles of water?

**Steps:**
1. Use `particles = moles × 6.022 × 10²³`
2. particles = 2 × 6.022 × 10²³ = **1.2044 × 10²⁴ molecules**

That's over a sextillion molecules in 36 grams of water. Mind-blowing.

---

## Topic 5 — Writing Formulas for Binary Ionic Compounds

Ionic compounds form when a metal gives up electrons to a non-metal. The metal becomes a positive ion (cation); the non-metal becomes a negative ion (anion). They stick together because opposite charges attract.

### The rule that makes it work

An ionic compound must be **electrically neutral**. That means the total positive charge from cations must exactly cancel the total negative charge from anions.

That's the ONLY rule. Everything else is just arithmetic to make the charges cancel.

### The 4 steps, with reasoning

**Step 1:** Write the cation (metal) first, then the anion (non-metal), with their charges written as superscripts.

**Step 2:** Figure out how many of each ion you need so the charges cancel. The trick: use the charge of one ion as the subscript of the other (the "crisscross method").

**Step 3:** Write those numbers as subscripts.

**Step 4:** Drop the charges.

### Walked-through example: aluminium oxide

- Aluminium: Al³⁺ (charge +3)
- Oxide: O²⁻ (charge −2)

We need the total positives to equal the total negatives. What's the smallest common multiple of 3 and 2? It's 6. So we need:
- 2 aluminium ions → 2 × (+3) = +6
- 3 oxide ions → 3 × (−2) = −6
- Total charge: +6 + (−6) = 0 ✓

So the formula is **Al₂O₃**.

Shortcut: take the charge number (not the sign) of each ion and swap them as subscripts. Al³⁺ and O²⁻ → Al₂O₃. Fast.

### Another one: magnesium chloride

- Mg²⁺, Cl⁻
- Crisscross: Mg gets subscript 1 (because Cl has charge 1), Cl gets subscript 2 (because Mg has charge 2)
- → MgCl₂
- Check: 1 × (+2) + 2 × (−1) = 0 ✓

### When they're already balanced

For Na⁺ + Cl⁻, both have charge 1, so the ratio is 1:1 → **NaCl**. No fancy steps needed.

For Ca²⁺ + O²⁻, both have charge 2, so the ratio is 1:1 → **CaO**. Again, no subscripts needed (you don't write Ca₁O₁).

---

## Topic 6 — Chemical Equations & Balancing: Why Atoms Can't Vanish

### The Law of Conservation of Mass

In 1789, a French chemist named Antoine Lavoisier (you'll meet him properly in [history.md](history.md)) discovered something profound: **in any chemical reaction, matter is neither created nor destroyed**. If you start with 100 grams of stuff, you end with 100 grams of stuff — maybe arranged differently, but nothing disappears.

That means every atom you put INTO a reaction must come OUT. Atoms can rearrange into new combinations, but they can't vanish and they can't appear from nowhere.

This is called the **Law of Conservation of Mass**, and it's why we balance chemical equations. The equation must literally "balance" — same atoms on both sides.

### What a chemical equation actually says

Take this simple one:

`2H₂ + O₂ → 2H₂O`

In plain English, this says: "If you react 2 hydrogen molecules with 1 oxygen molecule, you get 2 water molecules."

Count the atoms:
- **Left side:** 4 H atoms (from 2H₂), 2 O atoms (from O₂)
- **Right side:** 4 H atoms (from 2H₂O), 2 O atoms (from 2H₂O)

Perfectly matched! Nothing disappeared.

### The golden rule: coefficients, not subscripts

Here's the trickiest thing for students. When you balance an equation, you can ONLY change the big numbers in front (called **coefficients**). You can **never** change the small numbers inside formulas (called **subscripts**).

Why? Because changing a subscript changes the identity of the compound.

- H₂O is water.
- H₂O₂ is hydrogen peroxide (totally different — it bleaches hair and disinfects cuts).

If you "balance" an equation by changing H₂O into H₂O₂, you've just replaced water with hydrogen peroxide. You're not balancing — you're lying about what the reaction is.

So: **coefficients can change, subscripts can never change**.

### The step-by-step method

Let's balance methane combustion: `CH₄ + O₂ → CO₂ + H₂O`

1. **Count atoms on each side:**
   - Left: 1 C, 4 H, 2 O
   - Right: 1 C, 2 H, 3 O
   - C is already balanced ✓
   - H and O are not.

2. **Balance H first (there are 4 on the left, 2 on the right):**
   Put a 2 in front of H₂O.
   `CH₄ + O₂ → CO₂ + 2H₂O`
   Now: Left 4 H, Right 4 H ✓

3. **Recount oxygens:**
   Left: 2 O. Right: 2 (from CO₂) + 2 (from 2H₂O) = 4 O.
   Not balanced.

4. **Balance O:**
   Put a 2 in front of O₂.
   `CH₄ + 2O₂ → CO₂ + 2H₂O`
   Now: Left 4 O, Right 4 O ✓

5. **Final check:** C ✓, H ✓, O ✓. Done.

### Practical tips

- Always balance one element at a time.
- Start with elements that appear in only one compound on each side.
- Save O and H for last — they tend to show up in multiple places.
- If you get stuck with a fraction (like 5/2), multiply the entire equation by 2 to clear it.

---

## Topic 7 — Ionic Equations: Ignoring the Spectators

Sometimes in a chemical equation, some of the stuff isn't really *doing* anything. It's just hanging around in the water, unchanged from start to finish. We call these "spectator ions" — like people in a stadium watching a game but not playing in it.

An **ionic equation** cuts out the spectators and shows you ONLY what's actually reacting. This is useful because it focuses your attention on the real chemical change.

### The 4-step process

1. **Start with the balanced molecular equation.**
2. **Split every aqueous (dissolved) compound into its ions.**
3. **Cross out spectator ions** — the ones that appear identically on both sides.
4. **What's left is the net ionic equation.**

### Worked example — neutralization of acid and base

Molecular equation:
`HCl(aq) + NaOH(aq) → NaCl(aq) + H₂O(l)`

Step 2 — split everything aqueous into ions:
`H⁺(aq) + Cl⁻(aq) + Na⁺(aq) + OH⁻(aq) → Na⁺(aq) + Cl⁻(aq) + H₂O(l)`

Step 3 — notice that Na⁺ and Cl⁻ appear on both sides unchanged. Those are spectators. Cross them out.

Step 4 — what remains:
**`H⁺(aq) + OH⁻(aq) → H₂O(l)`**

That's the net ionic equation. Beautiful and simple. It tells you the real story: the only thing that happened is that an H⁺ ion combined with an OH⁻ ion to form water. Everything else was just watching.

### Why this matters

Net ionic equations reveal that many different-looking reactions are secretly the same reaction underneath. Every time you mix any acid with any base in water, the net ionic equation is `H⁺ + OH⁻ → H₂O`. Whether it's HCl + NaOH, HNO₃ + KOH, or H₂SO₄ + Ca(OH)₂ — underneath all the chemistry jargon, it's the same fundamental reaction.

### What you DO split and what you DON'T

- **SPLIT:** aqueous compounds — (aq). They're dissolved, so they exist as free ions.
- **DON'T SPLIT:** solids (s), liquids (l), gases (g). Those are whole, undissolved entities.

So in the neutralization above, H₂O(l) stays as H₂O (liquid water, not split) while NaCl(aq) splits into Na⁺ + Cl⁻.

---

## Topic 8 — Molecular vs Structural Formula

The **molecular formula** is a headcount. The **structural formula** is a seating chart.

### Molecular formula

Tells you how many atoms of each element are present in one molecule. For n-butane, the molecular formula is C₄H₁₀. That's it — 4 carbons, 10 hydrogens. You know what's inside, but you don't know how they're arranged.

### Structural formula

Shows you the actual arrangement — which atoms are bonded to which. For n-butane:

`CH₃–CH₂–CH₂–CH₃`

This tells you it's a straight chain: carbon bonded to carbon bonded to carbon bonded to carbon, with hydrogens filling all the other spots.

### Why both exist

Because **two compounds can have the same molecular formula but totally different structures**, and therefore totally different properties. This is called **isomerism**, and you'll see more of it in later chapters.

Example: C₂H₆O could be:
- **Ethanol** (CH₃–CH₂–OH) — the alcohol in beer and wine.
- **Dimethyl ether** (CH₃–O–CH₃) — a flammable gas.

Same atoms. Different arrangement. Totally different chemicals.

The molecular formula alone can't tell these apart. The structural formula can.

### Going from structural to molecular

Just count. For CH₃–CH₂–OH:
- C atoms: 2 (one in CH₃, one in CH₂)
- H atoms: 3 + 2 + 1 (from CH₃, CH₂, OH) = 6
- O atoms: 1

Molecular formula: **C₂H₆O**.

---

## Putting it all together

Look back at all 8 topics and notice something: every single one is a way of **counting** or **tracking** atoms. Formulas count which atoms are present. Masses measure how many we have. Moles let us count invisible particles using grams. Balanced equations make sure no atoms disappear. Ionic equations focus on which atoms actually react.

This whole chapter is one big idea — **atoms are conserved and countable** — told from eight different angles.

Once that clicks, stoichiometry becomes your favorite chapter.
